from homeharvest import scrape_property
from datetime import datetime

# Generate filename based on current timestamp
current_timestamp = datetime.now().strftime("%Y%m%d")
zipcode = [
"Aberdeen", "Airway Heights", "Algona", "Anacortes", "Arlington", "Asotin", "Auburn", "Bainbridge Island", "Battle Ground", 
    "Bellevue", "Bellingham", "Benton City", "Black Diamond", "Blaine", "Bonney Lake", "Bothell", "Bremerton", "Brier", 
    "Buckley", "Burien", "Burlington", "Camas", "Carnation", "Cashmere", "Castle Rock", "Centralia", "Chehalis", 
    "Chelan", "Cheney", "Clarkston", "Cle Elum", "Clyde Hill", "Colfax", "College Place", "Colville", "Connell", 
    "Cosmopolis", "Covington", "Des Moines", "DuPont", "Duvall", "East Wenatchee", "Edgewood", "Edmonds", "Elma", 
    "Ellensburg", "Elmer City", "Entiat", "Enumclaw", "Ephrata", "Everett", "Everson", "Federal Way", "Ferndale", 
    "Fife", "Fircrest", "Forks", "George", "Gig Harbor", "Gold Bar", "Goldendale", "Grandview", "Granger", "Granite Falls", 
    "Hartline", "Hoquiam", "Ilwaco", "Issaquah", "Kahlotus", "Kelso", "Kenmore", "Kennewick", "Kent", "Kettle Falls", 
    "Kirkland", "Kittitas", "La Center", "Lacey", "Lake Forest Park", "Lake Stevens", "Lakewood", "Langley", "Leavenworth", 
    "Liberty Lake", "Long Beach", "Longview", "Lynden", "Lynnwood", "Mabton", "Maple Valley", "Marysville", "Mattawa", 
    "McCleary", "Medina", "Mercer Island", "Mesa", "Mill Creek", "Millwood", "Milton", "Monroe", "Montesano", "Morton", 
    "Moses Lake", "Mossyrock", "Mount Vernon", "Mountlake Terrace", "Moxee", "Mukilteo", "Napavine", "Newcastle", 
    "Newport", "Normandy Park", "North Bend", "North Bonneville", "Oak Harbor", "Oakville", "Ocean Shores", "Odessa", 
    "Okanogan", "Olympia", "Omak", "Oroville", "Orting", "Othello", "Pacific", "Palouse", "Pasco", "Pateros", "Pe Ell", 
    "Pomeroy", "Port Angeles", "Port Orchard", "Port Townsend", "Poulsbo", "Prosser", "Pullman", "Puyallup", "Quincy", 
    "Rainier", "Raymond", "Redmond", "Renton", "Republic", "Richland", "Ridgefield", "Ritzville", "Rock Island", 
    "Roslyn", "Roy", "Royal City", "Ruston", "Sammamish", "SeaTac", "Seattle", "Sedro-Woolley", "Selah", "Sequim", 
    "Shelton", "Shoreline", "Snohomish", "Snoqualmie", "Soap Lake", "South Bend", "Spangle", "Spokane", "Spokane Valley", 
    "Sprague", "Stanwood", "Steilacoom", "Sultan", "Sumas", "Sumner", "Sunnyside", "Tacoma", "Tekoa", "Tenino", "Tieton", 
    "Toledo", "Tonasket", "Toppenish", "Tukwila", "Tumwater", "Union Gap", "University Place", "Vader", "Vancouver", 
    "Waitsburg", "Walla Walla", "Wapato", "Warden", "Washougal", "Waterville", "Wenatchee", "West Richland", 
    "Westport", "White Salmon", "Winlock", "Woodinville", "Woodland", "Woodway", "Yacolt", "Yakima", "Yarrow Point", 
    "Zillah"
]

filename = f"HomeHarvest_WA_{current_timestamp}.csv"
filePath = "/Users/alpaca/HomeHarvest/examples/Analysis/" + filename

for z in zipcode:
    properties = scrape_property(
        location=z + ', WA',
        listing_type="for_sale",  # or (for_sale, for_rent)
        past_days=30,  # sold in last 30 days - listed in last x days if (for_sale, for_rent)
    )
    # Export to csv
    properties.to_csv(filename, mode='a', index=False)
    print(f"Number of properties: {len(properties)}")