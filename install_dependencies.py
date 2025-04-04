# install_dependencies.py
import subprocess
import sys
import pkg_resources

# List of required dependencies
DEPENDENCIES = [
    "matplotlib",
    "pillow",
    "numpy"
]

def install_package(package):
    """Install a package using pip."""
    try:
        subprocess.check_call([sys.executable, "-m", "pip", "install", package])
        print(f"Successfully installed {package}")
    except subprocess.CalledProcessError as e:
        print(f"Failed to install {package}. Error: {e}")
        sys.exit(1)

def check_and_install_dependencies():
    """Check if dependencies are installed; install if missing."""
    missing = []
    for package in DEPENDENCIES:
        try:
            pkg_resources.get_distribution(package)
            print(f"{package} is already installed.")
        except pkg_resources.DistributionNotFound:
            print(f"{package} is not installed. Installing now...")
            missing.append(package)
    
    if missing:
        print("\nInstalling missing dependencies...")
        for package in missing:
            install_package(package)
        print("\nAll dependencies installed successfully!")
    else:
        print("\nAll dependencies are already installed!")

if __name__ == "__main__":
    print("Checking dependencies for AFOQT Study simulation...")
    check_and_install_dependencies()