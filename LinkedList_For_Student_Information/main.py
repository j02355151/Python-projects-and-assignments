class Node:
    def __init__(self, f_name="", l_name="", course_code="", grade=0.0):
        self.f_name = f_name
        self.l_name = l_name
        self.course_code = course_code
        self.grade = grade
        self.next = None

head = None

def insert_beg(temp):
    global head
    new_node = Node(temp.f_name, temp.l_name, temp.course_code, temp.grade)
    if head is None:
        head = new_node
        new_node.next = head
    else:
        temp_node = head
        while temp_node.next != head:
            temp_node = temp_node.next
        new_node.next = head
        temp_node.next = new_node
        head = new_node

def insert_pos(pos, temp):
    global head
    new_node = Node(temp.f_name, temp.l_name, temp.course_code, temp.grade)
    if head is None:
        head = new_node
        new_node.next = head
    else:
        k = 1
        p = head
        q = None
        while k < pos and p.next != head:
            k += 1
            q = p
            p = p.next
        if k != pos:
            print("This record does not exist!!")
            return
        else:
            new_node.next = p
            q.next = new_node

def delete_beg():
    global head
    if head is None:
        print("Empty List!!")
        return
    temp = head
    temp2 = head
    while temp.next != head:
        temp = temp.next
    temp.next = head.next
    head = head.next
    del temp2

def delete_pos(pos):
    global head
    if head is None:
        print("Empty List!!")
        return
    p = head
    q = None
    k = 1
    while k < pos and p.next != head:
        k += 1
        q = p
        p = p.next
    if k != pos:
        print("Desired record does not exist!!")
        return
    q.next = p.next
    del p

def search_by_last_name(l_name):
    global head
    temp = head
    passed = True
    while temp != head or passed:
        if temp.l_name == l_name:
            return temp
        temp = temp.next
        passed = False
    return Node()

def avg_marks():
    global head
    temp = head
    passed = True
    sum_grades = 0
    count = 0
    while temp != head or passed:
        print(f"{temp.f_name} -> ", end="")
        sum_grades += temp.grade
        count += 1
        temp = temp.next
        passed = False
    print()
    return sum_grades / count if count != 0 else 0

def get_options():
    print("\nWelcome to the database menu!")
    print("1. Press 1 to insert a new record")
    print("2. Press 2 to delete a record")
    print("3. Press 3 to search database(by last name)")
    print("4. Press 4 to enter class average grade")
    print("5. Press 5 to exit")
    return int(input("Enter your option: "))

def main():
    while True:
        option = get_options()
        if option == 1:
            pos = int(input("Enter new record to insert: "))
            f_name = input("Enter First Name to insert: ")
            l_name = input("Enter Last Name to insert: ")
            course_code = input("Enter Course Code to insert: ")
            grade = float(input("Enter Grade to insert: "))
            temp = Node(f_name, l_name, course_code, grade)
            if pos == 1:
                insert_beg(temp)
            else:
                insert_pos(pos, temp)
        elif option == 2:
            pos = int(input("Enter record to delete: "))
            if pos == 1:
                delete_beg()
            else:
                delete_pos(pos)
        elif option == 3:
            l_name = input("Enter the last name to search: ")
            temp = search_by_last_name(l_name)
            if temp.f_name:
                print("Student Found!!")
                print(f"First Name: {temp.f_name}")
                print(f"Last Name: {temp.l_name}")
                print(f"Course Code: {temp.course_code}")
                print(f"Grade: {temp.grade}")
            else:
                print("Not Found")
        elif option == 4:
            print(f"The Average Grade is: {avg_marks()}")
        elif option == 5:
            break

if __name__ == "__main__":
    main()

