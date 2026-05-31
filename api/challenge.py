import json
import hashlib
from urllib.parse import urlparse, parse_qs
VERIFICATION_TOKEN = "sportscardappverificationtoken2026abc123xyz7"
# MUST EXACTLY MATCH what you entered in eBay
ENDPOINT_URL = "https://ebay-deletion-endpoint-fillmore-marks-projects.vercel.app/api/ebay/deletion" print (request.url)
def handler(request):
    parsed_url = urlparse(request.url)
    query_params = parse_qs(parsed_url.query)
    challenge_code = query_params.get('challenge_code', [''])[0]
    if not challenge_code:
        return {
            'statusCode': 400,
            'body': json.dumps({'error': 'challenge_code parameter is required'})
        }
    #   THIS IS THE CRITICAL FIX
    data = challenge_code + VERIFICATION_TOKEN + ENDPOINT_URL
    challenge_response = hashlib.sha256(
        data.encode("utf-8")
    ).hexdigest()
    return {
        'statusCode': 200,
        'headers': {
            'Content-Type': 'application/json',
        },
        'body': json.dumps({
            "challengeResponse": challenge_response} ) }
