#import necessary libraries
import pandas as pd
import matplotlib.pyplot as plt

# Define a function to enter "view mode" for the DataFrame, passing in the current DataFrame as an argument
def viewmode(current_df):
    while True:
        print("View Mode Options:")
        print("1 - Display the Head")
        print("2 - Display the Tail")
        print("3 - Display the shape")
        print("4 - Display the description")
        print("5 - Display the info")
        print("6 - Display column")
        print("7 - Display row")
        print("8 - Display Data Types")
        print("9 - Exit View Mode")
        choice = input("Enter your choice: ")        
        if choice == '1':
            # Display the head of current DataFrame
            print("Displaying the head of the DataFrame:")
            print(current_df.head())
        elif choice == '2':
            # Display the tail of the DataFrame
            print("Displaying the tail of the DataFrame:")
            print(current_df.tail())
        elif choice == '3':
            # Display the shape of the DataFrame
            print("Displaying the shape of the DataFrame:")
            print(current_df.shape)
        elif choice == '4':
            # Display the description of the DataFrame
            print("Displaying the description of the DataFrame:")
            print(current_df.describe())
        elif choice == '5':
            # Display the info of the DataFrame
            print("Displaying the info of the DataFrame:")
            print(current_df.info())
        elif choice == '6':
            # Print a column from the DataFrame
            column_name = input("Enter the column name to print: ")
            # Check if the column name entered exists in the DataFrame
            if column_name in current_df.columns:
                # Print the specified column, use the f and {} syntax to format the string
                print(f"Displaying column '{column_name}':")
                print(current_df[column_name])
            else:
                print(f"Column '{column_name}' does not exist in the DataFrame.")
        elif choice == '7':
            # Print a row from the DataFrame
            row_index = input("Enter the row index to print: ")
            # Check if the row index entered is a valid integer and also within the range of the DataFrame
            #try/except block to handle potential errors, exception would be a value error if the input is not an integer
            try:
                row_index = int(row_index)
                if 0 <= row_index < len(current_df):
                    print(f"Displaying row {row_index}:")
                    print(current_df.iloc[row_index])
                else:
                    print("Row index out of range.")
            except ValueError:
                print("Invalid row index. Please enter a valid integer.")
        elif choice == '8':
            # Display the data types of the DataFrame
            print("Displaying the data types of the DataFrame:")
            print(current_df.dtypes)
        elif choice == '9':
            # Exit view mode
            print("Exiting view mode.")
            break
        else:
            # If the user enters an invalid choice (anything else), print an error message
            print("Invalid choice. Please try again.")

#define a function to enter "edit mode" for the DataFrame, passing in the current DataFrame as an argument
def editmode(current_df):
        while True:
            print("Edit Mode Options:")
            print("1 - Filter rows in the DataFrame")
            print("2 - Sort the DataFrame by a column")
            print("3 - Filter columns in the DataFrame ")
            print("7 - Save current dataframe edits")
            print("8 - Exit View Mode")
            choice = input("Enter your choice: ")        
            if choice == '1':
                # Select a column header from the DataFrame
                column_name = input("Enter the column name to select: ")
                # Check if the column name entered exists in the DataFrame
                # if it does, prompt the user to enter a value to filter by
                if column_name in current_df.columns:
                    print(f"Displaying column '{column_name}':")
                    value_choice = input("Enter the value to filter by: ")
                    #create a new Dataframe that filters by the selections made by the user
                    filtered_df = current_df[current_df[column_name] == value_choice]
                    #check the filtered dataframe is not empty
                    if not filtered_df.empty:
                        print("Filtered DataFrame:")
                        print(filtered_df)
                    else:
                        print(f"No rows found with {column_name} = {value_choice}.")   
                else:
                    print(f"Column '{column_name}' does not exist in the DataFrame.")
            elif choice == '2':
                # Select a column header from the DataFrame
                column_name = input("Enter the column name to select: ")
                # Check if the column name entered exists in the DataFrame
                # then prompt the user to enter a choice for sorting
                if column_name in current_df.columns:
                    print(f"Displaying column '{column_name}':")
                    ascending_choice = input("Enter 1 for Ascending, anything else for Descending: ")
                    sorted_df = current_df.sort_values(column_name, ascending=(ascending_choice == '1'))
                    print("Sorted DataFrame:")
                    print(sorted_df) 
                else:
                    print(f"Column '{column_name}' does not exist in the DataFrame.")
            elif choice == '7':
                # Save the current DataFrame edits to a CSV file
                save_path = input("Enter the path to save the edited DataFrame (e.g., 'edited_data.csv'): ")
                #catch any set of exceptions that may occur when attepting to save
                try:
                    current_df.to_csv(save_path, index=False)
                    print(f"DataFrame saved successfully to {save_path}.")
                except Exception as e:
                    print(f"Error saving DataFrame: {e}")
            elif choice == '8':
                print("Exiting edit mode.")
                break
            else:
                print("Invalid choice. Please try again.")

