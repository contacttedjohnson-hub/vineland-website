@echo off
rem Preview the website from this PC or from a phone on the same Tailscale
rem network. Double-click this file, leave the black window open, then:
rem
rem   On this PC:        http://localhost:8765/
rem   On your phone:     http://backofficetower:8765/  or  http://100.108.136.93:8765/  (Tailscale on)
rem
rem Add /option-b/ or /themes/c.html etc. to the address for the other designs.
rem Close the black window to stop. If Windows asks about the firewall the
rem first time, click Allow so the phone can reach it.
cd /d "%~dp0"
echo.
echo  Vineland website preview
echo  ------------------------
echo  This PC:     http://localhost:8765/
echo  Your phone:  http://backofficetower:8765/  or  http://100.108.136.93:8765/
echo.
echo  Close this window to stop.
echo.
python -m http.server 8765 --bind 0.0.0.0
