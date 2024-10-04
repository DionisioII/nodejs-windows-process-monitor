
# Native Node.js Process Monitor for Windows

A native Windows API binding to have a list of running processes on windows.

## How to Use
```javascript
const Controls  = require('.\\build\\Release\\nodejs-windows-process-monitor')
console.log(Controls)

ProcessMonitor = new Controls.JSProcessMonitor()


console.log("\nprocesses : " + ProcessMonitor.getActiveProcesses());
```
#### Note
Returns list of comma separated active process running in windows.

## Development

#### node-gyp install for node version <= [17.9.1]
To build the project you need in Windows to install [windows-build-tools](https://github.com/felixrieseberg/windows-build-tools) in an elevated PowerShell prompt `npm install --global --production windows-build-tools` and then `npm install` or if you have `node-gyp` installed globally

#### node-gyp install for node version >= [17.9.1]
`npm install -g node-gyp`

#### Build

```bash
$ node-gyp configure
$ node-gyp build

```
#### Run
The repository contains a demo of the usage
```bash
$ node demo.js
```




