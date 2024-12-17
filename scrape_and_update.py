import os
from datetime import datetime
import cv2
import numpy as np
import easyocr
from playwright.sync_api import sync_playwright
from supabase import create_client, Client
from dotenv import load_dotenv
from io import BytesIO

# Load environment variables
load_dotenv()
SUPABASE_URL = os.getenv("SUPABASE_URL")
SUPABASE_KEY = os.getenv("SUPABASE_KEY")
supabase: Client = create_client(SUPABASE_URL, SUPABASE_KEY)


def capture_element_screenshot():
    """
    Capture a screenshot of the target element and return it as an in-memory image.
    """
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=False)
        page = browser.new_page()
        url = "https://giacaphe.com/gia-ca-phe-noi-dia/"
        page.goto(url)

        target_selector = "#gia-noi-dia"
        page.wait_for_selector(target_selector, timeout=60000)

        # Take a screenshot and store it in memory
        screenshot_bytes = page.locator(target_selector).screenshot()
        browser.close()

    # Convert bytes to OpenCV image
    image_array = np.frombuffer(screenshot_bytes, np.uint8)
    image = cv2.imdecode(image_array, cv2.IMREAD_COLOR)
    return image


def preprocess_image(image):
    """
    Preprocess the in-memory image for OCR.
    """
    gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    _, binary_image = cv2.threshold(gray, 128, 255, cv2.THRESH_BINARY | cv2.THRESH_OTSU)
    resized = cv2.resize(binary_image, None, fx=2, fy=2, interpolation=cv2.INTER_LINEAR)
    denoised = cv2.fastNlMeansDenoising(resized, None, 30, 7, 21)
    return denoised


def extract_text(image):
    """
    Extract text from the preprocessed image using EasyOCR.
    """
    reader = easyocr.Reader(['vi'])
    results = reader.readtext(image)
    extracted_text = "\n".join([text for _, text, _ in results])
    return extracted_text


def insert_data_to_supabase(data):
    """
    Extract relevant table data and insert it into Supabase.
    """
    table_name = "coffee_prices"
    current_date = datetime.now().strftime("%Y-%m-%d")

    # List of valid provinces
    valid_provinces = ["Đắk Lắk", "Lâm", "Gia Lai", "Đắk Nông"]

    # Province name corrections
    province_corrections = {"Lâm": "Lâm Đồng"}

    # Split the text into lines
    lines = data.splitlines()
    structured_data = []

    i = 0
    while i < len(lines):
        province = lines[i].strip()

        # Check if the current line is a valid province
        if province in valid_provinces:
            price = lines[i + 1].strip() if i + 1 < len(lines) else None
            change = lines[i + 2].strip() if i + 2 < len(lines) else None

            # Ensure price and change are valid
            if price and change and price.replace(",", "").isdigit() and change.startswith("+"):
                province = province_corrections.get(province, province)
                structured_data.append({
                    "date": current_date,
                    "province": province,
                    "price": price,
                    "change": change
                })
            i += 3  # Move to the next set (province, price, change)
        else:
            i += 1  # Skip lines that are not valid provinces

    print("Structured Data to Insert:", structured_data)

    # Insert the structured data into Supabase
    for entry in structured_data:
        response = supabase.table(table_name).insert(entry).execute()
        print(f"Inserted: {entry}, Response: {response}")


def main():
    # Step 1: Capture screenshot in-memory
    print("Capturing screenshot...")
    image = capture_element_screenshot()

    # Step 2: Preprocess the image
    print("Preprocessing image...")
    preprocessed_image = preprocess_image(image)

    # Step 3: Extract text
    print("Extracting text...")
    extracted_text = extract_text(preprocessed_image)
    print("Extracted Text:", extracted_text)

    # Step 4: Insert data into Supabase
    print("Inserting data into Supabase...")
    insert_data_to_supabase(extracted_text)


if __name__ == "__main__":
    main()
