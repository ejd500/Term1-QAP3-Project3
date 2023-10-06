# Description: QAP 3 - Project 3: A program for Honest Harry to keep track
#                                 of his sales in his used car lot.
# Author: Ellen Dalton
# Date started: June 7, 2023
# Date finished: June 8, 2023

# Imports:

import datetime

# Constants:

BELOW_5000_RATE = 75.00
ABOVE_5000_RATE = 165
TRANSFER_FEE_RATE = 0.01
LUXURY_TAX_RATE = 0.016
HST_RATE = 0.15
FINANCING_FEE_RATE = 39.99

# Inputs:
while True:

    while True:
        allowed_char = set("ABCDEFGHIJKLMNOPQRSTUVWXYZ abcdefghijklmnopqrstuvwxyz-'")
        cus_first_name = input("Enter the customer's first name (enter END to quit): ").title()
        if cus_first_name == "":
            print("Error - customer's first name cannot be blank.")
        elif not set(cus_first_name).issubset(allowed_char):
            print("Error - customer's first name contains invalid characters.")
        else:
            break

    if cus_first_name == "End":
        break

    while True:
        allowed_char = set("ABCDEFGHIJKLMNOPQRSTUVWXYZ abcdefghijklmnopqrstuvwxyz-'")
        cus_last_name = input("Enter the customer's last name: ").title()
        if cus_last_name == "":
            print("Error - customer's last name cannot be blank.")
        elif not set(cus_last_name).issubset(allowed_char):
            print("Error - customer's last name contains invalid characters.")
        else:
            break

    while True:
        phone_num = input("Enter the phone number (##########): ")
        if phone_num == "":
            print("Error - phone number cannot be blank.")
        elif len(phone_num) != 10:
            print("Error - phone number must be 10 digits.")
        elif not phone_num.isdigit():
            print("Error - phone number must be 10 digits.")
        else:
            break

    street_address = input("Enter the street address: ").title()
    city = "St. John's" # input("Enter the city: ").title()
    province = "NL" # input("Enter the province (ex: NL): ").upper()
    postal_code = "A1E2V5" # input("Enter the postal code (ex: A1B0B4): ").upper()

    while True:
        plate_num = input("Enter the plate number (XXX999): ").upper()
        if plate_num == "":
            print("Error - plate number cannot be blank.")
        elif len(plate_num) != 6:
            print("Error - plate number must be 6 characters.")
        elif not plate_num[0:3].isalpha():
            print("Error - plate number must start with 3 letters.")
        elif not plate_num[3:6].isdigit():
            print("Error - plate number must end with 3 numbers.")
        else:
            break

    car_make = input("Enter the car make (ex: Toyota): ").title()

    car_model = input("Enter the car model (ex: Corolla): ").title()

    while True:
        car_year = input("Enter the year the car was made (ex: 2018): ")
        if car_year == "":
            print("Error - car year cannot be blank.")
        elif len(car_year) != 4:
            print("Error - car year must be 4 digits.")
        elif not car_year.isdigit():
            print("Error - car year must be 4 digits.")
        else:
            break

    while True:
        try:
            selling_price = float(input("Enter the selling price of the car (50000.00 or less): "))
        except:
            print("Error - Selling price is not a valid number. Please re-enter.")
        else:
            if selling_price > 50000.00:
                print("Error - Selling price cannot exceed 50000.00. Please re-enter.")
            else:
                break

    while True:
        try:
            trade_in_amt = float(input("Enter the trade-in amount (selling price or less): "))
        except:
            print("Error - Trade-in amount is not a valid number. Please re-enter.")
        else:
            if trade_in_amt > selling_price:
                print("Error - Trade-in amount cannot exceed the selling price. Please re-enter.")
            else:
                break

    salesperson_name = input("Enter the salesperson name: ").title()

    # Calculations

    price_after_trade = selling_price - trade_in_amt

    if selling_price <= 5000.00:
        licence_fee = BELOW_5000_RATE
    else:
        licence_fee = ABOVE_5000_RATE

    transfer_fee = TRANSFER_FEE_RATE * selling_price
    if selling_price > 20000.00:
        transfer_fee = transfer_fee + LUXURY_TAX_RATE*selling_price

    subtotal = price_after_trade + licence_fee + transfer_fee

    hst = HST_RATE*subtotal

    total_sales_price = subtotal + hst

    # Outputs

    print()
    invoice_date = datetime.datetime.now()
    invoice_date_dsp = invoice_date.strftime("%B %d, %Y")
    print(f"Honest Harry Car Sales                     Invoice Date:  {invoice_date_dsp:>s}")
    receipt_no = cus_first_name[0] + cus_last_name[0] + "-" + plate_num[3:6] + "-" + phone_num[6:10]
    print(f"Used Car Sale and Receipt                  Receipt No:      {receipt_no:>11s}")
    print()
    print(f"                                     Sale price:             ${selling_price:>9,.2f}")
    print(f"Sold to:                             Trade Allowance:        ${trade_in_amt:>9,.2f}")
    print("                                     ----------------------------------")
    print(f"     {cus_first_name[0]:<1s}. {cus_last_name:<26s}   Price after Trade:      ${price_after_trade:>9,.2f}")
    print(f"     {street_address:<29s}   Licence Fee:            ${licence_fee:>9,.2f}")
    city_province_postal_dsp = city + "," + province + " " + postal_code
    print(f"     {city_province_postal_dsp:<29s}   Transfer Fee:           ${transfer_fee:>9,.2f}")
    print("                                     ----------------------------------")
    print("Car Details:", " "*23, f"Subtotal:               ${subtotal:>9,.2f}")
    print(" "*36, f"HST:                    ${hst:>9,.2f}")
    year_make_model_dsp = car_year + " " + car_make + " " + car_model
    print(f"     {year_make_model_dsp:<29s}   ----------------------------------")
    print(" "*36, f"Total sales price:      ${total_sales_price:>9,.2f}")
    print("-"*71)
    print(" "*15, "Best used cars at the best prices!")
    print()
    print()
    print(" "*30, "Financing","    Total", "       Monthly")
    print("     # Years", "   # Payments", "       Fee", "       Price", "       Payment")
    print("    ", "-"*60)
    for years in range(1, 5):
        payments = years*12
        financing_fee = years*FINANCING_FEE_RATE
        tot_price = total_sales_price + financing_fee
        monthly_payment = tot_price/payments
        print(f"        {years:>1d}           {payments:>2d}          ${financing_fee:>6.2f}    ${tot_price:>9,.2f}   ${monthly_payment:>8,.2f}")
    print("    ", "-"*60)
    invoice_date_dsp2 = invoice_date.strftime("%d-%b-%y")
    first_payment_date = invoice_date + datetime.timedelta(days=30)
    first_payment_date_dsp = first_payment_date.strftime("%d-%b-%y")
    print(f"     Invoice date: {invoice_date_dsp2.upper():<9s}        First payment date: {first_payment_date_dsp.upper():<9s}")
    print()
    print()

    # Housekeeping

print()
print("Thanks for shopping at Honest Harry Car Sales.")
print("Come again soon.")
print()
