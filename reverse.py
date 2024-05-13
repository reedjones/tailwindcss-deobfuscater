from cssutils import parseString
import requests
import re



target_url = "<some obsfucated css file>"


original_sample = "https://tailwindcss.com/_next/static/css/de5d245bb39fc7b9.css" #< - this is just a random compiled tailwind from the offical site, need to find a reliable way to fetch 


def get_npm_url(version):
    return "https://www.npmjs.com/package/tailwindcss/v/{verison}"


def fetch_remote_css(url):
    try:
        # Send a GET request to the URL to fetch the CSS content
        response = requests.get(url)
        
        # Check if the request was successful (status code 200)
        if response.status_code == 200:
            # Return the content of the CSS file
            return response.text
        else:
            print("Error: Failed to fetch CSS file. Status code:", response.status_code)
            return None
    except requests.RequestException as e:
        print("Error: Failed to fetch CSS file:", e)
        return None




def extract_tailwind_version(css_content):
    # Regular expression pattern to match Tailwind version
    version_pattern = r'! tailwindcss v([\d.]+)'
    
    # Search for version pattern in the CSS content
    match = re.search(version_pattern, css_content)
    
    if match:
        return match.group(1)
    else:
        return None


def test_extract_tailwind_verison():
    css_content = fetch_remote_css(target_url)
    content = extract_tailwind_version(css_content)
    print(content)



# Parse original stylesheet


# Build mapping between obfuscated and valid class names
def deobfuscate_css(obfuscated_css, original_css):
    original_parser = parseString(original_css)
    original_rules = original_parser.cssRules

    # Parse obfuscated stylesheet
    obfuscated_parser = parseString(obfuscated_css)
    obfuscated_rules = obfuscated_parser.cssRules
    mapping = {}
    matches = 0 
    for obfuscated_rule in obfuscated_rules:
        print(f"Found {matches} matches")
        if obfuscated_rule.type == obfuscated_rule.STYLE_RULE:
            obfuscated_class = obfuscated_rule.selectorText.strip('.')
            obfuscated_style = obfuscated_rule.style.cssText
            for original_rule in original_rules:
                print(f"testing {original_rule}")

                if original_rule.type == original_rule.STYLE_RULE:
                    original_class = original_rule.selectorText.strip('.')
                    original_style = original_rule.style.cssText
                    if obfuscated_style == original_style:
                        matches += 1 
                        print(f"match {matches}")
                        mapping[obfuscated_class] = original_class
                        break

    print(mapping)


def test_deobsfuscate_simple():
  # Original stylesheet
    original = """
    .class1 {color: red; }
    .class2 {font-size: 16px; }
    """
  
    # Obfuscated stylesheet
    obfuscated = """
    .ajfirkv {color: red; }
    .hfgiusd {font-size: 16px; }
    """
    deobfuscate_css(obfuscated, original)

def test_deobsfuscate_live():
    obs = fetch_remote_css(target_url)
    org = fetch_remote_css(original_sample)
    deobfuscate_css(obs, org)

if __name__ == '__main__':
    # test_extract_tailwind_verison()
    test_deobsfuscate_simple()
