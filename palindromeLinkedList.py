def isPalindrome(head):

    info = []
    while head:
        info.append(str(head.val))
        head = head.next
    
    info = "".join(info)
    return True if info == info[::-1] else False
