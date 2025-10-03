QR Code Generator with Logo & PDF Export

This Python script generates QR codes with a centered logo (with a clean white border for better visibility) and exports them both as individual PNG/SVG files and as a multi-page PDF sheet.

Project Structure
qr-code-generator/
│
├── qr_pdf.py          # Main script
├── README.md          # Documentation
├── requirements.txt   # Dependencies
├── purl_links.csv     # Example input file with URLs
├── logo.png           # Example logo used in QR codes
├── qrcodes/           # Generated QR codes (PNG & SVG)
└── qr_codes_sheet.pdf # Generated PDF with all QR codes


Features

✅ Generate QR codes from a list of URLs (CSV or TXT).
✅ Add a centered logo with a white border for professional look.
✅ Export both PNG and SVG formats for high-quality printing.
✅ Automatically build a PDF sheet (3 per row) with each QR code and its URL displayed below.
✅ Clean and easy-to-customize Python script.


Installation

Clone the repository and install dependencies:

git clone https://github.com/your-username/qr-code-generator.git
cd qr-code-generator
python -m venv venv
source venv/bin/activate   # On Windows: venv\Scripts\activate
pip install -r requirements.txt

Usage

Add your URLs to a purl_links.csv or purl_links.txt file (one URL per line).

Place your logo.png in the project folder.

Run the script:

python qr_pdf.py

Find results in:

qrcodes/ → individual PNG & SVG QR codes.

qr_codes_sheet.pdf → combined PDF sheet with all codes and URLs.

🖼️ Example Output

QR Codes (PNG & SVG) with centered logo and white border.

PDF Sheet → 3 QR codes per row, URLs neatly aligned below each code.

🛠️ Requirements

Dependencies are listed in requirements.txt:

qrcode
pillow
reportlab
svglib


Install them with:

pip install -r requirements.txt

📌 Notes

For best results, use a square PNG logo with transparent background.

Ensure your URLs are valid — they will be embedded directly into the QR codes.

SVGs are fully vectorized and can be scaled without loss of quality.
