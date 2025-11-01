from rgbprint import gradient_print, Color
from secure_input import secure_input
from colorama import Fore
import requests
import os
import re

class utility:
    logo = """
    █████████                          █████                           ███████████            █████                                  
   ███░░░░░███                        ░░███                           ░░███░░░░░███          ░░███                                   
  ░███    ░███  █████ █████  ██████   ███████    ██████   ████████     ░███    ░███   ██████  ░███████   ██████  ████████  ████████  
  ░███████████ ░░███ ░░███  ░░░░░███ ░░░███░    ░░░░░███ ░░███░░███    ░██████████   ███░░███ ░███░░███ ███░░███░░███░░███░░███░░███ 
  ░███░░░░░███  ░███  ░███   ███████   ░███      ███████  ░███ ░░░     ░███░░░░░███ ░███████  ░███ ░███░███ ░███ ░███ ░░░  ░███ ░███ 
  ░███    ░███  ░░███ ███   ███░░███   ░███ ███ ███░░███  ░███         ░███    ░███ ░███░░░   ░███ ░███░███ ░███ ░███      ░███ ░███ 
  █████   █████  ░░█████   ░░████████  ░░█████ ░░████████ █████        █████   █████░░██████  ████████ ░░██████  █████     ████ █████
 ░░░░░   ░░░░░    ░░░░░     ░░░░░░░░    ░░░░░   ░░░░░░░░ ░░░░░        ░░░░░   ░░░░░  ░░░░░░  ░░░░░░░░   ░░░░░░  ░░░░░     ░░░░ ░░░░░
""" # Logo art 

    menu = """
                                                    ╔═══                    ═══╗
                                                       [1] Add Avatar to Cart   
                                                       [2] Preview Avatar
                                                    ╚═══                    ═══╝"""

    valid_regions = ["ar-AE", "ar-SA", "ar-KW", "ar-QA", "ar-OM", "ar-BH", "ar-LB", "ch-HK",
"ch-TW", "cs-CZ", "da-DK", "de-AT", "de-CH", "de-DE", "de-LU", "el-GR",
"en-AE", "en-AU", "en-AR", "en-BG", "en-BH", "en-BR", "en-CA", "en-CL",
"en-CO", "en-CR", "en-CY", "en-CZ", "en-DK", "en-EC", "en-FI", "en-GR",
"en-HK", "en-HR", "en-HU", "en-ID", "en-IE", "en-IL", "en-IN", "en-IS",
"en-KW", "en-LB", "en-MT", "en-MY", "en-MX", "en-NO", "en-NZ", "en-OM",
"en-PA", "en-PE", "en-PL", "en-QA", "en-RO", "en-SA", "en-SE", "en-SG",
"en-SI", "en-SK", "en-TH", "en-TR", "en-TW", "en-US", "en-ZA", "en-GB",
"es-AR", "es-BR", "es-CL", "es-CO", "es-CR", "es-EC", "es-ES", "es-GT",
"es-HN", "es-PA", "es-PE", "es-PY", "es-SV", "es-MX", "fi-FI", "fr-BE",
"fr-CA", "fr-CH", "fr-LU", "fr-FR", "hu-HU", "id-ID", "it-CH", "it-IT",
"ja-JP", "ko-KR", "nl-BE", "nl-NL", "no-NO", "pl-PL", "pt-PT", "pt-BR",
"ro-RO", "ru-RU", "ru-UA", "sv-SE", "th-TH", "tr-TR", "vi-VN", "zh-CN",
"zh-HK", "zh-TW"] # List of valid regions


    def add_to_cart(token, avatar_id, region): # Function to add avatar to cart
        try:
            if re.match(r".*-.+-.+", avatar_id) and token != "": # Basic validation for avatar ID and token
                regionx = region.replace("-", "/") # Format region for URL
                parts = regionx.split("/") # Split region into parts
                f_region = parts[0] # First part of region
                s_region = parts[1] # Second part of region
                headers = {
                    'Origin': 'https://checkout.playstation.com', # Origin header
                    'Content-Type': 'application/json', # Content type header
                    'Accept-Language': 'fr-FR,fr;q=0.9,en-US;q=0.8,en;q=0.7', # Accept language header
                    'Cookie': f'AKA_A2=A; pdccws_p={token}; isSignedIn=true; userinfo=6f5bce1b81cd103a24100aa1256323139a6d3bfeb87dcd85d8af32680f68f60f; p=0; gpdcTg=%5B1%5D' # Cookie header with token
                }
                response = requests.get(f'https://store.playstation.com/store/api/chihiro/00_09_000/container/{s_region}/{f_region}/19/{avatar_id}/', headers=headers) # GET request to fetch avatar info
                response.raise_for_status() # Raise error for bad responses
                SkuInfo = response.json() # Parse JSON response
                SkuGET = SkuInfo["default_sku"]["id"] # Extract SKU ID
                payload = {
                    "operationName": "addToCart", # GraphQL operation name
                    "variables": {"skus": [{"skuId": SkuGET}]}, # Variables for the operation
                    "extensions": {"persistedQuery": {"version": 1, "sha256Hash": "93eb198753e06cba3a30ed3a6cd3abc1f1214c11031ffc5b0a5ca6d08c77061f"}} # Persisted query info
                }
                response = requests.post('https://web.np.playstation.com/api/graphql/v1/op', json=payload, headers=headers) # POST request to add avatar to cart
                if "subTotalPrice" in response.text: # Check if the response indicates success
                    return True, "Avatar added to cart successfully" # Success
                else:
                    return False, "Failed to add avatar to cart" # Failure
            else:
                return False, "Invalid Avatar ID or Token" # Invalid input
        except Exception as e:
            return False, str(e) # Return exception message
        
    def get_avatar(avatar_id, region): # Function to get avatar preview URL
        try:
            if re.match(r".*-.+-.+", avatar_id): # Basic validation for avatar ID
                regionx = region.replace("-", "/") # Format region for URL
                parts = regionx.split("/") # Split region into parts
                f_region = parts[0] # First part of region
                s_region = parts[1] # Second part of region
                image_url = f"https://store.playstation.com/store/api/chihiro/00_09_000/container/{s_region}/{f_region}/19/{avatar_id}/image"
                return True, image_url # Return success and image URL
            else:
                return False, "Invalid Avatar ID" # Invalid input
        except Exception as e:
            return False, str(e) # Return exception message

