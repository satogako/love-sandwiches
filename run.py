import gspread
from google.oauth2.service_account import Credentials

SCOPE = [
    "https://www.googleapis.com/auth/spreadsheets",
    "https://www.googleapis.com/auth/drive.file",
    "https://www.googleapis.com/auth/drive"
    ]

CREDS = Credentials.from_service_account_file('creds.json')
SCOPED_CREDS = CREDS.with_scopes(SCOPE)
GSPREAD_CLIENT = gspread.authorize(SCOPED_CREDS)
SHEET = GSPREAD_CLIENT.open('love_sandwiches')

def get_sales_data():
    """
    Get sales figures input from the user.
    """
    while True:
        print("Please enter sales data from the last market.")
        print("Data should be six numbers, separated by commas.")
        print("Example: 10,20,30,40,50,60\n")

        data_str = input("Enter your data here: ")
        
        sales_data = data_str.split(',')
       
        if validate_data(sales_data):
            print('Data is Valid!')
            break
    return sales_data

def validate_data(values):
    '''
    Inside the try, converts all string values into integers.
    Raises ValueError if strings cannot be converted into int,
    or if there aren't exactly 6 values.
    print(values)
    '''
    try:
        [int(value) for value in values]
        if len(values) != 6:
            raise ValueError(
                f'Exactly 6 values requaired, you provided {len(values)}'
            )
    except ValueError as e:
            print(f'Invalid data: {e}, please try againe.\n')
            return False
    return True

def update_sales_worksheet(sales_data):
    """
    Update sales worksheet, add new row with the list data provided
    """
    print("Updating sales worksheet...\n")
    # методом worksheet() отримуэмо доступ до вкладки "sales" у вкладці google таблиці  Love_Sandwiches
    sales_worksheet = SHEET.worksheet("sales") 
    #Метод append_row додає новий рядок у кінець наших даних на вибраному аркуші
    sales_worksheet.append_row(data)
    print("Sales worksheet updated successfully.\n")

data = get_sales_data()
sales_data = [int(num) for num in data]
update_sales_worksheet(sales_data)