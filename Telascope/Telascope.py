from bs4 import BeautifulSoup
import requests

# Stellarium API URL
BASE_URL = "http://localhost:8090/api"

def parse_star_data(object_name="Polaris"):
    try:
        # Send the request to the Stellarium API
        response = requests.get(f"{BASE_URL}/objects/info", params={"name": object_name})
        
        # Check for response status
        response.raise_for_status()
        
        # Debug: Print the raw response text
        print("Raw response:", response.text)

        # Parse the HTML response
        soup = BeautifulSoup(response.text, "html.parser")

        # Initialize an empty dictionary to hold all data
        star_data = {}

        # Extract the name (in <h2> tag)
        if soup.h2:
            star_data["Name"] = soup.h2.text.strip()

        # Extract all key-value pairs dynamically
        for line in soup.find_all("br"):
            # Extract the text before the <br> tags
            text = line.previous_sibling.strip() if line.previous_sibling else None

            if text and ":" in text:
                key, value = text.split(":", 1)
                star_data[key.strip()] = value.strip()

        # Print the parsed data
        print("Parsed Star Data:")
        for key, value in star_data.items():
            print(f"{key}: {value}")
        
        return star_data

    except requests.exceptions.RequestException as e:
        print(f"Request Error: {e}")
    except Exception as e:
        print(f"Unexpected Error: {e}")

if __name__ == "__main__":
    star_data = parse_star_data("Polaris")
