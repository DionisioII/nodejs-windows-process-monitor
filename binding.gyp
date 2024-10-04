{
  "targets": [
    {
      "target_name": "nodejs-windows-process-monitor",
      "cflags!": [ "-fno-exceptions" ],
      "cflags_cc!": [ "-fno-exceptions" ],
      "sources": [
        "./src/background_process_monitor/background_process_monitor.cpp",
        "./src/background_process_monitor/background_process_monitor.h",
        "./src/index.cpp"
      ],
      "include_dirs": [
        "<!@(node -p \"require('node-addon-api').include\")"
      ],
      'defines': [ 'NAPI_CPP_EXCEPTIONS' ],
    }
  ]
}