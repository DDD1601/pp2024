import curses

<<<<<<< Updated upstream

=======
class CursesUI:
    def __init__(self):
        self.stdscr = curses.initscr()
        curses.curs_set(0)
        self.stdscr.keypad(True)
        self.stdscr.clear()

    def display_menu(self):
        self.stdscr.addstr(0, 0, "Menu:")
        self.stdscr.addstr(1, 0, "1. List courses")
        self.stdscr.addstr(2, 0, "2. List students")
        self.stdscr.addstr(3, 0, "3. Select a course and input marks for students")
        self.stdscr.addstr(4, 0, "4. Show student marks for a course")
        self.stdscr.addstr(5, 0, "5. Calculate and sort students by GPA")
        self.stdscr.addstr(6, 0, "6. Exit")
        self.stdscr.refresh()

    def get_user_choice(self):
        while True:
            try:
                choice = self.stdscr.getch() - ord('0')
                if 1 <= choice <= 6:
                    return choice
            except curses.error:
                pass

    def close(self):
        curses.endwin()

if __name__ == "__main__":
    ui = CursesUI()
    ui.display_menu()
    choice = ui.get_user_choice()
    ui.close()
>>>>>>> Stashed changes
