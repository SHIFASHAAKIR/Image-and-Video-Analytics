from PIL import Image
img = Image.open("myimage.jpg")
sampled = img.resize((img.width//2, img.height//2))
sampled.save("sampled.jpg")
quantized = img.quantize(colors=16)
quantized.save("quantized.jpg")
print("Sampling and Quantization completed")
