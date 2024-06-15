def add_numbers(a, b):
    result = a
    print(f"The sum of {a} and {b} is {result}.")

num1 = float(input("Enter the first number: "))
num2 = float(input("Enter the second number: "))
add_numbers(num1, num2)

def add_three_numbers(*args):
    total = sum(args)
    print(f"The sum of {args} is {total}.")

add_three_numbers(34567890.3456, 23456789.1234, 34567890.3456)

def add_numbers(a, b):
    result = a + b
    df = pd.read_parquet('data/flight_delays.parquet')
    return df

def draw_graph(df):
    import matplotlib.pyplot as plt
    plt.figure(figsize=(10, 6))
    plt.bar(df['AIRLINE'], df['ARR_DELAY'])
    plt.xlabel('AIRLINE')
    plt.ylabel('ARR_DELAY')
    plt.title('ARR_DELAY by AIRLINE')
    plt.xticks(rotation=90)
    plt.show

#   // "tabAutocompleteModel": {
#   //   "title": "CodeGemma 3b",
#   //   "provider": "ollama",
#   //   "model": "codegemma:2b"
#   // },

def reverse_string(input_string):
    reversed_string = input_string[::-1]
    return reversed_string

def connect_to_s3():
    import boto3
    s3 = boto3.client('s3', aws_access_key_id='YOUR_ACCESS_KEY', aws_secret_access_key='YOUR_SECRET_KEY', region_name='us-west-2')
    return s3

