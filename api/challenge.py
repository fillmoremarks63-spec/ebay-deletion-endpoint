from http.server import BaseHTTPRequestHandler



import json



import hashlib



VERIFICATION_TOKEN = "v^1.1#i^1#f^0#p^1#I^3#r^0#t^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"



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
