function generateCityStateLevel() {
  var ss = SpreadsheetApp.getActiveSpreadsheet();
  var sheet = ss.getSheetByName('Generate City And State');
  var column = sheet.getRange('E2:G');
  var values = column.getValues();
  
  var location = [];
  var level = [];
  for(i=0; i<values.length; i++) {
    if(values[i][0] != "" && values[i][1] !="") {
      location.push([values[i][0], values[i][1]]);
      level.push([values[i][2]]);
    }
  }

  // Paste City and State
  var pasteSheet = ss.getSheetByName('Main');
  pasteSheet.getRange(2, 2, location.length, location[0].length).clearContent();
  pasteSheet.getRange(2, 2, location.length, location[0].length).setValues(location);

  // Paste Level
  pasteSheet.getRange(2, 5, level.length, level[0].length).setValues(level);
}
