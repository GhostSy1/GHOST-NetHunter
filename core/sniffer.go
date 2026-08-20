package main

import (
	"fmt"
	"strings"
)

// Ghost-SY1 High-Speed Packet Sniffer & Credential Harvester (Go)
func HarvestCredentials(packetPayload string) {
	lower := strings.ToLower(packetPayload)
	if strings.Contains(lower, "authorization: basic") || strings.Contains(lower, "password=") {
		fmt.Println("[+] ALERT: Unencrypted credentials captured in network stream!")
		fmt.Printf("[+] Captured Packet Snippet: %s\n", packetPayload[:min(len(packetPayload), 100)])
	}
}

func min(a, b int) int {
	if a < b {
		return a
	}
	return b
}
