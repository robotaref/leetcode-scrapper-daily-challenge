#include "bits/stdc++.h"
#include <iostream>
#include <iomanip>
#include <math.h>
#include <cassert>

using namespace std;


struct ListNode {
  int val;
  ListNode *next;
  ListNode() : val(0), next(nullptr) {}
  ListNode(int x) : val(x), next(nullptr) {}
  ListNode(int x, ListNode *next) : val(x), next(next) {}
};


ListNode* makeListNode(vector<int> vec) {
  ListNode* head = nullptr;
  for (int i = 0; i < vec.size(); i++) {
    ListNode* newNode = new ListNode();
    newNode -> val = vec[i]; // Replace i with the actual data
    newNode -> next = nullptr;

  // Link the nodes
    if (head == nullptr) {
        // The list is empty, so the new node is the
        // head of the list
        head = newNode;
    }
    else {
        // The list is not empty, traverse the list to
        // find the last node
        ListNode* temp = head;
        while (temp->next != nullptr) {
            temp = temp->next;
        }

        // Now temp points to the last node, link the
        // new node
        temp->next = newNode;
    }
  }
  return head;
}
 
ListNode* addTwoNumbers(ListNode* l1, ListNode* l2) {
  int sum;
  int residue = 0;
  ListNode* head = nullptr;

  while (l1 != nullptr or l2 != 0) {
      sum = 0 + residue;

      if (l1 != nullptr) {
          sum += l1 -> val;
          l1 = l1 -> next;
      }
      if (l2 != nullptr) {
          sum += l2 -> val;
          l2 = l2 -> next;
      }

      if (sum > 9) {
          residue = 1;
          sum = sum - 10;
      } else {
          residue = 0;
      }
      ListNode* newNode = new ListNode();
      newNode -> val = sum; // Replace i with the actual data
      newNode -> next = nullptr;

      // Link the nodes
      if (head == nullptr) {
      // The list is empty, so the new node is the
      // head of the list
          head = newNode;
      }
      else {
      // The list is not empty, traverse the list to
      // find the last node
          ListNode* temp = head;
          while (temp->next != nullptr) {
          temp = temp->next;
      }

      // Now temp points to the last node, link the
      // new node
      temp->next = newNode;
      }
  }
  if (residue == 1) {
      ListNode* newNode = new ListNode();
      newNode -> val = 1; // Replace i with the actual data
      newNode -> next = nullptr;

      // Link the nodes
      if (head == nullptr) {
      // The list is empty, so the new node is the
      // head of the list
          head = newNode;
      }
      else {
      // The list is not empty, traverse the list to
      // find the last node
          ListNode* temp = head;
          while (temp->next != nullptr) {
          temp = temp->next;
      }

      // Now temp points to the last node, link the
      // new node
      temp->next = newNode;
      }
  }
  return head;
}


int main() {
    int list1[] = {2, 4, 3};
    vector<int> num1(begin(list1), end(list1));

    int list2[] = {5, 6, 4};
    vector<int> num2(begin(list2), end(list2));

    ListNode* ln_1 = makeListNode(num1);
    ListNode* ln_2= makeListNode(num2);

  ListNode* output = addTwoNumbers(ln_1, ln_2);
  cout << output -> val << endl;
}