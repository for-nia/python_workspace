#!/bin/bash

a=$(ls -l | grep fornia|awk '{print $3}'|head -n 1)
echo $a
