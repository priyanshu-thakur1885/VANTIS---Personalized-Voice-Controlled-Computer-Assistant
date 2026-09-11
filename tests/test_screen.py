from controllers.screen_controller import ScreenController
from core.vision_service import VisionService


screen = ScreenController()

image = screen.screenshot()

image.save("screen.png")


vision = VisionService()

result = vision.analyze_image(
    "screen.png",
    "Describe what is visible on this computer screen."
)

print(result)