def identify_object(classifications, target_object):
   
    found_blocks = []
    
    for block_name, details in classifications.items():
        if target_object.lower() in details["class"].lower():
            found_blocks.append(block_name)
            
    if found_blocks:
        print(f"Found {target_object} in blocks: {', '.join(found_blocks)}")
    else:
        print(f"{target_object} not found in any blocks.")
    
    return found_blocks
