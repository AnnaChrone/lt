Joanna Chronis (2817173)

TEST CASES:
Test 1. Column order changes - Verify the program correctly identifies the "Student Number" and "Mark" columns regardless of their position.
-Dynamic column detection using headers
-No hardcoded column indices

Test 2. Ignore unrelated columns - Ensure additional columns do not affect program correctness.
-Ability to extract only relevant data from a larger dataset
-Correct indexing when required columns are not adjacent

Test 3. Basic Correctness - verifies the program properly identifies the student with the highest mark

Test 4. Number of students - Verify the program works correctly regardless of the number of students.
-Loop processes all rows correctly
-No dependency on dataset size

Test 5. Testing that a single student doesnt impact functionality - Verify the program works even if there is only a single student in the class
-No dependency on dataset size

Edge cases:
Test 6. Highest Mark in First Row - Ensure the program correctly identifies the first row as the maximum when applicable.
-Proper initialization of best
-Correct comparison logic from the start

Test 7. Highest Mark in Last Row- Ensure the program correctly updates the best student when the maximum appears at the end.
-Full traversal of file
-Updating of best during iteration

Test 8. mark is zero- Test behaviour when the highest (or all) marks are 0
-Correct handling of zero values

Test 9. file is empty - Test how the program behaves with missing input data
-Robustness to invalid or empty files
