struct ListNode* removeNthFromEnd(struct ListNode* head, int n){
  
    
    int count=1;
    struct ListNode*ptr = NULL;
    ptr=head;
    
    while(ptr->next!= NULL){
        count++;
        ptr= ptr->next;
    }
    
    int k= count-n;
    
    struct ListNode *temp;
    temp=head;
    
    if(k==0){
        head=head->next;
        return(head);
    }
    else{
        while(k>1){
            temp=temp->next;
            k-=1;
        }
        temp->next=temp->next->next;
        
    }
    return head;
}