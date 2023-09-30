def get_app_info():
    app_name = input("Enter the Application Name: ")
    critical = input("Is it Critical (Critical/Non-Critical): ")
    fixed_asset = input("Is it a Fixed Asset (Yes/No): ")
    manufacturer = input("Enter the Manufacturer: ")
    comments = input("Enter Comments: ")
    backups = input("Enter Backups Frequency: ")
    return app_name, critical, fixed_asset, manufacturer, comments, backups

def generate_mermaid_diagram(cloud_apps, on_prem_apps):
    mermaid_code = """```mermaid
graph LR\n"""

    # Add Cloud Apps
    mermaid_code += "subgraph CloudApps\n"
    for app_info in cloud_apps:
        mermaid_code += f'    {app_info[0]}[[{app_info[0]}]] -->|{app_info[1]}| Backups\n'
    mermaid_code += "end\n"

    # Add On-Premises Apps
    mermaid_code += "subgraph OnPremApps\n"
    for app_info in on_prem_apps:
        mermaid_code += f'    {app_info[0]}[[{app_info[0]}]] -->|{app_info[1]}| Backups\n'
    mermaid_code += "end\n"

    mermaid_code += "\nstyle CloudApps fill:#e2f0d9,stroke:#6db84f\n"
    mermaid_code += "style OnPremApps fill:#fce4a4,stroke:#ffa726\n```"

    return mermaid_code

def main():
    cloud_apps = []
    on_prem_apps = []

    while True:
        app_type = input("Enter the App Type (Cloud/On-Premises) or 'quit' to exit: ").strip().lower()
        
        if app_type == 'quit':
            break
        
        if app_type == 'cloud':
            app_info = get_app_info()
            cloud_apps.append(app_info)
        elif app_type == 'on-premises':
            app_info = get_app_info()
            on_prem_apps.append(app_info)
        else:
            print("Invalid input. Please enter 'Cloud' or 'On-Premises'.")

    mermaid_code = generate_mermaid_diagram(cloud_apps, on_prem_apps)

    with open("diagram.md", "w") as file:
        file.write(mermaid_code)

    print("\nMermaid diagram saved to diagram.md")

if __name__ == "__main__":
    main()
