/**
 * Definition for singly-linked list.
 * public class ListNode {
 *     int val;
 *     ListNode next;
 *     ListNode() {}
 *     ListNode(int val) { this.val = val; }
 *     ListNode(int val, ListNode next) { this.val = val; this.next = next; }
 * }
 */

class Solution {
    public ListNode reverseList(ListNode head) {
        ListNode prev = null;
        ListNode curr = head;


        
        while(curr != null){
            ListNode temp = curr.next; //Iteration 1: temp is null, I2: temp is now head.next
            curr.next = prev; //Iteration 1: curr.next is null, I2: curr.next is head
            prev = curr; //Iteration 1: prev is now head, I2: prev is head
            curr = temp; //Iteration 1: curr is null, I2: curr is head.next

        }

        return prev;
    }
}
