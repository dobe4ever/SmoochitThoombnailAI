## python3 auto_thoombnail.py

from PIL import Image, ImageDraw, ImageFont

# def crop_center(image_path):
#     with Image.open(image_path) as img:
#         width, height = img.size
#         new_size = min(width, height)
#         left = (width - new_size) // 2
#         top = (height - new_size) // 2
#         right = (width + new_size) // 2
#         bottom = (height + new_size) // 2
#         img_cropped = img.crop((left, top, right, bottom))
#         img_cropped.save(image_path)

# def crop_center(image_path, horizontal_offset=1, vertical_offset=1):
#     with Image.open(image_path) as img:
#         width, height = img.size
#         new_size = min(width, height)

#         # Calculate the offset based on the orientation of the image
#         if width > height:  # Horizontal photo
#             left = int((width - new_size) * horizontal_offset)
#             right = width - int((width - new_size) * (1 - horizontal_offset))
#         else:  # Vertical photo
#             left = (width - new_size) // 2
#             right = (width + new_size) // 2

#         if height > width:  # Vertical photo
#             top = int((height - new_size) * vertical_offset)
#             bottom = height - int((height - new_size) * (1 - vertical_offset))
#         else:  # Horizontal photo
#             top = (height - new_size) // 2
#             bottom = (height + new_size) // 2

#         img_cropped = img.crop((left, top, right, bottom))
#         img_cropped.save(image_path)

def crop_edges(image_path, target_width=643, target_height=722):
    with Image.open(image_path) as img:
        width, height = img.size

        # Calculate the left and top coordinates for the crop box
        left = (width - target_width) / 2 if width > target_width else 0
        top = (height - target_height) / 2 if height > target_height else 0

        # Ensure the crop box is within the image bounds
        left = max(0, left)
        top = max(0, top)
        right = min(width, left + target_width)
        bottom = min(height, top + target_height)

        # Crop the image and save it
        img_cropped = img.crop((left, top, right, bottom))
        img_cropped.save(image_path)


def title_1_line(line1):
    # Open image
    image = Image.open("templates/Thumbnail-1.png")

    # Create a drawing object
    image_draw = ImageDraw.Draw(image)

    # Specify title text specs
    title_txt = line1.upper()  # Convert to uppercase
    title_font = ImageFont.truetype("templates/Gotham-Rounded-Bold.otf", 41)

    # Calculate the center of the left half of the thumbnail
    thumbnail_center_x = image.width // 4

    # Calculate the bounding box of the title text
    title_bbox = image_draw.textbbox((0, 0), title_txt, font=title_font)

    # Calculate the X position to center the title within the left half of the thumbnail
    title_x = thumbnail_center_x - ((title_bbox[2] - title_bbox[0]) // 2)

    # Specify title text position and draw it
    title_y = 595
    image_draw.text((title_x, title_y), title_txt, font=title_font, fill="white")

    # Save or display the modified image
    image.save("uploads/edit.png")

    return open("uploads/edit.png")


def title_2_lines(line1, line2):
    # Open image
    image = Image.open("templates/Thumbnail-2.png")

    # Create a drawing object
    image_draw = ImageDraw.Draw(image)

    # Specify title text specs
    title_font = ImageFont.truetype("templates/Gotham-Rounded-Bold.otf", 41)
    line1=line1.upper()
    line2=line2.upper()

    # Calculate the center of the left half of the thumbnail
    thumbnail_center_x = image.width // 4

    # Calculate the bounding box of the first line of text
    line1_bbox = image_draw.textbbox((0, 0), line1, font=title_font)

    # Calculate the X position to center the first line within the left half of the thumbnail
    line1_x = thumbnail_center_x - ((line1_bbox[2] - line1_bbox[0]) // 2)

    # Specify the position for the first line and draw it
    line1_y = 515
    image_draw.text((line1_x, line1_y), line1, font=title_font, fill="white")

    # Calculate the bounding box of the second line of text
    line2_bbox = image_draw.textbbox((0, 0), line2, font=title_font)

    # Calculate the X position to center the second line below the first line
    line2_x = thumbnail_center_x - ((line2_bbox[2] - line2_bbox[0]) // 2)

    # Specify the position for the second line and draw it
    line2_y = 631
    image_draw.text((line2_x, line2_y), line2, font=title_font, fill="white")

    # Save or display the modified image
    image.save("uploads/edit.png")

    return open("uploads/edit.png")

def write_ep_num(episode_num):
    # Open image
    image = Image.open("uploads/edit.png")

    # Create a drawing object
    image_draw = ImageDraw.Draw(image)

    # Specify episode text specs
    ep_font = ImageFont.truetype("templates/Gotham-Rounded-Bold.otf", 30)

    # Format the episode number
    ep_txt = f"Ep {episode_num}"

    # Specify episode text position and draw it
    ep_x, ep_y = 1150, 670
    image_draw.text((ep_x, ep_y), ep_txt, font=ep_font, fill="black")

    # Save or display the modified image
    image.save("uploads/edit.png")

    return open("uploads/edit.png")


def edit_photo():
    # Load the images
    image = Image.open("uploads/edit.png")
    photo = Image.open("uploads/photo.jpg")

    # Ensure both images have an alpha channel (transparency)
    image = image.convert("RGBA")
    # photo = photo.convert("RGBA")

    # Get the WH of the images
    width, height = image.size

    # Create a new image with the same WH and a fully transparent background
    result_image = Image.new("RGBA", (width, height), (0, 0, 0, 0))

    # Paste the bottom layer onto the new image
    result_image.paste(photo, (0, 0))

    # Paste the top layer onto the new image, using the alpha channel for transparency
    result_image.paste(image, (0, 0), mask=image)

    # Save the result
    result_image.save("uploads/new_thumbnail.png")

    return open("uploads/new_thumbnail.png")


def auto_thumbnail(episode_num, line1, line2=None):
    if line2:
        title_2_lines(line1, line2)
        write_ep_num(episode_num)
        edit_photo()
        return f"Here's your thumbnail! Ep {episode_num}: {line1} {line2}"

    else:
        title_1_line(line1)
        write_ep_num(episode_num)
        edit_photo()
        return f"Here's your thumbnail! Ep {episode_num}: {line1}"

