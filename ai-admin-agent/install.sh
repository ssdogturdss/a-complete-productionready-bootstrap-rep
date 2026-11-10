#!/bin/bash
set -e

echo "=== AI Admin Agent Installer ==="

# Detect Ubuntu
if [ -f /etc/os-release ]; then
    . /etc/os-release
    if [[ "$ID" != "ubuntu" ]]; then
        echo "Warning: Not Ubuntu. Continuing anyway."
    elif [[ "$VERSION_ID" != "22.04" ]]; then
        echo "Warning: Expected Ubuntu 22.04, got $VERSION_ID. Continuing."
    fi
fi

# Install prerequisites
echo "Installing prerequisites..."
sudo apt-get update -qq
sudo apt-get install -y -qq git curl python3 python3-venv python3-pip docker.io

# Create user if needed
if ! id "aiadmin" &>/dev/null; then
    sudo useradd -m -s /bin/bash aiadmin
    sudo usermod -aG docker aiadmin
    echo "Created user aiadmin"
fi

INSTALL_DIR="/opt/ai-admin-agent"
if [ ! -d "$INSTALL_DIR" ]; then
    sudo mkdir -p "$INSTALL_DIR"
    sudo chown aiadmin:aiadmin "$INSTALL_DIR"
    # Assume already cloned or user will place files here
    echo "Please ensure the repo is at $INSTALL_DIR"
fi

cd "$INSTALL_DIR"

# Run wizard
sudo -u aiadmin python3 -m venv wizard/venv || true
sudo -u aiadmin wizard/venv/bin/pip install -r wizard/requirements.txt -q
sudo -u aiadmin wizard/venv/bin/python wizard/wizard.py

echo "=== Installation Complete ==="
echo "Access the agent at http://<your-server-ip>:8080"
echo "Manage with: sudo systemctl status ai-admin-agent"
echo "Logs: journalctl -u ai-admin-agent -f"