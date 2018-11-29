window.onload = function () {
    runFirst("boards");
    runFirst("stims");
};

function runFirst(name) {
    var tbl = document.getElementById(name);

    if (tbl != null) {
        //rows
        for (var i = 1; i < tbl.rows.length; i++) {
            //column
            for (var j = 0; j < tbl.rows[i].cells.length; j++) {

                tbl.rows[i].cells[j].style.backgroundColor = "#ffffff"; //------------------change to background color / original

                tbl.rows[i].cells[j].onclick = function () {

                    for (var i = 1; i < tbl.rows.length; i++) {
                        //check all other cells in the column for any other's selected and revert the color back to the original color.
                        if (tbl.rows[i].cells[this.cellIndex].style.backgroundColor = "#e0e0e0") {
                            tbl.rows[i].cells[this.cellIndex].style.backgroundColor = "#ffffff"; //------------------change to background color / original
                        }
                    }
                    this.style.backgroundColor = "#e0e0e0";


                    getval(this, name);

                };
            }

        }

    }
}


function getval(cel, tableName) {

    if (cel != null) {
        //if tableName == "boards" it is a board, if it is == "stimuli" it is a stimuli set

        if (tableName == "boards") {
            //database
            //cel.innerHTML
        } else {
            //database

        }

    }
}