class functions:
    def avatar():
        os.system("cls" if os.name == "nt" else "clear") # Clear the console
        os.system("mode 135,30" if os.name == "nt" else "printf '\e[8;30;135t'") # Set console size
        gradient_print(utility.logo, start_color=Color.sky_blue, end_color=Color.ghost_white) # Print logo with a nice color gradient

        # How to get your Playstation Account Token:
        # 1. Open your browser and go to https://www.playstation.com/
        # 2. Log in to your account
        # 3. Open the developer tools (F12 or right click -> Inspect)
        # 4. Go to the "Application" tab
        # 5. In the left sidebar, under "Storage", click on "Cookies" and select "https://www.playstation.com"
        # 6. Look for the cookie named "pdccws_p" - this is your Playstation Account Token
        token = secure_input(f"{Fore.RESET} [{Fore.LIGHTCYAN_EX}+{Fore.RESET}] Enter your Playstation Account Token >{Fore.LIGHTCYAN_EX} ", show="*") # Secure input for token

        print() # New line for better readability

        # Get the Avatar ID from https://psprices.com/
        # 1. Click on the blue avatar button
        # 2. Select your Region on the Top Left
        # 3. Click on PS3 Avatars for example
        # 4. Click on any Avatar you like
        # 5. Copy the ID next to "Add to Library" or under the Price
        avatar_id = input(f"{Fore.RESET} [{Fore.LIGHTCYAN_EX}+{Fore.RESET}] Enter the Avatar ID >{Fore.LIGHTCYAN_EX} ") # Input for Avatar ID

        print() # New line for better readability

        # List of supported regions:
        # ar-AE, ar-SA, ar-KW, ar-QA, ar-OM, ar-BH, ar-LB, ch-HK,
        # ch-TW, cs-CZ, da-DK, de-AT, de-CH, de-DE, de-LU, el-GR,
        # en-AE, en-AU, en-AR, en-BG, en-BH, en-BR, en-CA, en-CL,
        # en-CO, en-CR, en-CY, en-CZ, en-DK, en-EC, en-FI, en-GR,
        # en-HK, en-HR, en-HU, en-ID, en-IE, en-IL, en-IN, en-IS,
        # en-KW, en-LB, en-MT, en-MY, en-MX, en-NO, en-NZ, en-OM,
        # en-PA, en-PE, en-PL, en-QA, en-RO, en-SA, en-SE, en-SG,
        # en-SI, en-SK, en-TH, en-TR, en-TW, en-US, en-ZA, en-GB,
        # es-AR, es-BR, es-CL, es-CO, es-CR, es-EC, es-ES, es-GT,
        # es-HN, es-PA, es-PE, es-PY, es-SV, es-MX, fi-FI, fr-BE,
        # fr-CA, fr-CH, fr-LU, fr-FR, hu-HU, id-ID, it-CH, it-IT,
        # ja-JP, ko-KR, nl-BE, nl-NL, no-NO, pl-PL, pt-PT, pt-BR,
        # ro-RO, ru-RU, ru-UA, sv-SE, th-TH, tr-TR, vi-VN, zh-CN,
        # zh-HK, zh-TW
        region = input(f"{Fore.RESET} [{Fore.LIGHTCYAN_EX}+{Fore.RESET}] Enter the Region (e.g. en-US, de-DE, ja-JP) >{Fore.LIGHTCYAN_EX} ") # Input for Region

        print() # New line for better readability

        if region not in utility.valid_regions: # Validate region
            print(f"{Fore.RESET} [{Fore.RED}!{Fore.RESET}] Invalid region! Please restart the program and enter a valid region from the list.") # Error message
            return # Exit the program

        print(f"{Fore.RESET} [{Fore.LIGHTGREEN_EX}+{Fore.RESET}] Starting to add Avatar ID {Fore.LIGHTCYAN_EX}{avatar_id}{Fore.RESET} to your account in region {Fore.LIGHTCYAN_EX}{region}{Fore.RESET}...") # Informational message

        success, message = utility.add_to_cart(token, avatar_id, region) # Attempt to add avatar to cart

        if success: # If successful
            print() # New line for better readability
            print(f"{Fore.RESET} [{Fore.LIGHTGREEN_EX}+{Fore.RESET}] Finished processing. Please check your PlayStation Cart to see if the avatar was added successfully.") # Success message
        else:
            print() # New line for better readability
            print(f"{Fore.RESET} [{Fore.RED}!{Fore.RESET}] Process was unsuccessful because:{Fore.RED} {message}") # Failure message

    #########################################################################################################################################################################################################################################

    def preview():
        os.system("cls" if os.name == "nt" else "clear") # Clear the console
        os.system("mode 135,30" if os.name == "nt" else "printf '\e[8;30;135t'") # Set console size
        gradient_print(utility.logo, start_color=Color.sky_blue, end_color=Color.ghost_white) # Print logo with a nice color gradient

        # Get the Avatar ID from https://psprices.com/
        # 1. Click on the blue avatar button
        # 2. Select your Region on the Top Left
        # 3. Click on PS3 Avatars for example
        # 4. Click on any Avatar you like
        # 5. Copy the ID next to "Add to Library" or under the Price
        avatar_id = input(f"{Fore.RESET} [{Fore.LIGHTCYAN_EX}+{Fore.RESET}] Enter the Avatar ID >{Fore.LIGHTCYAN_EX} ") # Input for Avatar ID

        print() # New line for better readability

        # List of supported regions:
        # ar-AE, ar-SA, ar-KW, ar-QA, ar-OM, ar-BH, ar-LB, ch-HK,
        # ch-TW, cs-CZ, da-DK, de-AT, de-CH, de-DE, de-LU, el-GR,
        # en-AE, en-AU, en-AR, en-BG, en-BH, en-BR, en-CA, en-CL,
        # en-CO, en-CR, en-CY, en-CZ, en-DK, en-EC, en-FI, en-GR,
        # en-HK, en-HR, en-HU, en-ID, en-IE, en-IL, en-IN, en-IS,
        # en-KW, en-LB, en-MT, en-MY, en-MX, en-NO, en-NZ, en-OM,
        # en-PA, en-PE, en-PL, en-QA, en-RO, en-SA, en-SE, en-SG,
        # en-SI, en-SK, en-TH, en-TR, en-TW, en-US, en-ZA, en-GB,
        # es-AR, es-BR, es-CL, es-CO, es-CR, es-EC, es-ES, es-GT,
        # es-HN, es-PA, es-PE, es-PY, es-SV, es-MX, fi-FI, fr-BE,
        # fr-CA, fr-CH, fr-LU, fr-FR, hu-HU, id-ID, it-CH, it-IT,
        # ja-JP, ko-KR, nl-BE, nl-NL, no-NO, pl-PL, pt-PT, pt-BR,
        # ro-RO, ru-RU, ru-UA, sv-SE, th-TH, tr-TR, vi-VN, zh-CN,
        # zh-HK, zh-TW
        region = input(f"{Fore.RESET} [{Fore.LIGHTCYAN_EX}+{Fore.RESET}] Enter the Region (e.g. en-US, de-DE, ja-JP) >{Fore.LIGHTCYAN_EX} ") # Input for Region

        print() # New line for better readability

        if region not in utility.valid_regions: # Validate region
            print(f"{Fore.RESET} [{Fore.RED}!{Fore.RESET}] Invalid region! Please restart the program and enter a valid region from the list.") # Error message
            return # Exit the program
        
        print(f"{Fore.RESET} [{Fore.LIGHTGREEN_EX}+{Fore.RESET}] Fetching preview for Avatar ID {Fore.LIGHTCYAN_EX}{avatar_id}{Fore.RESET} in region {Fore.LIGHTCYAN_EX}{region}{Fore.RESET}...") # Informational message

        success, result = utility.get_avatar(avatar_id, region) # Attempt to get avatar preview

        if success: # If successful
            print() # New line for better readability
            print(f"{Fore.RESET} [{Fore.LIGHTGREEN_EX}+{Fore.RESET}] View the Avatar in your Browser") # Informational message
            os.system(f'start {result}' if os.name == "nt" else f'xdg-open {result}') # Open the avatar preview URL in the default browser
        else:
            print() # New line for better readability
            print(f"{Fore.RESET} [{Fore.RED}!{Fore.RESET}] Could not fetch avatar preview because:{Fore.RED} {result}") # Failure message

    def error():
        print() # New line for better readability
        print(f"{Fore.RESET} [{Fore.RED}!{Fore.RESET}] Invalid choice! Please restart the program and select a valid option from the menu.") # Error message

def main():
    os.system("cls" if os.name == "nt" else "clear") # Clear the console
    os.system("mode 135,30" if os.name == "nt" else "printf '\e[8;30;135t'") # Set console size
    gradient_print(utility.logo, start_color=Color.sky_blue, end_color=Color.ghost_white) # Print logo with a nice color gradient
    gradient_print(utility.menu, start_color=Color.sky_blue, end_color=Color.ghost_white) # Print menu with a nice color gradient

    choice = input(f"{Fore.RESET} [{Fore.LIGHTCYAN_EX}+{Fore.RESET}] Enter your choice (1-2) >{Fore.LIGHTCYAN_EX} ") # Input for user choice

    if choice == "1": # If user chooses to add avatar to cart
        functions.avatar() # Call the avatar function
    elif choice == "2": # If user chooses to preview avatar
        functions.preview() # Call the preview function
    else:
        function.error() # Call the error function for invalid choice

if __name__ == "__main__":
    main() # Run the main function