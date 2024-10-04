
const Controls  = require('.\\build\\Release\\nodejs-windows-process-monitor')
console.log(Controls)

ProcessMonitor = new Controls.JSProcessMonitor()


console.log("\nprocesses : " + ProcessMonitor.getActiveProcesses());



