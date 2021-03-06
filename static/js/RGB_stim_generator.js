//Stimulus Peg
var StimSliderR = document.getElementById("RvalueStim");
var StimOutputR = document.getElementById("sR");
StimOutputR.innerHTML = StimSliderR.value;

StimSliderR.oninput = function () {
    StimOutputR.innerHTML = this.value;
};

var StimSliderG = document.getElementById("GvalueStim");
var StimOutputG = document.getElementById("sG");
StimOutputG.innerHTML = StimSliderG.value;

StimSliderG.oninput = function () {
    StimOutputG.innerHTML = this.value;
};

var StimSliderB = document.getElementById("BvalueStim");
var StimOutputB = document.getElementById("sB");
StimOutputB.innerHTML = StimSliderB.value;

StimSliderB.oninput = function () {
    StimOutputB.innerHTML = this.value;
};

//Stimulus label
var StimLabelSliderR = document.getElementById("lRvalueStim");
var StimLabelOutputR = document.getElementById("lR");
StimLabelOutputR.innerHTML = StimLabelSliderR.value;

StimLabelSliderR.oninput = function () {
    StimLabelOutputR.innerHTML = this.value;
};

var StimLabelSliderG = document.getElementById("lGvalueStim");
var StimLabelOutputG = document.getElementById("lG");
StimLabelOutputG.innerHTML = StimLabelSliderG.value;

StimLabelSliderG.oninput = function () {
    StimLabelOutputG.innerHTML = this.value;
};

var StimLabelSliderB = document.getElementById("lBvalueStim");
var StimLabelOutputB = document.getElementById("lB");
StimLabelOutputB.innerHTML = StimLabelSliderB.value;

StimLabelSliderB.oninput = function () {
    StimLabelOutputB.innerHTML = this.value;
};

//Board Sliders and Button that trigger on/off
var displaySliderBoard, displaySliderBackground, displaySliderCover;
var displayValueBoard, displayValueBackground, displayValueCover;
var boardBtn, backgroundBtn, coverBtn;

function displayColorSliderBoard() {
    displayValueBoard = document.getElementById("displayValueBoard");
    displayValueBackground = document.getElementById("displayValueBackground");
    displayValueCover = document.getElementById("displayValueCover");

    boardBtn = document.getElementById("boardBtn");
    backgroundBtn = document.getElementById("backgroundBtn");
    coverBtn = document.getElementById("coverBtn");

    displaySliderBoard = document.getElementById("displaySliderBoard");
    displaySliderBackground = document.getElementById("displaySliderBackground");
    displaySliderCover = document.getElementById("displaySliderCover");

    if (displaySliderBoard.style.display === "none") {

        boardBtn.classList.add("bg-primary");
        backgroundBtn.classList.remove("bg-primary");
        coverBtn.classList.remove("bg-primary");

        displayValueBoard.style.display = "block";
        displayValueBackground.style.display = "none";
        displayValueCover.style.display = "none";

        displaySliderBoard.style.display = "block";
        displaySliderBackground.style.display = "none";
        displaySliderCover.style.display = "none";

    }
}

function displayColorSliderBackground() {
    displayValueBoard = document.getElementById("displayValueBoard");
    displayValueBackground = document.getElementById("displayValueBackground");
    displayValueCover = document.getElementById("displayValueCover");

    boardBtn = document.getElementById("boardBtn");
    backgroundBtn = document.getElementById("backgroundBtn");
    coverBtn = document.getElementById("coverBtn");

    displaySliderBoard = document.getElementById("displaySliderBoard");
    displaySliderBackground = document.getElementById("displaySliderBackground");
    displaySliderCover = document.getElementById("displaySliderCover");

    if (displaySliderBackground.style.display === "none") {

        boardBtn.classList.remove("bg-primary");
        backgroundBtn.classList.add("bg-primary");
        coverBtn.classList.remove("bg-primary");

        displayValueBoard.style.display = "none";
        displayValueBackground.style.display = "block";
        displayValueCover.style.display = "none";

        displaySliderBoard.style.display = "none";
        displaySliderBackground.style.display = "block";
        displaySliderCover.style.display = "none";

    }
}

function displayColorSliderCover() {
    displayValueBoard = document.getElementById("displayValueBoard");
    displayValueBackground = document.getElementById("displayValueBackground");
    displayValueCover = document.getElementById("displayValueCover");

    boardBtn = document.getElementById("boardBtn");
    backgroundBtn = document.getElementById("backgroundBtn");
    coverBtn = document.getElementById("coverBtn");

    displaySliderBoard = document.getElementById("displaySliderBoard");
    displaySliderBackground = document.getElementById("displaySliderBackground");
    displaySliderCover = document.getElementById("displaySliderCover");

    if (displaySliderCover.style.display === "none") {

        boardBtn.classList.remove("bg-primary");
        backgroundBtn.classList.remove("bg-primary");
        coverBtn.classList.add("bg-primary");

        displayValueBoard.style.display = "none";
        displayValueBackground.style.display = "none";
        displayValueCover.style.display = "block";

        displaySliderBoard.style.display = "none";
        displaySliderBackground.style.display = "none";
        displaySliderCover.style.display = "block";

    }
}

//Stimulus Slider and Button that trigger on/off
var displaySliderLabel, displaySliderStimulus;
var displayValueLabelStimulus, displayValuePeg;
var labelBtn, pegBtn;

function displayColorSliderLabel() {
    displayValueLabelStimulus = document.getElementById("displayValueLabelStimulus");
    displayValuePeg = document.getElementById("displayValuePeg");

    labelBtn = document.getElementById("labelBtn");
    pegBtn = document.getElementById("pegBtn");

    displaySliderLabel = document.getElementById("displaySliderLabel");
    displaySliderStimulus = document.getElementById("displaySliderStimulus");

    if (displaySliderLabel.style.display === "none") {

        labelBtn.classList.add("bg-primary");
        pegBtn.classList.remove("bg-primary");

        displayValueLabelStimulus.style.display = "block";
        displayValuePeg.style.display = "none";

        displaySliderLabel.style.display = "block";
        displaySliderStimulus.style.display = "none";
    }
}

function displayColorSliderStimulus() {
    displayValueLabelStimulus = document.getElementById("displayValueLabelStimulus");
    displayValuePeg = document.getElementById("displayValuePeg");

    labelBtn = document.getElementById("labelBtn");
    pegBtn = document.getElementById("pegBtn");

    displaySliderLabel = document.getElementById("displaySliderLabel");
    displaySliderStimulus = document.getElementById("displaySliderStimulus");

    if (displaySliderStimulus.style.display === "none") {

        labelBtn.classList.remove("bg-primary");
        pegBtn.classList.add("bg-primary");

        displayValueLabelStimulus.style.display = "none";
        displayValuePeg.style.display = "block";

        displaySliderLabel.style.display = "none";
        displaySliderStimulus.style.display = "block";
    }
}