﻿Send-MailMessage -To "manfregl@ucmail.uc.edu" -From "gmanfredi10@gmail.com" -Subject "IT3038C Windows SysInfo" -Body $BODY -SmtpServer smtp.gmail.com -port 587 -UseSSL -Credential (Get-Credential)