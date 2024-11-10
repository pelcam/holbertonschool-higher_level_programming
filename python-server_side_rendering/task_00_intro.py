import os


def generate_invitations(template, attendees):
    """
    Generates invitations for a list of attendees based on a given template.
    Each invitation is saved to a separate text file.

    Parameters:
    template (str): The invitation template to be used.
    attendees (list): A list of dictionaries containing attendee details.
    """

    # Validate inputs
    if not isinstance(template, str):
        raise ValueError("Invalid template: must be a string.")

    if not isinstance(attendees, list) or any(
        not isinstance(attendee, dict) for attendee in attendees
    ):
        raise ValueError("Invalid attendees: must be a list of dictionaries.")

    if not template.strip():
        print("Warning: The template is empty. No invitations\
         will be generated.")
        return

    if not attendees:
        print("Warning: No attendees provided. No invitations\
         will be created.")
        return

    # Process each attendee
    for idx, attendee in enumerate(attendees, start=1):
        try:
            # Create the invitation content by replacing placeholders
            invitation = template.format(
                name=attendee.get("name", "N/A"),
                event_title=attendee.get("event_title", "N/A"),
                event_date=attendee.get("event_date", "N/A"),
                event_location=attendee.get("event_location", "N/A"),
            )

            # Define the output file path
            output_filename = f"invitation_{idx}.txt"

            # Check if the file already exists
            if os.path.exists(output_filename):
                print(f"Notice: '{output_filename}' already exists. "
                      f"Skipping file creation.")
                continue

            # Write the invitation to the file
            with open(output_filename, "w") as file:
                file.write(invitation)
                print(f"Success: Invitation written to '{output_filename}'.")

        except Exception as e:
            print(f"Error: Failed to generate invitation for\
             attendee {idx} - {e}")
