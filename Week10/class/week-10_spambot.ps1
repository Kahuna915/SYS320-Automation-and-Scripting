# Send an email using Powershell

# Create an array of emails 
$toSend = @('noah.stiles@mymail.champlain.edu', 'stiles@mymail.champlain.edu', 'noah@mymail.champlain.edu')

# Message Body
$msg = "Hello"

# The while loop will spam the target, sends it over and over again
while ($true) {
    foreach ($email in $toSend) {

        # Send the Email:
        write-host "Send-MailMessage -from 'noah.stiles@mymail.champlain.edu' -To $email -Subject 'Tisk Tisk'`
        -Body $msg -SmtpServer x.x.x.x"
        

        # Pause for 1 second (safeguard)
        Start-Sleep 1
    }
}
