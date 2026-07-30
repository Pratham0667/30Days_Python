import json
import os
from collections import Counter

def most_spoken_languages(filename, top_n=10):
    if not os.path.exists(filename):
        filename = os.path.join("data", os.path.basename(filename))

    try:
        with open(filename, 'r', encoding='utf-8') as file:
            countries_data = json.load(file)
            
        all_languages = []
        
        for country in countries_data:
            languages = country.get('languages', [])
            
            if isinstance(languages, dict):
                all_languages.extend(languages.values())
            elif isinstance(languages, list):
                all_languages.extend(languages)
        
        language_counts = Counter(all_languages)
        
        top_languages = language_counts.most_common(top_n)
        
        return [(count, name) for name, count in top_languages]

    except FileNotFoundError:
        return f"Error: File '{filename}' not found."
    except json.JSONDecodeError:
        return "Error: Invalid JSON format in the file."
    except Exception as e:
        return f"An error occurred: {e}"  
