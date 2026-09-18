#!/usr/bin/env python
# coding: utf-8

# In[1]:


import json
from datetime import datetime

expenses = {
    "Food" : [],
    "Transport": [],
    "Entertainment": [],
    "Bills": []
}
monthly_budget = 0
DATA_FILE = "expenses_tracker.json"
expenses_history = {}
current_month = datetime.now().strftime("%B %Y")
today = datetime.now().strftime("%Y-%m-%d")

def load_data():
    global current_month, expenses, expenses_history, monthly_budget
    try:
        with open(DATA_FILE,"r") as f:
            data = json.load(f)
            last_month = data.get("current_month",current_month)
            monthly_budget = data.get("monthly_budget",0)
            expenses = data.get("expenses",{
                "Food": [],
                "Transport": [],
                "Entertainment": [],
                "Bills": []
            })
            expenses_history = data.get("expenses_history",{})
        if last_month != current_month:
            total_spending = 0
            for category,info in expenses.items():
                total_spending = sum(items["amount"] for items in info)
            expenses_history[last_month] = {
                "monthly_budget":monthly_budget,
                "total_spending":total_spending,
                "expenses":expenses
            }
            monthly_budget = 0
            expenses = {
                "Food":[],
                "Transport":[],
                "Entertainment":[],
                "Bills":[]
            }
    except (FileNotFoundError,json.JSONDecodeError):
        monthly_budget = 0
        expenses = {
            "Food" : [],
            "Transport": [],
            "Entertainment": [],
            "Bills": []
        }
        expenses_history = {}

def save_data():
    saved_data = {
        "current_month":current_month,
        "monthly_budget":monthly_budget,
        "expenses":expenses,
        "expenses_history":expenses_history
    }
    with open(DATA_FILE,"w") as f:
        json.dump(saved_data,f,indent = 4)
    print(f"\nSuccessfully saved data!")
    print(f"Thank you for using this program")

# option 1 - add expense
def option_1():
    selection = {
        "A":"Food",
        "B":"Transport",
        "C":"Entertainment",
        "D":"Bills"
    }
    while True:
        print(f"==========================================================================================")
        print(f"                             Add expenses - {current_month}                               ")
        print(f"==========================================================================================")
        print(f"A. Food")
        print(f"B. Transport")
        print(f"C. Entertainment")
        print(f"D. Bills")
        print(f"E. Return to previous page")
        print(f"------------------------------------------------------------------------------------------")
        choice = input(f"Please select (A-E): ")
        if choice.upper() == "E":
            break
        elif choice.upper() in selection:
            amount_1 = input(f"\nHow much have you spent for {selection[choice.upper()]}?: $")
            clean_amount_1 = amount_1.replace(".","",1)
            try:
                if clean_amount_1.isdigit() and float(amount_1) >= 0:
                    remark_1 = input(f"Remarks: ")
                    expenses[selection[choice.upper()]].append({
                        "amount":float(amount_1),
                        "note":remark_1,
                        "date":today
                    })
                    print(f"Successfully record expenses!\n")
                else:
                    print(f"\n{amount_1} is invalid, please enter a positive whole number.")
            except ValueError:
                print(f"\nInvalid prompt! Please enter a positive value!.")
        else:
            print(f"\nInvalid prompt! Please select from the catalog!")
            continue

#View catalog breakdown
def option_2():
    word1 = "Category"
    word2 = "Subtotal ($)"
    total = 0
    subtotal = 0
    total_items = sum(len(items) for items in expenses.values())
    print(f"==========================================================================================")
    print(f"                          Catalog Breakdown - {current_month}                             ")
    print(f"==========================================================================================")
    if not total_items:
        print(f"Unable to display catalog breakdown since there are no spending in {current_month}\n")
    else:
        print(f"{word1:<20}{word2:<18}")
        print(f"------------------------------------------------------------------------------------------")
        for category,info in expenses.items():
            subtotal = sum(item["amount"] for item in info)
            total += subtotal
            print(f"{category:<20}{subtotal:>12.2f}")
        print(f"------------------------------------------------------------------------------------------")
        print(f"Total spending : ${total:.2f}")
        print(f"==========================================================================================")

# Display summary report
def option_3():
    word1 = "Category"
    word2 = "Cost ($)"
    word3 = "Remarks"
    word4 = "Date"
    total = 0
    total_items = sum(len(items) for items in expenses.values())
    print(f"==========================================================================================")
    print(f"                       Full financial report - {current_month}                            ")
    print(f"==========================================================================================")
    if not total_items:
        print(f"Unable to display financial summary since there are no spending in {current_month}")
    else:
        print(f"{word1:<20}{word2:>12}{word3:>15}{word4:>15}")
        print(f"------------------------------------------------------------------------------------------")
        for category,info in expenses.items():
            counter = 0
            for i in range(len(info)):
                amount_2 = info[i]["amount"]
                total += amount_2
                if counter == 0:
                    print(f"{category:<20}{amount_2:>12.2f}{info[i]["note"]:>15}{info[i]["date"]:>15}")
                    counter += 1
                elif counter >= 1:
                    print(f"{'':<20}{amount_2:>12.2f}{info[i]["note"]:>15}{info[i]["date"]:>15}")
            print()
        print(f"------------------------------------------------------------------------------------------")
        print(f"Monthly budget : ${monthly_budget:.2f}")
        print(f"Total spending : ${total:.2f}")
        remain_balance = monthly_budget - total
        print(f"Remain balance : ${remain_balance:.2f}")
        tolerance = 30
        try:
            percentage = (remain_balance/monthly_budget)*100
        except ZeroDivisionError:
            percentage = 0
        if percentage <= 0:
            sign = "Over Budget!"
        elif percentage <= tolerance:
            sign = "Warning! Near to limit!"
        else:
            sign = "Under budget."
        print(f"Usage (%)      : {100-round(percentage)}%")
        print(f"Status         : {sign}")
        print(f"==========================================================================================")

