#!/bin/bash
cp configs/agent.service /etc/systemd/system/ai-admin-agent.service
systemctl daemon-reload
systemctl enable --now ai-admin-agent
