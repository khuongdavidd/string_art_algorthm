from generate import create_string_art
import matplotlib.image as mpimg
import matplotlib.pyplot as plt

# result = create_string_art(input_file='StringArt/image.png', output_file='output.png', side_len=300, wb=False,  pull_amount = 3000, rgb= False)

# mpimg.imsave("StringArt/output.png", result, cmap=plt.get_cmap("gray"), vmin=0.0, vmax=1.0)


result_path = r'D:\Work_Space\django\string_art\Uploads/IMG_6959.JPG_result.png'
image_path = '/'.join(result_path.split('/')[-1:])

print(image_path)