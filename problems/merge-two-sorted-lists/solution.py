class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution:

    def mergeTwoLists(self, l1: ListNode, l2: ListNode) -> ListNode:
        ret_list = None
        first = None

        def append(val):
            nonlocal ret_list
            nonlocal first
            a = ListNode(val)
            if ret_list:
                ret_list.next = a
            else:
                first = a
            ret_list = a
            return True

        current_l1 = l1
        current_l2 = l2
        while current_l1 or current_l2:
            next_1 = False
            next_2 = False
            if not current_l1:
                next_2 = append(current_l2.val)
            elif not current_l2:
                next_1 = append(current_l1.val)
            else:
                if current_l1.val >= current_l2.val:
                    next_2 = append(current_l2.val)

                if current_l2.val >= current_l1.val:
                    next_1 = append(current_l1.val)

            if next_1:
                current_l1 = current_l1.next
            if next_2:
                current_l2 = current_l2.next

        return first


def create_list(ls):
    first = None
    current = None
    for item in ls:
        if not first:
            first = ListNode(item)
            current = first
            continue
        current.next = ListNode(item)
        current = current.next
    return first


if __name__ == '__main__':
    a = Solution().mergeTwoLists(
        create_list([1, 2, 4]), create_list([1, 3, 4]))
    print(a)
