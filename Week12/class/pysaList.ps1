# List the files in a directory and 
# List all files and print the full path.
# Get-ChildItem -Recurse -Include *.pdf,*.docx,*.txt -Path .\Week12\class\Documents | select FullName

Get-ChildItem -Recurse -Include *.pdf,*.docx,*.txt -Path .\Week12\class\Documents |Export-Csv `
-Path ./Week12/class/file.csv

# Import CSV File
$filelist = import-csv -Path ./Week12/class/file.csv -header FullName
# $filelist


# Loop through the results
foreach ($f in $filelist) {

    Get-ChildItem -Path $f.FullName

}
