from cx_Freeze import setup, Executable

setup(name = "Vision Insighta Object Detection Software",
      version = "0.1",
      description = "The Vision Insighta Software for detecting objects in realtime",
      executables = [Executable("main.py")]
      )