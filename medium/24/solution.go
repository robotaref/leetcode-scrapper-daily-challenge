func swapPairs(head *ListNode) *ListNode {
	rHead := &ListNode{
		Val:  0,
		Next: head,
	}
	used := rHead
	for used != nil && used.Next != nil && used.Next.Next != nil {
		a := used.Next
		b := used.Next.Next.Next
		used.Next = used.Next.Next
		used.Next.Next = a
		a.Next = b
		used = used.Next.Next
	}

	return rHead.Next
}