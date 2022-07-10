/*Q) You are given the head of a linked list, and an integer k.
    Return the head of the linked list after swapping the values of the kth node from the beginning 
    and the kth node from the end (the list is 1-indexed).*/

/**
 * Definition for singly-linked list.
 * struct ListNode {
 *     int val;
 *     struct ListNode *next;
 * };
 */


struct ListNode* swapNodes(struct ListNode* head, int k){
    int n;
    struct ListNode *ptr=head;
    for(int i=1;i<k;i++){
        ptr=ptr->next;
    }
    n=ptr->val;
    struct ListNode *current=head,*fast=ptr;
    while(fast->next!=NULL){
        current=current->next;
        fast=fast->next;
    }
    ptr->val=current->val;
    current->val=n;
    return head;
}
