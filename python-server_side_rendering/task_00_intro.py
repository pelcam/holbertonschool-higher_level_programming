import os

def generate_invitations(template, attendees):

    if not isinstance(template, str):
        print("Template is not a string")
        return

    if not isinstance(attendees, list) or not all(
            isinstance(item, dict) for item in attendees):
        print("Attendees is not a list of dictionaries")
        return

    if not template:
        print("Template is empty, no output files generated.")
        return

    if not attendees:
        print("No data provided, no output files generated.")
        return

    for index, attendee in enumerate(attendees, start=1):
        try:
            # Create an invitation using the "template"
            invitation = template
            # Replace {name} in invitation with the value
            # from the "name" key obtained through get in attendee
            invitation = invitation.replace(
                "{name}", attendee.get("name") or "N/A")
            invitation = invitation.replace(
                "{event_title}", attendee.get("event_title") or "N/A")
            invitation = invitation.replace(
                "{event_date}", attendee.get("event_date") or "N/A")
            invitation = invitation.replace(
                "{event_location}", attendee.get("event_location") or "N/A")

            # Create the output file name
            output_filename = f"output_{index}.txt"

            # Check if the file exists
            if os.path.exists(output_filename):
                print(f"The file '{output_filename}' already exists, "
                      "it will not be overwritten")
                continue

            # Write to the file
            with open(output_filename, "w") as file:
                file.write(invitation)
                print(f"Invitation successfully written to "
                      f"'{output_filename}'.")

        except Exception as e:
            print(f"Error: An error occurred while generating "
                  f"'{output_filename}': {e}")
