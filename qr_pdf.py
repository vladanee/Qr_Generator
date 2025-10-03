import qrcode
from PIL import Image
import os
import csv
from reportlab.lib.pagesizes import A4
from reportlab.pdfgen import canvas
from textwrap import wrap

# === CONFIG ===
OUTPUT_DIR = "qrcodes"
CSV_FILE = "purl_links.csv"
LOGO_FILE = "logo.png"   # Optional logo (PNG with transparent background recommended)
PDF_FILE = "qr_codes_sheet.pdf"

os.makedirs(OUTPUT_DIR, exist_ok=True)


def generate_qr(url, filename, logo_path=None):
    qr = qrcode.QRCode(
        version=4,  # bigger for logo space
        error_correction=qrcode.constants.ERROR_CORRECT_H,
        box_size=10,
        border=4,
    )
    qr.add_data(url)
    qr.make(fit=True)

    img = qr.make_image(fill_color="black", back_color="white").convert("RGB")

    if logo_path and os.path.exists(logo_path):
        logo = Image.open(logo_path).convert("RGBA")

        # Resize logo to fit in center
        qr_width, qr_height = img.size
        logo_size = qr_width // 5
        logo = logo.resize((logo_size, logo_size))

        pos = ((qr_width - logo_size) // 2, (qr_height - logo_size) // 2)

        img.paste(logo, pos, mask=logo)  # apply transparency mask

    img_path = os.path.join(OUTPUT_DIR, filename)
    img.save(img_path)
    return img_path


def create_pdf(qr_entries, pdf_file):
    c = canvas.Canvas(pdf_file, pagesize=A4)
    width, height = A4

    x, y = 50, height - 200
    max_per_row = 3
    counter = 0

    for qr_file, url in qr_entries:
        # Place QR image
        c.drawImage(qr_file, x, y, width=150, height=150)

        # Wrap long URL into multiple lines
        wrapped_url = wrap(url, 40)  # 40 chars per line
        c.setFont("Helvetica", 8)
        line_y = y - 12
        for line in wrapped_url:
            c.drawString(x, line_y, line)
            line_y -= 10  # spacing between lines

        x += 170
        counter += 1

        # New row
        if counter % max_per_row == 0:
            x = 50
            y -= 220

        # New page
        if y < 200:
            c.showPage()
            x, y = 50, height - 200

    c.save()


def main():
    qr_entries = []
    with open(CSV_FILE, newline="", encoding="utf-8") as csvfile:
        reader = csv.reader(csvfile)
        for i, row in enumerate(reader):
            if not row:
                continue
            url = row[0].strip()
            if not url.startswith("http"):
                continue

            filename = f"qr_{i+1}.png"
            img_path = generate_qr(url, filename, LOGO_FILE)
            qr_entries.append((img_path, url))
            print(f"[✔] QR generated for: {url} → {filename}")

    if qr_entries:
        create_pdf(qr_entries, PDF_FILE)
        print(f"\n📄 PDF sheet created: {PDF_FILE}")


if __name__ == "__main__":
    main()
