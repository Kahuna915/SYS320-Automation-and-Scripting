# Array of websites containg threat intell
$drop_urls = @('https://rules.emergingthreats.net/blockrules/emerging-botcc.rules','https://rules.emergingthreats.net/blockrules/compromised-ips.txt')

# Loop through the URLs for the rules list
foreach ($u in $drop_urls) {
    # Extract the filename
    $temp = $u.split("/")
    
    # The last element in the array plucked off is the filename
    $file_name = $temp[-1]

    if (Test-Path $file_name) {

        continue
    } else {

          # Download the rules list
          Invoke-WebRequest -Uri $u -OutFile $file_name

} # Close the statement

}# Close the foreach loop

# Array containing the filename
$input_paths = @('Week11\class\compromised-ips.txt', 'Week11\class\emerging-botcc.rules')

# Extract IP addressess
$regex_drop = '\b\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3}\b'

# Append the IP addresses to the temporary IP list.
Select-string -Path $input_paths -Pattern $regex_drop | `
ForEach-Object { $_.Matches } | `
ForEach-Object { $_.Value } | Sort-Object | ` 
Get-Unique | `
Out-File -FilePath "ips-bad.tmp"

# Get OS Selection 
$var = Read-Host -Prompt "Please enter Windows or IPTables"

switch ( $var )
{
    # Refrence: https://docs.microsoft.com/en-us/windows/security/threat-protection/windows-firewall/windows-firewall-with-advanced-security-administration-with-windows-powershell
    # Set up the IPlist in windows firewall
    Windows {(Get-Content -Path "Week11\class\ips-bad.tmp") | % `
    {"netsh advfirewall firewall add rule name=`"Block certain IPs $_`" action=block dir=in remoteip=$_"} | Out-File -FilePath "block_windowsIP.bat" `
    | Set-SCPItem -ComputerName '192.168.4.22' -Port 2222 -Credential (Get-Credential sys320)`
    -RemotePath '/home/sys320' -LocalFile '.\block_windowsIP.bat'}



    # Get the IP addresses discovered, loop through and replace the beginning of the liune with the IPTables syntax
    # After the IP address, add the remaining IPTables syntax and save the results to a file. 
    # iptables -A INPUT -s IP -j DROP
    IPTables {(Get-Content -Path "Week11\class\ips-bad.tmp") | % `
    { $_ -replace "^","iptables -A INPUT -s " -replace "$", " -j DROP"} | `
    Out-File -FilePath "./hwiptables.bash" | Set-SCPItem -ComputerName '192.168.4.22' -Port 2222 -Credential (Get-Credential sys320)`
    -RemotePath '/home/sys320' -LocalFile '.\hwiptables.bash'}
}

