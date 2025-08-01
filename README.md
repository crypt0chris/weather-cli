# Weather CLI

![Python](https://img.shields.io/badge/Python-3.10%2B-blue)
![License](https://img.shields.io/badge/License-MIT-green)
![PRs Welcome](https://img.shields.io/badge/PRs-welcome-brightgreen)

A sleek and minimalist terminal tool for fetching real-time weather conditions by city, using the OpenWeatherMap API. Perfect for CLI enjoyers and automation enthusiasts.

## ✨ Features

- 🌤 Current weather conditions by city name
- 🌡 Temperature shown in both °C / °F
- 💧 Humidity and 🌬 Wind speed included
- 🔧 Clean CLI output, easy to integrate and extend
- 📂 Supports `.env` file for API key management

## 📦 Installation

Clone the repo:

```bash
git clone https://github.com/crypt0chris/weather-cli.git
cd weather-cli
```

Install dependencies:

```bash
pip install -r requirements.txt
```

## 🔑 Setup

Create a `.env` file with your OpenWeatherMap API key:

```env
OPENWEATHER_API_KEY=your_api_key_here
```

Alternatively, copy `.env.example` and add your key:

```bash
cp .env.example .env
```

## 🚀 Usage

Run the CLI:

```bash
python3 main.py
```

Then enter a city in the format:  
`City,StateCode,CountryCode`  
_Examples:_

- `New York,NY,US`
- `Washington,DC,US`
- `Tokyo,JP`

## 📄 License

This project is licensed under the MIT License.
