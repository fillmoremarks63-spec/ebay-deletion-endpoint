import json
import hashlib
from urllib.parse import urlparse, parse_qs

VERIFICATION_TOKEN = "YOUR_TOKEN_HERE"

def handler(request):
    """Vercel serverless function handler"""
    
    # Parse query parameters
    parsed_url = urlparse(request.url)
    query_params = parse_qs(parsed_url.query)
    
    challenge_code = query_params.get('challenge_code', [''])[0]
    
    if not challenge_code:
        return {
            'statusCode': 400,
            'body': json.dumps({'error': 'challenge_code parameter is required'})
        }
    
    # Generate challenge response
    challenge_response = hashlib.sha256(
        (challenge_code + VERIFICATION_TOKEN).encode()
    ).hexdigest()
    
    response = {
        "challengeResponse": challenge_response
    }
    
    return {
        'statusCode': 200,
        'headers': {
            'Content-Type': 'application/json',
        },
        'body': json.dumps(response)
    }

# Export handler for Vercel
__all__ = ['handler']
