import argparse
from diffusers import StableDiffusionImg2ImgPipeline
from PIL import Image
import torch
import os

if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument('--prompt', type=str, required=True)
    parser.add_argument('--input_path', type=str, required=True)
    parser.add_argument('--output_path', type=str, required=True)
    args = parser.parse_args()
    prompt = args.prompt
    input_path = args.input_path
    output_path = args.output_path
    init_image = Image.open(input_path).resize((768, 512))

    pipe_image_to_image = StableDiffusionImg2ImgPipeline.from_pretrained("CompVis/stable-diffusion-v1-4",
                                                                  torch_dtype=torch.float16)
    pipe_image_to_image.to("cuda")
    images = pipe_image_to_image(prompt=prompt, image=init_image, num_images_per_prompt=4).images
    os.makedirs(output_path, exist_ok=True)
    for i, image in enumerate(images):
        image_path = os.path.join(output_path, f"image_{i + 1}.png")
        image.save(image_path)

