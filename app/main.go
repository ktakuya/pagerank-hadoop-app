package main

import (
	"github.com/ktakuya/vote-app/vote"
	"log"
	"net/http"
)

func main() {
	server := vote.NewServer("/wsentry")
	go server.Listen()

	http.Handle("/", http.FileServer(http.Dir("./public")))

	log.Fatal(http.ListenAndServe(":8080", nil))
}
