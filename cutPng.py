from PIL import Image

def crop_transparent(image_path):
    # 打开图像
    img = Image.open(image_path)

    # 获取图像的宽度和高度
    width, height = img.size

    # 获取图像非透明区域的边界框
    bbox = img.getbbox()

    # 裁剪图像，使用非透明区域的边界框作为裁剪框
    cropped_img = img.crop(bbox)

    # 保存裁剪后的图像
    cropped_img.save("cropped_image.png")

    print("裁剪完成")

if __name__ == "__main__":
    image_path = "your_image.png"  # 替换为你的图片路径
    crop_transparent(image_path)