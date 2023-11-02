import argparse
import requests
import re
import sys

def help_message():
    print("""vpl: No arguments found\n-h, --help for more information.\n-s, --search to search for template fields""")

# Use GET request to pull a specified package template
def get_template(package_name):
    url = f"https://raw.githubusercontent.com/void-linux/void-packages/master/srcpkgs/{package_name}/template"
    response = requests.get(url)
    if response.status_code == 200:
        content = response.text
        return content
    else:
        print(f"GET Request failed. Status code: {response.status_code}")
        sys.exit(1)

# Outputs package templates specified fields, eg. checksum
def output_argument(template_text, var_name):
    if var_name == "search":
        var_name = input("Search: ")

    arg_match = re.search(rf'^{var_name}=\s*("([^"]*)"|(\S+))', template_text, re.MULTILINE)
    if arg_match:
        argument = arg_match.group(2) or arg_match.group(3)
        print(f"{argument}")
    else:
        print(f"No {var_name} information found.")

def output_template(template_text):
    print(template_text)

def output_keywords():
    print("""Common keywords for search:
          - makedepends
          - depends
          - distfiles
          - homepage
          - version
          - checksum
          - short_desc
          - license
          - maintainer
          - hostmakedepends
          - build_style
          - revision
          - pkgname
          """)
def main():
    parser = argparse.ArgumentParser(description="void-package-lookup 0.1")
    parser.add_argument("-s", "--search", metavar='<package-name>', help="search for a field")
    parser.add_argument("-p", "--package", metavar='<package-name>', help="show package template")
    parser.add_argument("-m", "--makedepends",  metavar='<package-name>', help="show make dependencies")
    parser.add_argument("-c", "--checksum", metavar='<package-name>', help="show package checksum")
    parser.add_argument("-v", "--version", metavar='<package-name>', help="show package version")
    parser.add_argument("-d", "--distfiles", metavar='<package-name>', help="show distfiles")
    parser.add_argument("-k", "--keywords", action="store_true", help="show common keywords for search argument")

    args = parser.parse_args()

    if not any(vars(args).values()):
        help_message()
        sys.exit(1)
    
    if args.keywords:
        output_keywords()
        sys.exit(0)

    package_name = None
    for arg_name, value in vars(args).items():
        if value:
            package_name = value
            break

    template_text = get_template(package_name)

    if args.package:
        output_template(template_text)
    elif args.makedepends:
        output_argument(template_text, "makedepends")
    elif args.checksum:
        output_argument(template_text, "checksum")
    elif args.version:
        output_argument(template_text, "version")
    elif args.distfiles:
        output_argument(template_text, "distfiles")
    elif args.search:
        output_argument(template_text, "search")
    elif args.keywords:
        output_keywords()

if __name__ == "__main__":
    main()
