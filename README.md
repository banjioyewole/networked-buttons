# Networked-Buttons

## Top Level

This Script makes http request to localhost to get the `homebridge-http-webhooks` library to activate buttons in HomeKit. The registered URLs correspond to different buttons which can be bound to different scenes within the Home app.

# Distinction from electronic-gong

Electronic Gong uses `homebridge-http-switch` to add itself as switch to homekit that can make http requests when toggled. This is different from `networked-buttons` because networked-buttons adds switches that can then be used to control arbitrary homekit accessories. 

Requires `git://github.com/psf/requests.git`
