import os

def generate_invitations(template, attendees):
    # Check input types
    if not isinstance(template, str):
        print("Error: Template should be a string.")
        return
    if not isinstance(attendees, list) or not all(isinstance(att, dict) for att in attendees):
        print("Error: Attendees should be a list of dictionaries.")
        return

    # Handle empty inputs
    if template.strip() == "":
        print("Error: Template is empty, no output files generated.")
        return
    if not attendees:
        print("No data provided, no output files generated.")
        return

    # Process each attendee
    for index, attendee in enumerate(attendees, start=1):
        # Replace placeholders with values or "N/A" if missing
        invitation_content = template
        for key in ["name", "event_title", "event_date", "event_location"]:
            value = attendee.get(key, "N/A") or "N/A"
            placeholder = "{" + key + "}"
            invitation_content = invitation_content.replace(placeholder, value)
        
        # Generate the output file name
        output_file = f"output_{index}.txt"

        # Write to file
        with open(output_file, 'w') as file:
            file.write(invitation_content)
        
        print(f"Generated {output_file}")
