// Auto fetch GPS location
navigator.geolocation.getCurrentPosition(
    position => {
        document.getElementById("location").value =
            position.coords.latitude + ", " + position.coords.longitude;
    },
    () => {
        document.getElementById("location").value = "Location unavailable";
    }
);

function sendSOS() {
    let name = document.getElementById("name").value;
    let location = document.getElementById("location").value;

    if (name === "") {
        alert("Please enter your name");
        return;
    }

    fetch("/send_sos", {
        method: "POST",
        headers: { "Content-Type": "application/json" },
        body: JSON.stringify({ name, location })
    })
    .then(res => res.json())
    .then(data => alert(data.message));
}
