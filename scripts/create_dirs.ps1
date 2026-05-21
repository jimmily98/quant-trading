# Create directories and files for quant-trading project
# This script is project-root aware: it resolves the parent of the scripts folder and works from there

$scriptDir = Split-Path -Parent $MyInvocation.MyCommand.Definition
$projectRoot = Resolve-Path (Join-Path $scriptDir "..")
Set-Location -Path $projectRoot

# Directories to create
$dirs = @(
    "frontend/src/styles",
    "frontend/src/components/ControlPanel",
    "frontend/src/components/Chart",
    "frontend/src/components/MetricsCards",
    "frontend/src/components/Common",
    "frontend/src/services",
    "frontend/src/hooks",
    "frontend/src/pages",
    "frontend/src/tests",
    "backend/app/api/routers",
    "backend/app/models",
    "backend/app/services",
    "backend/app/repositories",
    "backend/app/utils",
    "backend/app/tests/unit",
    "backend/app/tests/integration",
    "infra/docker",
    "infra/k8s",
    "scripts",
    "docs",
    "backend/alembic"
)

foreach ($d in $dirs) {
    New-Item -ItemType Directory -Path $d -Force | Out-Null
}

# Top-level files
$files = @(
    "README.md",
    "pyproject.toml",
    "requirements.txt",
    "docker-compose.yml",
    "Dockerfile",
    "frontend/package.json",
    "frontend/tsconfig.json",
    "frontend/src/App.tsx",
    "frontend/src/index.tsx",
    "backend/app/main.py",
    "backend/app/config.py",
    "backend/app/api/__init__.py",
    "backend/app/api/routers/backtest.py",
    "backend/app/api/routers/health.py",
    "backend/app/models/db.py",
    "backend/app/models/schemas.py",
    "backend/app/models/orm_models.py",
    "backend/app/services/data_ingest.py",
    "backend/app/services/indicators.py",
    "backend/app/services/signal.py",
    "backend/app/services/backtester.py",
    "backend/app/repositories/backtest_repo.py",
    "backend/app/deps.py",
    "backend/app/utils/time_utils.py",
    "backend/app/utils/finance.py",
    "scripts/run_local.sh",
    "scripts/seed_data.py",
    "docs/architecture.md",
    "docs/api_contract.md"
)

foreach ($f in $files) {
    $full = Join-Path $projectRoot $f
    if (-not (Test-Path $full)) {
        New-Item -ItemType File -Path $full -Force | Out-Null
    }
}

Write-Output "Directories and files created under: $projectRoot"
