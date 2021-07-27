# Creation of the stack class using a linked list
class Node:

    # Class to create nodes of linked list
    # constructor initializes node automatically
    def __init__(self, text):
        self.text = text
        self.next = None


class Stack:

    # head is default NULL
    def __init__(self):
        self.top = None

    # Checks if stack is empty
    def is_empty(self):
        if self.top is None:
            return True
        else:
            return False

    # Method to add data to the stack
    # adds to the start of the stack
    def push(self, text):

        if self.top is None:
            self.top = Node(text)

        else:
            newnode = Node(text)
            newnode.next = self.top
            self.top = newnode

    # Remove element that is the current head (start of the stack)
    def pop(self):

        # returns None if the stack is empty
        if self.is_empty():
            return None

        else:
            # Removes the head node and makes
            # the preceding one the new head
            poppednode = self.top
            self.top = self.top.next
            poppednode.next = None
            return poppednode.text

    # Returns the data in the head node
    def peek(self):

        if self.is_empty():
            return None

        else:
            return self.top.text

    # Prints out the stack
    def show_stack(self):

        top_node = self.top
        while True:
            if top_node is None:
                break
            else:
                print(top_node.text, "~~", end=" ")
                top_node = top_node.next
        return ''


# A separate class to check for the parenthesis
class checker:
    def __init__(self):
        self.new_stack = Stack()
        self.is_error = False  # Returns True if an error is found and False otherwise
        self.ever_popped = False
        self.j = 0  # stores last position of an unclosed opening delimiter

    # Method to check for opening brackets,push them to the stack and report errors
    def check_brackets(self, text):

        # Iterating through every character in the input given
        for i in range(len(text)):
            # storing each character of the text given by the user
            current = text[i]

            # checking if the current character is an opening delimiter
            if current in ['[', '(', '{', '<']:
                self.j = i
                # Pushing all opening delimiters found to a stack
                self.new_stack.push(current)
                # printing out the condition of the stack every time we push to it
                #print(self.new_stack.show_stack())
                # checking if the current character is a closing delimiter
            elif current in [']', ')', '}', '>']:
                # checking if the stack of opening delimiters is not empty
                if not (self.new_stack.is_empty()):
                    # accessing the top item in the stack of opening delimiters
                    self.ever_popped = True

                    # Finding matching opening and closing delimiters
                    if (current == ']' and self.new_stack.peek() != '[') or \
                            (current == '}' and self.new_stack.peek() != '{') or \
                            (current == ')' and self.new_stack.peek() != '(') or \
                            (current == '>' and self.new_stack.peek() != '<'):
                        # Returns True if a mismatching delimiter is found
                        self.is_error = True
                        print("Error: Closing delimiter " + current + " at position " + str(i + 1) + " needs an opening delimiter")
                        break  # breaking out of the loop if an error is encountered


                    else:
                        # popping from the stack when a matching opening delimiter is found for the current closing delimiter,
                        self.new_stack.pop()
                        # showing the condition of the stack every time an item is popped from it
                        # print(self.new_stack.show_stack())
                        # moving to other characters in the text
                        continue

                # when the current character is a closing delimiter but the stack is empty
                elif self.new_stack.is_empty():
                    # A closing delimiter without an opening leads to an error
                    self.is_error = True

                    print(" Error: Expected opening delimiter for  " + current + " at position " + (str(i + 1)))
                    break
                # If no delimiter is found, no action is carried on any other character
            else:
                continue

                # When the sentence has balanced parenthesis
        if not self.is_error and (self.new_stack.is_empty()) and self.ever_popped:
            print("Balanced pair(s) of parenthesis,good to go")
            # When the sentence has no parenthesis at all
        elif not self.is_error and (self.new_stack.is_empty()) and not self.ever_popped:
            print("No error found")
            # when an opening delimiter is found without a closing one
        elif not self.new_stack.is_empty() and not self.is_error:
            print('Error: Expected closing delimiter for ' + str(self.new_stack.peek()) + ' at position ' + str(self.j + 1))


# Main program
if __name__ == "__main__":
    # Taking input until an empty line is met
    while True:
        Input_text = input("********************************\nenter a sentence with delimiters: \n  ")
        if not Input_text:
            break
        # creating an instance for the checker class
        checker1 = checker()
        # calling the method to check brackets
        checker1.check_brackets(Input_text)