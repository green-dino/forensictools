import os

# Define the directory tree structure this get_started sets the framework for a Flask App for quick locally hosted locally processed data 
directory_tree = {
    'my_project': {
        'app': {
            'templates': {
                'index.html': '',
                'about.html': '',
                'contact.html': '',
            },
            'static': {
                'css': {
                    'style.css': '',
                    'responsive.css': '',
                },
                'js': {
                    'script.js': '',
                    'jquery.js': '',
                },
                'img': {
                    'logo.png': '',
                    'banner.jpg': '',
                    'icon.png': '',
                },
            },
            'app.py': '',
            'config.py': '',
            'models.py': '',
        },
        'data': {
            'data.csv': '',
            'logs.txt': '',
        },
        'docs': {
            'readme.md': '',
            'documentation.pdf': '',
        },
        'tests': {
            'test_utils.py': '',
            'test_models.py': '',
            'test_views.py': '',
        },
        'requirements.txt': '',
        'README.md': '',
        'LICENSE': '',
    }
}
# Function to create the directory tree
def create_directory_tree(base_path, tree):
    for name, contents in tree.items():
        path = os.path.join(base_path, name)
        if isinstance(contents, dict):
            if not os.path.exists(path):
                os.makedirs(path)
            create_directory_tree(path, contents)
        elif contents:
            with open(path, 'w') as file:
                file.write(contents)

# Prompt the user for the base directory
base_directory = input("Enter the base directory where you want to create the directory tree: ")

# Check if the specified directory exists
if not os.path.exists(base_directory):
    print(f"Error: The specified directory '{base_directory}' does not exist.")
else:
    # Create the directory tree
    create_directory_tree(base_directory, directory_tree)
    print(f"Directory tree created at {base_directory}")