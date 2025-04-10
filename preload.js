const { contextBridge, ipcRenderer } = require('electron');

// Expose protected methods that allow the renderer process to use
// the ipcRenderer without exposing the entire Electron API
contextBridge.exposeInMainWorld('electronAPI', {
    sendMessage: (channel, data) => {
        // List of allowed channels
        const validChannels = ['navigate', 'update-content'];
        if (validChannels.includes(channel)) {
            ipcRenderer.send(channel, data);
        }
    },
    onMessage: (channel, callback) => {
        const validChannels = ['update-content'];
        if (validChannels.includes(channel)) {
            ipcRenderer.on(channel, (event, ...args) => callback(...args));
        }
    }
});