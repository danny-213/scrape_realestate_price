import pandas as pd

import re


def text_to_number(text):
    # Check if the text contains "triệu" (million)
    if "triệu" in text:
        # Remove non-digit characters and multiply by 10^6
        text = re.sub(r'\D', '', text)  # Remove non-digits
        number = int(text) * 10**6
    elif "tỷ" in text and "triệu" not in text:
        # Check if the text contains "tỷ" (billion) and not "triệu" (million)
        # Remove non-digit characters and multiply by 10^9
        text = re.sub(r'\D', '', text)  # Remove non-digits
        number = int(text) * 10**9
    else:
        # If none of the conditions are met, return 0 or handle as needed
        number = 0  # You can change this to a different default value or handle the case differently
    
    return number

# Example usage:
text1 = "3 triệu"
text2 = "2 tỷ"
text3 = "2 tỷ 5 triệu"
number1 = text_to_number(text1)
number2 = text_to_number(text2)
number3 = text_to_number(text3)

print(number1)  # Output: 3000000
print(number2)  # Output: 2000000000
print(number3)  # Output: 0 (or handle as needed)



def convert(path):
    data = pd.read_excel(path)
    data['Price'] = data['Price'].apply(text_to_number)
    print (data['Price'])
    return data

if __name__ == "__main__":
    data = convert("pricing-data.xlsx")
    data.to_excel("converted-pricing-data.xlsx")
