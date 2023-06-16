# Sending SMS using Python script on WAGO PFC200 4G

## Requirements
- A WAGO PFC200 4G 750-8217
- Set up the PIN code in the WBM

## How to use
```
 docker run --rm --device=/dev/ttyUSB2:/dev/ttyUSB2:rw quenorha/sendsms -r "+336XXXXXXXX" -m "hello world"
```

"-r" is the phone number of the recipient

"-m" is the message to send

Make sure to link the /dev/ttyUSB2 of the host to the device of the container by the --device=/dev/ttyUSB2:/dev/ttyUSB2:rw argument


