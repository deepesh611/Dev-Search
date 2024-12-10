# IMPORT MODULES
import json                                     # read JSON file
import requests                                 # to check the url status
import inquirer                                 # for Checkboxes
import webbrowser                               # to search on the browser
from colorama import Fore                       # for colored texts
from urllib.parse import urlencode, urljoin     # to generate complete URL



# DEFINE REQUIRED FUNCTIONS
# take input
def get_query():
    query = input(Fore.YELLOW + "\nEnter your search query: " + Fore.RESET)
    return query.strip()


# the checkboxes
def use_checkboxs(options, msg):
    questions = [
        inquirer.Checkbox(
            'selected',
            message=msg,
            choices=list(options.keys())
        )
    ]
    selected = inquirer.prompt(questions)['selected']
    return selected


# get sites from json
def load_sites(file_path):
    with open(file_path, 'r') as f:
        return json.load(f)


# get site choices from the user.
def get_site_choices(options):
    print("\nSelect the sites you want to search:")
    selected_sites = use_checkboxs(options, "Choose sites")
    return selected_sites


# construct a valid search URL
def construct_url(base_url, search_term):
    query = urlencode({'q': search_term})                   # Encode the search term to handle spaces and special characters
    full_url = urljoin(base_url, f"/search?{query}")    # Join the base URL with the query string
    return full_url


# open links in the browser
def open_in_browser(urls):
    success = []
    failed = []

    for url in urls:
        is_valid, error_message = check_url_status(url)
        if is_valid:
            webbrowser.open(url)
            success.append(url)
        else:
            failed.append((url, error_message))

    # Provide feedback to the user
    print(Fore.GREEN + "\nThe following URLs were opened successfully:" + Fore.RESET)
    for url in success:
        print(url)

    if failed:
        print(Fore.RED + "\nThe following URLs encountered an error:" + Fore.RESET)
        for url, error in failed:
            print(f"{url} - Error: {error}")
    print('\n')


# check HTTP status of the URL
def check_url_status(url):
    try:
        response = requests.get(url)
        # Check if the status code is 404 or other errors
        if response.status_code == 404:
            return False, "404 Not Found"
        # You can check for other status codes if needed, e.g. 403 for Forbidden, 500 for Server errors
        elif response.status_code != 200:
            return False, f"Error: {response.status_code}"
        return True, None
    except requests.exceptions.RequestException as e:
        return False, str(e)


# save the user's last selected sites
def save_last_selection(selection, file_path="json/last_selection.json"):
    with open(file_path, 'w') as f:
        json.dump(selection, f)


# load the user's last selected sites
def load_last_selection(file_path="json/last_selection.json"):
    try:
        with open(file_path, 'r') as f:
            return json.load(f)
    except FileNotFoundError:
        return []


