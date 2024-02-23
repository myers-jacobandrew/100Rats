import re

def extract_speeds(speed_text):
    speeds = {}
    
    # Regular expression pattern to match speed values and types
    speed_pattern = r'(\d+)\s*ft\.|\b(\w+)\b\s*(\d*)\s*ft\.'
    
    # Find all matches of speed pattern in the text
    matches = re.findall(speed_pattern, speed_text)
    
    # Iterate through matches and extract speed values
    for match in matches:
        if match[0]:  # If there's a match for numeric speed value
            speed_value = int(match[0])
            speed_type = 'land'  # Default speed type is land
        else:  # If there's a match for non-numeric speed type
            speed_value = int(match[2])
            speed_type = match[1]  # Set speed type
        
        speeds[speed_type] = speed_value  # Add speed to dictionary
    
    return speeds

