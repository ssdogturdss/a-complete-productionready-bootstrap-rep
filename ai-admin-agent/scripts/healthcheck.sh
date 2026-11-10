#!/bin/bash
curl -f http://localhost:8080/ || exit 1
echo "Agent healthy"
