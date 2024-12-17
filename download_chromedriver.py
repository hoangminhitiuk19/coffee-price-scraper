import os
from datetime import datetime
import cv2
import easyocr
from playwright.sync_api import sync_playwright

def capture_screenshot():
    # Step 1: Define folder path and create it if it doesn't exist
    folder_path = "screenshots"
    os.makedirs(folder_path, exist_ok=True)

    # Step 2: Generate a filename based on the current date
    current_date = datetime.now().strftime("%d-%m-%Y")
    screenshot_name = f"{current_date}.png"
    screenshot_path = os.path.join(folder_path, screenshot_name)

    with sync_playwright() as p:
        # Step 3: Launch a browser
        browser = p.chromium.launch(headless=False)  # Set headless=True for automation
        page = browser.new_page()

        # Step 4: Navigate to the webpage
        url = "https://giacaphe.com/gia-ca-phe-noi-dia/"
        page.goto(url)

        # Step 5: Wait for the main content to load
        page.wait_for_selector("#gia-noi-dia", timeout=60000)

        # Step 6: Take a screenshot
        page.screenshot(path=screenshot_path, full_page=True)

        # Confirm screenshot saved
        print(f"Screenshot saved at {screenshot_path}")

        # Step 7: Close the browser
        browser.close()

    return screenshot_path

def preprocess_image(image_path):
    # Load the image
    image = cv2.imread(image_path)

    # Convert to grayscale
    gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

    # Apply thresholding to remove noise
    _, binary_image = cv2.threshold(gray, 128, 255, cv2.THRESH_BINARY | cv2.THRESH_OTSU)

    # Resize the image to enhance text readability
    resized = cv2.resize(binary_image, None, fx=2, fy=2, interpolation=cv2.INTER_LINEAR)

    # Apply denoising
    denoised = cv2.fastNlMeansDenoising(resized, None, 30, 7, 21)

    # Save preprocessed image for reference (optional)
    preprocessed_path = image_path.replace(".png", "_preprocessed.png")
    cv2.imwrite(preprocessed_path, denoised)
    print(f"Preprocessed image saved at {preprocessed_path}")

    return denoised

def extract_text(image):
    # Initialize EasyOCR reader
    reader = easyocr.Reader(['en', 'vi'])  # Include relevant languages

    # Perform OCR
    results = reader.readtext(image)

    # Extract and join text
    extracted_text = "\n".join([text for _, text, _ in results])
    return extracted_text

def save_text_to_file(text, output_path):
    # Save extracted text to a file
    with open(output_path, "w", encoding="utf-8") as file:
        file.write(text)
    print(f"Extracted text saved at {output_path}")

def main():
    # Step 1: Capture screenshot
    screenshot_path = capture_screenshot()

    # Step 2: Preprocess the screenshot
    preprocessed_image = preprocess_image(screenshot_path)

    # Step 3: Extract text using OCR
    extracted_text = extract_text(preprocessed_image)

    # Step 4: Save the extracted text to a file
    text_output_path = screenshot_path.replace(".png", ".txt")
    save_text_to_file(extracted_text, text_output_path)

if __name__ == "__main__":
    main()
