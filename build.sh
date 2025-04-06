
pip install --upgrade pip
pip install poetry

# First try without updating
poetry install --no-interaction --no-ansi --sync || {
    # If fails, update lock file then install
    poetry lock --no-interaction
    poetry install --no-interaction --no-ansi
}