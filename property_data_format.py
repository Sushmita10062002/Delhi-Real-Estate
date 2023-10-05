
# extracted format of properties
def data_format(property):
    prop_dict = {}
    try:
        prop_dict["PROP_ID"]= property["PROP_ID"]
    except:
        prop_dict["PROP_ID"] = ''
    try:
        prop_dict["PREFERENCE"] = property["PREFERENCE"]
    except:
        prop_dict["PREFERENCE"] = ''
    try:
        prop_dict["PROPERTY_TYPE"] = property["PROPERTY_TYPE"]
    except:
        prop_dict["PROPERTY_TYPE"] = ''
    try:
        prop_dict["PROP_NAME"] = property["PROP_NAME"]
    except:
        prop_dict["PROP_NAME"] = ''
    try:
        prop_dict["DESCRIPTION"]= property["DESCRIPTION"]
    except:
        prop_dict["DESCRIPTION"] = ''
    try:
        prop_dict["CITY_NAME"] = property["location"]["CITY_NAME"]
    except:
        prop_dict["CITY_NAME"] = ''
    try:
        prop_dict["BUILDING_NAME"] = property["location"]["BUILDING_NAME"]
    except:
        prop_dict["BUILDING_NAME"] = ''
    try:
        prop_dict["LOCALITY_NAME"] = property["location"]["LOCALITY_NAME"]
    except:
        prop_dict["LOCALITY_NAME"] = ''
    try:
        prop_dict["GATED"] = property["GATED"]
    except:
        prop_dict["GATED"] = ''
    try:
        prop_dict["TRANSACT_TYPE"] = property["TRANSACT_TYPE"]
    except:
        prop_dict["TRANSACT_TYPE"] = ''
    try:
        prop_dict["OWNTYPE"] = property["OWNTYPE"]
    except:
        prop_dict["OWNTYPE"] = ''
    try:
        prop_dict["BEDROOM_NUM"] = property["BEDROOM_NUM"]
    except:
        prop_dict["BEDROOM_NUM"] = ''
    try:
        prop_dict["BATHROOM_NUM"] = property["BATHROOM_NUM"]
    except:
        prop_dict["BATHROOM_NUM"] = ''
    try:
        prop_dict["BATHROOM_ATTACHED"] = property["BATHROOM_ATTACHED"]
    except:
        prop_dict["BATHROOM_ATTACHED"] = ''
    try:
        prop_dict["BALCONY_NUM"] = property["BALCONY_NUM"]
    except:
        prop_dict["BALCONY_NUM"] = ''
    try:
        prop_dict["BALCONY_ATTACHED"] = property["BALCONY_ATTACHED"]
    except:
        prop_dict["BALCONY_ATTACHED"] = ''
    try:
        prop_dict["CAPACITY"] = property["CAPACITY"]
    except:
        prop_dict["CAPACITY"] = ''
    try:
        prop_dict["SHARING_COUNT"] = property["SHARING_COUNT"]
    except:
        prop_dict["SHARING_COUNT"] = ''
    try:
        prop_dict["BUILTUP_SQFT"] = property["BUILTUP_SQFT"]
    except:
        prop_dict["BUILTUP_SQFT"] = ''
    try:
        prop_dict["CARPET_SQFT"] = property["CARPET_SQFT"]
    except:
        prop_dict["CARPET_SQFT"] = ''
    try:
        prop_dict["SUPERBUILTUP_SQFT"] = property["BUILTUP_SQFT"]
    except:
        prop_dict["SUPERBUILTUP_SQFT"] = ''
    try:
        prop_dict["FURNISH"] = property["FURNISH"]
    except:
        prop_dict["FURNISH"] = ''
    try:
        prop_dict["FURNISHING_ATTRIBUTES"] = property["FORMATTED"]["FURNISHING_ATTRIBUTES"]
    except:
        prop_dict["FURNISHING_ATTRIBUTES"] = ''
    try:
        prop_dict["FACING"] = property["FACING"]
    except:
        prop_dict["FACING"] = ''
    try:
        prop_dict["AGE"] = property["AGE"]
    except:
        prop_dict["AGE"] = ''
    try:
        prop_dict["FLOOR_NUM"] = property["FLOOR_NUM"]
    except:
        prop_dict["FLOOR_NUM"] = ''
    try:
        prop_dict["TOTAL_FLOOR"] = property["TOTAL_FLOOR"]
    except:
        prop_dict["TOTAL_FLOOR"] = ''
    try:
        prop_dict["FEATURES"] = property["FEATURES"]
    except:
        prop_dict["FEATURES"] = ''
    try:
        prop_dict["LATITUDE"] = property["MAP_DETAILS"]["LATITUDE"]
        prop_dict["LONGITUDE"] = property["MAP_DETAILS"]["LONGITUDE"]
    except:
        prop_dict["LATITUDE"] = ''
        prop_dict["LONGITUDE"] = ''
    try:
        prop_dict["AVAILABILITY"] = property["FORMATTED"]["AVAIL"]["AVAILABILITY"]
    except:
        prop_dict["AVAILABILITY"] = ''
    try:
        prop_dict["SUB_AVAILABILITY"] = property["FORMATTED"]["AVAIL"]["SUB_AVAILABILITY"]
    except:
        prop_dict["SUB_AVAILABILITY"] = ''
    try:
        prop_dict["CORNER_PROPERTY"] = property["CORNER_PROPERTY"]
    except:
        prop_dict["CORNER_PROPERTY"] = ''
    try:
        prop_dict["AVG_PRICE"] = property["FORMATTED"]["AVG_PRICE"]
    except:
        prop_dict["AVG_PRICE"] = ''
    try:
        prop_dict["PRICE_SQFT"] = property["FORMATTED"]["PRICE_SQFT"]
    except:
        prop_dict["PRICE_SQFT"] = ''

    try:
        prop_dict["AMENITIES"] = property["AMENITIES"]
    except:
        prop_dict["AMENITIES"] = ''
    return prop_dict