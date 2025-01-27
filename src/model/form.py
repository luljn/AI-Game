import pygame



class Form :
    
    def __init__(self, window):
        
        self.window = window
        self.position = 0
        
        #Keyboard keys
        self.keys = 0
    
    def move(self, dt) :
        
        self.keys = pygame.key.get_pressed()
        if self.keys[pygame.K_UP] : 
            
            self.position.y -= 300 * dt
        
        if self.keys[pygame.K_DOWN] : 
            
            self.position.y += 300 * dt
            
        if self.keys[pygame.K_LEFT] : 
            
            self.position.x -= 300 * dt
            
        if self.keys[pygame.K_RIGHT] : 
            
            self.position.x += 300 * dt
            
        dt = self.window.clock.tick(60) / 1000
    
    def drawSprite(self) :
        
        pass