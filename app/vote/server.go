package vote

import (
	"bufio"
	"log"
	"net/http"
	"os"
	"strconv"
	"strings"
	"sync"

	"code.google.com/p/go.net/websocket"
	"github.com/garyburd/redigo/redis"
)

type Server struct {
	entry     string
	conn      redis.Conn
	clients   map[*Client]bool
	points    []*Point
	scores    map[string]int
	mu        *sync.Mutex
	delCh     chan *Client
	addCh     chan *Client
	sendAllCh chan *Point
}

func check(err error) {
	if err != nil {
		panic(err)
	}
}

func (s *Server) del(c *Client) {
	delete(s.clients, c)
}

func (s *Server) DelHandler(c *Client) {
	s.delCh <- c
}

func (s *Server) sendAll(point *Point) {
	s.mu.Lock()
	var err error
	_, err = s.conn.Do("INCR", point.Name)
	check(err)
	s.scores[point.Name]++
	for idx, v := range s.points {
		if v.Name == point.Name {
			s.points[idx].Score++
			break
		}
	}
	s.mu.Unlock()

	for k := range s.clients {
		k.Write(s.points)
	}
}

func (s *Server) SendAllHandler(p *Point) {
	s.sendAllCh <- p
}

func (s *Server) add(c *Client) {
	s.mu.Lock()
	defer s.mu.Unlock()
	s.clients[c] = true
	c.Write(s.points)
}

func (s *Server) AddHandler(c *Client) {
	s.addCh <- c
}

// ファイルを読み取ってスコアを0にする
func (s *Server) redisInit() {
	filePath := "data/result.txt"
	f, err := os.Open(filePath)
	check(err)
	scanner := bufio.NewScanner(f)
	for scanner.Scan() {
		line := scanner.Text()
		split := strings.Split(line, "\t")
		s.scores[split[1]] = 0
		s.points = append(s.points, &Point{split[1], 0})
		s.conn.Do("SET", split[1], strconv.FormatInt(0, 10))
	}
}

func NewServer(entrypoint string) *Server {
	s := new(Server)
	s.entry = entrypoint
	s.clients = make(map[*Client]bool)
	s.points = make([]*Point, 0)
	s.scores = make(map[string]int)
	s.mu = new(sync.Mutex)
	s.delCh = make(chan *Client)
	s.addCh = make(chan *Client)
	s.sendAllCh = make(chan *Point)

	var err error
	s.conn, err = redis.Dial("tcp", "redis:6379")
	if err != nil {
		panic(err)
	}
	s.redisInit()
	return s
}

func (s *Server) Listen() {
	defer log.Println("finished")
	handler := func(ws *websocket.Conn) {

		client := NewClient(ws, s)
		s.AddHandler(client)
		client.Listen()
	}

	http.Handle(s.entry, websocket.Handler(handler))
	log.Println("Created handler")

	for {
		select {
		case c := <-s.sendAllCh:
			s.sendAll(c)
			log.Println("Called SendAll")
		case c := <-s.delCh:
			s.del(c)
			log.Println("Called Del")
		case c := <-s.addCh:
			s.add(c)
			log.Println("New connection")
		}
	}
}
