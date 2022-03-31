<#
    Write Powershell code that copies the file "C:\Windows\system32\WindowsPowerShell\v1.0\powershell.exe" to your home directory using the "Copy-item" cmdlet.
    Rename the powershell.exe file based on the threat intell report so it should be something like "C:\Users\dunston\EnNoB-1214.exe."
    Check that the copied file exists.
    If so, then print it is found.  If not, then print an error.
#> 
# Set execution policy for this session to bypass
Set-ExecutionPolicy -ExecutionPolicy Bypass

# Create a message
$msg = "If you want your files restored, please contact me at dunston@champlain.edu. I look forward to doing business with you."
$filepath = "C:\Users\noahs\OneDrive\Desktop\Readme.READ"
$msg | Out-File -FilePath $filepath

# Check to see if readme file is there
if (Test-Path $filepath) {
    Write-Host -BackgroundColor "green" -ForegroundColor "white" "Readme file was created!"
    }
    else {
        Write-Host -BackgroundColor "red" -ForegroundColor "white" "Not Created!"
    
    }

# Directory to store the results of obtaining powershell execution
$dirstore = "C:\Users\noahs\OneDrive\Desktop\Sys_Automation\SYS320-Automation-and-Scripting\Week10\homework\"

# Create a random number to add to the powershell execution file.
$sbRand = Get-Random -Minimum 1000 -Maximum 1999

# Renamed file
$filepowershell = $dirstore + "EnNoB-"+  $sbRand + ".exe"

# Copy "C:\Windows\system32\WindowsPowerShell\v1.0\powershell.exe" to your home directory using the "Copy-item" cmdlet.
Copy-Item -Path "C:\Windows\system32\WindowsPowerShell\v1.0\powershell.exe" -Destination $filepowershell

# Check to see if powershell copy exists
if (Test-Path $filepowershell) {
    Write-Host -BackgroundColor "green" -ForegroundColor "white" "powershell file was created!"
    }
    else {
        Write-Host -BackgroundColor "red" -ForegroundColor "white" "Not Created!"
    
    }

