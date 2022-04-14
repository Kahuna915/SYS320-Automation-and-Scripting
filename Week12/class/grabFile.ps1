# Create commandline parameters to copy a file and place into an evidence directory

param(
    [Parameter(Mandatory = $true)]
    [int]$reportNo,


    [Parameter(Mandatory = $true)]
    [String]$FilePath
)

# Create a directory with the report number
$reportDir = "rpt$reportNo"

# Creating a new directory
mkdir ./Week12/class/$reportDir 

# Copy the file into the new directory
copy-item $FilePath ./Week12/class/$reportDir