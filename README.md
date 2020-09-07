# Password Locker

- A terminal based aplication for managing user accounts, storing and creating passwords for the accounts.

## User Stories

- To create an account for the application or log into the application.
- Store my existing acounts login details for various accounts that I have registered for.
- Create new accounts I haven't registered for and generate a random password or user my preferred choice.
- Delete stored account login details that I do now want anymore.

## Installation

### Requirements

- Python3.6 or an updated version

#### Cloning

- Open terminal/command prompt
- `git clone https://github.com/DerrickOdhiambo/Password-Locker.git`
- `cd Password-Locker`
- `code .`

### Running the application

- Run the following command in terminal
- `chmod +x interface.py`
- `./run.py`

## Behavior Driven Development

| Behavior                                                                                      | Input                                                                                                                          | Output                                                                                                                                               |
| --------------------------------------------------------------------------------------------- | ------------------------------------------------------------------------------------------------------------------------------ | ---------------------------------------------------------------------------------------------------------------------------------------------------- |
| Open terminal                                                                                 | Run command `\$ ./run.py`                                                                                                      | Welcome to password Locker<br>Use the following commands to proceed<br>                                                                              |
| New - new user<br>Log - Log into account <br>Quit - Terminate process                         |
| Select `new`                                                                                  | Input fullname, username , password and confirm password                                                                       | Welcome `username`.Your account has been created successfully<br>Proceed to log in using command 'log'                                               |
| Select `log`                                                                                  | Input `username` and `password`                                                                                                | Succesful login - Your usename is `name` and password `password`<br>Unsuccessful login - Sorry                                                       | Account does not exist. Please try again or create an account |
| Succesful login - Procceed to manage your accounts. Use the following short codes to navigate |
| Select `nw`                                                                                   | Input account name, account username<br>Would you like your own password or a random generated password?<br>Input `my` or `pg` | User credential :Page-name:`name` Username: `username` Password:`password` created.                                                                  |
| Select vw                                                                                     | Input `vw`                                                                                                                     | Displays the accounts exists or a message 'Sorry. You don't seem to have any acounts yet. Would you like to create an account?'                      |
| Select sr                                                                                     | Input `sr`                                                                                                                     | Enter the username you want to search for : <br>Succesful - The account was found <br>Unsuccessful - The account you are looking for does not exist. |
| Select dl                                                                                     | Input `dl`<br>Input name of particular account user wants to delete `username`                                                 | Your account was successfully deleted!                                                                                                               |
| Selects a bad command                                                                         | Example `mg `                                                                                                                  | Message 'Sorry. I didnt catch that. Try again..'                                                                                                     |
| Select `quit`                                                                                 | Input `quit`                                                                                                                   | Exits the application with message "Thank you for using Password Locker. See you soon!"                                                              |

## Technologies Used

- Python

## Known bugs

- The copy to clip-board using pyperclip does not work

## Contact Information

- Email: odhiamboderrick56@gmail.com

## License

MIT License

Copyright (c) [2020] [DerrickOdhiambo]

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all
copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
SOFTWARE.
