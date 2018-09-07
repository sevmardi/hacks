// simple exmaple to show how to write a simple version of curl using the io. packge and io reader and io.writer interface support
package main

import (
	"fmt"
	"io"
	"net/http"
	"os"
)

// init is called before main
func init() {
	if len(os.Args) != 2 {
		fmt.Println("Usage: ./example2 <url>")
		os.Exit(-1)
	}

}
func main() {
	// get the response from the web server
	r, err := http.Get(os.Args[1])
	if err != nil {
		fmt.Println(err)
		return
	}

	io.Copy(os.Stdout, r.Body)
	if err := r.Body.Close(); err != nil {
		fmt.Println(err)
	}
}
