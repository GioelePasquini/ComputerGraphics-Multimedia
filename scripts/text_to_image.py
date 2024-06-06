import argparse
from diffusers import StableDiffusionPipeline
import torch
import os

if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument('--prompt', type=str, required=True)
    parser.add_argument('--output_path', type=str, required=True)
    args = parser.parse_args()
    prompt = args.prompt
    output_path = args.output_path
    pipe_text_to_image = StableDiffusionPipeline.from_pretrained("CompVis/stable-diffusion-v1-4",
                                                                 torch_dtype=torch.float16)
    pipe_text_to_image.to("cuda")
    prompt_finale = "A zoomed out DSLR photo of " + prompt + ", with a white background"
    images = pipe_text_to_image(prompt=prompt_finale, num_images_per_prompt=4).images
    os.makedirs(output_path, exist_ok=True)

    for i, image in enumerate(images):
        image_path = os.path.join(output_path, f"image_{i + 1}.png")
        image.save(image_path)



