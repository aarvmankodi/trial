const searchInput = document.getElementById('search-input');
const searchButton = document.getElementById('search-button');
const outputLabel = document.querySelector('.output-label');

// Replace this with your actual logic for matching keywords and responses
const wordConversion = {
  "hi": "hello there how may i assist you today",
    "bye": "goodbye, i look forward to helping you again",
    "on lights": "ofcourse, turning the lights on now",
    "off lights": "ofcourse, turning the lights off now",
    "temperature": "The temperature in your location is 98 C according to my sensors." ,
    "humidity": "The current humidity is x% according to my sensors",
    "weather": "The  weather right now is x degrees and with a y% chance of rain",

  // ... add more key-value pairs
};

searchButton.addEventListener('click', () => {
  const userInput = searchInput.value.toLowerCase().split();
  let bestMatch = null;
  let maxMatches = 0;

  for (const keyword in wordConversion) {
    let count = 0;
    for (const userWord of userInput) {
      if (keyword.toLowerCase().includes(userWord)) {
        count++;
      }
    }
    if (count > maxMatches) {
      maxMatches = count;
      bestMatch = keyword;
    }
  }

  if (bestMatch) {
    outputLabel.textContent = wordConversion[bestMatch];
  } else {
    outputLabel.textContent = "Sorry, I couldn't understand your request.";
  }
  searchInput.value = "";
});

// Text-to-speech functionality cannot be directly implemented in pure HTML/CSS/JS
// Consider using a third-party library for text-to-speech or exploring browser APIs (if available).