'''
    Linked List implementation
    Michael Lacroix
'''

from __future__ import print_function
import unittest

''' when run with "-m unittest", the following produces:
    FAILED (failures=9, errors=2)
    your task is to fix the failing tests by implementing the necessary
    methods. '''


class LinkedList(object):
    class Node(object):
        # pylint: disable=too-few-public-methods
        ''' no need for get or set, we only access the values inside the
            LinkedList class. and really, never have setters. '''
        def __init__(self, value, next_node):
            self.value = value
            self.next_node = next_node

    def __init__(self, initial=None):
        self.front = self.back = self.current = None
        self.size = 0
        if initial != None:
            for x in initial:
                self.push_back(x)

    def empty(self):
        return self.front == self.back == None

    def __iter__(self):
        self.current = self.front
        return self

    def __next__(self):
        if self.current:
            tmp = self.current.value
            self.current = self.current.next_node
            return tmp
        else:
            raise StopIteration()

    def __str__ (self):
        list_string = ''
        current_node = self.front
        while current_node != None:
            if current_node.next_node == None:
                list_string += object.__str__(current_node.value)
            else:
                list_string += object.__str__(current_node.value) + ', '
            current_node = current_node.next_node
        return list_string

    def __repr__(self):
        return 'LinkedList((' + self.__str__() +'))'

    def push_front(self, value):
        '''Create a new node and place it at the front of the Linked List'''

        self.size = self.size + 1
        new = self.Node(value, self.front)

        if self.empty():
            self.front = self.back = new
        else:
            self.front = new

    ''' you need to(at least) implement the following three methods'''

    def pop_front(self):

        '''Remove the first node from the Linked List and return it's value'''

        if self.empty():
            raise RuntimeError('Empty List')

        self.size = self.size - 1
        pop_value = self.front.value

        if self.front.next_node == self.back.next_node:
            self.front = self.back = None
        else:
            self.front = self.front.next_node

        return pop_value

    def push_back(self, value):

        '''Adding a new node to the back of the Linked List'''

        self.size = self.size + 1
        new = self.Node(value, None)

        if self.empty():
            self.front = self.back = new
        else:
            self.back.next_node = new
            self.back = new

    def pop_back(self):

        '''Remove the back node of the Linked List and return it's value'''

        if self.empty():
            raise RuntimeError()

        self.size = self.size - 1
        pop_value = self.back.value
        current_node = self.front

        if self.front.next_node == self.back.next_node:
            self.front = self.back = None
        else:
            while current_node != self.back:
                if current_node.next_node == self.back:
                    self.back = current_node
                else:
                    current_node = current_node.next_node

        return pop_value

    def swap(self, first_value, sec_value):

        '''Swap the value in two nodes'''

        if self.front == self.back:
            raise RuntimeError()

        first_node = self.front
        sec_node = self.front

        while first_node != None:
            if first_value == first_node.value:

                first_tmp = first_node.value

                while sec_node != None:
                    if sec_value == sec_node.value:
                        if first_node != sec_node:
                            sec_tmp = sec_node.value
                            first_node.value = sec_tmp
                            sec_node.value = first_tmp
                            return
                    else:
                        sec_node = sec_node.next_node

            first_node = first_node.next_node

        raise RuntimeError()

    def insert(self, value, prev_value):

        '''Insert a node with value after the node with prev_value'''

        if self.empty():
            raise RuntimeError()

        current_node = self.front

        while current_node != None:
            if prev_value == current_node.value:
                new = self.Node(value, current_node.next_node)
                current_node.next_node = new
            current_node = current_node.next_node

    def middle(self):

        '''Find the middle node of the Linked List and return the value of the node. If there are an even
        number of elements, then the first of middle element of the Linked List. For example, a linked list with
        nodes A>B>C>D, the middle will be node B'''

        if self.empty():
            return None

        if self.size % 2 == 1:
            list_size = int(self.size / 2) + 1
        else:
            list_size = int(self.size) / 2

        index = 1
        current_node = self.front

        while index < list_size:
            current_node = current_node.next_node
            index = index + 1

        return current_node.value

    def delete(self, value):

        '''Delete the first node with the specified value in the Linked List'''

        if self.empty():
            raise RuntimeError()

        if value == self.front.value:
            self.pop_front()
            return self.__str__()

        prev_node = self.front
        current_node = self.front.next_node

        while current_node.next_node != None:

            if value == current_node.value:
                prev_node.next_node = current_node.next_node
                return self.__str__()

            prev_node = current_node
            current_node = current_node.next_node

        return self.__str__()

