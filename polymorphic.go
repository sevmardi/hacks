// sample program to show how polymorphic behavior with interfaces.
package main

import (
	"fmt"
)

type notifier interface {
	notify()
}
type user struct {
	name       string
	first_name string
	last_name  string
	email      string
}

func (u *user) notify() {
	fmt.Printf("Sending user email to %s<%s>\n", u.name, u.email)
}

type admin struct {
	name  string
	email string
}

func (u *admin) notify() {
	fmt.Printf("Sending admin email to %s<%s>\n", u.name, u.email)
}

func main() {
	// create a user value and pass it to sendNotification
	bill := user{"Bill", "Bill", "John", "bill@exmaple.com"}

	sendNotification(&bill)

	lise := admin{"admin", "admin@adminc.om"}
	sendNotification(&lise)

}

func sendNotification(n notifier) {
	n.notify()
}
