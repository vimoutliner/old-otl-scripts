#!/bin/bash
otl2ooimpress.py $1 > content.xml
zip $1.sxi content.xml
