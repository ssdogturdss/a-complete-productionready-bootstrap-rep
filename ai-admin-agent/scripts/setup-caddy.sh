#!/bin/bash
# Install Caddy
curl -1sLf 'https://dl.cloudsmith.io/public/caddy/stable/gpg.key' | gpg --dearmor -o /etc/apt/keyrings/caddy-stable.gpg
echo "deb [signed-by=/etc/apt/keyrings/caddy-stable.gpg] https://dl.cloudsmith.io/public/caddy/stable/deb/ubuntu jammy main" > /etc/apt/sources.list.d/caddy.list
apt update && apt install -y caddy
systemctl enable --now caddy
