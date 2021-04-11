import datetime


class Transaction:
    """Represents a single transaction"""

    def __init__(self, description, income_or_expense, amount, month=datetime.date.today().month,
                 day=datetime.date.today().day, year=datetime.date.today().year):
        self._name = description
        self._type = income_or_expense
        self._amount = amount
        self._date = datetime.date(year, month, day)

    def get_name(self):
        return self._name

    def get_type(self):
        return self._type

    def get_amount(self):
        return self._amount

    def get_date(self):
        return self._date

    def change_amount(self, new_amt):
        self._amount = new_amt

    def change_type(self, new_type):
        self._type = new_type

    def change_date(self, new_date=datetime.date.today()):
        self._date = new_date

    def print_info(self):
        text = "${:.2f}      Desc: {}"
        if self._type == 'expense':
            text = '-' + text

        text = "     " + text

        print(text.format(self._amount, self._name))


class Day:
    """Represents one day's info."""

    def __init__(self, date):
        self._date = date
        self._transactions = []
        self._daily_expense = 0
        self._daily_income = 0
        self._net_changes = 0
        self._daily_budget = 0
        self._in_budget_status = True
        self._remaining_budget = 0

    def get_date(self):
        return self._date

    def get_transactions(self):
        return self._transactions

    def get_daily_expense(self):
        return self._daily_expense

    def get_daily_income(self):
        return self._daily_income

    def get_net_change(self):
        return self._net_changes

    def get_daily_budget(self):
        return self._daily_budget

    def get_budget_status(self):
        return self._past_budget_status

    def set_net_changes(self):
        self._net_changes = self._daily_income - self._daily_expense

    def set_daily_budget(self, budget):
        self._daily_budget = budget

    def get_remaining_budget(self):
        if self._daily_budget == 0:
            return False
        else:
            return self._remaining_budget

    def set_remaining_budget(self):
        if self._daily_budget == 0:
            return False
        remain_budget = self._daily_budget + self._net_changes
        if remain_budget <= 0:
            self._in_budget_status = False
        self._remaining_budget = remain_budget

    def compare_date(self, date_in):
        if self._date == date_in:
            return True
        else:
            return False

    def add_transaction(self, transaction):
        self._transactions.append(transaction)
        transaction_type = transaction.get_type()
        amount = transaction.get_amount()

        if transaction_type == "expense":
            self._daily_expense += amount
        elif transaction_type == "income":
            self._daily_income += amount

        self.set_net_changes()
        if self._daily_budget != 0:
            self.set_remaining_budget()

    def remove_transaction(self, transaction):
        self._transactions.remove(transaction)
        transaction_type = transaction.get_type()
        amount = transaction.get_amount()

        if transaction_type == "expense":
            self._daily_expense -= amount
        elif transaction_type == "income":
            self._daily_income -= amount

        self.set_net_changes()
        if self._daily_budget != 0:
            self.set_remaining_budget()

    def print_amounts(self):
        print("Date: {}".format(self._date))
        print("     Income: {:.2f}".format(self._daily_income))
        print("   Expenses: {:.2f}".format(self._daily_expense))
        print("      Total: {:.2f}".format(self._net_changes))
        if self._daily_budget != 0:
            print("  Remaining Budget: {:.2f}".format(self._remaining_budget))

    def print_ending_balance(self):
        print("Date: {}       {:.2f}".format(self._date, self._net_changes))
        if self._daily_budget != 0:
            print("  Remaining Budget: {:.2f}".format(self._remaining_budget))

    def print_activity(self):
        print("Date: {}".format(self._date))
        for t in self._transactions:
            t.print_info()

    def print_full_info(self):
        print("Date: {}".format(self._date))
        for t in self._transactions:
            t.print_info()
        print("            Income: {:.2f}".format(self._daily_income))
        print("          Expenses: {:.2f}".format(self._daily_expense))
        print("             Total: {:.2f}".format(self._net_changes))
        if self._daily_budget != 0:
            print("  Remaining Budget: {:.2f}".format(self._remaining_budget))


class Account:
    """Represents an account"""

    def __init__(self, name):
        self._name = name
        self._days = []
        self._total_budget = 0

    def get_name(self):
        return self._name

    def get_days(self):
        return self._days

    def get_total_budget(self):
        return self._total_budget

    def set_total_budget(self, budget):
        self._total_budget = budget

    def add_a_day(self, new_day):
        if self._total_budget != 0:
            new_day.set_daily_budget(self._total_budget)
            new_day.set_remaining_budget()
        self._days.append(new_day)

    def sort_days_arr(self):
        def get_dates(day):
            return day.get_date()

        self._days.sort(key=get_dates)

    def print_days(self):
        for d in self._days:
            print(d.get_date())

    def print_all_transactions(self):
        for d in self._days:
            d.print_activity()


