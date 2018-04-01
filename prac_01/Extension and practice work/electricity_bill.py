TARIFF_11 = 0.244618
TARIFF_31 = 0.136928
tariff = float(input('Which tariff? 11 or 31: '))
while not tariff == 11 and not tariff == 31:
    print("Incorrect tariff")
    tariff = float(input('Which tariff? 11 or 31: '))
if tariff == 11:
    price_per_kwh = TARIFF_11
elif tariff == 31:
    price_per_kwh = TARIFF_31
daily_use_in_kwh = float(input('Enter daily use in kWh: '))
no_of_days = float(input('Enter number of billing days: '))
total_bill = round((price_per_kwh * daily_use_in_kwh * no_of_days), 2)
print('Estimated bill: $', total_bill)
