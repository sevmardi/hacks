package main

import (
	"fmt"
)

type user struct {
	name  string
	email string
}

// notify implements a method with value reciver
func (u user) notify() {
	fmt.Printf("Sending user email to %s<%s>\n", u.name, u.email)

}

// changeEmail implements a method with a pointer receiver
func (u *user) changeEmail(email string) {
	u.email = email
}

func main() {
	// Values of type user can be used to call methods
	// declared with a value receiver.
	bill := user{"bill", "bill@exmaple.com"}
	bill.notify()

	// pointers of type user can be used to call methods declared with a value receiver.
	// declared with a value receiver.
	lise := &user{"Lise", "Lise@email.com"}
	lise.notify()

	// Values of type user can be used to call methods
	// declared with a pointer reciver
	bill.changeEmail("bill@emialischange.com")
	bill.notify()

	// Pointers of type user can be used to call methods
	// declared with a pointer receiver.
	lise.changeEmail("lisa@comcast.com")
	lise.notify()

}
