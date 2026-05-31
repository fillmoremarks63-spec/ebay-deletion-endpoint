import json
import hashlib
from urllib.parse import parse_qs

VERIFICATION_TOKEN = "YOUR_TOKEN_HERE"

def app(environ, start_response):
    """WSGI application for Vercel"""
    
    # Get the full request path and query string
    path = environ.get('PATH_INFO', '/')
    query_string = environ.get('QUERY_STRING', '')
    
    # Parse query parameters
    query_params = parse_qs(query_string)
    challenge_code = query_params.get('challenge_code', [''])[0]
    
    if not challenge_code:
        response_body = json.dumps({'error': 'challenge_code parameter is required'})
        status = '400 Bad Request'
    else:
        # Generate challenge response
        challenge_response = hashlib.sha256(
            (challenge_code + VERIFICATION_TOKEN).encode()
        ).hexdigest()
        
        response_body = json.dumps({
            "challengeResponse": challenge_response
        })
        status = '200 OK'
    
    response_headers = [
        ('Content-Type', 'application/json'),
        ('Content-Length', str(len(response_body)))
    ]
    
    start_response(status, response_headers)
    return [response_body.encode()]
