#!/bin/bash
ping -c 1 $1 | grep 'from' | awk '{print $1}'
