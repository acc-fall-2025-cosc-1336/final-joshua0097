def get_most_likely_ancestor_consensus(dna_string1, dna_string2):
    """
    Find all locations of dna_string2 as a substring of dna_string1.
    
    Args:
        dna_string1: The main DNA string to search in
        dna_string2: The substring to search for
    
    Returns:
        Multiple parameters representing the 1-indexed positions of occurrences
    """
    positions = []
    
    # Search for all occurrences of dna_string2 in dna_string1
    for i in range(len(dna_string1) - len(dna_string2) + 1):
        if dna_string1[i:i + len(dna_string2)] == dna_string2:
            # Add 1 to convert from 0-indexed to 1-indexed
            positions.append(i + 1)
    
    # Return as multiple parameters (unpacked tuple)
    return tuple(positions) if positions else ()


def validate_dna_string(dna_string, min_length=None, max_length=None, exact_length=None):
    """
    Validate a DNA string contains only valid characters and meets length requirements.
    
    Args:
        dna_string: The DNA string to validate
        min_length: Minimum length (exclusive)
        max_length: Maximum length (inclusive)
        exact_length: Exact required length
    
    Returns:
        True if valid, False otherwise
    """
    # Check if string contains only valid DNA characters
    valid_chars = set('ACGT')
    if not all(c in valid_chars for c in dna_string.upper()):
        return False
    
    # Check length requirements
    if exact_length is not None and len(dna_string) != exact_length:
        return False
    
    if min_length is not None and len(dna_string) <= min_length:
        return False
    
    if max_length is not None and len(dna_string) > max_length:
        return False
    
    return True

