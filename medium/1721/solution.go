func swapNodes(head *ListNode, k int) *ListNode {
	used := head
    first *ListNode
    second := head
    cnt :=0
    for used!=nil{
        if cnt==k{
            first=&used
        }
        if cnt>k{
            second = second.Next
        }
    }
}