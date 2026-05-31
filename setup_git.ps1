Param(
    [string]$Name = "vansh3452",
    [string]$Email = "11vanshgupta345@gmail.com",
    [string]$RepoPath = (Get-Location).Path
)

Write-Output "Repository path: $RepoPath"

if (-not (Get-Command git -ErrorAction SilentlyContinue)) {
    Write-Error "Git not found. Install Git first: winget install --id Git.Git -e --source winget"
    exit 1
}

git --version

Write-Output "Setting global git config..."
git config --global user.name $Name
git config --global user.email $Email

Set-Location $RepoPath

if (-not (Test-Path -Path (Join-Path $RepoPath '.git'))) {
    Write-Output "Initializing repository..."
    git init
} else {
    Write-Output ".git already exists in repository"
}

if (-not (Test-Path -Path (Join-Path $RepoPath '.gitignore'))) {
    @"
# Python
__pycache__/
*.py[cod]
*.so

# Virtualenv
env/
venv/
.venv/

# VSCode
.vscode/

# macOS
.DS_Store

# Jupyter
.ipynb_checkpoints/

# Logs
*.log

"@ | Out-File -Encoding utf8 .gitignore
    Write-Output "Created .gitignore"
} else {
    Write-Output ".gitignore already exists"
}

Write-Output "Staging files..."
git add .

$hasCommit = git rev-parse --verify HEAD 2>$null
if ($LASTEXITCODE -ne 0) {
    Write-Output "Creating initial commit..."
    git commit -m "Initial commit"
} else {
    Write-Output "Repository already has commits"
}

Write-Output "Setup complete. Run 'git status' to verify."
