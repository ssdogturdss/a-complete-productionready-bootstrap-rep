#!/bin/bash
set -e
INSTALL_DIR="/opt/ai-admin-agent"
cat > /tmp/ai-admin-agent.service <<EOF
[Unit]
Description=AI Admin Agent
After=network.target

[Service]
Type=simple
User=aiadmin
WorkingDirectory=$INSTALL_DIR
EnvironmentFile=$INSTALL_DIR/.env
ExecStart=$INSTALL_DIR/agent/venv/bin/python -m uvicorn agent.main:app --host 0.0.0.0 --port 8080
Restart=always

[Install]
WantedBy=multi-user.target
EOF
sudo mv /tmp/ai-admin-agent.service /etc/systemd/system/ai-admin-agent.service
sudo systemctl daemon-reload
sudo systemctl enable ai-admin-agent
echo "systemd service installed."