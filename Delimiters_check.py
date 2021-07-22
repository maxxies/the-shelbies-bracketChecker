#Creation of the stack class
class Node:

    # Class to create nodes of linked list
    # constructor initializes node automatically
    def __init__(self, delim):
        self.delim = delim
        self.next = None


class Stack:

    # head is default NULL
    def __init__(self):
        self.head = None

    # Checks if stack is empty
    def isempty(self):
        if self.head == None:
            return True
        else:
            return False

    # Method to add data to the stack
    # adds to the start of the stack
    def push(self, delim):

        if self.head == None:
            self.head = Node(delim)

        else:
            newnode = Node(delim)
            newnode.next = self.head
            self.head = newnode

    # Remove element that is the current head (start of the stack)
    def pop(self):

        if self.isempty():
            return None

        else:
            # Removes the head node and makes
            # the preceeding one the new head
            poppednode = self.head
            self.head = self.head.next
            poppednode.next = None
            return poppednode.data

    # Returns the head node data
    def peek(self):

        if self.isempty():
            return None

        else:
            return self.head.delim

    # Prints out the stack
    def display(self):

        iternode = self.head
        if self.isempty():
            print("Stack Underflow")

        else:

            while (iternode != None):
                print(iternode.data, "->", end = " ")
                iternode = iternode.next
            return



# A separate class to check for the parenthesis
class checker():
    def __init__(self):
        self.new_stack = Stack()
        self.is_error = False #Boolean responsible for signifying an error
        self.ever_popped = False
        self.top = "" #stores the top item of the stack

    #Method to check for opening brackets,push them to the stack and report errors
    def check_brackets(self,text):
        #Iterating through every character in the input given
        for i in range(len(text)):
            #storing each character of the text given by the user
            current = text[i]
            #checking if the current character is an opening delimiter
            if current in ['[','(','{']:
                #Pushing all opening delimiters found to a stack 
                self.new_stack.push(current)
                #printing out the condition of the stack every time we push to it
                #print(self.new_stack.show_stack())
            #checking if the current character is a closing delimiter
            elif current in [']',')','}']:
                # checking if the stack of opening delimiters is not empty
                if not (self.new_stack.is_empty()):
                    #accessing the top item in the stack of opening delimiters
                    self.top = self.new_stack.peek()
                    self.ever_popped = True
                    #showing the condition of the stack every time an item is popped from it
                    #print(self.new_stack.show_stack())
                    #Finding matching opening and closing delimiters 
                    if (current == ']' and self.top != '[') or (current == '}' and self.top != '{') or (current == ')' and self.top != '('):
                        # Returns True if a mismatching delimiter is found
                        self.is_error = True
                        print("Expected opening delimiter for " + current)

                        break #breaking out of the loop if an error is encountered


                    else:
                        # popping from the stack when a matching opening delimiter is found for the closing delimiter,
                        self.new_stack.pop()
                        #moving to other characters in the text
                        continue

                #when the cuurent character is a closing delimiter but the stack is empty
                elif self.new_stack.is_empty():
                    #A closing delimiter without an opening leads to an error
                    self.is_error = True
                    print("Expected opening delimiter for  " + current + " at position " + (str(i+1)))
                    break
            #If no delimiter is found, no action is carried on any other character
            else:
                continue

        #When the sentence has balanced parenthesis
        if not self.is_error and (self.new_stack.is_empty()) and self.ever_popped:
            print("Balanced pair(s) of n parenthesis,good to go")
            # When the sentence has no parenthesis at all
        elif not (self.is_error) and (self.new_stack.is_empty()) and not self.ever_popped:
            print("No error found")
            #when an opening delimiter is found without a closing one
        elif not self.new_stack.is_empty() and not self.is_error:
            print(' Expected closing delimiter for ' + self.top + ' at position ' + str(i+1))

            
#Main program
if __name__ == "__main__":
    #Taking input until an empty line is met
    while True:
        Input_text = input("********************************\nenter a sentence with delimiters: \n  ")
        if not Input_text:
            break
        #creating an instance if the checker class
        checker1 = checker()

        checker1.check_brackets(Input_text)
        
    #Remember to keep track of the number of left parenthesis   
