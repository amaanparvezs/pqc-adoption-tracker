package main

import "fmt"

func main() {
	s := "hello"
	runes := []rune(s)
	i, j := 0, len(runes) - 1
	for i < j {
		runes[i], runes[j] = runes[j], runes[i]
		i += 1
		j -= 1
	}
	str := string(runes)
	fmt.Print(str)
}