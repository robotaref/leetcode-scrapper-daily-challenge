package main

import (
	"fmt"
)

func findIndex(s []byte, b byte) int {
	for i := range len(s) {
		if s[i] == b {
			return i
		}
	}
	return -1
}

func indexAt(s []byte, sep0 byte, sep1 byte, n int) (int, int) {
	counter := 0
	idx := 0
	for {
		idx = findIndex(s[n:], sep1)
		if idx > 0 && s[n+idx-1] == sep0 {
			counter++
			idx += n
			for {
				if idx-counter-1 >= 0 && idx+counter < len(s) {
					if s[idx-counter-1] == sep0 && s[idx+counter] == sep1 {
						counter++
					} else {
						break
					}
				} else {
					break
				}
			}

			if counter > 0 {
				break
			}
		} else if idx == -1 {
			break
		} else {
			n += idx + 1
		}
	}
	return idx, counter
}

func maximumGain(s string, x int, y int) int {
	s_array := make([]byte, len(s))
	for i := range len(s) {
		s_array[i] = s[i]
	}
	gain := 0
	indice := 0
	count := 0

	a := "a"
	b := "b"
	subs0 := []byte{a[0], b[0]}
	subs1 := []byte{b[0], a[0]}
	xy := [2]int{x, y}

	if x < y {
		subs0 = []byte{b[0], a[0]}
		subs1 = []byte{a[0], b[0]}
		xy[0] = y
		xy[1] = x
	}

	for i := range 2 {
		indice = 0
		for {
			indice, count = indexAt(s_array, subs0[i], subs1[i], indice)
			if indice == -1 {
				break
			} else {
				s_array = append(s_array[:indice-count], s_array[indice+count:]...)
				gain += xy[i] * count
				indice -= count
			}
		}
	}

	return gain
}

func main() {
	gain := maximumGain("cdbcbbaaabab", 4, 5)
	fmt.Println(gain)
}
