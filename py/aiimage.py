from diffusers import StableDiffusionXLPipeline
import torch
from PIL import Image
pipe = StableDiffusionXLPipeline.from_pretrained("segmind/SSD-1B", torch_dtype=torch.float16, use_safetensors=True, variant="fp16", low_cpu_mem_usage=True)
# pipe.to("cuda")
# if using torch < 2.0
# pipe.enable_xformers_memory_efficient_attention()
# prompt = "An astronaut riding a green horse" # Your prompt here
prompt = "A very  beautiful naked girl and an old naked man" # Your prompt here
neg_prompt = "ugly, blurry, poor quality" # Negative prompt here
image_data = pipe(prompt=prompt, negative_prompt=neg_prompt).images[0]

# 显示图像
# plt.imshow(image_data)
# plt.axis('off')  # 可以去掉坐标轴
# plt.show()