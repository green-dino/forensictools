from flask import Flask, render_template, request, redirect, url_for
import tempfile
from scapy.all import *
import networkx as nx
import matplotlib.pyplot as plt  # Import Matplotlib
from bokeh.io import output_file, show
from bokeh.models import Plot, Range1d, MultiLine, Circle, HoverTool, BoxZoomTool, ResetTool, LabelSet, ColumnDataSource
from bokeh.plotting import from_networkx
from bokeh.palettes import Spectral4
import webbrowser

app = Flask(__name__)

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/upload_pcap", methods=["POST"])
def upload_pcap():
    pcap_file = request.files["pcap_file"]
    if not pcap_file:
        return "No PCAP file uploaded", 400

    with tempfile.NamedTemporaryFile(delete=False) as temp_pcap:
        temp_pcap.write(pcap_file.read())
        pcap_path = temp_pcap.name

    G = generate_network_map(pcap_path)
    output_path = "network.html"
    plot_network_map(G, output_path)
    
    return redirect(url_for("show_network_map"))

@app.route("/show_network_map")
def show_network_map():
    return render_template("show_network_map.html")
def generate_network_map(pcap_path):
    try:
        pcap = rdpcap(pcap_path)
    except Exception as e:
        print(f"Failed to read PCAP file: {e}")
        return None

    G = nx.DiGraph()

    for packet in pcap:
        if IP in packet:
            src_ip = packet[IP].src
            dst_ip = packet[IP].dst
            G.add_edge(src_ip, dst_ip)

    mapping = {node: i for i, node in enumerate(G.nodes())}
    G_relabeled = nx.relabel_nodes(G, mapping)

    return G_relabeled  # Return the generated graph

def plot_network_map(G, output_path=None):
    pos = nx.spring_layout(G, k=0.15, iterations=20)
    # ...

    if output_path:
        plt.savefig(output_path)
        return f"Network map saved to {output_path}"  # Return a status message
    else:
        plt.show()
        return "Network map displayed in the browser"  # Return a status message

if __name__ == "__main__":
    app.run(debug=True)
