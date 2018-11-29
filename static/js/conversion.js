var header = 
    [
{
    Experiment: "name",
    Subject: "subname",
    Date: Date.now()
}
        ]
;
var times = [
    {
        TimeStart: Date.now(),
        
        TimeEnd: Date.now()
    }
]
;
//this is a blank array
var subjectActions =[]
var items =[]
var finalposs = []



var time = Date.now();
var id = 2;
var label = "oaiwf;oijawe;oifj";
var fromx = 12.44444;
var fromy = 12.5555;
var tox = 12.3059348509;
var toy = 23.000000000000000000000000001;

function newAction(time, id, label, fromx, fromy, tox, toy)
{
    subjectaction = {
        subjectTime : time,
        stimid : id,
        stimlabel: label,
        xvalfrom : fromx,
        yvalfrom : fromy,
        xvalto : tox,
        yvalto : toy
    }
    subjectActions.push(subjectaction);
}

function newItem(id, label){
   stim =
   {
       stimid : id,
    stimlabel : label
   }
    
    items.push(stim);
}

function finalPositions(id, label, positionx, positiony)
{
    fp =    
    {
        stimid : id,
        stimlabel : label,
        stimpossx : positionx,
        stimpossy : positiony
    }
    finalposs.push(fp);
}

function finddistances(finalposs){
    var firstarray = finalposs;
    var holdarray =  [firstarray.size][firstarray.size];
    (var i = 0; i < firstarray.size; i++ ){
        (var j = 0; j < firstarray.size; j++ ){
            if(i == j){
                holdarray[i][j] = "N/A";
            }
            else{
                holdarray[i][j] = calculateDistance(finalposs[i].stimpossx, finalposs[i].stimpossy, finalposs[j].stimpossx, finalposs[j].stimpossy);
            }
        }
        holdarray[i];
    }
}
    




function convertArrayOfObjectsToCSV(args) {  
        var result, ctr, keys, columnDelimiter, lineDelimiter, data;

        data = args.data || null;
        if (data == null || !data.length) {
            return null;
        }

        columnDelimiter = args.columnDelimiter || ',';
        lineDelimiter = args.lineDelimiter || '\n';

        keys = Object.keys(data[0]);
        

        result = '';
    data.forEach(function(item) {
        for(var i = 0; i < keys.length; i++){
            result += keys[i];
            result += columnDelimiter;
            result += item[keys[i]];
            result += lineDelimiter;
            }
            
        })
    
    
    result += lineDelimiter;
    result += lineDelimiter;
    
        
//        result += columnDelimiter;
//        data.forEach(function(item) {
//            ctr = 0;
//            keys.forEach(function(key) {
//                
//
//               result += item[key];
//               result += lineDelimiter;
//                ctr++;
//            });
//            result += lineDelimiter;
//            result += "hey";
//            
     //   });
    
//    result += "hello 1";
//    result += "hello 2";
//    result += lineDelimiter;
//    result += "hello 3";

        return result;
    }

function downloadCSV(args) {  
    
    
    newAction(time, id, label, fromx, fromy, tox, toy);
    newItem(id, label)
    finalPositions(id, label, 12.4, 11.24435)
    
    
    
    //call to convert to excel file
        var data, filename, link;
        var count = 0;
        var csv; 
        
                csv = convertArrayOfObjectsToCSV({
                data: subjectActions
                });
        
                 
            csv+= convertArrayOfObjectsToCSV({
                data: items
           });
    
             csv+= convertArrayOfObjectsToCSV({
                data: finalposs
           });
        

        if (csv == null) return;

        filename = args.filename || 'export.csv';

        if (!csv.match(/^data:text\/csv/i)) {
            csv = 'data:text/csv;charset=utf-8,' + csv;
        }
        data = encodeURI(csv);

        link = document.createElement('a');
        link.setAttribute('href', data);
        link.setAttribute('download', filename);
        link.click();
    }


function calculateDistance(x1, y1, x2, y2){
    var x = x1 - x2;
    var y = y1- y2;
    
    return Math.sqrt(x*x + y*y);
}