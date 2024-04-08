#!/usr/bin/env python3
from flask import Flask, request
from app import App

router = Flask(__name__)

@router.route('/')
def home():
	return 'Hello, World!'

@router.route('/api/test', methods=['POST'])
def test():
	data = request.get_json()
	print(data)
	return App.test(data)

if __name__ == '__main__':
	router.run(debug=True, port=5000)