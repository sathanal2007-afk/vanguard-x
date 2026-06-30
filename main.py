from fastapi import FastAPI, Request
from fastapi.responses import HTMLResponse, JSONResponse
import random
import time

app = FastAPI(title="Vanguard-X: Cyber Security Threat Control")

# 📊 Live Attack Data Storage
threat_logs = [
    {"id": 1, "timestamp": "18:50:15", "ip": "185.220.101.5", "country": "Russia", "attack_type": "Brute Force", "severity": "HIGH"},
    {"id": 2, "timestamp": "18:52:40", "ip": "45.133.1.42", "country": "China", "attack_type": "SQL Injection", "severity": "CRITICAL"},
    {"id": 3, "timestamp": "18:55:02", "ip": "91.241.17.9", "country": "USA", "attack_type": "Phishing Link", "severity": "MEDIUM"}
]

COUNTRIES = ["Russia", "China", "USA", "Germany", "North Korea", "Netherlands"]
ATTACK_TYPES = ["SQL Injection", "Brute Force", "XSS Attack", "DDoS Payload"]
SEVERITIES = ["LOW", "MEDIUM", "HIGH", "CRITICAL"]

@app.get("/api/threats")
def get_threats():
    return JSONResponse(content=threat_logs)

@app.post("/api/simulate-attack")
def simulate_attack():
    new_id = len(threat_logs) + 1
    current_time = time.strftime("%H:%M:%S")
    random_ip = f"{random.randint(40,220)}.{random.randint(10,250)}.{random.randint(1,250)}.{random.randint(1,250)}"
    
    attack = {
        "id": new_id,
        "timestamp": current_time,
        "ip": random_ip,
        "country": random.choice(COUNTRIES),
        "attack_type": random.choice(ATTACK_TYPES),
        "severity": random.choice(SEVERITIES)
    }
    
    threat_logs.insert(0, attack)
    if len(threat_logs) > 15:
        threat_logs.pop()
        
    return JSONResponse(content={"status": "ATTACK_TRIGGERED", "details": attack})

