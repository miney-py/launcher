; Needs to be compiled with purebasic from https://www.purebasic.com/download.php
; If someone has the ability and resources to replace this, please do so.

curdir.s = GetCurrentDirectory()

; look for python.exe
If FileSize(curdir.s + "python\pythonw.exe") > 0
  RunProgram(curdir.s + "python\pythonw.exe", "miney\launcher.py", curdir.s)
Else
  MessageRequester("Error", "python.exe not found in " + curdir + "Python", #PB_MessageRequester_Error)
EndIf

; IDE Options = PureBasic 5.71 LTS (Windows - x86)
; CursorPosition = 7
; EnableXP
; UseIcon = ..\res\miney-logo-hires.ico
; Executable = launcher.exe
; DisableDebugger