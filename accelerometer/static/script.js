window.addEventListener("deviceorientation", handleMotion, true);

function handleMotion(event) {
    let xmlhttp = new XMLHttpRequest();
    xmlhttp.open("POST", "/acc");
    xmlhttp.setRequestHeader("Content-Type", "application/json");
    rot = event.acceleration;
    xmlhttp.send(JSON.stringify({
        alpha : rot.alpha,
        beta : rot.beta,
        gamma : rot.gamma,
    }));
}
