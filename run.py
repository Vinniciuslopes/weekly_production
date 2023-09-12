def item_pick_data():
    '''Function colects number of items picked per 3 hour  shift'''
    print('Please enter the number of items picked last week.')
    print('The data provided should be 5 numbers separed by commas.')
    
    print('Example: 23,50,60,40')

    data_str = input('Please enter the data here:')
    print(f'The data provided is  {data_str}')

    item_data = data_str.split(',')
    validate_data(item_data)


def validate_data(values):
    '''In the try.function turns strings into intergens'''
    try:
        if len(values) != 5:
            raise ValueError(f'The data provided was not 5 numbers, it was {len(values)}')
    except ValueError as e:
        print(f'Ivalid data:{e} please try again')
        
    

item_pick_data()   

    