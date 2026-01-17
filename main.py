from linked_list import LinkedList

if __name__ == "__main__":
    # 1) Create a LinkedList instance
    ll = LinkedList()

    # 2) Insert some sample data using insert_at_front or insert_at_end
    ll.insert_at_front(10)
    ll.insert_at_front(20)
    ll.insert_at_front(30)
    ll.insert_at_end(5)

    # 3) Display the list to verify insertion
    print("List after insertions:")
    ll.display()

    # 4) Call recursive_sum and print the result
    print("Sum of all elements:", ll.recursive_sum())

    # 5) Call recursive_search with a target and print result
    print("Search for 20:", ll.recursive_search(20))
    print("Search for 100:", ll.recursive_search(100))

    # 6) Call recursive_reverse, then display the reversed list
    ll.recursive_reverse()
    print("List after reverse:")
    ll.display()
