from PIL import Image
import os

# 输入文件夹路径和输出文件夹路径
input_folder = 'big'
output_folder = 'small'

# 目标高度（1080像素）
target_height = 1080
target_width = 1080

def convert_to_webp(input_folder, output_folder):

    # 遍历输入文件夹中的所有文件
    for filename in os.listdir(input_folder):
        # 判断是不是文件夹 
        if os.path.isdir(os.path.join(input_folder, filename)):
            convert_to_webp(os.path.join(input_folder, filename), os.path.join(output_folder, filename))
        else:
            if filename.endswith('.webp'):
                input_path = os.path.join(input_folder, filename)
                output_path = os.path.join(output_folder, filename)
                if not os.path.exists(os.path.dirname( output_path)):
                    # 创建文件夹
                    os.makedirs(os.path.dirname( output_path))
                # 打开图片
                img = Image.open(input_path)

                # 计算新的宽度以保持宽高比
                width_percent = (target_width / float(img.size[0]))
                new_height = int(float(img.size[1]) * float(width_percent))

                # 调整图片分辨率
                resized_img = img.resize((target_width, new_height), Image.LANCZOS)

                # 保存调整后的图片
                resized_img.save(output_path, 'webp')

                print(f'{filename} 处理完成')

# 调用函数
convert_to_webp(input_folder, output_folder)
print('批量处理完成')
