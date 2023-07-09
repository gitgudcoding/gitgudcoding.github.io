function generateGoogleAdsLocation() {
  var ss = SpreadsheetApp.getActiveSpreadsheet();
  var sheet = ss.getSheetByName('Generate Location And Campaign');
  var column = sheet.getRange('A2:C');
  var values = column.getValues();
  
  var location = [];
  var campaign = []
  for(i=0; i<values.length; i++) {
    if(values[i][0] != "" && values[i][1] !="") {
      location.push([values[i][0] +", "+ values[i][1] + ", United States"]);
      campaign.push([values[i][2]]);
    }
  }

  // Paste locations
  var pasteSheet = ss.getSheetByName('Campaign');
  pasteSheet.getRange(2, 1, location.length, location[0].length).clearContent();
  pasteSheet.getRange(2, 1, location.length, location[0].length).setValues(location);

  // Paste campaigns
  pasteSheet.getRange(2, 2, campaign.length, campaign[0].length).setValues(campaign);
}

