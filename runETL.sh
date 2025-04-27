#!/bin/bash

echo "🚀 Installing requirements..."
pip install -r requirements.txt

echo "🔄 Running ETL pipeline..."
python main.py