#createmode function
def createmode():
        while True:
            print("Create Mode Options:")
            print("1 - Create a new DataFrame")
            print("2 - Add a new column to the DataFrame")
            print("3 - Add a new row to the DataFrame")
            print("4 - Save current DataFrame")
            print("8 - Exit Create Mode")
            choice = input("Enter your choice: ")        
            if choice == '1':
                # Create a new DataFrame
                print("Creating a new DataFrame...")
                new_df = pd.DataFrame()
                print("New DataFrame created:")
                print(new_df)
            elif choice == '2':
                # Fill data in the DataFrame in a new column
                if 'new_df' in locals():
                    print("New column in the DataFrame...")
                    column_name = input("Enter the column name: ")
                    # Prompt the user to enter values for the new column
                    # Store the values in a list, if the user enters an empty value, replace it with a zero
                    values = input("Enter the values (comma-separated): ").split(',')
                    #if any values in the list are empty, add a zero to the list
                    for value in values:
                        # Check if the value is empty and replace it with '0'
                        if value.strip() == '':
                            values[values.index(value)] = '0'
                    # Add the new column to the DataFrame
                    new_df[column_name] = [value.strip() for value in values]
                    print("Data filled in the DataFrame:")
                    print(new_df)
                else:
                    print("No DataFrame available. Please create a new DataFrame first.")
            elif choice == '3':
                # Fill data in the DataFrame in a new row
                if 'new_df' in locals():
                    print("New row in the DataFrame...")
                    values = input("Enter the values (comma-separated): ").split(',')
                    for value in values:
                        # Check if the value is empty and replace it with '0'
                        if value.strip() == '':
                            values[values.index(value)] = '0'
                    # Add the new row to the DataFrame
                    new_df.loc[len(new_df)] = [value.strip() for value in values]
                    print("New row added to the DataFrame:")
                    print(new_df)
                else:
                    print("No DataFrame available. Please create a new DataFrame first.")
            elif choice == '4':
                # Fill data in the DataFrame
                if 'new_df' in locals():
                    print("Filling data in the DataFrame...")
                    column_name = input("Enter the column name: ")
                    values = input("Enter the values (comma-separated): ").split(',')
                    new_df[column_name] = [value.strip() for value in values]
                    print("Data filled in the DataFrame:")
                    print(new_df)
                else:
                    print("No DataFrame available. Please create a new DataFrame first.")
            elif choice == '8':
                print("Exiting edit mode.")
                break
            else:
                print("Invalid choice. Please try again.")

def plotmode(current_df):
    print("Plotting mode enabled, currently bar chart only")
    plot_title = input("Enter the title for the plot: ")
    plot_names = input("Enter the names column you wish to plot: ")
    plot_values = input("Enter the values column you wish to plot: ")
    df.plot(x=plot_names, y=plot_values, kind='bar', color='teal')
    plt.title(plot_title)
    plt.ylabel(plot_values)
    plt.xlabel(plot_names)
    plt.show()


while True:
    print("Welcome to the DataFrame Explorer!")
    print("Select an option: 1 - Import sample DataFrame, 2 - Import from CSV 'localdata.csv', 3 - Import large scale dataset, 4 - Import csv URL, 5 - Enter view mode,  6 - Enter edit mode, 7 - Create Mode, 8 - Plot Mode, 9 - Exit ")
    choice = input("Enter your choice: ")
    if choice == '1':
        # Create a sample DataFrame
        sample_data = {'Name': ['Alice', 'Bob', 'Charlie'],
                       'Age': [25, 30, 35],
                       'City': ['New York', 'Los Angeles', 'Chicago']}
        #send that DataFrame to the variable df
        df = pd.DataFrame(sample_data)
        #print it
        print("Sample DataFrame created:")
        print(df)
    elif choice == '2':
        # Import DataFrame from a CSV file
        print("Importing DataFrame from a CSV file")
        file_path = ('sampledata.csv')
        # Attempt to read the CSV file into a DataFrame
        try:
            # Read the CSV file into a DataFrame and confirm it
            df = pd.read_csv(file_path)
            print("DataFrame imported from CSV:")
            print(df)
        #if exception occurs, print error message
        except Exception as e:
            print(f"Error importing CSV: {e}")
    #On choice 3, import a large scale dataset
    elif choice == '3':
        # Import a large scale dataset
        print("Importing large scale dataset...")
        try:
            df = pd.read_csv('titanic.csv')
            print("Large scale dataset imported:")
        except Exception as e:
            print(f"Error importing large scale dataset: {e}")
    elif choice == '4':
        # Enter url to import a DataFrame
        print("Enter URL to import, eg 'https://docs.google.com/spreadsheets/d/1YgY-TBsLrmMnrT_vBBHMUXB6O8erVM91HOWK4cLZhgs/export?format=csv':")
        target_url = input("Enter URL: ")
        try:
            df = pd.read_csv(target_url)
            print("DataFrame imported from URL:")
            print(df)
        except Exception as e:
            print(f"Error importing DataFrame from URL: {e}")
    elif choice == '5':
        # Enter view mode to display the DataFrame
        if 'df' in locals():
            print("Entering view mode for Current DataFrame:")
            print(df)
            viewmode(df)
        else:
            print("No DataFrame available. Please import a DataFrame first.")
    elif choice == '6':
        # Enter edit mode to change the DataFrame
        if 'df' in locals():
            print("Entering edit mode for Current DataFrame:")
            print(df)
            editmode(df)
        else:
            print("No DataFrame available. Please import a DataFrame first.")
    elif choice == '7':
        # Enter create mode to create a new custom DataFrame
        if 'df' not in locals():
            print("Creating a custom DataFrame:")
            createmode()
        else:
            print("A DataFrame already exists. Are you sure you wish to proceed? (y/n)")
            confirm = input("Enter 'y' to proceed or 'n' to cancel: ")
            if confirm.lower() == 'y':
                createmode()
            else:
                print("Cancelled creating a new DataFrame.")
    elif choice == '8':
        # Enter plotting mode to visualize the DataFrame
        if 'df' in locals():
            print("Entering plot mode for Current DataFrame:")
            print(df)
            plotmode(df)
        else:
            print("No DataFrame available. Please import a DataFrame first.")
    elif choice == '9':
        print("Exiting the program.")
        break
    else:
        print("Invalid choice. Please try again.")
