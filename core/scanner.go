package main

import (
	"fmt"
	"net"
	"time"
)

// Ghost-SY1 High-Performance Go Port Scanner & Service Fingerprinter
func ScanPort(target string, port int, results chan<- string) {
	address := fmt.Sprintf("%s:%d", target, port)
	conn, err := net.DialTimeout("tcp", address, 2*time.Second)
	if err != nil {
		return
	}
	conn.Close()
	results <- fmt.Sprintf("[+] Port %d is OPEN on %s", port, target)
}

func RunGoScanner(target string) {
	ports := []int{21, 22, 23, 25, 53, 80, 110, 443, 445, 3306, 3389, 8080}
	results := make(chan string, len(ports))

	for _, port := range ports {
		go ScanPort(target, port, results)
	}

	for i := 0; i < len(ports); i++ {
		select {
		case res := <-results:
			fmt.Println(res)
		case <-time.After(3 * time.Second):
			// Timeout non-blocking
		}
	}
}
