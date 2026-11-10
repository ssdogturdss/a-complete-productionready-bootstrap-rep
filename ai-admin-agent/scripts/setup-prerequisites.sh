#!/bin/bash
set -e
echo "Setting up prerequisites..."
sudo apt-get update -qq
sudo apt-get install -y -qq git curl python3 python3-venv docker.io caddy
echo "Prerequisites ready."