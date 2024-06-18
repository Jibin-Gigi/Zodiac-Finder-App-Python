import streamlit as st

def zodiac_finder(date, month):
    month = month.lower()
    if month == "january":
        if date <= 19:
            return "Capricorn"
        else:
            return "Aquarius"
    elif month == "february":
        if date <= 18:
            return "Aquarius"
        else:
            return "Pisces"
    elif month == "march":
        if date <= 20:
            return "Pisces"
        else:
            return "Aries"
    elif month == "april":
        if date <= 19:
            return "Aries"
        else:
            return "Taurus"
    elif month == "may":
        if date <= 20:
            return "Taurus"
        else:
            return "Gemini"
    elif month == "june":
        if date <= 20:
            return "Gemini"
        else:
            return "Cancer"
    elif month == "july":
        if date <= 22:
            return "Cancer"
        else:
            return "Leo"
    elif month == "august":
        if date <= 22:
            return "Leo"
        else:
            return "Virgo"
    elif month == "september":
        if date <= 22:
            return "Virgo"
        else:
            return "Libra"
    elif month == "october":
        if date <= 22:
            return "Libra"
        else:
            return "Scorpio"
    elif month == "november":
        if date <= 21:
            return "Scorpio"
        else:
            return "Sagittarius"
    elif month == "december":
        if date <= 21:
            return "Sagittarius"
        else:
            return "Capricorn"
    else:
        return "Invalid input"

def main():
    st.title("Zodiac Sign Finder")
    st.write("Enter your Date of Birth in 'Date/Month' format (e.g., 08/May)")

    dob = st.text_input("Date of Birth")
    if dob:
        try:
            date, month = dob.split('/')
            date = int(date)
            sign = zodiac_finder(date, month)
            st.write(f"Your zodiac sign is: {sign}")
        except ValueError:
            st.write("Invalid input format. Please enter in 'Date/Month' format (e.g., 08/May).")

if __name__ == "__main__":
    main()
