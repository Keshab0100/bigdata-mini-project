#!/bin/bash
echo ""
echo "==== Count Sales ===="
echo ""
cat data.csv | python3 msalecount.py | sort | python3 rsalecount.py
echo ""
echo ""
echo "==== Count Accidents ===="
echo ""
cat data.csv | python3 mcountacc.py | sort | python3 rcountacc.py
echo ""
echo ""
echo "==== Type of Accidents ===="
echo ""
cat data.csv | python3 mtypeofa.py | sort | python3 rtypeofa.py
echo ""
