
# Check if Python is installed
$pythonInstalled = Get-Command python3 -ErrorAction SilentlyContinue
if (-not $pythonInstalled) {
    Write-Host "`nPython is not installed." -ForegroundColor Red
    exit 1
} else {
    try {
        $pythonVersion = python --version
        Write-Host ""
        Write-Host $pythonVersion
    } catch {
        $pythonVersion = python3 --version
        Write-Host ""
        Write-Host $pythonVersion
    }
}

# Check if pip is installed
$pipInstalled = Get-Command pip -ErrorAction SilentlyContinue
if (-not $pipInstalled) {
    Write-Host "`nPIP is not installed" -ForegroundColor Red
    exit 1
} else {
    $pipVersion = pip --version
    Write-Host $pipVersion
    Write-Host ""
}

# Install dependencies from requirements.txt
try {
    pip install -r requirements.txt
    Write-Host "`nSetup Complete..." -ForegroundColor Green
} catch {
    Write-Host "`nFailed to install modules..." -ForegroundColor Red
    exit 1
}

# Pause for 1 second
Start-Sleep -Seconds 1

# Display prompt message in yellow
Write-Host "`nPress Enter to continue..." -ForegroundColor Magenta
# Read user input
[void][System.Console]::ReadKey($true)
