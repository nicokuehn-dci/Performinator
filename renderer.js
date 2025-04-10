const { ipcRenderer } = require('electron');

// Function to send a message to the main process
function sendMessageToMainProcess(message) {
  ipcRenderer.send('message-from-renderer', message);
}

// Function to receive a message from the main process
ipcRenderer.on('message-from-main', (event, message) => {
  console.log('Message from main process:', message);
});

// Example usage: send a message to the main process when a button is clicked
document.getElementById('sendMessageButton').addEventListener('click', () => {
  sendMessageToMainProcess('Hello from renderer process!');
});

// Handle UI interactions for device and visualizer panels
document.getElementById('device-panel').addEventListener('input', (event) => {
  const control = event.target;
  if (control.tagName === 'INPUT' || control.tagName === 'BUTTON') {
    const action = {
      type: control.tagName,
      id: control.id,
      value: control.value
    };
    sendMessageToMainProcess(action);
  }
});

document.getElementById('visualizer-panel').addEventListener('input', (event) => {
  const control = event.target;
  if (control.tagName === 'INPUT' || control.tagName === 'BUTTON') {
    const action = {
      type: control.tagName,
      id: control.id,
      value: control.value
    };
    sendMessageToMainProcess(action);
  }
});

const content = document.getElementById("content");
const buttons = document.querySelectorAll(".sidebar button");

const views = {
  dashboard: "<h2>Dashboard</h2><p>Overview of your projects.</p>",
  sequencer: "<h2>Sequencer</h2><p>Grid-based beat maker interface.</p>",
  sampler: "<h2>Sampler</h2><p>Load and assign samples.</p>",
  effects: "<h2>Effects Rack</h2><p>Chain your effects here.</p>",
  settings: "<h2>Settings</h2><p>Adjust audio/MIDI prefs here.</p>",
  profile: "<h2>Artist Profile</h2><p>Set up your artist name and favorite genre.</p>",
  projects: "<h2>Projects</h2><p>View, start, or add new projects.</p>",
  engine: "<h2>App Engine</h2><p>Start the app engine to begin creating.</p>",
};

buttons.forEach(btn => {
  btn.addEventListener("click", () => {
    const view = btn.dataset.view;
    content.innerHTML = views[view] || "<p>Coming soon...</p>";
  });
});

document.addEventListener('DOMContentLoaded', () => {
    const sidebar = document.querySelector('.sidebar');

    sidebar.addEventListener('click', (event) => {
        if (event.target.tagName === 'BUTTON') {
            const view = event.target.dataset.view;
            ipcRenderer.send('navigate', view); // Send the view name to the main process
        }
    });

    ipcRenderer.on('update-content', (event, content) => {
        const contentArea = document.getElementById('content');
        contentArea.innerHTML = content; // Update the content area with data from the backend
    });
});
