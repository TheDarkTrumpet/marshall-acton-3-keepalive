# Makefile for building executables using pyinstaller

# Define the source Python file
SOURCE_FILE = keepalive.py

# Define the output directory
OUTPUT_DIR = dist

# Default target: build all
build-all: cur-system

# Build for the current system
cur-system:
	pyinstaller --onefile --distpath $(OUTPUT_DIR) --name keepalive-$(shell date +%Y%m%d) --clean $(SOURCE_FILE)

# Clean build artifacts
clean:
	rm -rf $(OUTPUT_DIR)

.PHONY: build-all
