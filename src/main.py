import lib
import time
from colorama import Fore
from InquirerPy import prompt


def main():
    urls = []
    sites = lib.load_sites("json/sites.json")  # Load sites from JSON file
    last_selection = lib.load_last_selection("json/last_selection.json")  # Load last selected sites
    query = lib.get_query()  # Get query input from user

    search_path = None
    selected_sites = []

    # Prompt user for selection method
    if last_selection:
        answer = prompt([
            {
                "type": "list",
                "name": "selection_method",
                "message": "How do you want to proceed?",
                "choices": ["Use last selection", "Select by Category", "Manually select sites"],
            }
        ])
        choice = answer["selection_method"]
    else:
        print(Fore.YELLOW + "\nNo previous selection found. Proceeding to manual selection..." + Fore.RESET)
        choice = "Manually select sites"

    # Handle user choice
    if choice == "Use last selection" and last_selection:
        selected_sites = last_selection

    elif choice == "Select by Category":
        categories = lib.get_unique_categories(sites)  # Get unique categories
        category_answer = prompt([
            {
                "type": "list",
                "name": "category",
                "message": "Choose a category:",
                "choices": categories,
            }
        ])
        selected_category = category_answer["category"]

        # Update search_path for specific categories
        if selected_category == "Web Development":
            search_path = "/components/"

        selected_sites = lib.filter_sites_by_category(sites, selected_category)

        if not selected_sites:
            print(Fore.RED + "No sites found for the selected category.\n" + Fore.RESET)
            time.sleep(2)
            return

    elif choice == "Manually select sites":
        selected_sites = lib.get_site_choices(sites)

        if not selected_sites:
            print(Fore.RED + "No sites selected...\n" + Fore.RESET)
            time.sleep(3)
            return

    # Save the current selection and construct URLs
    lib.save_last_selection(selected_sites, "json/last_selection.json")
    for site in selected_sites:
        urls.append(lib.construct_url(
                sites[site]["baseurl"],
                query,
                sites[site].get("search_path", "/search?q=")
            ))

    lib.open_in_browser(urls)


if __name__ == "__main__":
    main()
