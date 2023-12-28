
# Temperature-Blanket
This tool can be used to make a spreadsheet of the average temperatures on a given day to make a temperature blanket.
# Setup
### Google
To keep track of your data, we will use a Google sheet. To begin, create a Google sheet, and add the following to the first row:
|**Month**|**Day**|**Temperature**|**Color**|
|--|--|--|--|
||

 Next, head over to [Google Cloud Console](https://console.cloud.google.com/), and create a new project. Name it something like "Temperature Blanket". Once in the project, go to **IAM & ADMIN**, and **Service Accounts**, and create an account (you can name it whatever). Under Step 2, "Grant this service account access to project", add the role of editor. Once you are back on the Service Accounts screen, click the three dots on the right of the service account you created and click **Manage Keys**. Then click **Create New Key** and select JSON as the type. Add the key to the folder with the rest of the code and rename it to something that makes sense to you. Now, enable the [Google Drive API](https://console.cloud.google.com/apis/library/drive.googleapis.com) and the [Google Sheets API](https://console.cloud.google.com/apis/library/sheets.googleapis.com). 
**Note: Make sure you are in the same project you created earlier when you enable the APIs.** 
Now, open the JSON file and copy the *client_email* parameter. Go back to the Google sheet you created and share the sheet with this email. This allows the service account to add data to the Google sheet
### Weather API
To collect the weather data, we will be using [WeatherApi.com](https://www.weatherapi.com/). To get your API key, simply go to [WeatherApi.com](https://www.weatherapi.com/) and sign up for an account. In the [My Account](https://www.weatherapi.com/my/) section, you will see your API key at the top. Copy this and save it for later.

### Putting it all together
Once you have your APIs set up, it's time to put it all together. To start, clone the repository with `git clone https://github.com/MusicalJonah/Temperature-Blanket.git`, and go into the directory. Next, install the Python requirements with
 `pip install -r requirements.txt`. Now, open the config.conf file and enter the details for each item.
 **Colors in the config file:**
 
|Name|Temperature|
|--|--|
|Color 1|<20°F
|Color 2|20°-29°F
|Color 3|30°-39°F
|Color 4|40°-49°F
|Color 5|50°-59°F
|Color 6|60°-69°F
|Color 7|70°-79°F
|Color 8|>80°F

### Using the Program:
To update the sheet, just run `python3 main.py` once a day to update the sheet. 
Happy Knitting/Crocheting!