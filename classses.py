from settings import *

FPS = 40
_node_nums = 40
_node_scale_factor = 0.96

_node_size = W / _node_nums

class node(pygame.sprite.Sprite):
    def __init__(self, pos, *groups):
        super().__init__(*groups)
        
        self.colour_filled = 'bisque'
        self.colour_empty = 'maroon'
        self.filled = False

        self.image = pygame.Surface((_node_size, _node_size), pygame.SRCALPHA)
        self.rect = self.image.get_frect(topleft=pos)
        self.handle_col()

    def handle_col(self):
        self.colour = self.colour_filled if self.filled else self.colour_empty
        pygame.draw.rect(
            self.image, 
            self.colour, 
            self.image.get_frect().inflate(-_node_size * (1 - _node_scale_factor), -_node_size * (1 - _node_scale_factor)), 
            0, 
            5 if _node_scale_factor <= 0.95 else 1)
        pygame.draw.rect(
            self.image, 
            (30, 10, 10), 
            self.image.get_frect().inflate(-_node_size * (1 - _node_scale_factor), -_node_size * (1 - _node_scale_factor)), 
            3 if _node_scale_factor <= 0.95 else 1, 
            5 if _node_scale_factor <= 0.95 else 1)

    def update(self, *args, **kwargs):
        if pygame.mouse.get_pressed()[0] and self.rect.collidepoint(pygame.mouse.get_pos()): self.filled = True
        self.handle_col()
       
    
        
class board:
    def __init__(self, *groups):
        self.nodes:list[node] = [node((_node_size*i, _node_size*j), *groups) for j in range(_node_nums) for i in range(_node_nums)]
        
    def update(self):
        for j in range(_node_nums - 2, -1, -1):  # Avoid the bottom row
            for i in range(_node_nums):
                effective_index = j * _node_nums + i
                node = self.nodes[effective_index]
                below_index = (j + 1) * _node_nums + i
                below_left = below_index - 1 
                below_right = below_index + 1
                if not self.nodes[below_index].filled:
                    below_node = self.nodes[below_index]
                elif i < _node_nums - 1 and not self.nodes[below_right].filled:
                    below_node = self.nodes[below_right]
                elif i > 0 and not self.nodes[below_left].filled:
                    below_node = self.nodes[below_left]
                else:
                    continue
                 
                if node.filled and not below_node.filled:
                    node.filled = False
                    below_node.filled = True
                    

        
        
    