''' C-level work '''

class TestEmpty(unittest.TestCase):
    def test(self):
        self.assertTrue(LinkedList().empty())


class TestPushFrontPopBack(unittest.TestCase):
    def test(self):
        linked_list = LinkedList()
        linked_list.push_front(1)
        linked_list.push_front(2)
        linked_list.push_front(3)
        self.assertFalse(linked_list.empty())
        self.assertEqual(linked_list.pop_back(), 1)
        self.assertEqual(linked_list.pop_back(), 2)
        self.assertEqual(linked_list.pop_back(), 3)
        self.assertTrue(linked_list.empty())


class TestPushFrontPopFront(unittest.TestCase):
    def test(self):
        linked_list = LinkedList()
        linked_list.push_front(1)
        linked_list.push_front(2)
        linked_list.push_front(3)
        self.assertFalse(linked_list.empty())
        self.assertEqual(linked_list.pop_front(), 3)
        self.assertEqual(linked_list.pop_front(), 2)
        self.assertEqual(linked_list.pop_front(), 1)
        self.assertTrue(linked_list.empty())


class TestPushBackPopFront(unittest.TestCase):
    def test(self):
        linked_list = LinkedList()
        linked_list.push_back(1)
        linked_list.push_back(2)
        linked_list.push_back(3)
        self.assertFalse(linked_list.empty())
        self.assertEqual(linked_list.pop_front(), 1)
        self.assertEqual(linked_list.pop_front(), 2)
        self.assertEqual(linked_list.pop_front(), 3)
        self.assertTrue(linked_list.empty())


class TestPushBackPopBack(unittest.TestCase):
    def test(self):
        linked_list = LinkedList()
        linked_list.push_back(1)
        linked_list.push_back("foo")
        linked_list.push_back([3, 2, 1])
        self.assertFalse(linked_list.empty())
        self.assertEqual(linked_list.pop_back(), [3, 2, 1])
        self.assertEqual(linked_list.pop_back(), "foo")
        self.assertEqual(linked_list.pop_back(), 1)
        self.assertTrue(linked_list.empty())

''' B-level work '''


class TestInitialization(unittest.TestCase):
    def test(self):
        linked_list = LinkedList(("one", 2, 3.141592))
        self.assertEqual(linked_list.pop_back(), 3.141592)
        self.assertEqual(linked_list.pop_back(), 2)
        self.assertEqual(linked_list.pop_back(), "one")

class TestStr(unittest.TestCase):
    def test(self):
        linked_list = LinkedList((1, 2, 3))
        self.assertEqual(linked_list.__str__(), '1, 2, 3')

''' A-level work '''


class TestRepr(unittest.TestCase):
    def test(self):
        linked_list = LinkedList((1, 2, 3))
        self.assertEqual(linked_list.__repr__(), 'LinkedList((1, 2, 3))')

class TestErrors(unittest.TestCase):
    def test_pop_front_empty(self):
        self.assertRaises(RuntimeError, lambda: LinkedList().pop_front())

    def test_pop_back_empty(self):
        self.assertRaises(RuntimeError, lambda: LinkedList().pop_back())

''' write some more test cases. '''

