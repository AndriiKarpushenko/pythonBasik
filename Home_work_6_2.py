
number_of_seconds = int(input("Введіть кількість секунд: "))

if number_of_seconds < 0 or number_of_seconds >= 8640000:
    print("Число повинно бути більше або дорівнювати 0 і менше ніж 8640000.")
else:
    number_days_seconds_remaining = (number_of_seconds // 86400, number_of_seconds % 86400)
    number_hours_seconds_remaining = (number_days_seconds_remaining[1] // 3600, number_days_seconds_remaining[1] % 3600)
    number_minutes_seconds_remaining = (number_hours_seconds_remaining[1] // 60, number_hours_seconds_remaining[1] % 60)

    num_days = number_days_seconds_remaining[0]
    num_hours = number_hours_seconds_remaining[0]
    num_minutes = number_minutes_seconds_remaining[0]
    num_seconds = number_minutes_seconds_remaining[1]

    if num_days % 10 == 1 and num_days % 100 != 11:
        day_string = "день"
    elif 2 <= num_days % 10 <= 4 and (num_days % 100 < 10 or num_days % 100 >= 20):
        day_string = "дні"
    else:
        day_string = "днів"

    number_hour_format_time = "{} {}, {}:{}:{}".format(
        num_days,
        day_string,
        str(num_hours).zfill(2),
        str(num_minutes).zfill(2),
        str(num_seconds).zfill(2)
    )

    print(number_hour_format_time)