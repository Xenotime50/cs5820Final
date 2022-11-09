import numpy as np
import pygame

SCREEN_WIDTH = 700
SCREEN_HEIGHT = 500

class LayerForSine:
    def __init__(self, weights, biases, inputs):
        self.inputs = inputs
        self.weights = weights
        self.biases = biases
        self.outputs = []

    def forward(self):
        for neuron in range(0, len(self.weights)):
            output = self.weights[neuron]*self.inputs[neuron] + self.biases[neuron]
            self.outputs.append(np.maximum(0, output))


class OutputLayer:
    def __init__(self, weights, inputs):
        self.weights = weights
        self.inputs = inputs
        self.output = 0

    def print_result(self):
        for x in range(0, len(self.weights)):
            self.output += self.weights[x]*self.inputs[x]
        print("y =", self.output)

    def get_output(self):
        for x in range(0, len(self.weights)):
            self.output += self.weights[x]*self.inputs[x]
        return self.output

def main():
    try:
        x = float(input("Enter a decimal value between 0 and 1: "))
        x = x - int(x)
        while x != "end":
            layer1 = LayerForSine([6.0, 3.5, -3.5, -6.0, -3.5, 3.6, 6.0, 0.0],
                                  [0.0, -0.42, 1.35, 3.69, 2.44, -2.9, -5.3, 0.0],
                                  [x]*8)
            layer1.forward()

            middle_weights = [-1.0]*7
            middle_weights.append(0.0)
            layer2 = LayerForSine(middle_weights,
                                  [0.7, 0.27, 0.3, 1.37, 0.27, 0.27, 0.7, 1],
                                  layer1.outputs)
            layer2.forward()

            output_weights = [-1.0]*7
            output_weights.append(1.94)
            output = OutputLayer(output_weights, layer2.outputs)
            output.print_result()

            x = float(input("Enter a decimal value between 0 and 1: "))
            x = x - int(x)
    except ValueError:
        print("Thanks for playing!")



def pygame_main():
    pygame.init()

    screen = pygame.display.set_mode([SCREEN_WIDTH, SCREEN_HEIGHT])

    running = True

    font = pygame.font.Font('freesansbold.ttf', 32)
    text = font.render("", True, (255, 255, 255))
    textRect = text.get_rect()
    textRect.center = (50, 450)

    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            elif event.type == pygame.MOUSEBUTTONDOWN:
                x_pos, y_pos = pygame.mouse.get_pos()
                x_val = round(x_pos/700, 2)
                layer1 = LayerForSine([6.0, 3.5, -3.5, -6.0, -3.5, 3.6, 6.0, 0.0],
                                      [0.0, -0.42, 1.35, 3.69, 2.44, -2.9, -5.3, 0.0],
                                      [x_val] * 8)
                layer1.forward()

                middle_weights = [-1.0] * 7
                middle_weights.append(0.0)
                layer2 = LayerForSine(middle_weights,
                                      [0.7, 0.27, 0.3, 1.37, 0.27, 0.27, 0.7, 1],
                                      layer1.outputs)
                layer2.forward()

                output_weights = [-1.0] * 7
                output_weights.append(1.94)
                output = OutputLayer(output_weights, layer2.outputs)
                y_val = round(output.get_output(), 2)

                pos_message = "x: " + str(x_val) + "  y: " + str(y_val)
                text = font.render(pos_message, True, (255, 255, 255))
                textRect = text.get_rect()
                textRect.center = (150, 450)

        screen.fill((0, 0, 0))
        screen.blit(text, textRect)

        x_prev = 0
        y_prev = SCREEN_HEIGHT / 2
        for x in range(0, 101):
            layer1 = LayerForSine([6.0, 3.5, -3.5, -6.0, -3.5, 3.6, 6.0, 0.0],
                                  [0.0, -0.42, 1.35, 3.69, 2.44, -2.9, -5.3, 0.0],
                                  [x/100] * 8)
            layer1.forward()

            middle_weights = [-1.0] * 7
            middle_weights.append(0.0)
            layer2 = LayerForSine(middle_weights,
                                  [0.7, 0.27, 0.3, 1.37, 0.27, 0.27, 0.7, 1],
                                  layer1.outputs)
            layer2.forward()

            output_weights = [-1.0] * 7
            output_weights.append(1.94)
            output = OutputLayer(output_weights, layer2.outputs)
            new_y = output.get_output()*250
            if x_prev != x:
                pygame.draw.line(screen, (255, 0, 0), (x_prev*7, SCREEN_HEIGHT/2 - y_prev),
                                 (x*7, SCREEN_HEIGHT/2 - new_y), width=5)
            x_prev = x
            y_prev = new_y
        pygame.display.flip()
    pygame.quit()


# if __name__ == "__main__":
#     main()

pygame_main()
