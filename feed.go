package search

import (
	"encoding/json"
	"os"
)

const dataFile = "data/data.json"

//Feed contians information we need to process a feed
type Feed struct {
	Name string `json:"site"`
	URI  string `json:"link"`
	Type string `json:"type"`
}

func RetrieveFeeds() ([]*Feed, error) {
	//open the file
	file, err := os.open(dataFile)
	if err != nil {
		return nil, err
	}
	//Schedule the file to be closed once
	defer file.Close()

	//Decode the file into a slice of pointers
	//to feed values

	var feeds []*Feed
	err = json.NewDecode(file).Decode(&feeds)

	return feeds, err

}
