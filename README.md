# Restaurant Data Interface

This project fetches restaurant data from the Just Eat API using a postcode (SE8 3NB) and displays key information in a simple console interface.

The application extracts and displays:
- Name
- Cuisines
- Rating
- Address

Only the first 10 restaurants are shown.

Used:
- Terminal/bash
- VSC/Python

The application is structured into separate modules to improve readability and maintainability:

- main.py: Entry point of the application, responsible for running the program and displaying output
- api.py: Handles API requests and returns restaurant data
- parser.py: Extracts and formats relevant restaurant information

This separation ensures the code is easier to understand, test, and extend.

How to run:

1. Clone the repository:
git clone <your-repo-link>

2. Navigate into the project folder:
cd restaurant-app

3. Install dependencies:
pip3 install -r requirements.txt

4. Run the application:
python3 main.py


To run unit tests:
pytest

Assumptions: 
- The API always returns restaurant data in the expected format
- All restaurants include name, cuisines, rating, and address fields

Errors encountered:

- Encountered an issue where the API response could not be parsed as JSON.
This was resolved by adding a User-Agent header to the request, which I found out is  required by some APIs.

- Faced module import issues when running tests.
This was fixed by adjusting the Python path to include the project root, because Python couldn’t locate my project files.

Future improvements:

- Add a user interface/allow users to input different postcodes
- Improve error handling for missing or incomplete data
- Add more comprehensive unit tests
