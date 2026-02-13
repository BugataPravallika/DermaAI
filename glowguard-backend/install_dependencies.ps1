# GlowGuard Backend Dependencies Installation Script
# Run this in PowerShell to install all required packages

Write-Host "🚀 Installing GlowGuard Backend Dependencies..." -ForegroundColor Green
Write-Host ""

# Define the Python executable path
$pythonExe = "$PSScriptRoot\venv\Scripts\python.exe"
$pipExe = "$PSScriptRoot\venv\Scripts\pip.exe"

# Check if virtual environment exists
if (Test-Path -Path "$PSScriptRoot\venv" -PathType Container) {
    Write-Host "✅ Virtual environment found" -ForegroundColor Green
} else {
    Write-Host "❌ Virtual environment not found. Creating..." -ForegroundColor Yellow
    python -m venv "$PSScriptRoot\venv"
}

Write-Host ""
Write-Host "📦 Installing packages..." -ForegroundColor Cyan

# Install packages
& $pythonExe -m pip install --upgrade pip
& $pythonExe -m pip install -r "$PSScriptRoot\requirements.txt"

Write-Host ""
Write-Host "✅ Installation complete!" -ForegroundColor Green
Write-Host ""
Write-Host "📝 Next steps:" -ForegroundColor Cyan
Write-Host "1. To activate the environment, run:"
Write-Host "   & '$pythonExe' -m venv\Scripts\activate"
Write-Host "2. Or run the backend directly:"
Write-Host "   & '$pythonExe' main.py"
Write-Host ""
