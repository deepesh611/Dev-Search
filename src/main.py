
# IMPORT REQUIRED MODULES
import lib
import time
from colorama import Fore



# DEFINE FUNCTIONS
# main function
def main():
    sites = lib.load_sites("json/sites.json")                                                                      # load sites from json file
    last_selection = lib.load_last_selection("json/last_selection.json")                                           # load last selected sites
    query = lib.get_query()                                                                                        # get query input from user

    if last_selection :
        use_last = input(Fore.YELLOW + "\nDo you want to use your last selection of sites? (y/n): " + Fore.RESET).lower()

        if use_last == "y":
            selected_sites = last_selection
        else:
            selected_sites = lib.get_site_choices(sites)
            if not selected_sites:
                print(Fore.RED + "No sites selected..." + Fore.RESET)
                time.sleep(3)
                return
    else:
        selected_sites = lib.get_site_choices(sites)
        if not selected_sites:
            print(Fore.RED + "No sites selected..." + Fore.RESET)
            time.sleep(3)
            return

    lib.save_last_selection(selected_sites, "json/last_selection.json")
    urls = [lib.construct_url(sites[site], query) for site in selected_sites]
    lib.open_in_browser(urls)


if __name__ == "__main__":
    main()