class TestInsert(unittest.TestCase):
    def test(self):
        linked_list = LinkedList((1,2,3))
        linked_list.insert("one", 2)
        self.assertEqual(linked_list.__str__(), '1, 2, \'one\', 3')
        linked_list.insert(7, 4)
        self.assertEqual(linked_list.__str__(), '1, 2, \'one\', 3')

class TestSwap(unittest.TestCase):
    def test(self):
        linked_list = LinkedList(("seven", 3, 5, 4))
        linked_list.swap("seven", 3)
        self.assertEqual(linked_list.__str__(), '3, \'seven\', 5, 4')
        linked_list.swap(4, 3)
        self.assertEqual(linked_list.__str__(), '4, \'seven\', 5, 3')
        linked_list.swap(5, 3)
        self.assertEqual(linked_list.__str__(), '4, \'seven\', 3, 5')
        linked_list.swap(5, 3)
        self.assertEqual(linked_list.__str__(), '4, \'seven\', 5, 3')

class TestSwapError(unittest.TestCase):
    def testEmpty(self):
        self.assertRaises(RuntimeError, lambda: LinkedList().swap(1,2))

    def testSingle(self):
        linked_list = LinkedList()
        linked_list.push_front('a')
        self.assertRaises(RuntimeError, lambda: linked_list.swap('a',2))

    def testNoValue(self):
        linked_list = LinkedList((1,2,3))
        self.assertRaises(RuntimeError, lambda: linked_list.swap(1,4))

''' extra credit.
    - write test cases for and implement a delete(value) method.
    - write test cases for and implement a method that finds the middle
      element with only a single traversal.
'''
class TestDelete(unittest.TestCase):
    def test(self):
        linked_list = LinkedList((1,2,3))
        linked_list.delete(4)
        self.assertEqual(linked_list.__str__(), '1, 2, 3')
        linked_list = LinkedList((1,2,3))
        linked_list.delete(2)
        self.assertEqual(linked_list.__str__(), '1, 3')
        linked_list = LinkedList((1,2,"3",4,4))
        linked_list.delete(3)
        self.assertEqual(linked_list.__str__(), '1, 2, \'3\', 4, 4')
        linked_list.delete(4)
        self.assertEqual(linked_list.__str__(), '1, 2, \'3\', 4')

class TestDeleteError(unittest.TestCase):
    def test(self):
        self.assertRaises(RuntimeError, lambda: LinkedList().delete(1))

class TestMiddle(unittest.TestCase):
    def test(self):
        linked_list = LinkedList()
        self.assertEqual(linked_list.middle(), None)
        linked_list.push_front(3)
        self.assertEqual(linked_list.middle(), 3)
        linked_list = LinkedList((1, 1, 1))
        self.assertEqual(linked_list.middle(), 1)
        linked_list = LinkedList((1,2,3,4))
        self.assertEqual(linked_list.middle(), 2)
        linked_list = LinkedList((1,2,3,4,5))
        self.assertEqual(linked_list.middle(), 3)

''' the following is a demonstration that uses our data structure as a
    stack'''


def fact(number):
    '''"Pretend" to do recursion via a stack and iteration'''

    if number < 0: raise ValueError("Less than zero")
    if number == 0 or number == 1: return 1

    stack = LinkedList()
    while number > 1:
        stack.push_front(number)
        number -= 1

    result = 1
    while not stack.empty():
        result *= stack.pop_front()

    return result


class TestFactorial(unittest.TestCase):
    def test_less_than_zero(self):
        self.assertRaises(ValueError, lambda: fact(-1))

    def test_zero(self):
        self.assertEqual(fact(0), 1)

    def test_one(self):
        self.assertEqual(fact(1), 1)

    def test_two(self):
        self.assertEqual(fact(2), 2)

    def test_10(self):
        self.assertEqual(fact(10), 10 * 9 * 8 * 7 * 6 * 5 * 4 * 3 * 2 * 1)


if '__main__' == __name__:
    unittest.main()