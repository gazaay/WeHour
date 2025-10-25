#!/usr/bin/env python3
"""
Simple HTTP server for Docsify documentation
"""
import http.server
import socketserver
import os
import sys

class DocsifyHTTPRequestHandler(http.server.SimpleHTTPRequestHandler):
    def end_headers(self):
        # Add CORS headers
        self.send_header('Access-Control-Allow-Origin', '*')
        self.send_header('Access-Control-Allow-Methods', 'GET, POST, OPTIONS')
        self.send_header('Access-Control-Allow-Headers', '*')
        
        # Set proper MIME type for markdown files
        if self.path.endswith('.md'):
            self.send_header('Content-Type', 'text/markdown; charset=utf-8')
        
        # Add aggressive cache control headers for development
        self.send_header('Cache-Control', 'no-cache, no-store, must-revalidate, max-age=0')
        self.send_header('Pragma', 'no-cache')
        self.send_header('Expires', '0')
        self.send_header('Last-Modified', self.date_time_string())
        self.send_header('ETag', '"no-cache"')
        
        super().end_headers()
    
    def log_message(self, format, *args):
        # Override to show cleaner logs
        sys.stderr.write("%s - - [%s] %s\n" %
                         (self.address_string(),
                          self.log_date_time_string(),
                          format%args))

def main():
    PORT = 3000
    
    # Change to the directory where this script is located
    os.chdir(os.path.dirname(os.path.abspath(__file__)))
    
    with socketserver.TCPServer(("", PORT), DocsifyHTTPRequestHandler) as httpd:
        print(f"🚀 Docsify server running on http://localhost:{PORT}")
        print("📖 Open http://localhost:3000 in your browser")
        print("⏹️  Press Ctrl+C to stop the server")
        print("-" * 60)
        try:
            httpd.serve_forever()
        except KeyboardInterrupt:
            print("\n🛑 Server stopped")
            sys.exit(0)

if __name__ == '__main__':
    main()
