import wx
import datetime


class Transaction:
    """Represents a single transaction"""

    def __init__(self, name, debit_or_credit, amount):
        self._name = name
        self._type = debit_or_credit
        self._amount = amount

    def get_name(self):
        return self._name

    def get_type(self):
        return self._name

    def get_amount(self):
        return self._amount

    def change_amount(self, new_amt):
        self._amount = new_amt


class Day:
    """Represents one day's info."""

    def __init__(self, date):
        self._date = date
        self._transactions = []
        self._daily_expense = 0
        self._daily_income = 0
        self._net_changes = 0

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

    def set_net_changes(self):
        self._net_changes = self._daily_income - self._daily_expense

    def add_transaction(self, transaction):
        self._transactions.append(transaction)
        transaction_type = transaction.get_type()
        amount = transaction.get_amount()

        if transaction_type == "debit":
            self._daily_expense += amount
        elif transaction_type == "credit":
            self._daily_income += amount

        self.set_net_changes()

    def remove_transaction(self, transaction):
        self._transactions.remove(transaction)
        transaction_type = transaction.get_type()
        amount = transaction.get_amount()

        if transaction_type == "debit":
            self._daily_expense -= amount
        elif transaction_type == "credit":
            self._daily_income -= amount

        self.set_net_changes()


class Account:
    """Represents an account"""

    def __init__(self):
        self._days = []
        self._total_budget = 0
        self._budget_type = None

    def get_days(self):
        return self._days

    def get_total_budget(self):
        return self._total_budget

    def get_budget_type(self):
        return self._budget_type

    def add_a_day(self, date):
        new_day = Day(date)
        self._days.append(new_day)






if __name__ == '__main__':
    main()
