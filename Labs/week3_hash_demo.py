import hashlib

def sha256_hex(text: str) -> str:
    return hashlib.sha256(text.encode('utf-8')).hexdigest()

def main():
    msg1 = input("Enter a message: ").strip()
    msg2 = input("Enter a slightly modified message: ").strip()

    print("message 1:", msg1)
    print("message 2:", msg2)

    h1 = sha256_hex(msg1)
    h2 = sha256_hex(msg2)

    print("\nSHA-256(msg1) =", h1)
    print("SHA-256(msg2) =", h2)

    if h1 == h2:
        if msg1 == msg2:
            print("\nObservation: hashes are identical because the inputs are identical.")
        else:
            print("\nObservation: hashes are identical even though inputs differ (this would be extremely unlikely).")
    else:
        print("\nObservation: hashes differ (avalanche effect).")

if __name__ == "__main__":
    main()
