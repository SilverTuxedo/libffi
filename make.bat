@echo off
if exist "%~dp0objlib.vcxproj" del /f "%~dp0objlib.vcxproj"
cmake %~dp0 && py patch_vcxproj.py "%~dp0objlib.vcxproj"
