import json
from app.models import IndianCityName


class FetchCitiesNameIndia:

    def __init__(self):

        self.raw_data = '{"data": {"cities_current": [{"type": "top metropolitan cities", "name": "Ahmedabad", "value": "Ahmedabad"}, {"type": "top metropolitan cities", "name": "Bangalore", "value": "Bangalore", "alter": ["Bengaluru"]}, {"type": "top metropolitan cities", "name": "Chandigarh", "value": "Chandigarh"}, {"type": "top metropolitan cities", "name": "Chennai", "value": "Chennai"}, {"type": "top metropolitan cities", "name": "Delhi", "value": "Delhi", "alter": ["New Delhi"]}, {"type": "top metropolitan cities", "name": "Gurgaon", "value": "Gurgaon"}, {"type": "top metropolitan cities", "name": "Hyderabad", "value": "Hyderabad", "alter": ["Secunderabad"]}, {"type": "top metropolitan cities", "name": "Kolkata", "value": "Kolkata"}, {"type": "top metropolitan cities", "name": "Mumbai", "value": "Mumbai"}, {"type": "top metropolitan cities", "name": "Noida", "value": "Noida"}, {"type": "top metropolitan cities", "name": "Pune", "value": "Pune"}, {"type": "andhra pradesh", "name": "Anantapur", "value": "Anantapur"}, {"type": "andhra pradesh", "name": "Chitoor", "value": "Chitoor"}, {"type": "andhra pradesh", "name": "Eluru", "value": "Eluru"}, {"type": "andhra pradesh", "name": "Gannavaram", "value": "Gannavaram"}, {"type": "andhra pradesh", "name": "Guntakal", "value": "Guntakal"}, {"type": "andhra pradesh", "name": "Guntur", "value": "Guntur"}, {"type": "andhra pradesh", "name": "Kadapa", "value": "Kadapa", "alter": ["Cudappah"]}, {"type": "andhra pradesh", "name": "Kakinada", "value": "Kakinada"}, {"type": "andhra pradesh", "name": "Kurnool", "value": "Kurnool"}, {"type": "andhra pradesh", "name": "Machilipatnam", "value": "Machilipatnam"}, {"type": "andhra pradesh", "name": "Nandyal", "value": "Nandyal"}, {"type": "andhra pradesh", "name": "Nellore", "value": "Nellore"}, {"type": "andhra pradesh", "name": "Ongole", "value": "Ongole"}, {"type": "andhra pradesh", "name": "Rajahmundry", "value": "Rajahmundry"}, {"type": "andhra pradesh", "name": "Tada", "value": "Tada"}, {"type": "andhra pradesh", "name": "Tirupati", "value": "Tirupati"}, {"type": "andhra pradesh", "name": "Vijayawada", "value": "Vijayawada"}, {"type": "andhra pradesh", "name": "Visakhapatnam", "value": "Visakhapatnam"}, {"type": "andhra pradesh", "name": "Vizianagaram", "value": "Vizianagaram"}, {"type": "arunachal pradesh", "name": "Itanagar", "value": "Itanagar"}, {"type": "assam", "name": "Dibrugarh", "value": "Dibrugarh"}, {"type": "assam", "name": "Guwahati", "value": "Guwahati"}, {"type": "assam", "name": "Silchar", "value": "Silchar"}, {"type": "bihar", "name": "Bhagalpur", "value": "Bhagalpur"}, {"type": "bihar", "name": "Patna", "value": "Patna"}, {"type": "chhattisgarh", "name": "Bhillai", "value": "Bhillai"}, {"type": "chhattisgarh", "name": "Bilaspur", "value": "Bilaspur"}, {"type": "chhattisgarh", "name": "Korba", "value": "Korba"}, {"type": "chhattisgarh", "name": "Raipur", "value": "Raipur"}, {"type": "chhattisgarh", "name": "Raigarh", "value": "Raigarh"}, {"type": "goa", "name": "Panaji", "value": "Panaji", "alter": ["Panjim"]}, {"type": "goa", "name": "Vasco Da Gama", "value": "Vasco Da Gama"}, {"type": "gujarat", "name": "Ahmedabad", "value": "Ahmedabad"}, {"type": "gujarat", "name": "Anand", "value": "Anand"}, {"type": "gujarat", "name": "Ankleshwar", "value": "Ankleshwar"}, {"type": "gujarat", "name": "Bharuch", "value": "Bharuch"}, {"type": "gujarat", "name": "Bhavnagar", "value": "Bhavnagar"}, {"type": "gujarat", "name": "Bhuj", "value": "Bhuj"}, {"type": "gujarat", "name": "Dahej", "value": "Dahej"}, {"type": "gujarat", "name": "Gandhidham", "value": "Gandhidham"}, {"type": "gujarat", "name": "Gandhinagar", "value": "Gandhinagar"}, {"type": "gujarat", "name": "Gir", "value": "Gir"}, {"type": "gujarat", "name": "Jamnagar", "value": "Jamnagar"}, {"type": "gujarat", "name": "Kandla", "value": "Kandla"}, {"type": "gujarat", "name": "Porbandar", "value": "Porbandar"}, {"type": "gujarat", "name": "Mehsana", "value": "Mehsana"}, {"type": "gujarat", "name": "Rajkot", "value": "Rajkot"}, {"type": "gujarat", "name": "Surat", "value": "Surat"}, {"type": "gujarat", "name": "Vadodara", "value": "Vadodara", "alter": ["Baroda"]}, {"type": "gujarat", "name": "Valsad", "value": "Valsad"}, {"type": "gujarat", "name": "Vapi", "value": "Vapi"}, {"type": "haryana", "name": "Ambala", "value": "Ambala"}, {"type": "haryana", "name": "Chandigarh", "value": "Chandigarh"}, {"type": "haryana", "name": "Faridabad", "value": "Faridabad"}, {"type": "haryana", "name": "Gurgaon", "value": "Gurgaon"}, {"type": "haryana", "name": "Hisar", "value": "Hisar"}, {"type": "haryana", "name": "Karnal", "value": "Karnal"}, {"type": "haryana", "name": "Kurukshetra", "value": "Kurukshetra"}, {"type": "haryana", "name": "Panipat", "value": "Panipat"}, {"type": "haryana", "name": "Rohtak", "value": "Rohtak"}, {"type": "himachal pradesh", "name": "Baddi", "value": "Baddi"}, {"type": "himachal pradesh", "name": "Dalhousie", "value": "Dalhousie"}, {"type": "himachal pradesh", "name": "Dharmasala", "value": "Dharmasala"}, {"type": "himachal pradesh", "name": "Kulu / Manali", "value": "Kulu / Manali"}, {"type": "himachal pradesh", "name": "Shimla", "value": "Shimla"}, {"type": "jammu & kashmir", "name": "Jammu", "value": "Jammu"}, {"type": "jammu & kashmir", "name": "Srinagar", "value": "Srinagar"}, {"type": "jharkhand", "name": "Bokaro", "value": "Bokaro"}, {"type": "jharkhand", "name": "Dhanbad", "value": "Dhanbad"}, {"type": "jharkhand", "name": "Jamshedpur", "value": "Jamshedpur"}, {"type": "jharkhand", "name": "Ranchi", "value": "Ranchi"}, {"type": "karnataka", "name": "Bangalore", "value": "Bangalore", "alter": ["Bengaluru"]}, {"type": "karnataka", "name": "Belgaum", "value": "Belgaum"}, {"type": "karnataka", "name": "Bellary", "value": "Bellary"}, {"type": "karnataka", "name": "Bidar", "value": "Bidar"}, {"type": "karnataka", "name": "Davangere", "value": "Davangere"}, {"type": "karnataka", "name": "Dharwad", "value": "Dharwad"}, {"type": "karnataka", "name": "Gulbarga", "value": "Gulbarga"}, {"type": "karnataka", "name": "Hubli", "value": "Hubli"}, {"type": "karnataka", "name": "Kolar", "value": "Kolar"}, {"type": "karnataka", "name": "Mangalore", "value": "Mangalore"}, {"type": "karnataka", "name": "Mysuru", "value": "Mysuru", "alter": ["Mysore"]}, {"type": "kerala", "name": "Calicut", "value": "Calicut"}, {"type": "kerala", "name": "Cochin", "value": "Cochin"}, {"type": "kerala", "name": "Ernakulam", "value": "Ernakulam"}, {"type": "kerala", "name": "Idukki", "value": "Idukki"}, {"type": "kerala", "name": "Kannur", "value": "Kannur"}, {"type": "kerala", "name": "Kasargode", "value": "Kasargode"}, {"type": "kerala", "name": "Kochi", "value": "Kochi"}, {"type": "kerala", "name": "Kollam", "value": "Kollam"}, {"type": "kerala", "name": "Kottayam", "value": "Kottayam"}, {"type": "kerala", "name": "Kozhikode", "value": "Kozhikode"}, {"type": "kerala", "name": "Malappuram", "value": "Malappuram"}, {"type": "kerala", "name": "Palakkad", "value": "Palakkad"}, {"type": "kerala", "name": "Palghat", "value": "Palghat"}, {"type": "kerala", "name": "Pathanamthitta", "value": "Pathanamthitta"}, {"type": "kerala", "name": "Thrissur", "value": "Thrissur"}, {"type": "kerala", "name": "Trivandrum", "value": "Trivandrum"}, {"type": "kerala", "name": "Wayanad", "value": "Wayanad"}, {"type": "madhya pradesh", "name": "Bhopal", "value": "Bhopal"}, {"type": "madhya pradesh", "name": "Gwalior", "value": "Gwalior"}, {"type": "madhya pradesh", "name": "Indore", "value": "Indore"}, {"type": "madhya pradesh", "name": "Jabalpur", "value": "Jabalpur"}, {"type": "madhya pradesh", "name": "Katni", "value": "Katni"}, {"type": "madhya pradesh", "name": "Ujjain", "value": "Ujjain"}, {"type": "maharashtra", "name": "Ahmednagar", "value": "Ahmednagar"}, {"type": "maharashtra", "name": "Aurangabad", "value": "Aurangabad"}, {"type": "maharashtra", "name": "Chandrapur", "value": "Chandrapur"}, {"type": "maharashtra", "name": "Jalgaon", "value": "Jalgaon"}, {"type": "maharashtra", "name": "Kolhapur", "value": "Kolhapur"}, {"type": "maharashtra", "name": "Khopoli", "value": "Khopoli"}, {"type": "maharashtra", "name": "Mumbai", "value": "Mumbai"}, {"type": "maharashtra", "name": "Nagpur", "value": "Nagpur"}, {"type": "maharashtra", "name": "Nasik", "value": "Nasik"}, {"type": "maharashtra", "name": "Navi Mumbai", "value": "Navi Mumbai"}, {"type": "maharashtra", "name": "Pune", "value": "Pune"}, {"type": "maharashtra", "name": "Ratnagiri", "value": "Ratnagiri"}, {"type": "maharashtra", "name": "Solapur", "value": "Solapur"}, {"type": "maharashtra", "name": "Vasai", "value": "Vasai"}, {"type": "manipur", "name": "Imphal", "value": "Imphal"}, {"type": "meghalaya", "name": "Shillong", "value": "Shillong"}, {"type": "mizoram", "name": "Aizawl", "value": "Aizawl"}, {"type": "nagaland", "name": "Dimapur", "value": "Dimapur"}, {"type": "orissa", "name": "Bhubaneshwar", "value": "Bhubaneshwar"}, {"type": "orissa", "name": "Cuttack", "value": "Cuttack"}, {"type": "orissa", "name": "Jharsuguda", "value": "Jharsuguda"}, {"type": "orissa", "name": "Paradeep", "value": "Paradeep"}, {"type": "orissa", "name": "Puri", "value": "Puri"}, {"type": "orissa", "name": "Rourkela", "value": "Rourkela"}, {"type": "orissa", "name": "Sambalpur", "value": "Sambalpur"}, {"type": "punjab", "name": "Amritsar", "value": "Amritsar"}, {"type": "punjab", "name": "Bathinda", "value": "Bathinda"}, {"type": "punjab", "name": "Chandigarh", "value": "Chandigarh"}, {"type": "punjab", "name": "Jalandhar", "value": "Jalandhar"}, {"type": "punjab", "name": "Ludhiana", "value": "Ludhiana"}, {"type": "punjab", "name": "Mohali", "value": "Mohali"}, {"type": "punjab", "name": "Pathankot", "value": "Pathankot"}, {"type": "punjab", "name": "Patiala", "value": "Patiala"}, {"type": "rajasthan", "name": "Ajmer", "value": "Ajmer"}, {"type": "rajasthan", "name": "Barmer", "value": "Barmer"}, {"type": "rajasthan", "name": "Bhilwara", "value": "Bhilwara"}, {"type": "rajasthan", "name": "Jaipur", "value": "Jaipur"}, {"type": "rajasthan", "name": "Jaisalmer", "value": "Jaisalmer"}, {"type": "rajasthan", "name": "Jodhpur", "value": "Jodhpur"}, {"type": "rajasthan", "name": "Kota", "value": "Kota"}, {"type": "rajasthan", "name": "Neemrana", "value": "Neemrana"}, {"type": "rajasthan", "name": "Udaipur", "value": "Udaipur"}, {"type": "sikkim", "name": "Gangtok", "value": "Gangtok"}, {"type": "tamil nadu", "name": "Chennai", "value": "Chennai"}, {"type": "tamil nadu", "name": "Coimbatore", "value": "Coimbatore"}, {"type": "tamil nadu", "name": "Cuddalore", "value": "Cuddalore"}, {"type": "tamil nadu", "name": "Erode", "value": "Erode"}, {"type": "tamil nadu", "name": "Hosur", "value": "Hosur"}, {"type": "tamil nadu", "name": "Madurai", "value": "Madurai"}, {"type": "tamil nadu", "name": "Nagercoil", "value": "Nagercoil"}, {"type": "tamil nadu", "name": "Ooty", "value": "Ooty"}, {"type": "tamil nadu", "name": "Salem", "value": "Salem"}, {"type": "tamil nadu", "name": "Thanjavur", "value": "Thanjavur"}, {"type": "tamil nadu", "name": "Tirunelveli", "value": "Tirunelveli"}, {"type": "tamil nadu", "name": "Trichy", "value": "Trichy"}, {"type": "tamil nadu", "name": "Tuticorin", "value": "Tuticorin"}, {"type": "tamil nadu", "name": "Vellore", "value": "Vellore"}, {"type": "telangana", "name": "Adilabad", "value": "Adilabad"}, {"type": "telangana", "name": "Bhadrachalam", "value": "Bhadrachalam"}, {"type": "telangana", "name": "Godavarikhani", "value": "Godavarikhani"}, {"type": "telangana", "name": "Hanumakonda", "value": "Hanumakonda"}, {"type": "telangana", "name": "Hyderabad", "value": "Hyderabad", "alter": ["Secunderabad"]}, {"type": "telangana", "name": "Karimnagar", "value": "Karimnagar"}, {"type": "telangana", "name": "Khammam", "value": "Khammam"}, {"type": "telangana", "name": "Kodad", "value": "Kodad"}, {"type": "telangana", "name": "Kothagudem", "value": "Kothagudem"}, {"type": "telangana", "name": "Mahabubnagar", "value": "Mahabubnagar", "alter": ["Mahaboobnagar"]}, {"type": "telangana", "name": "Mancherial", "value": "Mancherial"}, {"type": "telangana", "name": "Medak", "value": "Medak"}, {"type": "telangana", "name": "Nalgonda", "value": "Nalgonda"}, {"type": "telangana", "name": "Nizamabad", "value": "Nizamabad"}, {"type": "telangana", "name": "Rangareddy", "value": "Rangareddy"}, {"type": "telangana", "name": "Razole", "value": "Razole"}, {"type": "telangana", "name": "Sangareddy", "value": "Sangareddy"}, {"type": "telangana", "name": "Siddipet", "value": "Siddipet"}, {"type": "telangana", "name": "Suryapet", "value": "Suryapet"}, {"type": "telangana", "name": "Tuni", "value": "Tuni"}, {"type": "telangana", "name": "Warangal", "value": "Warangal"}, {"type": "tripura", "name": "Agartala", "value": "Agartala"}, {"type": "union territories", "name": "Chandigarh", "value": "Chandigarh"}, {"type": "union territories", "name": "Dadra & Nagar Haveli", "value": "Dadra & Nagar Haveli"}, {"type": "union territories", "name": "Daman & Diu", "value": "Daman & Diu"}, {"type": "union territories", "name": "Delhi", "value": "Delhi", "alter": ["New Delhi"]}, {"type": "union territories", "name": "Lakshadweep", "value": "Lakshadweep"}, {"type": "union territories", "name": "Pondicherry", "value": "Pondicherry"}, {"type": "uttar pradesh", "name": "Agra", "value": "Agra"}, {"type": "uttar pradesh", "name": "Aligarh", "value": "Aligarh"}, {"type": "uttar pradesh", "name": "Allahabad", "value": "Allahabad"}, {"type": "uttar pradesh", "name": "Bareilly", "value": "Bareilly"}, {"type": "uttar pradesh", "name": "Bijnor", "value": "Bijnor"}, {"type": "uttar pradesh", "name": "Faizabad", "value": "Faizabad"}, {"type": "uttar pradesh", "name": "Ghaziabad", "value": "Ghaziabad"}, {"type": "uttar pradesh", "name": "Gorakhpur", "value": "Gorakhpur"}, {"type": "uttar pradesh", "name": "Greater Noida", "value": "Greater Noida"}, {"type": "uttar pradesh", "name": "Kanpur", "value": "Kanpur"}, {"type": "uttar pradesh", "name": "Lucknow", "value": "Lucknow"}, {"type": "uttar pradesh", "name": "Mathura", "value": "Mathura"}, {"type": "uttar pradesh", "name": "Meerut", "value": "Meerut"}, {"type": "uttar pradesh", "name": "Moradabad", "value": "Moradabad"}, {"type": "uttar pradesh", "name": "Noida", "value": "Noida"}, {"type": "uttar pradesh", "name": "Saharanpur", "value": "Saharanpur"}, {"type": "uttar pradesh", "name": "Varanasi", "value": "Varanasi"}, {"type": "uttaranchal", "name": "Dehradun", "value": "Dehradun"}, {"type": "uttaranchal", "name": "Haldwani", "value": "Haldwani"}, {"type": "uttaranchal", "name": "Kashipur", "value": "Kashipur"}, {"type": "uttaranchal", "name": "Roorkee", "value": "Roorkee"}, {"type": "west bengal", "name": "Asansol", "value": "Asansol"}, {"type": "west bengal", "name": "Burdwan", "value": "Burdwan"}, {"type": "west bengal", "name": "Durgapur", "value": "Durgapur"}, {"type": "west bengal", "name": "Haldia", "value": "Haldia"}, {"type": "west bengal", "name": "Kharagpur", "value": "Kharagpur"}, {"type": "west bengal", "name": "Kolkata", "value": "Kolkata"}, {"type": "west bengal", "name": "Siliguri", "value": "Siliguri"}], "cities_current_groups": [{"value": "top metropolitan cities", "label": "-----Top Metropolitan Cities-----"}, {"value": "andhra pradesh", "label": "-----Andhra Pradesh-----"}, {"value": "arunachal pradesh", "label": "-----Arunachal Pradesh-----"}, {"value": "assam", "label": "-----Assam-----"}, {"value": "bihar", "label": "-----Bihar-----"}, {"value": "chhattisgarh", "label": "-----Chhattisgarh-----"}, {"value": "goa", "label": "-----Goa-----"}, {"value": "gujarat", "label": "-----Gujarat-----"}, {"value": "haryana", "label": "-----Haryana-----"}, {"value": "himachal pradesh", "label": "-----Himachal Pradesh-----"}, {"value": "jammu & kashmir", "label": "-----Jammu & Kashmir-----"}, {"value": "jharkhand", "label": "-----Jharkhand-----"}, {"value": "karnataka", "label": "-----Karnataka-----"}, {"value": "kerala", "label": "-----Kerala-----"}, {"value": "madhya pradesh", "label": "-----Madhya Pradesh-----"}, {"value": "maharashtra", "label": "-----Maharashtra-----"}, {"value": "manipur", "label": "-----Manipur-----"}, {"value": "meghalaya", "label": "-----Meghalaya-----"}, {"value": "mizoram", "label": "-----Mizoram-----"}, {"value": "nagaland", "label": "-----Nagaland-----"}, {"value": "orissa", "label": "-----Orissa-----"}, {"value": "punjab", "label": "-----Punjab-----"}, {"value": "rajasthan", "label": "-----Rajasthan-----"}, {"value": "sikkim", "label": "-----Sikkim-----"}, {"value": "tamil nadu", "label": "-----Tamil Nadu-----"}, {"value": "telangana", "label": "-----Telangana-----"}, {"value": "tripura", "label": "-----Tripura-----"}, {"value": "union territories", "label": "-----Union Territories-----"}, {"value": "uttar pradesh", "label": "-----Uttar Pradesh-----"}, {"value": "uttaranchal", "label": "-----Uttaranchal-----"}, {"value": "west bengal", "label": "-----West Bengal-----"}], "cities_preferred_groups": [{"value": "regions", "label": "-----Regions-----"}, {"value": "top metropolitan cities", "label": "-----Top Metropolitan Cities-----"}, {"value": "all cities", "label": "-----All Cities-----"}, {"value": "international locations", "label": "-----International Locations-----"}, {"value": "other", "label": "-----Other-----"}], "cities_preferred": [{"type": "regions", "name": "Anywhere in India", "value": "Anywhere in India"}, {"type": "regions", "name": "North India", "value": "North India"}, {"type": "regions", "name": "South India", "value": "South India"}, {"type": "regions", "name": "East India", "value": "East India"}, {"type": "regions", "name": "West India", "value": "West India"}, {"type": "top metropolitan cities", "name": "Ahmedabad", "value": "Ahmedabad"}, {"type": "top metropolitan cities", "name": "Bangalore", "value": "Bangalore", "alter": ["Bengaluru"]}, {"type": "top metropolitan cities", "name": "Chandigarh", "value": "Chandigarh"}, {"type": "top metropolitan cities", "name": "Chennai", "value": "Chennai"}, {"type": "top metropolitan cities", "name": "Delhi", "value": "Delhi", "alter": ["New Delhi"]}, {"type": "top metropolitan cities", "name": "Delhi / NCR", "value": "Delhi / NCR", "alter": ["Delhi NCR"]}, {"type": "top metropolitan cities", "name": "Gurgaon", "value": "Gurgaon"}, {"type": "top metropolitan cities", "name": "Hyderabad", "value": "Hyderabad", "alter": ["Secunderabad"]}, {"type": "top metropolitan cities", "name": "Kolkata", "value": "Kolkata"}, {"type": "top metropolitan cities", "name": "Mumbai", "value": "Mumbai", "alter": ["Bombay"]}, {"type": "top metropolitan cities", "name": "Noida", "value": "Noida"}, {"type": "top metropolitan cities", "name": "Pune", "value": "Pune"}, {"type": "all cities", "name": "Adilabad", "value": "Adilabad"}, {"type": "all cities", "name": "Agartala", "value": "Agartala"}, {"type": "all cities", "name": "Agra", "value": "Agra"}, {"type": "all cities", "name": "Ahmedabad", "value": "Ahmedabad"}, {"type": "all cities", "name": "Ahmednagar", "value": "Ahmednagar"}, {"type": "all cities", "name": "Aizawl", "value": "Aizawl"}, {"type": "all cities", "name": "Ajmer", "value": "Ajmer"}, {"type": "all cities", "name": "Aligarh", "value": "Aligarh"}, {"type": "all cities", "name": "Allahabad", "value": "Allahabad"}, {"type": "all cities", "name": "Ambala", "value": "Ambala"}, {"type": "all cities", "name": "Amritsar", "value": "Amritsar"}, {"type": "all cities", "name": "Anand", "value": "Anand"}, {"type": "all cities", "name": "Anantapur", "value": "Anantapur"}, {"type": "all cities", "name": "Ankleshwar", "value": "Ankleshwar"}, {"type": "all cities", "name": "Asansol", "value": "Asansol"}, {"type": "all cities", "name": "Aurangabad", "value": "Aurangabad"}, {"type": "all cities", "name": "Baddi", "value": "Baddi"}, {"type": "all cities", "name": "Bareilly", "value": "Bareilly"}, {"type": "all cities", "name": "Barmer", "value": "Barmer"}, {"type": "all cities", "name": "Bathinda", "value": "Bathinda"}, {"type": "all cities", "name": "Belgaum", "value": "Belgaum"}, {"type": "all cities", "name": "Bellary", "value": "Bellary"}, {"type": "all cities", "name": "Bangalore", "value": "Bangalore", "alter": ["Bengaluru"]}, {"type": "all cities", "name": "Bhadrachalam", "value": "Bhadrachalam"}, {"type": "all cities", "name": "Bhagalpur", "value": "Bhagalpur"}, {"type": "all cities", "name": "Bharuch", "value": "Bharuch"}, {"type": "all cities", "name": "Bhavnagar", "value": "Bhavnagar"}, {"type": "all cities", "name": "Bhillai", "value": "Bhillai"}, {"type": "all cities", "name": "Bhilwara", "value": "Bhilwara"}, {"type": "all cities", "name": "Bhopal", "value": "Bhopal"}, {"type": "all cities", "name": "Bhubaneshwar", "value": "Bhubaneshwar"}, {"type": "all cities", "name": "Bhuj", "value": "Bhuj"}, {"type": "all cities", "name": "Bidar", "value": "Bidar"}, {"type": "all cities", "name": "Bijnor", "value": "Bijnor"}, {"type": "all cities", "name": "Bilaspur", "value": "Bilaspur"}, {"type": "all cities", "name": "Bokaro", "value": "Bokaro"}, {"type": "all cities", "name": "Burdwan", "value": "Burdwan"}, {"type": "all cities", "name": "Calicut", "value": "Calicut"}, {"type": "all cities", "name": "Chandigarh", "value": "Chandigarh"}, {"type": "all cities", "name": "Chandrapur", "value": "Chandrapur"}, {"type": "all cities", "name": "Chennai", "value": "Chennai"}, {"type": "all cities", "name": "Chitoor", "value": "Chitoor"}, {"type": "all cities", "name": "Cochin", "value": "Cochin"}, {"type": "all cities", "name": "Coimbatore", "value": "Coimbatore"}, {"type": "all cities", "name": "Cuddalore", "value": "Cuddalore"}, {"type": "all cities", "name": "Cuttack", "value": "Cuttack"}, {"type": "all cities", "name": "Dadra & Nagar Haveli", "value": "Dadra & Nagar Haveli"}, {"type": "all cities", "name": "Dahej", "value": "Dahej"}, {"type": "all cities", "name": "Dalhousie", "value": "Dalhousie"}, {"type": "all cities", "name": "Daman & Diu", "value": "Daman & Diu"}, {"type": "all cities", "name": "Davangere", "value": "Davangere"}, {"type": "all cities", "name": "Dehradun", "value": "Dehradun"}, {"type": "all cities", "name": "Delhi", "value": "Delhi", "alter": ["New Delhi"]}, {"type": "all cities", "name": "Dhanbad", "value": "Dhanbad"}, {"type": "all cities", "name": "Dharmasala", "value": "Dharmasala"}, {"type": "all cities", "name": "Dharwad", "value": "Dharwad"}, {"type": "all cities", "name": "Dibrugarh", "value": "Dibrugarh"}, {"type": "all cities", "name": "Dimapur", "value": "Dimapur"}, {"type": "all cities", "name": "Durgapur", "value": "Durgapur"}, {"type": "all cities", "name": "Eluru", "value": "Eluru"}, {"type": "all cities", "name": "Ernakulam", "value": "Ernakulam"}, {"type": "all cities", "name": "Erode", "value": "Erode"}, {"type": "all cities", "name": "Faizabad", "value": "Faizabad"}, {"type": "all cities", "name": "Faridabad", "value": "Faridabad"}, {"type": "all cities", "name": "Gandhidham", "value": "Gandhidham"}, {"type": "all cities", "name": "Gandhinagar", "value": "Gandhinagar"}, {"type": "all cities", "name": "Gangtok", "value": "Gangtok"}, {"type": "all cities", "name": "Gannavaram", "value": "Gannavaram"}, {"type": "all cities", "name": "Ghaziabad", "value": "Ghaziabad"}, {"type": "all cities", "name": "Gir", "value": "Gir"}, {"type": "all cities", "name": "Godavarikhani", "value": "Godavarikhani"}, {"type": "all cities", "name": "Gorakhpur", "value": "Gorakhpur"}, {"type": "all cities", "name": "Greater Noida", "value": "Greater Noida"}, {"type": "all cities", "name": "Gulbarga", "value": "Gulbarga"}, {"type": "all cities", "name": "Guntakal", "value": "Guntakal"}, {"type": "all cities", "name": "Guntur", "value": "Guntur"}, {"type": "all cities", "name": "Gurgaon", "value": "Gurgaon"}, {"type": "all cities", "name": "Guwahati", "value": "Guwahati"}, {"type": "all cities", "name": "Gwalior", "value": "Gwalior"}, {"type": "all cities", "name": "Haldia", "value": "Haldia"}, {"type": "all cities", "name": "Haldwani", "value": "Haldwani"}, {"type": "all cities", "name": "Hanumakonda", "value": "Hanumakonda"}, {"type": "all cities", "name": "Hisar", "value": "Hisar"}, {"type": "all cities", "name": "Hosur", "value": "Hosur"}, {"type": "all cities", "name": "Hubli", "value": "Hubli"}, {"type": "all cities", "name": "Hyderabad", "value": "Hyderabad", "alter": ["Secunderabad"]}, {"type": "all cities", "name": "Idukki", "value": "Idukki"}, {"type": "all cities", "name": "Imphal", "value": "Imphal"}, {"type": "all cities", "name": "Indore", "value": "Indore"}, {"type": "all cities", "name": "Itanagar", "value": "Itanagar"}, {"type": "all cities", "name": "Jabalpur", "value": "Jabalpur"}, {"type": "all cities", "name": "Jaipur", "value": "Jaipur"}, {"type": "all cities", "name": "Jaisalmer", "value": "Jaisalmer"}, {"type": "all cities", "name": "Jalandhar", "value": "Jalandhar"}, {"type": "all cities", "name": "Jalgaon", "value": "Jalgaon"}, {"type": "all cities", "name": "Jammu", "value": "Jammu"}, {"type": "all cities", "name": "Jamnagar", "value": "Jamnagar"}, {"type": "all cities", "name": "Jamshedpur", "value": "Jamshedpur"}, {"type": "all cities", "name": "Jharsuguda", "value": "Jharsuguda"}, {"type": "all cities", "name": "Jodhpur", "value": "Jodhpur"}, {"type": "all cities", "name": "Kadapa", "value": "Kadapa", "alter": ["Cudappah"]}, {"type": "all cities", "name": "Kakinada", "value": "Kakinada"}, {"type": "all cities", "name": "Kandla", "value": "Kandla"}, {"type": "all cities", "name": "Kannur", "value": "Kannur"}, {"type": "all cities", "name": "Kanpur", "value": "Kanpur"}, {"type": "all cities", "name": "Karimnagar", "value": "Karimnagar"}, {"type": "all cities", "name": "Karnal", "value": "Karnal"}, {"type": "all cities", "name": "Kasargode", "value": "Kasargode"}, {"type": "all cities", "name": "Kashipur", "value": "Kashipur"}, {"type": "all cities", "name": "Katni", "value": "Katni"}, {"type": "all cities", "name": "Khammam", "value": "Khammam"}, {"type": "all cities", "name": "Kharagpur", "value": "Kharagpur"}, {"type": "all cities", "name": "Khopoli", "value": "Khopoli"}, {"type": "all cities", "name": "Kochi", "value": "Kochi"}, {"type": "all cities", "name": "Kodad", "value": "Kodad"}, {"type": "all cities", "name": "Kolar", "value": "Kolar"}, {"type": "all cities", "name": "Kolhapur", "value": "Kolhapur"}, {"type": "all cities", "name": "Kolkata", "value": "Kolkata"}, {"type": "all cities", "name": "Kollam", "value": "Kollam"}, {"type": "all cities", "name": "Korba", "value": "Korba"}, {"type": "all cities", "name": "Kota", "value": "Kota"}, {"type": "all cities", "name": "Kothagudem", "value": "Kothagudem"}, {"type": "all cities", "name": "Kottayam", "value": "Kottayam"}, {"type": "all cities", "name": "Kozhikode", "value": "Kozhikode"}, {"type": "all cities", "name": "Kulu / Manali", "value": "Kulu / Manali"}, {"type": "all cities", "name": "Kurnool", "value": "Kurnool"}, {"type": "all cities", "name": "Kurukshetra", "value": "Kurukshetra"}, {"type": "all cities", "name": "Lakshadweep", "value": "Lakshadweep"}, {"type": "all cities", "name": "Lucknow", "value": "Lucknow"}, {"type": "all cities", "name": "Ludhiana", "value": "Ludhiana"}, {"type": "all cities", "name": "Machilipatnam", "value": "Machilipatnam"}, {"type": "all cities", "name": "Madurai", "value": "Madurai"}, {"type": "all cities", "name": "Mahabubnagar", "value": "Mahabubnagar", "alter": ["Mahaboobnagar"]}, {"type": "all cities", "name": "Malappuram", "value": "Malappuram"}, {"type": "all cities", "name": "Mancherial", "value": "Mancherial"}, {"type": "all cities", "name": "Mangalore", "value": "Mangalore"}, {"type": "all cities", "name": "Mathura", "value": "Mathura"}, {"type": "all cities", "name": "Medak", "value": "Medak"}, {"type": "all cities", "name": "Meerut", "value": "Meerut"}, {"type": "all cities", "name": "Mehsana", "value": "Mehsana"}, {"type": "all cities", "name": "Mohali", "value": "Mohali"}, {"type": "all cities", "name": "Moradabad", "value": "Moradabad"}, {"type": "all cities", "name": "Mumbai", "value": "Mumbai"}, {"type": "all cities", "name": "Mysuru", "value": "Mysuru", "alter": ["Mysore"]}, {"type": "all cities", "name": "Nagercoil", "value": "Nagercoil"}, {"type": "all cities", "name": "Nagpur", "value": "Nagpur"}, {"type": "all cities", "name": "Nalgonda", "value": "Nalgonda"}, {"type": "all cities", "name": "Nandyal", "value": "Nandyal"}, {"type": "all cities", "name": "Nasik", "value": "Nasik"}, {"type": "all cities", "name": "Navi Mumbai", "value": "Navi Mumbai"}, {"type": "all cities", "name": "Neemrana", "value": "Neemrana"}, {"type": "all cities", "name": "Nellore", "value": "Nellore"}, {"type": "all cities", "name": "Nizamabad", "value": "Nizamabad"}, {"type": "all cities", "name": "Noida", "value": "Noida"}, {"type": "all cities", "name": "Ongole", "value": "Ongole"}, {"type": "all cities", "name": "Ooty", "value": "Ooty"}, {"type": "all cities", "name": "Palakkad", "value": "Palakkad"}, {"type": "all cities", "name": "Palghat", "value": "Palghat"}, {"type": "all cities", "name": "Panipat", "value": "Panipat"}, {"type": "all cities", "name": "Panaji", "value": "Panaji", "alter": ["Panjim"]}, {"type": "all cities", "name": "Paradeep", "value": "Paradeep"}, {"type": "all cities", "name": "Pathanamthitta", "value": "Pathanamthitta"}, {"type": "all cities", "name": "Pathankot", "value": "Pathankot"}, {"type": "all cities", "name": "Patiala", "value": "Patiala"}, {"type": "all cities", "name": "Patna", "value": "Patna"}, {"type": "all cities", "name": "Pondicherry", "value": "Pondicherry"}, {"type": "all cities", "name": "Porbandar", "value": "Porbandar"}, {"type": "all cities", "name": "Pune", "value": "Pune"}, {"type": "all cities", "name": "Puri", "value": "Puri"}, {"type": "all cities", "name": "Raigarh", "value": "Raigarh"}, {"type": "all cities", "name": "Raipur", "value": "Raipur"}, {"type": "all cities", "name": "Rajahmundry", "value": "Rajahmundry"}, {"type": "all cities", "name": "Rajkot", "value": "Rajkot"}, {"type": "all cities", "name": "Ranchi", "value": "Ranchi"}, {"type": "all cities", "name": "Rangareddy", "value": "Rangareddy"}, {"type": "all cities", "name": "Ratnagiri", "value": "Ratnagiri"}, {"type": "all cities", "name": "Razole", "value": "Razole"}, {"type": "all cities", "name": "Rohtak", "value": "Rohtak"}, {"type": "all cities", "name": "Roorkee", "value": "Roorkee"}, {"type": "all cities", "name": "Rourkela", "value": "Rourkela"}, {"type": "all cities", "name": "Saharanpur", "value": "Saharanpur"}, {"type": "all cities", "name": "Salem", "value": "Salem"}, {"type": "all cities", "name": "Sambalpur", "value": "Sambalpur"}, {"type": "all cities", "name": "Sangareddy", "value": "Sangareddy"}, {"type": "all cities", "name": "Shillong", "value": "Shillong"}, {"type": "all cities", "name": "Shimla", "value": "Shimla"}, {"type": "all cities", "name": "Siddipet", "value": "Siddipet"}, {"type": "all cities", "name": "Silchar", "value": "Silchar"}, {"type": "all cities", "name": "Siliguri", "value": "Siliguri"}, {"type": "all cities", "name": "Solapur", "value": "Solapur"}, {"type": "all cities", "name": "Srinagar", "value": "Srinagar"}, {"type": "all cities", "name": "Surat", "value": "Surat"}, {"type": "all cities", "name": "Suryapet", "value": "Suryapet"}, {"type": "all cities", "name": "Tada", "value": "Tada"}, {"type": "all cities", "name": "Thanjavur", "value": "Thanjavur"}, {"type": "all cities", "name": "Thrissur", "value": "Thrissur"}, {"type": "all cities", "name": "Tirunelveli", "value": "Tirunelveli"}, {"type": "all cities", "name": "Tirupati", "value": "Tirupati"}, {"type": "all cities", "name": "Trichy", "value": "Trichy"}, {"type": "all cities", "name": "Trivandrum", "value": "Trivandrum"}, {"type": "all cities", "name": "Tuni", "value": "Tuni"}, {"type": "all cities", "name": "Tuticorin", "value": "Tuticorin"}, {"type": "all cities", "name": "Udaipur", "value": "Udaipur"}, {"type": "all cities", "name": "Ujjain", "value": "Ujjain"}, {"type": "all cities", "name": "Vadodara", "value": "Vadodara", "alter": ["Baroda"]}, {"type": "all cities", "name": "Valsad", "value": "Valsad"}, {"type": "all cities", "name": "Vapi", "value": "Vapi"}, {"type": "all cities", "name": "Varanasi", "value": "Varanasi"}, {"type": "all cities", "name": "Vasai", "value": "Vasai"}, {"type": "all cities", "name": "Vasco Da Gama", "value": "Vasco Da Gama"}, {"type": "all cities", "name": "Vellore", "value": "Vellore"}, {"type": "all cities", "name": "Vijayawada", "value": "Vijayawada"}, {"type": "all cities", "name": "Visakhapatnam", "value": "Visakhapatnam"}, {"type": "all cities", "name": "Vizianagaram", "value": "Vizianagaram"}, {"type": "all cities", "name": "Warangal", "value": "Warangal"}, {"type": "all cities", "name": "Wayanad", "value": "Wayanad"}, {"iso_alpha_code": "AU", "type": "international locations", "name": "Australia", "value": "Australia"}, {"iso_alpha_code": "AT", "type": "international locations", "name": "Austria", "value": "Austria"}, {"iso_alpha_code": "BH", "type": "international locations", "name": "Bahrain", "value": "Bahrain"}, {"iso_alpha_code": "BD", "type": "international locations", "name": "Bangladesh", "value": "Bangladesh"}, {"iso_alpha_code": "BE", "type": "international locations", "name": "Belgium", "value": "Belgium"}, {"iso_alpha_code": "CA", "type": "international locations", "name": "Canada", "value": "Canada"}, {"iso_alpha_code": "CN", "type": "international locations", "name": "China", "value": "China"}, {"iso_alpha_code": "QA", "type": "international locations", "name": "Doha", "value": "Doha"}, {"iso_alpha_code": "AE", "type": "international locations", "name": "Dubai", "value": "Dubai"}, {"iso_alpha_code": "FR", "type": "international locations", "name": "France", "value": "France"}, {"iso_alpha_code": "DE", "type": "international locations", "name": "Germany", "value": "Germany"}, {"iso_alpha_code": "GR", "type": "international locations", "name": "Greece", "value": "Greece"}, {"iso_alpha_code": "HK", "type": "international locations", "name": "Hong Kong", "value": "Hong Kong"}, {"iso_alpha_code": "IS", "type": "international locations", "name": "Iceland", "value": "Iceland"}, {"iso_alpha_code": "ID", "type": "international locations", "name": "Indonesia", "value": "Indonesia"}, {"iso_alpha_code": "IE", "type": "international locations", "name": "Ireland", "value": "Ireland"}, {"iso_alpha_code": "IT", "type": "international locations", "name": "Italy", "value": "Italy"}, {"iso_alpha_code": "JP", "type": "international locations", "name": "Japan", "value": "Japan"}, {"iso_alpha_code": "KE", "type": "international locations", "name": "Kenya", "value": "Kenya"}, {"iso_alpha_code": "KW", "type": "international locations", "name": "Kuwait", "value": "Kuwait"}, {"iso_alpha_code": "LB", "type": "international locations", "name": "Lebanon", "value": "Lebanon"}, {"iso_alpha_code": "LY", "type": "international locations", "name": "Libya", "value": "Libya"}, {"iso_alpha_code": "MY", "type": "international locations", "name": "Malaysia", "value": "Malaysia"}, {"iso_alpha_code": "MV", "type": "international locations", "name": "Maldives", "value": "Maldives"}, {"iso_alpha_code": "MU", "type": "international locations", "name": "Mauritius", "value": "Mauritius"}, {"iso_alpha_code": "MX", "type": "international locations", "name": "Mexico", "value": "Mexico"}, {"iso_alpha_code": "NP", "type": "international locations", "name": "Nepal", "value": "Nepal"}, {"iso_alpha_code": "NL", "type": "international locations", "name": "Netherlands", "value": "Netherlands"}, {"iso_alpha_code": "NZ", "type": "international locations", "name": "New Zealand", "value": "New Zealand"}, {"iso_alpha_code": "NO", "type": "international locations", "name": "Norway", "value": "Norway"}, {"iso_alpha_code": "OM", "type": "international locations", "name": "Oman", "value": "Oman"}, {"iso_alpha_code": "PK", "type": "international locations", "name": "Pakistan", "value": "Pakistan"}, {"iso_alpha_code": "PL", "type": "international locations", "name": "Poland", "value": "Poland"}, {"iso_alpha_code": "QA", "type": "international locations", "name": "Qatar", "value": "Qatar"}, {"iso_alpha_code": "IN", "type": "international locations", "name": "Quilon", "value": "Quilon"}, {"iso_alpha_code": "RU", "type": "international locations", "name": "Russia", "value": "Russia"}, {"iso_alpha_code": "SA", "type": "international locations", "name": "Saudi Arabia", "value": "Saudi Arabia"}, {"iso_alpha_code": "SG", "type": "international locations", "name": "Singapore", "value": "Singapore"}, {"iso_alpha_code": "ZA", "type": "international locations", "name": "South Africa", "value": "South Africa"}, {"iso_alpha_code": "KR", "type": "international locations", "name": "South Korea", "value": "South Korea"}, {"iso_alpha_code": "ES", "type": "international locations", "name": "Spain", "value": "Spain"}, {"iso_alpha_code": "LK", "type": "international locations", "name": "Sri Lanka", "value": "Sri Lanka"}, {"iso_alpha_code": "SE", "type": "international locations", "name": "Sweden", "value": "Sweden"}, {"iso_alpha_code": "CH", "type": "international locations", "name": "Switzerland", "value": "Switzerland"}, {"iso_alpha_code": "TH", "type": "international locations", "name": "Thailand", "value": "Thailand"}, {"iso_alpha_code": "AE", "type": "international locations", "name": "United Arab Emirates (UAE)", "value": "United Arab Emirates (UAE)"}, {"iso_alpha_code": "GB", "type": "international locations", "name": "United Kingdom (UK)", "value": "United Kingdom (UK)"}, {"iso_alpha_code": "US", "type": "international locations", "name": "United States (USA)", "value": "United States (USA)"}, {"iso_alpha_code": "YE", "type": "international locations", "name": "Yemen", "value": "Yemen"}, {"iso_alpha_code": "ZW", "type": "international locations", "name": "Zimbabwe", "value": "Zimbabwe"}, {"type": "other", "name": "Work from home / Remote", "value": "Work From Home"}]}, "success": true}'
        self.json_data = json.loads(self.raw_data)

    def fetch_data(self):

        for city in self.json_data['data']['cities_current']:

            new_city = IndianCityName()

            new_city.city_name = city['name']
            new_city.city_value = city['value']

            new_city.save()