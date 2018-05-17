package search

import (
	"log"
	"sync"
)

// A map of registerd matchers for searching
var matchers = make(map[string]Matcher)
