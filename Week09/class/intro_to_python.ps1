# get a list of running process



# Get list of members
#Get-Process | Get-Member

# Get a list of process: name, id, path

# Get-Process | Select-Object ProcessName, id, Path

# Save the output to a CSV File
#Get-Process | Select-object ProcessName, id, Path | Export-Csv -Path `
#"C:\Users\noahs\OneDrive\Desktop\processes.csv"

$OutputName = "C:\Users\noahs\OneDrive\Desktop\running_services.csv"
# System Services and properties
#Get-Service | Get-Member
#Get-Service | select-object Status, Name, DisplayName, BinaryPathName | export-csv -Path `
#$OutputName

# Get a list of running Services
Get-service | Where-Object { $_.Status -eq "Running"} | Export-Csv -Path `
$OutputName

# # Check to see if file exists
if (Test-Path $OutputName) {
Write-Host -BackgroundColor "green" -ForegroundColor "white" "Services file was created!"
}
else {
    Write-Host -BackgroundColor "red" -ForegroundColor "white" "Not Created!"

}