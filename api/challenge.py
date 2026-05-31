from http.server import BaseHTTPRequestHandler



import json



import hashlib



VERIFICATION_TOKEN = "YOUR_TOKEN_HERE"



class handler(BaseHTTPRequestHandler):



    def do_GET(self):



        challenge_code = self.path.split("challenge_code=")[-1]



        challenge_response = hashlib.sha256(



            (challenge_code + VERIFICATION_TOKEN).encode()



        ).hexdigest()



        response = {



            "challengeResponse": challenge_response



        }



        self.send_response(200)



        self.send_header("Content-Type", "application/json")



        self.end_headers()



        self.wfile.write(json.dumps(response).encode())
