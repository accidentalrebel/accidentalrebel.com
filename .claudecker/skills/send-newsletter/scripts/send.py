#!/usr/bin/env python3
"""Send a newsletter email via the Buttondown API."""

import argparse
import json
import os
import sys

import requests


def main():
    parser = argparse.ArgumentParser(description="Send newsletter via Buttondown API")
    parser.add_argument("--subject", required=True, help="Email subject line")
    parser.add_argument("--body-file", required=True, help="Path to markdown file with email body")
    parser.add_argument("--dry-run", action="store_true", help="Print payload without sending")
    args = parser.parse_args()

    api_key = os.environ.get("BUTTONDOWN_API_KEY")
    if not api_key:
        print("ERROR: BUTTONDOWN_API_KEY environment variable not set", file=sys.stderr)
        sys.exit(1)

    with open(args.body_file, "r") as f:
        body = f.read()

    if not body.strip():
        print("ERROR: Body file is empty", file=sys.stderr)
        sys.exit(1)

    payload = {"subject": args.subject, "body": body}

    if args.dry_run:
        print("=== DRY RUN ===")
        print(f"Subject: {args.subject}")
        print(f"Body length: {len(body)} chars")
        print(f"Payload:\n{json.dumps(payload, indent=2)[:500]}")
        return

    response = requests.post(
        "https://api.buttondown.com/v1/emails",
        headers={"Authorization": f"Token {api_key}"},
        json=payload,
    )

    if response.status_code in (200, 201):
        print(f"Newsletter sent successfully! Status: {response.status_code}")
        result = response.json()
        if result.get("id"):
            print(f"Email ID: {result['id']}")
    else:
        print(f"ERROR: API returned {response.status_code}", file=sys.stderr)
        print(response.text, file=sys.stderr)
        sys.exit(1)


if __name__ == "__main__":
    main()
