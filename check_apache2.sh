#!/bin/bash

echo "Checking first.."
service apache2 status
echo "restarting.."
service apache2 restart
