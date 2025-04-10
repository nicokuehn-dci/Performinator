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

document.addEventListener('DOMContentLoaded', () => {
    const content = document.getElementById('content');
    const buttons = document.querySelectorAll('.sidebar button');

    const views = {
        dashboard: "<h2>Dashboard</h2><p>Overview of your projects.</p>",
        sequencer: "<h2>Sequencer</h2><p>Grid-based beat maker interface.</p>",
        sampler: "<h2>Sampler</h2><p>Load and assign samples.</p>",
        effects: "<h2>Effects Rack</h2><p>Chain your effects here.</p>",
        settings: "<h2>Settings</h2><p>Adjust audio/MIDI prefs here.</p>"
    };

    buttons.forEach(button => {
        button.addEventListener('click', () => {
            const view = button.dataset.view;
            content.innerHTML = views[view] || "<p>Coming soon...</p>";
            ipcRenderer.send('navigate', view);
        });
    });

    // Example of sending a message to the main process
    const menuItems = document.querySelectorAll('.menu-bar .dropdown-content a');
    menuItems.forEach(item => {
        item.addEventListener('click', (event) => {
            const action = event.target.textContent;
            ipcRenderer.send('menu-action', action);
        });
    });

    ipcRenderer.on('update-content', (event, newContent) => {
        content.innerHTML = newContent;
    });

    const pythonExecuteButton = document.getElementById('python-execute-button');
    const pythonCodeInput = document.getElementById('python-code-input');
    const pythonOutput = document.getElementById('python-output');

    pythonExecuteButton.addEventListener('click', () => {
        const code = pythonCodeInput.value;
        pythonOutput.textContent = 'Executing...';

        // Send the Python code to the main process for execution
        ipcRenderer.invoke('execute-python-code', code).then(output => {
            pythonOutput.textContent = output;
        }).catch(error => {
            pythonOutput.textContent = `Error: ${error.message}`;
        });
    });

    const samplerButton = document.querySelector("button[data-view='sampler']");
    samplerButton.addEventListener('click', () => {
        ipcRenderer.send('sampler-action', 'load-sampler');
    });
});
