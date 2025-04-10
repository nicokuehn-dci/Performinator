const { app, BrowserWindow, ipcMain } = require('electron');
const path = require('path');
const { spawn, exec } = require('child_process');

let mainWindow;
let pythonProcess;
let splash;

function createWindow() {
  splash = new BrowserWindow({
    width: 400,
    height: 300,
    frame: false,
    transparent: false,
    alwaysOnTop: true,
    resizable: false,
  });
  splash.loadFile('splash.html');

  mainWindow = new BrowserWindow({
    width: 1280,
    height: 800,
    show: false, // hide until ready
    webPreferences: {
      preload: path.join(__dirname, 'preload.js'),
      contextIsolation: true,
      enableRemoteModule: false
    }
  });

  mainWindow.loadFile('index.html');

  // Show main window after a short delay or when ready
  mainWindow.once('ready-to-show', () => {
    setTimeout(() => {
      splash.close();
      mainWindow.show();
    }, 1500); // show splash for at least 1.5s
  });

  // Start the Python backend
  pythonProcess = spawn('python3', ['main.py']);

  pythonProcess.stdout.on('data', (data) => {
    console.log(`Python: ${data}`);
  });

  pythonProcess.stderr.on('data', (data) => {
    console.error(`Python Error: ${data}`);
  });

  pythonProcess.on('close', (code) => {
    console.log(`Python process exited with code ${code}`);
  });

  ipcMain.on('navigate', (event, view) => {
    console.log(`Navigating to: ${view}`);
    if (pythonProcess) {
        pythonProcess.stdin.write(`${view}\n`);
    }
  });

  ipcMain.handle('execute-python-code', async (event, code) => {
    return new Promise((resolve, reject) => {
      const pythonPath = path.join(__dirname, 'daw_env', 'bin', 'python');
      const command = `${pythonPath} -c "${code.replace(/"/g, '\\"')}"`;

      exec(command, (error, stdout, stderr) => {
        if (error) {
          reject(new Error(stderr || error.message));
        } else {
          resolve(stdout);
        }
      });
    });
  });

  ipcMain.on('sampler-action', (event, action) => {
    if (action === 'load-sampler') {
        console.log('Sampler button clicked');
        // Here you can invoke Python backend or other logic
        pythonProcess.stdin.write('sampler\n');
    }
  });
}

app.on('ready', createWindow);

app.on('window-all-closed', () => {
    if (process.platform !== 'darwin') {
        app.quit();
    }

    if (pythonProcess) {
        pythonProcess.kill();
    }
});

app.on('activate', () => {
    if (BrowserWindow.getAllWindows().length === 0) {
        createWindow();
    }
});
