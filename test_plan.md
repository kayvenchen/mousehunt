Author: Kayven Chen
SID: 530654658
Unikey: kche4026


**Test Cases**
Table 1. Summary of test cases for `buy_cheese` function in `shop.py`. 
| Test ID | Description            | Inputs | Expected Output | Status |
| ------- | ---------------------- | ------ | --------------- | ------ |
| 01      | marble 1 - Positive Case. | argument: 125 input: marble 1, back | print Successfully purchase 1 Marble You have 75 gold to spend. return (50, (0, 1, 0)) | Pass   |
| 02      | cheddar 1 - Positive Case. | argument: 125 input: cheddar 1, back | Successfully purchase 1 Cheddar! You have 115 gold to spend. return (10, (1, 0, 0)) | Pass   |
| 03      | mozzerella 1 - Negative Case | argument: 125 input: mozzerella 1, back | We don't sell mozzerella You have 125 gold to spend. return (0, (0, 0, 0)) | Pass   |
| 04      | cheddar -1 - Negative Case | argument: 125 input: cheddar  -1, back | Must purchase positive amount of cheese. You have 115 gold to spend. return (0, (0, 0, 0)) | Pass   |
| 05      | integer cheese - Edge Case | argument: 125 input: 1 1, back | We don't sell 1! You have 115 gold to spend. return (0, (0, 0, 0)) | Pass   |
| 06      | Empty String - Edge Case |  | argument: 125 input: We don't sell ! You have 115 gold to spend. return (0, (0, 0, 0)) | Pass   |


Table 2. Summary of test cases for `change_cheese` function in `game.py`.
| Test ID | Description            | Inputs | Expected Output | Status |
| ------- | ---------------------- | ------ | --------------- | ------ |
| 01      | Cheddar - positive case | arguments: "Bob", "Cardboard and Hook Trap", [["Cheddar", 1], ["Marble", 0], ["Swiss", 0]] user_input: Cheddar, yes | prints "Do you want to arm your trap with Cheddar" "Cardboard and Hook Trap is now armed with Cheddar." returns True, "Cheddar" | Pass    |
| 02      | Marble - positive case | arguments: "Bob", "Cardboard and Hook Trap", [["Cheddar", 0], ["Marble", 1], ["Swiss", 0]] user_input: Marble, yes | prints "Do you want to arm your trap with Marble" "Cardboard and Hook Trap is now armed with Marble." returns True, "Marble" | Pass    |
| 03      | Mozzerella - negative case | arguments: "Bob", "Cardboard and Hook Trap", [["Cheddar", 1], ["Marble", 1], ["Swiss", 1]] user_input: Mozzerella, back| prints "No such cheese!" "" returns False, None | Pass    |
| 04      | Cheddar but 0 Cheddar in inventory - negative case | arguments: "Bob", "Cardboard and Hook Trap", [["Cheddar", 0], ["Marble", 1], ["Swiss", 1]] user_input: Cheddar, back | prints "Out of cheese!" returns False, None | Pass    |
| 05      | empty string - edge case | arguments: "Bob", "Cardboard and Hook Trap", [["Cheddar", 1], ["Marble", 1], ["Swiss", 1]] print "No such cheese!" user_input: "", back | prints "No such cheese!" "" returns False, None | Pass    |
| 06      | integer cheese - edge case | arguments: "Bob", "Cardboard and Hook Trap", [["Cheddar", 1], ["Marble", 1], ["Swiss", 1]] print "No such cheese!" user_input: 100, back | prints "No such cheese!" "" returns False, None | Pass    |


How I would implement these test cases


from <file> import <function> 

def test_function():

    captured_output = StringIO()
    output = captured_output.getvalue().strip()
    assert output == expected print statements .strip()
    print("print looks good")

    assert function(arguments) == expected output for return
    print("return looks good")
