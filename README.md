# eBay Deletion Endpoint

A serverless API endpoint for eBay Marketplace Notification Service verification.

## Overview

This endpoint handles eBay's challenge verification requests for webhook integration. When eBay needs to verify your endpoint, it sends a GET request with a `challenge_code` parameter, and this service responds with a challenge response hash.

## Setup

### Prerequisites
- eBay Developer Account
- Vercel Account
- Git

### Installation

1. Clone the repository
2. Update `VERIFICATION_TOKEN` in `api/challenge.py` with your eBay verification token
3. Deploy to Vercel (see below)

### Deployment to Vercel

1. Connect your repository to Vercel:
   - Go to https://vercel.com
   - Click "New Project"
   - Import your GitHub repository

2. Vercel will automatically detect the configuration and deploy

3. Once deployed, you'll get a URL like: `https://your-project.vercel.app`

4. Register your endpoint with eBay:
   - Go to eBay Developer Account
   - Add your endpoint: `https://your-project.vercel.app/api/challenge`

## How it Works

The endpoint receives a GET request with a challenge code:
```
GET /api/challenge?challenge_code=YOUR_CHALLENGE_CODE
```

It returns a JSON response with the challenge response:
```json
{
  "challengeResponse": "sha256_hash_of_code_plus_token"
}
```

## Environment Variables

- `VERIFICATION_TOKEN`: Your eBay verification token (currently hardcoded in the file)
