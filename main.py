
import argparse
import os
import qrcode

def generate_qr_code(url):
    os.makedirs("qr_codes", exist_ok=True)

    img = qrcode.make(url)
    filename = "qr_codes/qr_code.png"

    img.save(filename)
    print(f"QR code generated successfully for: {url}")
    print(f"Saved to: {filename}")

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="QR Code Generator")
    parser.add_argument(
        "--url",
        default="http://github.com/kaw393939",
        help="URL to convert into a QR code"
    )

    args = parser.parse_args()
    generate_qr_code(args.url)
