package vote

import (
	"io"
	"log"

	"code.google.com/p/go.net/websocket"
)

type Client struct {
	ws     *websocket.Conn
	server *Server
	done   chan bool
}

func (c *Client) Conn() *websocket.Conn {
	return c.ws
}

func (c *Client) Write(p []*Point) {
	websocket.JSON.Send(c.ws, p)
}

func NewClient(ws *websocket.Conn, s *Server) *Client {
	c := new(Client)
	c.ws = ws
	c.server = s
	c.done = make(chan bool)

	return c
}

func (c *Client) Listen() {
	for {
		select {
		case <-c.done:
			c.server.DelHandler(c)
			log.Println("c.done")
			return

		default:
			var p Point
			err := websocket.JSON.Receive(c.ws, &p)
			log.Println("receive!")
			if err == io.EOF {
				log.Println("io.EOF")
				c.done <- true
			} else if err != nil {
				log.Println(err, p)
				c.done <- true
			} else {
				c.server.SendAllHandler(&p)
			}
		}
	}
}
