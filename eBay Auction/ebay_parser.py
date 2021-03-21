import sys
from json import loads
from re import sub

columnSeparator = "|"

# Dictionary of months used for date transformation
MONTHS = {'Jan':'01','Feb':'02','Mar':'03','Apr':'04','May':'05','Jun':'06',\
        'Jul':'07','Aug':'08','Sep':'09','Oct':'10','Nov':'11','Dec':'12'}

"""
Returns true if a file ends in .json
"""
def isJson(f):
    return len(f) > 5 and f[-5:] == '.json'

"""
Converts month to a number, e.g. 'Dec' to '12'
"""
def transformMonth(mon):
    if mon in MONTHS:
        return MONTHS[mon]
    else:
        return mon

"""
Transforms a timestamp from Mon-DD-YY HH:MM:SS to YYYY-MM-DD HH:MM:SS
"""
def transformDttm(dttm):
    dttm = dttm.strip().split(' ')
    dt = dttm[0].split('-')
    date = '20' + dt[2] + '-'
    date += transformMonth(dt[0]) + '-' + dt[1]
    return date + ' ' + dttm[1]

"""
Transform a dollar value amount from a string like $3,453.23 to XXXXX.xx
"""

def transformDollar(money):
    if money == None or len(money) == 0:
        return money
    return sub(r'[^\d.]', '', money)

"""
Parses a single json file. Currently, there's a loop that iterates over each
item in the data set. Your job is to extend this functionality to create all
of the necessary SQL tables for your database.
"""
def parseJson(json_file):
    with open(json_file, 'r') as f:
        items = loads(f.read())['Items'] # creates a Python dictionary of Items for the supplied json file
        seller_k = "Seller"
        category_k = "Category"
        bid_k = "Bids"
        location = "Location"
        country = "Country"
        user_id = "UserID"
        rating = "Rating"
        
        bidder_f = open("bidder.dat", "a")
        category = open("category_tmp.dat", "a")
        seller = open("seller.dat", "a")
        item_info = open("item.dat", "a")

        for item in items:
            item_id = item["ItemID"]
            
            item_line = item_id + columnSeparator
            seller_line = item_id
            
            
            # write item.dat
            if "Buy_Price" not in item.keys():
                item_line += '"' + sub(r'\"', '\"\"', item["Name"]) + '"'+ columnSeparator + "NULL" + columnSeparator + transformDollar(item["Currently"]) + columnSeparator + transformDollar(item["First_Bid"]) + columnSeparator + item["Number_of_Bids"] + columnSeparator + transformDttm(item["Started"]) + columnSeparator + transformDttm(item["Ends"])
            
            else:
                item_line += '"' + sub(r'\"', '\"\"', item["Name"]) + '"' + columnSeparator + transformDollar(item["Buy_Price"]) + columnSeparator + transformDollar(item["Currently"]) + columnSeparator + transformDollar(item["First_Bid"]) + columnSeparator + item["Number_of_Bids"] + columnSeparator + transformDttm(item["Started"]) + columnSeparator + transformDttm(item["Ends"])

            if item["Description"] == None:
                item_line += columnSeparator + "NULL" + "\n"
            else:
                item_line += columnSeparator + '"' + sub(r'\"', '\"\"', item["Description"]) + '"' + "\n"

            item_info.write(item_line)
                
            # write seller.dat
            
            for value in item[seller_k].values():
                seller_line += columnSeparator + value
                    
            seller_line += columnSeparator + '"' + sub(r'\"', '\"\"', item[location]) + '"'
            seller_line += columnSeparator + '"' + sub(r'\"', '\"\"', item[location]) + '"' + "\n"
            seller.write(seller_line)
            
            # write category.dat
            for c in item[category_k]:
                category.write(item_id + columnSeparator + c + '\n') 
            
            #write bid.dat
            if item[bid_k] is not None:

                bidder_list = item[bid_k]
                
                for bidder_info in bidder_list:
                    bidder = bidder_info['Bid']['Bidder']
                    time = transformDttm(bidder_info['Bid']['Time'])
                    amount = transformDollar(bidder_info['Bid']['Amount'])
                    bid_line = item_id + columnSeparator
                    bid_line += bidder[user_id] + columnSeparator
                    bid_line += bidder[rating] + columnSeparator
                    if location in bidder.keys():
                        bid_line += '"' + sub(r'\"', '\"\"', bidder[location]) + '"' + columnSeparator
                    else:
                        bid_line += "NULL" + columnSeparator
                    if country in bidder.keys():
                        bid_line += '"' + sub(r'\"', '\"\"', bidder[country]) + '"' + columnSeparator
                    else:
                        bid_line += "NULL" + columnSeparator
                    bid_line += time + columnSeparator
                    bid_line += amount + '\n'
                    
                    bidder_f.write(bid_line)
                    
                    
        bidder_f.close()
        category.close()
        seller.close()   
        item_info.close() 
            

"""
Loops through each json files provided on the command line and passes each file
to the parser
"""
def main(argv):
    if len(argv) < 2:
        print('Usage: python skeleton_json_parser.py <path to json files>', file=sys.stderr)
        sys.exit(1)
    # loops over all .json files in the argument
    for f in argv[1:]:
        if isJson(f):
            parseJson(f)
            print("Success parsing " + f)

if __name__ == '__main__':
    main(sys.argv)