def main():
    print("Welcome to Budget Track!")
    account_name = input("Enter name of account: ")
    acc = Account(account_name)
    print("----------------------------------------")
    print("\nAccount Name: {}".format(acc.get_name()))
    running_status = True

    while running_status:
        print("\n1. Add a transaction")
        print("2. Display all transactions")
        print("3. Display a specific day")
        print("4. Display all daily balances and budget status")
        print("5. Set a daily budget")
        print("6. Remove a transaction")
        print("\n0. Exit")

        main_menu_input = input("\nEnter a number choice: ")

        if main_menu_input == "1":
            type_of_tr = input("Type of transaction (income or expense): ")
            while type_of_tr != "income" and type_of_tr != "expense":
                print("\nMust enter 'income' or expense' ")
                type_of_tr = input("Type of transaction: ")

            amount = float(input("Amount: $"))
            description = input("Description: ")

            print("Enter Date (MMDDYYYY): ")

            month_input = int(input("Month: "))
            day_input = int(input("Day: "))
            year_input = int(input("Year: "))

            while True:
                valid_date = True
                try:
                    datetime.date(year_input, month_input, day_input)
                except ValueError:
                    valid_date = False
                    print("Invalid date, try again: ")

                if valid_date:
                    break

                month_input = int(input("Month: "))
                day_input = int(input("Day: "))
                year_input = int(input("Year: "))

            tr = Transaction(description, type_of_tr, amount, month_input, day_input, year_input)

            # get existing days, append new day if not in Account array
            existing_days = acc.get_days()
            existing_day_check = False
            for day in existing_days:
                if day.get_date() == tr.get_date():
                    day.add_transaction(tr)
                    existing_day_check = True

            if not existing_day_check:
                d1 = Day(tr.get_date())
                d1.add_transaction(tr)
                acc.add_a_day(d1)

            acc.sort_days_arr()

        elif main_menu_input == "2":
            print("")
            acc.print_all_transactions()

        elif main_menu_input == "3":
            print("Enter a date to see: ")
            month_input = int(input("Month: "))
            day_input = int(input("Day: "))
            year_input = int(input("Year: "))

            while True:
                valid_date = True
                try:
                    datetime.date(year_input, month_input, day_input)
                except ValueError:
                    valid_date = False
                    print("Invalid date, try again: ")

                if valid_date:
                    break

                month_input = int(input("Month: "))
                day_input = int(input("Day: "))
                year_input = int(input("Year: "))

            specified_date = datetime.date(year_input, month_input, day_input)
            day_arr = acc.get_days()
            existing_day_check = False
            for d3 in day_arr:
                if d3.compare_date(specified_date):
                    d3.print_full_info()
                    existing_day_check = True

            if not existing_day_check:
                print("\nNo transactions on that date.")


        elif main_menu_input == "4":
            print("   1. Show Daily Ending Balances and Remaining Budget")
            print("   2. Show Full Info")

            choice4 = input("Enter choice: ")
            print("")
            day_arr = acc.get_days()
            if choice4 == "1":
                for d4 in day_arr:
                    d4.print_ending_balance()
            elif choice4 == "2":
                for d4 in day_arr:
                    d4.print_amounts()
        elif main_menu_input == "5":
            if acc.get_total_budget() != 0:
                print("Current Daily Budget: {:.2f}".format(acc.get_total_budget()))

            budget_input = input("Enter a daily budget: $")
            acc.set_total_budget(float(budget_input))
            day_arr = acc.get_days()
            for d5 in day_arr:
                d5.set_daily_budget(float(budget_input))
                d5.set_remaining_budget()
        elif main_menu_input == "6":
            print("Enter Date (MMDDYYYY): ")

            month_input = int(input("Month: "))
            day_input = int(input("Day: "))
            year_input = int(input("Year: "))

            while True:
                valid_date = True
                try:
                    datetime.date(year_input, month_input, day_input)
                except ValueError:
                    valid_date = False
                    print("Invalid date, try again: ")

                if valid_date:
                    break

                month_input = int(input("Month: "))
                day_input = int(input("Day: "))
                year_input = int(input("Year: "))
            desc_in = input("Transaction Description: ")

            specified_date = datetime.date(year_input, month_input, day_input)
            day_arr = acc.get_days()
            existing_tr_check = False
            for d3 in day_arr:
                if d3.compare_date(specified_date):
                    tr_array = d3.get_transactions()
                    for t6 in tr_array:
                        if t6.get_name() == desc_in:
                            d3.remove_transaction(t6)
                            if not d3.get_transactions():
                                day_arr.remove(d3)
                            existing_tr_check = True

            if not existing_tr_check:
                print("\nNo matching transaction.")


        elif main_menu_input == "0":
            print("Goodbye")
            running_status = False
        else:
            print("Enter a valid number choice: ")


if __name__ == '__main__':
    main()
