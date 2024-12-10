# max_bitrate.py
#
# Usage: py max_bitrate.py tx_w tx_gain_db freq_hz dist_km rx_gain_db n0_j bw_hz
#
# Arguments:
#   tx_w
#   tx_gain_db
#   freq_hz
#   dist_km
#   rx_gain_db
#   n0_j
#   bw_hz
#
# Output: Determines the maximum achievable bitrate given several input parameters
# Written by Wheat Sturtevant
# Other contributers: None

# import modules
import math # math module
import sys # argv

# constants
c = 2.99792458e8
LLoss = 0.79
LAtmo = 1

# initialize script arguments
tx_w = float('nan')
tx_gain_db = float('nan')
freq_hz = float('nan')
dist_km = float('nan')
rx_gain_db = float('nan')
n0_j = float('nan')
bw_hz = float('nan')

# parse Script Arguments
if len(sys.argv)==8:
    tx_w = float(sys.argv[1])
    tx_gain_db = float(sys.argv[2])
    freq_hz = float(sys.argv[3])
    dist_km = float(sys.argv[4])
    rx_gain_db = float(sys.argv[5])
    n0_j = float(sys.argv[6])
    bw_hz = float(sys.argv[7])
else:
    print(\
        'Usage: '\
        'py max_bitrate.py tx_w tx_gain_db freq_hz dist_km rx_gain_db n0_j bw_hz'\
        )
    exit()

# write script below this line
C = tx_w*LLoss*tx_gain_db*(((c/freq_hz)/(4*math.pi*(dist_km*1000)))**2)*LAtmo*rx_gain_db
N = n0_j*bw_hz
r_max = bw_hz * math.log2((1+C/N))

print(math.floor(r_max))

# Test Usage:
# py max_bitrate.py tx_w tx_gain_db freq_hz dist_km rx_gain_db n0_j bw_hz