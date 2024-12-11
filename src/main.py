import lib
import time
from colorama import Fore
from InquirerPy import prompt


def main():
    sites = lib.load_sites("json/sites.json")  # load sites from json file
    last_selection = lib.load_last_selection("json/last_selection.json")  # load last selected sites
    query = lib.get_query()  # get query input from user

    if last_selection:
        # Prompt user for selection method
        answer = prompt([
            {
                "type": "list",
                "name": "selection_method",
                "message": "How do you want to proceed ",
                "choices": ["Use last selection", "Manually select sites again"],
            }
        ])
        choice = answer["selection_method"]
    else:
        print(Fore.YELLOW + "\nNo previous selection found. Proceeding to manual selection..." + Fore.RESET)
        choice = "Manually select sites again"

    # Process choice
    if choice == "Use last selection" and last_selection:
        selected_sites = last_selection
    else:
        selected_sites = lib.get_site_choices(sites)
        if not selected_sites:
            print(Fore.RED + "No sites selected...\n" + Fore.RESET)
            time.sleep(3)
            return

    # Save last selection and construct URLs
    lib.save_last_selection(selected_sites, "json/last_selection.json")
    urls = [lib.construct_url(sites[site], query) for site in selected_sites]
    lib.open_in_browser(urls)


if __name__ == "__main__":
    main()
