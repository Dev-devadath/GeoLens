// Function to get the user's location
function getLocation() {
  if (navigator.geolocation) {
    navigator.geolocation.getCurrentPosition(showPosition, handleError);
  } else {
    console.error("Geolocation is not supported by this browser.");
  }
}

// Function to handle successful location retrieval
function showPosition(position) {
  const lat = position.coords.latitude;
  const lon = position.coords.longitude;

  // Update the search input with latitude and longitude
  const searchInput = document.querySelector(".search-bar input");
  searchInput.value = `Lat: ${lat}, Lon: ${lon}`; // Optional: Display lat/lon in the search bar

  // Fetch soil details after button click
  document
    .querySelector(".know-land-button")
    .addEventListener("click", function () {
      fetchSoilDetails(lat, lon);
    });
}

function handleError(error) {
  console.error("Error getting location:", error);
}

// Function to fetch soil details from the Django backend
async function fetchSoilDetails(lat, lon) {
  try {
    // Adjust the background div height before fetching data
    document.querySelector(".background").style.height = "58%";

    // Send a POST request to the Django backend with latitude and longitude
    const response = await fetch("/api/get-soil-data/", {
      method: "POST",
      headers: {
        "Content-Type": "application/json",
      },
      body: JSON.stringify({ lat: lat, lon: lon }),
    });

    if (!response.ok) {
      throw new Error("Network response was not ok");
    }

    const soilData = await response.json();
    console.log("Soil details:", soilData);

    // Handle the soil data as needed (update UI, etc.)
  } catch (error) {
    console.error("Error fetching soil details:", error);
  }
}

getLocation();
