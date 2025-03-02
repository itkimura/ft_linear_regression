# Makefile for Python project using Poetry

# Define default target
.DEFAULT_GOAL := help

# Install dependencies using Poetry
install:
	poetry install

# Run tests using Poetry
test:
	poetry run pytest

# Clean up the Poetry virtual environment
clean:
	poetry env remove --all

# Display help
help:
	@echo "Makefile commands:"
	@echo "  install      - Install dependencies using Poetry"
	@echo "  test         - Run tests with Poetry"
	@echo "  clean        - Remove the Poetry virtual environment"
	@echo "  help         - Display this help message"

