from Kernel.Modules._Core.DeterministicFunction._search_open_registry import _search
from Kernel.Modules._Core.DeterministicFunction._post import _post
from Kernel.Modules._Core.DeterministicFunction._generate_truth_cert import _generate_truth_cert
from Kernel.Modules._Core.DeterministicFunction._validate_truth_integrity import _validate_truth_integrity
from Kernel.Modules._Core.main import Core

# ******************************
# InputOutputTransformer
# ******************************


class TabularDataCleaner(Core):
    import pandas as pd

    '''
    OBJECTIVE:
    The objective of this module is to help you clean tabular data
    things i can do:
    1. 

    LOGIC:
    
    
    EXAMPLE:
    
    '''
    
    

    def __init__(self, data=None):
        # Call the constructor of the parent class
        super().__init__(input_objective='Clean and prepare tabular data')
        self.data = data
    

    def load_data(self, file_path):
        """
        Load tabular data from a file.
        """
        if self.is_csv(file_path):
            self.data = pd.read_csv(file_path)
        elif self.is_tsv(file_path):
            self.data = pd.read_csv(file_path, delimiter='\t')
        else:
            raise ValueError("Unsupported file type. Only CSV and TSV files are supported.")

    def is_csv(self, file_path):
        """
        Check if the file has a CSV extension.
        """
        return file_path.lower().endswith('.csv')

    def is_tsv(self, file_path):
        """
        Check if the file has a TSV extension.
        """
        return file_path.lower().endswith(('.tsv', '.txt'))

    def display_data(self, num_rows=5):
        """
        Display the first few rows of the data.
        """
        print(self.data.head(num_rows))

    def check_missing_values(self):
        """
        Check for missing values in the data.
        """
        missing_values = self.data.isnull().sum()
        print("Missing Values:\n", missing_values)

    def remove_duplicates(self):
        """
        Remove duplicate rows from the data.
        """
        self.data = self.data.drop_duplicates()
        print("Duplicates removed.")

    def handle_missing_values(self, strategy='mean'):
        """
        Handle missing values using a specified strategy (default is mean).
        Other strategies: 'median', 'mode', 'ffill', 'bfill', etc.
        """
        self.data.fillna(self.data.mean(), inplace=True)
        print(f"Missing values handled using {strategy}.")

    def save_cleaned_data(self, file_path):
        """
        Save cleaned data to a new file.
        """
        self.data.to_csv(file_path, index=False)
        print(f"Cleaned data saved to {file_path}.")

    def execute(self, file_path):
        """
        Execute the data cleaning process.
        """
        print("Loading data...")
        self.load_data(file_path)

        print("\nDisplaying data:")
        self.display_data()

        print("\nChecking for missing values:")
        self.check_missing_values()

        print("\nRemoving duplicates:")
        self.remove_duplicates()

        print("\nHandling missing values:")
        self.handle_missing_values()

        cleaned_file_path = 'cleaned_data.csv'
        print(f"\nSaving cleaned data to {cleaned_file_path}:")
        self.save_cleaned_data(cleaned_file_path)

        print("\nData cleaning process completed.")

# Example usage:
# data_cleaner.run('your_data.csv')
