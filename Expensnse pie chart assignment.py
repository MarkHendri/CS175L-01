#Mark Hendri
#Professor Eckert
#Expense pie chart

import matplotlib.pyplot as plt

def read_expenses(filename):
    try:
        with open(filename, 'r') as f:
            expenses = {}
            for line in f:
                category, amount = line.strip().split('\t')
                expenses[category] = int(amount)
        return expenses
    except IOError:
        print(f"Error: Unable to read file '{filename}'")
        return {}
    except ValueError as e:
        print(f"Invalid value in '{filename}': {e}")
        return {}

def plot_pie_chart(expenses):
    fig, ax = plt.subplots()
    ax.pie(expenses.values(), labels=expenses.keys(), autopct='%1.1f%%')
    ax.set_title("Expenses Pie Chart")
    plt.show()

def main():
    expenses = read_expenses('expenses.txt')
    if expenses:
        plot_pie_chart(expenses)

if __name__ == '__main__':
    main()

