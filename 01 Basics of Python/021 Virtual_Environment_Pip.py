# ============================================================
#        VIRTUAL ENVIRONMENT & PIP IN PYTHON
# ============================================================

# Virtual Environment (venv) is an isolated Python environment
# that allows you to install packages separately for each project.

# pip is Python's package manager used to:
# - Install packages
# - Upgrade packages
# - Remove packages
# - Manage dependencies

# ============================================================
#        WHY VIRTUAL ENVIRONMENTS ARE IMPORTANT
# ============================================================

# Without Virtual Environment:
# - Package version conflicts
# - One project can break another

# With Virtual Environment:
# - Isolated dependencies
# - Clean project structure
# - Production-safe development

# ============================================================
#        VENV & PIP SUMMARY TABLE
# ============================================================

# +---------------------+-------------------------------------+
# | Tool                | Purpose                             |
# +---------------------+-------------------------------------+
# | venv                | Create isolated Python environment  |
# | pip                 | Install & manage Python packages    |
# | requirements.txt    | Store project dependencies          |
# | pip freeze          | List installed packages             |
# +---------------------+-------------------------------------+

# ============================================================
#        CHECK PYTHON & PIP VERSION
# ============================================================

# Run in terminal / command prompt:
# python --version
# pip --version

# ============================================================
#        CREATING A VIRTUAL ENVIRONMENT
# ============================================================

# Command (Windows / Linux / Mac):
# python -m venv venv

# This creates a folder named "venv"

# ============================================================
#        ACTIVATING VIRTUAL ENVIRONMENT
# ============================================================

# Windows:
# venv\Scripts\activate

# Linux / macOS:
# source venv/bin/activate

# After activation, terminal shows:
# (venv)

# ============================================================
#        DEACTIVATING VIRTUAL ENVIRONMENT
# ============================================================

# deactivate

# ============================================================
#        INSTALLING PACKAGES USING pip
# ============================================================

# Install a package
# pip install requests

# Install specific version
# pip install django==4.2

# Upgrade a package
# pip install --upgrade pip

# ============================================================
#        LIST INSTALLED PACKAGES
# ============================================================

# pip list

# OR
# pip freeze

# ============================================================
#        UNINSTALL A PACKAGE
# ============================================================

# pip uninstall requests

# ============================================================
#        REQUIREMENTS.TXT FILE
# ============================================================

# Used to store project dependencies

# Create requirements.txt
# pip freeze > requirements.txt

# Example content:
# requests==2.31.0
# flask==2.3.2

# Install from requirements.txt
# pip install -r requirements.txt

# ============================================================
#        PROJECT STRUCTURE (BEST PRACTICE)
# ============================================================

# my_project/
# ├── venv/
# ├── app.py
# ├── requirements.txt
# └── README.md

# ============================================================
#        REAL-LIFE EXAMPLES
# ============================================================

# ------------------------------------------------------------
# Example 1: Web development project
# ------------------------------------------------------------

# python -m venv venv
# venv\Scripts\activate
# pip install flask
# pip freeze > requirements.txt

# ------------------------------------------------------------
# Example 2: Data science project
# ------------------------------------------------------------

# pip install numpy pandas matplotlib
# pip freeze > requirements.txt

# ------------------------------------------------------------
# Example 3: Clone & run someone else's project
# ------------------------------------------------------------

# git clone <repo_url>
# cd project
# python -m venv venv
# source venv/bin/activate
# pip install -r requirements.txt

# ============================================================
#        COMMON MISTAKES
# ============================================================

# 1. Installing packages globally instead of venv
# 2. Forgetting to activate virtual environment
# 3. Not using requirements.txt
# 4. Pushing venv folder to GitHub (❌)

# ============================================================
#        GITIGNORE FOR VENV
# ============================================================

# Add this to .gitignore:
# venv/
# __pycache__/
# *.pyc

# ============================================================
#        IMPORTANT POINTS
# ============================================================

# 1. Always use venv for projects
# 2. One project = one virtual environment
# 3. Never commit venv folder
# 4. Use requirements.txt for dependency sharing
# 5. pip is essential for real-world Python projects

# ============================================================
# End of File: 021 Virtual_Environment_Pip.py
# ============================================================
