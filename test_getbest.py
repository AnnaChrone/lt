import pytest
import subprocess
import os


#Helper function to allow each test to create a temporary CSV file with test data in it
def create_file(filename, content): 
    with open(filename, "w") as f:
        f.write(content)

#Helper function that runs the program and captures the printed output and whether the program crashes or not
def run_program(filename):
    result = subprocess.run(
        ["python3", "getbest.py", filename],
        capture_output=True,
        text=True
    )
    return result


#test 1.Column order changes
def test_column_order_changes():
    filename = "test1.csv"
    create_file(filename,
    """Mark,Student Number
    70,100001
    85,100002
    95,100003
    """)
    
    result = run_program(filename)
    assert "100001" in result.stdout #checks for the correct student number in the result
    assert "95" in result.stdout #checks for correct grade in the result
    os.remove(filename) #declutters project

#test 2. Ignoring unrelated columns
def test_ignore_unrelated_columns():
    filename = "test2.csv"
    create_file(filename, 
    """Name,Student Number,Mark,Course
    Linsey,100001,60,Math
    Claire,100002,99,CS
    Charlie,100003,80,Physics
    """)
    
    result = run_program(filename)
    assert "100002" in result.stdout
    assert "99" in result.stdout
    os.remove(filename)

#test 3.Testing basic correctness of program
def test_basic_correctness():
    filename = "test3.csv"
    create_file(filename, 
    """Student Number,Mark
    100005,70
    100006,65
    100007,95
    """)
    
    result= run_program(filename)
    assert "100007" in result.stdout
    assert "95" in result.stdout
    os.remove(filename)

#test 4. Testing the number of students doesnt impact functionality
def test_number_of_students():
    filename = "test4.csv"
    filecontent = "Student Number,Mark\n"
    for i in range(1, 101): #generates a 100 person file
        filecontent += f"{100000+i},{i}\n"

    create_file(filename, filecontent)

    result = run_program(filename)
    assert "110000" in result.stdout 
    assert "100" in result.stdout 
    os.remove(filename)

#test 5. Testing that a single student doesnt impact functionality
def test_single_student():
    filename = "test5.csv"
    create_file(filename, 
    """Student Number,Mark
    100001,75
    """)

    result = run_program(filename)
    assert "100001" in result.stdout
    assert "75" in result.stdout
    os.remove(filename)

#Edge case testing
#test 6. Testing correct functionality when the highest mark is in the first row
def test_highest_mark_in_first_row():
    filename = "test6.csv"
    create_file(filename, 
    """Student Number,Mark
    100001,99
    100002,40
    100003,50
    """)
    
    result = run_program(filename)
    assert "100001" in result.stdout
    assert "99" in result.stdout
    os.remove(filename)

#test 7. Testing correct functionality when the highest mark is in the last row
def test_highest_mark_in_last_row():
    filename = "test7.csv"
    create_file(filename, 
    """Student Number,Mark
    100001,30
    100002,20
    100003,99
    """)

    result = run_program(filename)
    assert "100003" in result.stdout
    assert "99" in result.stdout
    os.remove(filename)

#test 8.Testing correct functionality when the highest mark is 0
def test_mark_is_zero():
    filename = "test8.csv"
    create_file(filename,
    """Student Number,Mark
    100001,0
    """)

    result = run_program(filename)
    assert "100001" in result.stdout
    assert "0" in result.stdout
    os.remove(filename)


#test 9.Testing correct response to an empty file
def test_empty_file():
    filename = "test9.csv"
    create_file(filename, "")

    result = run_program
    assert result.returncode != 0
    os.remove(filename)
