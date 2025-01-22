import re
import csv

def extract_products_from_html_with_buffer(file_path, output_csv):
    product_pattern = re.compile(r"""
        <div\s+class="product-grid-item.*?">
        .*?                             
        <img.*?class="lazy\s+first-image".*?src="(.*?)".*?>
        .*?                                    
        <h4\s+class="name"><a\s+href=".*?">(.*?)</a></h4>
    """, re.DOTALL | re.VERBOSE)

    with open(file_path, 'r', encoding='utf-8') as file, open(output_csv, 'w', newline='', encoding='utf-8') as csv_file:
        csv_writer = csv.DictWriter(csv_file, fieldnames=["product_name", "photo_url"])
        csv_writer.writeheader()  # Write CSV header

        buffer_size = 1024 * 4  # CHUNK SIZE
        buffer = ""
        while chunk := file.read(buffer_size):
            buffer += chunk # Add new chunk of Data at the end of buffer

            # Find Matches in current buffer
            while match := product_pattern.search(buffer):
                photo_url, product_name = match.groups()
                csv_writer.writerow({
                    "product_name": product_name.strip(),
                    "photo_url": photo_url.strip()
                })

                # Remove Saved Matches from buffer
                buffer = buffer[match.end():]

        # Check the final data on the buffer
        while match := product_pattern.search(buffer):
            photo_url, product_name = match.groups()
            csv_writer.writerow({
                "product_name": product_name.strip(),
                "photo_url": photo_url.strip()
            })
            buffer = buffer[match.end():]

html_file = "MiHoYo.html"
output_csv = "products.csv"
extract_products_from_html_with_buffer(html_file, output_csv)
print(f"Products have been saved to {output_csv}.")