#Update monthly budget limit
def option_4():
    global monthly_budget
    print(f"==========================================================================================")
    print(f"                            Update budget - {current_month}                               ")
    print(f"==========================================================================================")
    print(f"Remaining budget : ${monthly_budget:.2f}")
    budget = input(f"\nPlease enter your monthly budget: $")
    clean_budget = budget.replace(".","",1)
    if clean_budget.isdigit() and float(budget)>=0:
        monthly_budget = float(budget)
        print(f"Successfully added budget!\nCurrent budget is ${monthly_budget:.2f}.")
    else:
        print(f"Error! Please enter a positive value.\n")

#Reveal archive
def option_5():
    print(f"==========================================================================================")
    print(f"                                 Reveal archive                                           ")
    print(f"==========================================================================================")
    if not expenses_history:
        print(f"No historical archives found. Archive will be updated automatically every month.")
        return

    month_list = list(expenses_history.keys())
    print(f"{'No':<5}{'Month':<15}{'Total budget ($)':>18}{'Total spent ($)':>18}")
    for index,month in enumerate(expenses_history,start=1):
        print(f"{index:<5}{month:<15}{expenses_history[month]["monthly_budget"]:>18.2f}{expenses_history[month]["total_spending"]:>18.2f}")
    print(f"------------------------------------------------------------------------------------------")
    choice = input(f"Please select your choice (1 to {index}): ")
    if choice.isdigit() and int(choice) > 0:
        idx = int(choice)-1
        if 0<= idx < len(month_list):
            month_idx = month_list[idx]
            selected_month = expenses_history[month_idx]
            month_budget = selected_month.get("monthly_budget",0)
            total_spent = selected_month.get("total_spending",0)
            past_expenses = selected_month["expenses"]
            remain_balance = month_budget - total_spent
            tolerance = 30
            try:
                percentage = (remain_balance/month_budget)*100
            except ZeroDivisionError:
                percentage = 0
            if percentage <= 0:
                sign = "Over Budget!"
            elif percentage <= tolerance:
                sign = "Warning! Near to limit!"
            else:
                sign = "Under budget."
            print()
            print(f"==========================================================================================")
            print(f"                         Past financial report - {month_idx}                              ")
            print(f"==========================================================================================")
            print(f"{'Category':<20}{'Cost ($)':>12}{'Remarks':>15}{'Date':>15}")
            print(f"------------------------------------------------------------------------------------------")
            for cat,info in past_expenses.items():
                counter = 0
                for items in info:
                    if counter == 0:
                        print(f"{cat:<20}{items["amount"]:>12.2f}{items["note"]:>15}{items["date"]:>15}")
                        counter += 1
                    else:
                        print(f"{'':<20}{items["amount"]:>12.2f}{items["note"]:>15}{items["date"]:>15}")
            print(f"------------------------------------------------------------------------------------------")
            print(f"Monthly budget : ${month_budget:.2f}")
            print(f"Total spending : ${total_spent:.2f}")
            print(f"Remain balance : ${remain_balance:.2f}")
            print(f"Usage (%)      : {100-round(percentage)}%")
            print(f"Status         : {sign}")
            print(f"==========================================================================================")
    else:
        print(f"Invalid Prompt!")

def main():
    load_data()
    while True:
        print(f"\n==========================================================================================")
        print(f"                    Personal expenses tracker - {current_month}                           ")
        print(f"==========================================================================================")
        print(f"1. Add expenses")
        print(f"2. View catalog breakdown")
        print(f"3. View full report summary")
        print(f"4. Update budget")
        print(f"5. Reveal archived expenses")
        print(f"6. Save and Exit")
        print(f"------------------------------------------------------------------------------------------")
        choice = input(f"Please select from (1-6): ")
        if choice == "6":
            save_data()
            break
        elif choice == "1":
            print()
            option_1()
            save_data()
            print()
        elif choice == "2":
            print()
            option_2()
            print()
        elif choice == "3":
            print()
            option_3()
            print()
        elif choice == "4":
            print()
            option_4()
            save_data()
            print()
        elif choice == "5":
            print()
            option_5()
            print()
        else:
            print(f"\nInvalid prompt! Please select from (1-6).\n")
            continue

if __name__ == "__main__":
    main()


# In[ ]:




