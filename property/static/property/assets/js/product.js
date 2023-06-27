function openProducts(productName, elmnt, color) {
    // Hide all elements with class="tabcontent" by default */
    var i, allproducts, navigatorbtn;
    allproducts = document.getElementsByClassName("allproducts");
    for (i = 0; i < allproducts.length; i++) {
        allproducts[i].style.display = "none";
    }

    // Remove the background color of all tablinks/buttons
    navigatorbtn = document.getElementsByClassName("navigatorbtn");
    for (i = 0; i < navigatorbtn.length; i++) {
        navigatorbtn[i].style.backgroundColor = "";
    }

    // Show the specific tab content
    document.getElementById(productName).style.display = "flex";

    // Add the specific style to the button used to open the tab content
    elmnt.style.backgroundColor = color;
}


// Get the element with id="defaultOpen" and click on it
document.getElementById("defaultOpen").click();

