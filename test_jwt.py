from app.core.security import (
    create_access_token,
    decode_access_token,
)

# Generate a token representing user ID 1.
token = create_access_token({"sub": "1"})

print("Generated token:")
print(token)

# Decode and verify the token.
payload = decode_access_token(token)

print("\nDecoded payload:")
print(payload)

print("\nUser ID:", payload["sub"])
print("\nTesting an invalid token:")

try:
    decode_access_token("this-is-not-a-valid-token")
except Exception as exc:
    print(type(exc).__name__)
    print(exc)