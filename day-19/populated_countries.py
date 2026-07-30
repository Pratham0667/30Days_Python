#Read the countries_data.json data file in data directory, create a function that creates a list of the ten most populated countries
import json
import os

def most_populated_countries(filename, top_n=10):
    if not os.path.exists(filename):
        filename = os.path.join("data", os.path.basename(filename))

    try:
        with open(filename, 'r', encoding='utf-8') as file:
            countries_data = json.load(file)
            
        sorted_countries = sorted(
            countries_data, 
            key=lambda x: x.get('population', 0), 
            reverse=True
        )
        
        result = []
        for country in sorted_countries[:top_n]:
            result.append({
                'country': country.get('name', 'Unknown'),
                'population': country.get('population', 0)
            })
            
        return result

    except FileNotFoundError:
        return f"Error: File '{filename}' not found."
    except json.JSONDecodeError:
        return "Error: Invalid JSON format in the file."
    except Exception as e:
        return f"An error occurred: {e}"
