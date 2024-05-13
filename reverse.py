from cssutils import parseString
import requests
import re
import typer
from typing_extensions import Annotated
import contextlib

app = typer.Typer()


@app.command()
def main(obsfuscated_url: Annotated[str, typer.Argument(help="Url of the obsfuscated css")], 
         normal_url: Annotated[str, typer.Argument(help="Url containing normal (non-obsfuscated) tailwindcss")]):
    obs = fetch_remote_css(obsfuscated_url)
    org = fetch_remote_css(normal_url)
    deobfuscate_css(obs, org)
    


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
    with contextlib.redirect_stdout(None):
        original_parser = parseString(original_css)
        original_rules = original_parser.cssRules
        # Parse obfuscated stylesheet
        obfuscated_parser = parseString(obfuscated_css)
        obfuscated_rules = obfuscated_parser.cssRules
    mapping = {}
    classes = {}
    matched_classes = set()  # Set to keep track of already matched obfuscated class names
    matches = 0 
    total_classes = len(obfuscated_rules)  # Total number of obfuscated classes
    print("DEOBSFUCATOR")
    print("Classes:", total_classes)
    print("Matches:", matches)
    print("Done: 0%", end=" ")
    for obfuscated_rule in obfuscated_rules:
        if obfuscated_rule.type == obfuscated_rule.STYLE_RULE:
            obfuscated_class = obfuscated_rule.selectorText.strip('.')
            obfuscated_style = obfuscated_rule.style.cssText
            if obfuscated_class not in classes:
                classes[obfuscated_class] = {
                    "match": None,
                    "css": obfuscated_style
                }
            if obfuscated_class not in matched_classes:  # Check if the class has not been matched already
                for original_rule in original_rules:
                    if original_rule.type == original_rule.STYLE_RULE:
                        original_class = original_rule.selectorText.strip('.')
                        original_style = original_rule.style.cssText
                        if obfuscated_style == original_style:
                            matches += 1 
                            classes[obfuscated_class]['match'] = original_class
                            mapping[obfuscated_class] = original_class
                            matched_classes.add(obfuscated_class)  # Add the matched class to the set
                            break
        # Update progress bar
        progress = int((len(matched_classes) / total_classes) * 100)
        progress_bar = '-' * progress + '>' + '-' * (100 - progress)
        print(f"\rDone: {progress}% [{progress_bar}]", end="")
    
    print("\nDeobfuscation completed!")
    return mapping, classes


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



def replace_obfuscated_classes(obfuscated_css, mapping):
    for obfuscated_class, original_class in mapping.items():
        obfuscated_css = re.sub(fr'\.{obfuscated_class}', f'.{original_class}', obfuscated_css)
    return obfuscated_css

if __name__ == '__main__':
    # test_extract_tailwind_verison()
    test_deobsfuscate_simple()
