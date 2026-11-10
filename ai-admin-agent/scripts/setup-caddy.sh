#!/bin/bash
set -e
echo "Configuring Caddy..."
sudo systemctl enable --now caddy
echo "Caddy ready."