# 🖥️ Advanced Cyber Security Control Room UI
HTML_TEMPLATE = """
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Vanguard-X SOC Control Room</title>
    <script src="https://cdn.tailwindcss.com"></script>
    <link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/font-awesome/6.0.0/css/all.min.css">
    <style>
        @keyframes pulse-red {
            0%, 100% { background-color: rgba(220, 38, 38, 0.2); }
            50% { background-color: rgba(220, 38, 38, 0.6); }
        }
        .critical-alert { animation: pulse-red 1.5s infinite; }
    </style>
</head>
<body class="bg-slate-950 text-slate-100 min-h-screen font-mono p-6">

    <!-- Header Block -->
    <div class="border-b border-slate-800 pb-4 mb-6 flex justify-between items-center">
        <div>
            <h1 class="text-3xl font-extrabold text-cyan-400 tracking-wider"><i class="fa-solid fa-shield-halved text-rose-500 animate-pulse"></i> VANGUARD-X</h1>
            <p class="text-xs text-slate-500 mt-1">AI-Powered Zero-Trust Threat Intelligence Center</p>
        </div>
        <div class="flex gap-4">
            <button onclick="triggerAttack()" class="bg-rose-950 border border-rose-600 hover:bg-rose-900 text-rose-400 font-bold px-4 py-2 rounded-xl text-xs uppercase tracking-widest transition flex items-center gap-2">
                <i class="fa-solid fa-skull"></i> Simulate Hacker Attack
            </button>
        </div>
    </div>

    <!-- Stats Grid -->
    <div class="grid grid-cols-1 md:grid-cols-3 gap-6 mb-6">
        <div class="bg-slate-900 border border-slate-800 p-4 rounded-xl flex items-center justify-between shadow-lg">
            <div>
                <p class="text-xs text-slate-400 uppercase font-bold">System Status</p>
                <p class="text-xl font-bold text-emerald-400 mt-1">ACTIVE / SECURE</p>
            </div>
            <i class="fa-solid fa-circle-check text-2xl text-emerald-500"></i>
        </div>
        <div id="alert-banner" class="bg-slate-900 border border-slate-800 p-4 rounded-xl flex items-center justify-between shadow-lg transition-all duration-300">
            <div>
                <p class="text-xs text-slate-400 uppercase font-bold">Live Threat Level</p>
                <p id="threat-level-text" class="text-xl font-bold text-cyan-400 mt-1">MONITORING</p>
            </div>
            <i id="threat-icon" class="fa-solid fa-wave-square text-2xl text-cyan-500 animate-pulse"></i>
        </div>
        <div class="bg-slate-900 border border-slate-800 p-4 rounded-xl flex items-center justify-between shadow-lg">
            <div>
                <p class="text-xs text-slate-400 uppercase font-bold">Total Interceptions</p>
                <p id="total-attacks-count" class="text-xl font-bold text-amber-500 mt-1">3</p>
            </div>
            <i class="fa-solid fa-bolt text-2xl text-amber-500"></i>
        </div>
    </div>

    <!-- Main Live Activity Console -->
    <div class="bg-slate-900 border border-slate-800 rounded-xl p-6 shadow-2xl">
        <div class="flex justify-between items-center mb-4">
            <h2 class="text-sm font-bold text-slate-400 uppercase tracking-wider flex items-center gap-2">
                <span class="w-2 h-2 rounded-full bg-rose-500 animate-ping"></span> Live Threat Intelligence Stream
            </h2>
            <span class="text-xs text-slate-500 font-mono">Auto-refreshing via Core Engine Pipeline</span>
        </div>

        <div class="overflow-x-auto">
            <table class="w-full text-left border-collapse">
                <thead>
                    <tr class="border-b border-slate-800 text-slate-400 text-xs tracking-wider uppercase bg-slate-950/40">
                        <th class="py-3 px-4">Timestamp</th>
                        <th class="py-3 px-4">Attacker IP</th>
                        <th class="py-3 px-4">Origin Node</th>
                        <th class="py-3 px-4">Attack Vector</th>
                        <th class="py-3 px-4 text-right">Severity</th>
                    </tr>
                </thead>
                <tbody id="threat-table-body" class="divide-y divide-slate-800 text-sm">
                    <!-- Dynamic Log Ingestion Point -->
                </tbody>
            </table>
        </div>
    </div>

    <!-- Audio Beep for Hacker Intrusion Simulation -->
    <audio id="alert-sound" src="https://assets.mixkit.co/active_storage/sfx/951/951-84.wav" preload="auto"></audio>

    <script>
        async function fetchThreatLogs() {
            try {
                const response = await fetch('/api/threats');
                const data = await response.json();
                
                document.getElementById('total-attacks-count').innerText = data.length;
                const tbody = document.getElementById('threat-table-body');
                tbody.innerHTML = "";

                let topSeverity = "LOW";

                data.forEach(log => {
                    if(log.severity === "CRITICAL") topSeverity = "CRITICAL";
                    else if(log.severity === "HIGH" && topSeverity !== "CRITICAL") topSeverity = "HIGH";

                    let badgeColor = "bg-slate-800 text-slate-400";
                    if(log.severity === "CRITICAL") badgeColor = "bg-rose-950/60 border border-rose-500 text-rose-400 animate-pulse";
                    else if(log.severity === "HIGH") badgeColor = "bg-amber-950/60 border border-amber-500 text-amber-400";
                    else if(log.severity === "MEDIUM") badgeColor = "bg-blue-950/60 border border-blue-500 text-blue-400";

                    const row = `
                        <tr class="hover:bg-slate-800/50 transition duration-150">
                            <td class="py-3 px-4 text-slate-500 font-mono text-xs">${log.timestamp}</td>
                            <td class="py-3 px-4 text-cyan-400 font-bold">${log.ip}</td>
                            <td class="py-3 px-4 text-slate-300 font-medium"><i class="fa-solid fa-globe opacity-40 mr-1"></i> ${log.country}</td>
                            <td class="py-3 px-4 font-mono text-xs text-rose-400">${log.attack_type}</td>
                            <td class="py-3 px-4 text-right"><span class="px-2 py-0.5 rounded text-[10px] font-bold tracking-widest ${badgeColor}">${log.severity}</span></td>
                        </tr>
                    `;
                    tbody.innerHTML += row;
                });

                // Dynamically update UI state based on threat engine severity output
                const banner = document.getElementById('alert-banner');
                const levelText = document.getElementById('threat-level-text');
                const icon = document.getElementById('threat-icon');

                if (topSeverity === "CRITICAL") {
                    banner.className = "critical-alert border border-rose-600 p-4 rounded-xl flex items-center justify-between shadow-lg transition-all";
                    levelText.innerText = "🚨 CRITICAL THREAT DETECTED";
                    levelText.className = "text-xl font-bold text-rose-400 mt-1";
                    icon.className = "fa-solid fa-triangle-exclamation text-2xl text-rose-500 animate-bounce";
                } else if (topSeverity === "HIGH") {
                    banner.className = "bg-amber-950/40 border border-amber-600 p-4 rounded-xl flex items-center justify-between shadow-lg transition-all";
                    levelText.innerText = "⚠️ ELEVATED THREAT LEVEL";
                    levelText.className = "text-xl font-bold text-amber-400 mt-1";
                    icon.className = "fa-solid fa-radiation text-2xl text-amber-500 text-amber-500 animate-spin";
                } else {
                    banner.className = "bg-slate-900 border border-slate-800 p-4 rounded-xl flex items-center justify-between shadow-lg transition-all";
                    levelText.innerText = "MONITORING LOGS";
                    levelText.className = "text-xl font-bold text-cyan-400 mt-1";
                    icon.className = "fa-solid fa-wave-square text-2xl text-cyan-500 animate-pulse";
                }

            } catch (error) {
                console.error("Failed to sync threat pipelines:", error);
            }
        }

        async function triggerAttack() {
            try {
                document.getElementById('alert-sound').play();
            } catch(e) {}
            
            await fetch('/api/simulate-attack', { method: 'POST' });
            fetchThreatLogs();
        }

        // Initial setup execution
        fetchThreatLogs();
        // Polling loop interval mapping every 3 seconds
        setInterval(fetchThreatLogs, 3000);
    </script>
</body>
</html>
"""

@app.get("/", response_class=HTMLResponse)
def dashboard_ui():
    return HTML_TEMPLATE