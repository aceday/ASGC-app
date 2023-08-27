# ASGC App
> This project is under development

 __Collaborators: Mark Cedie Buday and John Lester Balmaceda @ BSCS2-Block 1__

## Features
- Calculate Assignment, Quizzes, Final Exam using weighted average.
- Support 'add' or 'delete' entry grades.
- Support 'process' the assigned grades for comuputation.
- Export the student's grades data into '.txt' file.
- When exporting data sshould be formatted ('yyyymmddhhmmss-name_report.txt')
- Only process student's data per entry.


To test this project
> For collaborators can access and test it

`$ git clone https://github.com/aceday/scratch_ASGC` 

`$ cd scratch_ASGC`

`$ python function01.py`

### Versions:
#### 1.2:
- Fixed bug 'ZeroDivisionError'.
- Replace from old student data to re-add 'display_student'.
- Updated form 'display_student'.
- Add version for display.
- Optimize code for write date to text.
- Set file new format ('yyyymmddhhmmss-student_id.txt')
#### 1.1:
- Added comment in every variables
- Added 'Last Name, First Name' when inputting name of the student
- Added version, but not yet display
- Optimize export data with the file format('yyyymmddhhmmss-name_report.txt')
- Added error handling support
- Removes the unecessary codes
- Remove 'display_student' temporary
#### 1.0:
- Initial commit