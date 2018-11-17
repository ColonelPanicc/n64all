window.addEventListener("deviceorientation", handleOrientation, true);

function handleOrientation(event) {
    let xmlhttp = new XMLHttpRequest();
    xmlhttp.open("POST", "/acc");
    xmlhttp.setRequestHeader("Content-Type", "application/json");
    xmlhttp.send(JSON.stringify({
        absolute: event.absolute,
        alpha : event.alpha,
        beta : event.beta,
        gamma : event.gamma,
    }));
}
