class Camera:

    def __init__(self, width, height):
        self.width = width
        self.height = height
        self.offset_x = 0
        self.offset_y = 0

    def update(self, target):
        target_center_x = target.position.x + target.width // 2  # Access Vector2 components
        target_center_y = target.position.y + target.height // 2

        self.offset_x = target_center_x - (self.width // (2 * target.pixel_size))
        self.offset_y = target_center_y - (self.height // (2 * target.pixel_size))

    def apply(self, entity):
        return (entity.position.x - self.offset_x, entity.position.y - self.offset_y)  # Return tuple for drawing