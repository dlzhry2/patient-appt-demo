def format_postcode(postcode: str) -> str:
    """
    Formats a pre-validated postcode to ensure there is a single space before the incode e.g. AA12 7AA
    for more info on UK postcode formats see: https://ideal-postcodes.co.uk/guides/uk-postcode-format
    """
    trimmed_postcode = postcode.strip()

    if " " in trimmed_postcode:
        return " ".join(postcode.split())

    # Adds space to a postcode containing no space e.g. AA127AA
    return trimmed_postcode[:-3] + " " + trimmed_postcode[-3:]
