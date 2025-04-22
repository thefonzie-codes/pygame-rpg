class Camera:

    def __init__(self, width, height, grid_size):
        self.width = width
        self.height = height
        self.grid_size = grid_size
        self.offset_x = 0
        self.offset_y = 0

    def update(self, target):
        target_center_x = target.x + target.width // 2
        target_center_y = target.y + target.height // 2

        self.offset_x = target_center_x - (self.width // (2 * target.pixel_size))
        self.offset_y = target_center_y - (self.height // (2 * target.pixel_size))
       
    def apply(self, entity):
        return (entity.x - self.offset_x, entity.y - self.offset_y)
