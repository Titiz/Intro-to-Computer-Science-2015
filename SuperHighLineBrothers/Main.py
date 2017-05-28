import pygame
import math
import eztext
import operator


class Player(pygame.sprite.Sprite):

    def __init__(self):
        super().__init__()
        self.win = False
        self.suspicion = 0
        self.mealswipes = 14
        self.hit = False
        self.hittimer = 0
        self.score = 999
        self.folder = 'Sequence/'
        self.image_count = 1
        self.image_add = 0
        self.set_image(self.folder + '000' + str(self.image_count % 4) + '.gif')
        self.set_properties()
        self.frame = 0
        self.v_x = 0
        self.v_y = 0

        self.orientation = 'right'



        self.level = None

    def set_properties(self):

        self.rect = self.image.get_rect()

        self.origin_x = self.rect.centerx
        self.origin_y = self.rect.centery

        self.speed = 6



    def set_position(self, x, y):
        self.rect.x = x - self.origin_x
        self.rect.y = y - self.origin_y


    def set_image(self, filename = None):
        if filename is not None:
            self.image = pygame.image.load(filename)
            self.image = self.image.convert()


    def update(self, collidable = pygame.sprite.Group, event = None):



        self.set_image(self.folder + '000' + str(self.image_count % 4) + '.gif')
        if self.orientation == 'left':
            self.image = pygame.transform.flip(self.image, True, False)
        self.experience_gravity()

        self.rect.x += self.v_x

        collision_list = pygame.sprite.spritecollide(self, collidable, False)

        self.frame += 1
        if self.frame % 30 == 0 and self.score > 0:
            self.score -= 1


        if self.suspicion < 100:
            for collided_object in collision_list:
                if self.v_x > 0 and hasattr(collided_object, 'velocity') is False:
                    self.rect.right = collided_object.rect.left
                    self.v_x = 0
                if self.v_x < 0 and hasattr(collided_object, 'velocity') is False:
                    self.rect.left = collided_object.rect.right
                    self.v_x = 0

        projectiles = self.level.projectiles_bad        # Check for collision with projectiles that are harmful
        projectile_collision = pygame.sprite.spritecollide(self, projectiles , True)

        if len(projectile_collision) > 0 and self.hit is False:
            self.suspicion += 15
            self.v_y = -5
            self.hit = True

        enemies = self.level.enemies
        enemy_collision = pygame.sprite.spritecollide(self, enemies, False)

        if len(enemy_collision) > 0 and self.hit is False:
            self.suspicion += 20
            self.v_y = -5
            self.hit = True

        if self.hit is True:
            self.hittimer += 1
            if self.hittimer % 20 >= 0:
                self.image.set_alpha(60)
            if self.hittimer % 40 >= 20:
                self.image.set_alpha(255)
            if self.hittimer % 140 == 0:   #invulnerable after being hit. self.hit = False
                self.image.set_alpha(255)
                self.hittimer = 0
                self.hit = False

        self.rect.y += self.v_y

        collision_list = pygame.sprite.spritecollide(self, collidable, False)

        if self.suspicion < 100:
            for collided_object in collision_list:
                if self.v_y > 0:
                    # down direction
                    self.rect.bottom = collided_object.rect.top
                    self.v_y = 0
                elif self.v_y < 0:
                    # up direction
                    self.rect.top = collided_object.rect.bottom
                    self.v_y = 0
        if event is not None:
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_a:
                    self.v_x = -self.speed
                    self.image_add = 1
                    self.orientation = 'left'
                if event.key == pygame.K_d:
                    self.v_x = self.speed
                    self.image_add = 1
                    self.orientation = 'right'
                if event.key == pygame.K_w:
                    if self.v_y < 2:
                        self.v_y = -1.8*self.speed
                if event.key == pygame.K_SPACE:
                    if self.mealswipes > 0:
                        if self.orientation == 'right':
                            self.level.projectiles_good.add(Projectile(self.rect.right, self.rect.centery, 20, 20, 10, 'Proj_player/', 1))
                        else:
                            self.level.projectiles_good.add(Projectile(self.rect.left, self.rect.centery, 20, 20, -10, 'Proj_player/', 1))
                        self.mealswipes -= 1
            if event.type == pygame.KEYUP:
                if event.key == pygame.K_a:
                    self.v_x = 0
                    self.image_count = 1
                    self.image_add = 0
                if event.key == pygame.K_d:
                    self.v_x = 0
                    self.image_count = 1
                    self.image_add = 0
                if event.key == pygame.K_w and self.v_y < 0:
                    self.v_y = 0
        if self.frame % 12 == 0:
            self.image_count += self.image_add

        winbox = self.level.winbox
        winbox_collision = pygame.sprite.spritecollide(self, winbox, False)

        if len(winbox_collision) > 0:
            self.win = True


    def experience_gravity(self, gravity = 0.30):
        if self.v_y == 0: self.v_y = 1
        else: self.v_y += gravity









class Projectile(pygame.sprite.Sprite):

    def __init__(self, x, y, width, height, velocity, folder,  frames):

        super().__init__()

        self.image = pygame.Surface((width, height))
        self.folder = folder
        self.set_properties()
        self.rect.centerx = x
        self.rect.centery = y
        self.image_count = 0
        self.speed = velocity
        self.distance_travelled = 0
        self.frames = frames


    def set_properties(self):

        self.rect = self.image.get_rect()
        self.origin_x = self.rect.centerx
        self.origin_y = self.rect.centery


    def set_image(self, filename = None):
        if filename is not None:
            self.image = pygame.image.load(filename)
            self.image = self.image.convert()

    def update(self):
        self.set_image(self.folder + '000' + str(self.image_count % self.frames) + '.gif')
        self.image_count += 1
        self.rect.x += self.speed
        self.distance_travelled += self.speed


class Projectile2D(Projectile):
    def __init__(self, x, y, width, height, v_x, v_y, folder, frames):
        super().__init__(x, y, width, height, v_x, folder, frames)
        self.v_x = v_x
        self.v_y = v_y


    def update(self):
        self.set_image(self.folder + '000' + str(self.image_count % self.frames) + '.png')
        self.image_count += 1
        self.rect.x += self.v_x
        self.rect.y += self.v_y
        self.distance_travelled += self.speed




class RA(Player):
    def __init__(self, x ,y, current_level, width = 64, height = 64):
        super().__init__()
        self.health = 1
        self.rect.x = x
        self.rect.y = y
        self.level = current_level
        self.folder = 'RA/'
        self.animation_count = 0
        self.frame_wait = 12
        self.frames = 4



    def update(self, collidable = pygame.sprite.Group, event = None):

        if self.animation_count % self.frame_wait == 0:
            self.set_image(self.folder + '000' + str(self.image_count % self.frames) + '.gif')
            if self.check_distance(self.level.player_object) is True:
                self.image = pygame.transform.flip(self.image, True, False)
            self.image_count += 1
        self.animation_count += 1

        self.experience_gravity()

        self.rect.x += self.v_x

        if self.health > 0:

            collision_list = pygame.sprite.spritecollide(self, collidable, False)

            for collided_object in collision_list:
                if self.v_x > 0:
                    # down direction
                    self.rect.right = collided_object.rect.left
                    self.v_x = 0
                elif self.v_x < 0:
                    # up direction
                    self.rect.left = collided_object.rect.right
                    self.v_x = 0

            projectiles = self.level.projectiles_good       # Check for collision with projectiles that are harmful
            projectile_collision = pygame.sprite.spritecollide(self, projectiles , True)

            if len(projectile_collision) > 0:
                self.v_y = -5
                self.health -= 1


        self.rect.y += self.v_y


        if self.health > 0:
            collision_list = pygame.sprite.spritecollide(self, collidable, False)

            for collided_object in collision_list:
                if self.v_y > 0:
                    # down direction
                    self.rect.bottom = collided_object.rect.top
                    self.v_y = 0
                elif self.v_y < 0:
                    # up direction
                    self.rect.top = collided_object.rect.bottom
                    self.v_y = 0

        if self.health <= 0:
            self.level.enemies.remove(self)
            self.level.dead_enemies.add(self)
        if self.rect.y > window_height*2:
            self.level.dead_enemies.remove(self)

    def check_distance(self, player):
        if self.rect.x - player.rect.x < window_width/2:
            self.v_x = -2
        if self.rect.x - player.rect.x < -window_width * 1:
            self.health = 0
        return True

class PS(RA):
    def __init__(self, x, y, current_level):
        super().__init__(x, y, current_level)
        self.folder = 'PS/'
        self.timer = 0
        self.health = 2
        self.frames = 2
        self.frame_wait = 30


    def check_distance(self, player):
        vtotal = 4
        x_c = player.rect.centerx - self.rect.centerx
        y_c = player.rect.centery - self.rect.centery
        if x_c > 0:
            flip = False
        else:
            flip = True
        angle = math.atan2(y_c, x_c)
        v_x = math.cos(angle) * vtotal
        v_y = math.sin(angle) * vtotal
        if self.health > 0:
            if abs(self.rect.x - player.rect.x) < window_width/1:
                if self.timer % 180 == 0:
                    print(v_x)
                    print(v_y)
                    print(angle)
                    self.level.projectiles_bad.add(Projectile2D(
                        self.rect.centerx,
                        self.rect.centery,
                        30, 30, v_x, v_y, 'Proj_ps/B', 1
                    ))
        return flip

    def update(self, collidable = pygame.sprite.Group, event = None):
        super().update(collidable, event)
        self.timer += 1


class Block(pygame.sprite.Sprite):

    def __init__(self, x, y, width, height, image = False):

        super().__init__()


        self.image = pygame.Surface((width, height))
        if image is False:
            self.image.set_alpha(0)
        else:
            try:
                self.image = pygame.image.load(image)
                self.image = self.image.convert()
            except:
                self.image.fill((255,255,255))

        self.rect = self.image.get_rect()

        self.origin_x = self.rect.centerx
        self.origin_y = self.rect.centery

        self.rect.x = x - self.origin_x
        self.rect.y = y - self.origin_y


class MovingBlock(Block):
    def __init__(self, x, y, width, height, plusminus, velocity, image = True, direction = [1,0]):
        super().__init__(x, y, width, height, image)
        self.velocity = velocity
        self.plusminus = plusminus
        self.moved = 0
        self.direction = direction

    def update(self):
        if self.moved > self.plusminus:
            self.velocity *= -1
        elif self.moved < 0:
            self.velocity *= -1

        self.rect.x += self.velocity * self.direction[0]
        self.rect.y += self.velocity * self.direction[1]
        self.moved += self.velocity






class Level(object):

    def __init__(self, player_object):

        self.object_list = pygame.sprite.Group()
        self.projectiles_good = pygame.sprite.Group()
        self.projectiles_bad = pygame.sprite.Group()
        self.enemies = pygame.sprite.Group()
        self.background = pygame.sprite.Group()
        self.dead_enemies = pygame.sprite.Group()
        self.winbox = pygame.sprite.Group()
        self.player_object = player_object


        self.world_shift_x = 0

        self.right_viewbox = window_width/2 + window_width/8
        self.left_viewbox = window_width/2 - window_width/8

    def update(self):

        self.object_list.update()
        self.projectiles_bad.update()
        self.projectiles_good.update()
        for enemy in self.enemies:
            enemy.update(self.object_list)
        for dead_enemy in self.dead_enemies:
            dead_enemy.update(self.object_list)
        self.background.update()
        for each_projectile in self.projectiles_bad:
           if abs(each_projectile.distance_travelled) > window_width * 1:
               self.projectiles_bad.remove(each_projectile)
        for each_projectile in self.projectiles_good:
            if abs(each_projectile.distance_travelled) > window_width * 1:
                self.projectiles_good.remove(each_projectile)

        print(self.enemies)
        print(self.dead_enemies)

    def HUD(self):
        scoreFont = pygame.font.SysFont("VCR OSD Mono", 20)
        suspicion = 'suspicion: ' + str(self.player_object.suspicion) + '%'
        label = scoreFont.render(suspicion, 1, (255, 255, 255))
        score = 'score: ' + str(self.player_object.score)
        label_2 = scoreFont.render(score, 1, (255, 255, 255))
        swipes = 'meal swipes: ' + str(self.player_object.mealswipes)
        label_3 = scoreFont.render(swipes, 1, (255, 255, 255))
        window.blit(label, (window_width/7 * 6, 10))
        window.blit(label_2, (window_width/7 * 6, 30))
        window.blit(label_3, (window_width/7 *6, 50))


    def draw(self, window):
        window.fill((0,0,0))
        self.background.draw(window)
        self.object_list.draw(window)
        self.projectiles_bad.draw(window)
        self.projectiles_good.draw(window)
        self.enemies.draw(window)
        self.dead_enemies.draw(window)
        self.winbox.draw(window)
        self.HUD()

    def shift_world(self, shift_x):

        self.world_shift_x += shift_x

        for each_object in self.object_list:
            each_object.rect.x += shift_x
        for each_projectile in self.projectiles_good:
            each_projectile.rect.x += shift_x
        for each_projectile in self.projectiles_bad:
            each_projectile.rect.x += shift_x
        for each_enemy in self.enemies:
            each_enemy.rect.x += shift_x
        for background in self.background:
            background.rect.x += shift_x
        for dead_enemy in self.dead_enemies:
            dead_enemy.rect.x += shift_x
        for win_box in self.winbox:
            win_box.rect.x += shift_x

    def run_viewbox(self):

        if self.player_object.rect.x <= self.left_viewbox:
            view_difference = self.left_viewbox - self.player_object.rect.x
            self.player_object.rect.x = self.left_viewbox
            self.shift_world(view_difference)

        if self.player_object.rect.x >= self.right_viewbox:
            view_difference = self.right_viewbox - self.player_object.rect.x
            self.player_object.rect.x = self.right_viewbox
            self.shift_world(view_difference)



class Level_01(Level):

    def __init__(self, player_object):
        super().__init__(player_object)

        self.background.add(Block(3666.5, 400, 7333, 801, 'Levelm.png'))

        level = [
            [820, window_height - 105, 1640, 30],
            [1855, window_height - 105, 290, 30],
            [2820, window_height - 105, 1400, 30],
            [4450, window_height - 105, 1200, 30],
            [6920, window_height - 105, 880, 30],
            [431, 505, 120, 30],
            [1870, 570, 80, 30],
            [2010, 470, 190, 30],
            [2220, 475, 100, 30],
            [2410, 570, 58, 30],
            [2615, 570, 165, 30],
            [2830, 570, 30, 30],
            [2945, 470, 102, 30],
            [3100, 505, 102, 30],
            [3100, 600, 60, 30],
            [3270, 640, 75, 30],
            [3250, 670, 100, 30],
            [3680, 580, 105, 30],
            [4300, 620, 60, 130],
            [3520, 650, 10, 40],
            [3860, 650, 10, 40],
            [5540, 570, 100, 30],
            [6320, 690, 93, 30],
            [6440, 640, 110, 30],
            [6635, 606, 54, 30],
            [6770, 640,145, 90],
            [6800, 566, 100, 45],


        ]

        for block in level:
            block = Block(block[0], block[1], block[2], block[3])
            self.object_list.add(block)

        boundary_block = Block(-250, 400, 500, 2000, 'Boundary.png')
        self.object_list.add(boundary_block)
        boundary_block = Block(7580, 400, 500, 2000, 'Boundary.png')
        self.object_list.add(boundary_block)

        Ras = [
            [2100, 430],
            [1590, 430],
            [1620, 430],
            [2000, 500],
            [3020, 600],
            [2970, 100],
            [2400, 600],
            [3300, 100],
            [4250, 100],
            [4600, 100],
            [6630, 100]
        ]
        for Ra in Ras:
            self.enemies.add(RA(Ra[0], Ra[1], self))

        Pss = [
            [5530, 400],
            [3670, 200],
            [2224, 0],
            [6800, 0]
        ]
        for Ps in Pss:
            self.enemies.add(PS(Ps[0], Ps[1], self))

        moving_blocks = [
            [5160, 630, 100, 100, 330, 1, [1, -1]],
            [5700, 700, 100, 100, 330, 1, [0, -1]],
            [5940, 630, 100, 100, 300, 1, [1, 0]]
        ]
        for block in moving_blocks:
            block = MovingBlock(block[0], block[1], block[2], block[3], block[4], block[5], 'Moving Block.png', block[6])
            self.object_list.add(block)

        self.winbox.add(Block(7220, 600, 250, 200))


class MenuBox:
    def __init__(self, text, action):
        self.color = (255, 255, 255)
        self.width= window_width/1.8
        self.height = window_height/8
        self.text = text
        self.action = action
        self.selected = False
        self.x = 0
        self.y = 0
        Menu_choices.append(self)

class Score:
    def __init__(self, name, score):
        self.name = name
        self.score = score

if __name__ == "__main__":


    pygame.init()

    window_size = window_width, window_height = 1280, 800
    window = pygame.display.set_mode(window_size, pygame.RESIZABLE)

    pygame.display.set_caption('Super Highline Brothers')

    clock = pygame.time.Clock()
    frames_per_second = 60






    Menu_choices = []
    Play_box = MenuBox( 'PLAY', 'reset')
    How_box = MenuBox( 'How TO PLAY', 'howto')
    Score_box = MenuBox('HIGHSCORES', 'highscore')
    Quit_box = MenuBox('QUIT', 'quit')


    menuFont = pygame.font.SysFont("VCR OSD Mono", 75)
    scoreFont = pygame.font.SysFont("VCR OSD Mono", 50)



    gameCode = 'menu'
    gameActive = True
    selection = 0

    for i in range(len(Menu_choices)):
        item = Menu_choices[i]
        item.x = window_width/2 - item.width/2
        item.y = (window_height/5) + item.height * (i+1) + window_height/40 * (i+1)



    menuFont = pygame.font.SysFont("VCR OSD Mono", 75)
    scoreFont = pygame.font.SysFont("VCR OSD Mono", 50)

    menubackground_x = 0
    menubackground_moved = 0
    difference = 1

    while gameActive:
        window.fill((0,0,0))

        if gameCode == 'menu':
            for event in pygame.event.get():
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_s:
                        selection += 1
                    if event.key == pygame.K_w:
                        selection -= 1
                    if event.key == pygame.K_RETURN:
                        gameCode = Menu_choices[selection].action
            selection %= len(Menu_choices)

            menubackground = pygame.image.load('levelm.png')
            window.blit(menubackground, (menubackground_x, 0))


            print(menubackground_moved)
            if menubackground_moved > 7300 - window_width:
                difference *= -1
                print('yh')
                menubackground_moved = 0

            print(difference)
            menubackground_x -= difference
            menubackground_moved += abs(difference)

            image = pygame.image.load('title.png')
            window.blit(image, (0, 0))


            for item in Menu_choices:
                if Menu_choices[selection] == item:
                    window.fill((255,255,100), rect = [item.x, item.y, item.width, item.height])
                    label = menuFont.render(item.text, 1, (0,0,0))
                    window.blit(label, (item.x, item.y))
                else:
                    window.fill((255,255,255), rect = [item.x, item.y, item.width, item.height])
                    label = menuFont.render(item.text, 1, (0,0,0))
                    window.blit(label, (item.x, item.y))


        if gameCode == 'howto':
            for event in pygame.event.get():
                if event.type == pygame.KEYDOWN:
                        if event.key == pygame.K_SPACE> 0:
                            gameCode = 'menu'
            image = pygame.image.load('howto.gif')
            window.blit(image, (0, 0))


        if gameCode == 'reset':
            active_object_list = pygame.sprite.Group()
            player = Player()
            player.set_position(40, 600)

            active_object_list.add(player)

            level_list = []
            level_list.append(Level_01(player))

            current_level_number = 0
            current_level = level_list[current_level_number]
            player.level = current_level

            txtbx = eztext.Input(maxlength=10, color=(255, 255, 255), prompt='Name: ')
            txtbx.set_pos(window_width/5, window_height/6 * 5)

            gameCode = 'play'

        if gameCode == 'play':
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    gameActive = False

            # Update functions
            player.update(current_level.object_list, event)
            event = None
            current_level.update()
            # Logic testing

            current_level.run_viewbox()
            if player.rect.y > window_height * 2:
                gameCode = 'lose'
            if player.win == True:
                gameCode = 'input'

            # Draw everything

            current_level.draw(window)
            active_object_list.draw(window)


        if gameCode == 'highscore':

            image = pygame.image.load('Hbackground.png')
            window.blit(image, (0, 0))

            f = open('highscores.txt')
            scores = []
            l = []
            top_scores = []
            scores_d = {}
            for line in f:
                if line != '\n':
                    row = line.split(',')
                    scores.append(Score(row[0], int(row[1][:-1])))
                    scores_d[row[0]] = row[1][:-1]
            if len(scores) < 10:
                iteration = range(len(scores))
            else:
                iteration = range(10)
            for i in iteration:
                top_scores.append(max(scores, key=operator.attrgetter('score')))
                scores.remove(max(scores, key=operator.attrgetter('score')))
            print(scores_d)
            f.close()
            for event in pygame.event.get():
                if event.type == pygame.KEYDOWN:
                    gameCode = 'menu'

            for i in range(len(top_scores)):
                label_name = scoreFont.render(top_scores[i].name, 1, (255,255,255))
                label_score = scoreFont.render(str(top_scores[i].score), 1, (255,255,255))
                label_col = scoreFont.render(':', 1, (255,255,255))
                window.blit(label_col, (window_width/2, window_height/10 * i))
                window.blit(label_name, (window_width/4, window_height/10 * i))
                window.blit(label_score, (window_width/2 + window_width/20, window_height/10 * i))

        if gameCode == 'input':

            image = pygame.image.load('Hbackground.png')
            window.blit(image, (0, 0))

            time_score = 'Time Score:'
            time_score_v = player.score
            label = scoreFont.render(time_score, 1, (255, 255, 255))
            window.blit(label, (window_width/5, window_height/6))
            label = scoreFont.render(str(time_score_v), 1, (0, 255, 0))
            window.blit(label, (window_width/4 * 3, window_height/6))

            meal = 'Meal Swipe Multiplier:'
            meal_v = round((1 + (player.mealswipes * 0.1)), 2)
            label = scoreFont.render(meal, 1, (255, 255, 255))
            window.blit(label, (window_width/5, window_height/6 * 2))
            label = scoreFont.render(str(meal_v), 1, (0, 255, 0))
            window.blit(label, (window_width/4 * 3, window_height/6 * 2))

            suspicion = 'Suspicion deduction:'
            suspicion_v = player.suspicion * -10
            label = scoreFont.render(suspicion, 1, (255, 255, 255))
            window.blit(label, (window_width/5, window_height/6 * 3))
            label = scoreFont.render(str(suspicion_v), 1, (255, 0, 0))
            window.blit(label, (window_width/4 * 3, window_height/6 * 3))

            total = 'Total Score:'
            total_v = time_score_v * meal_v + suspicion_v
            total_v = int(round(total_v, 0))
            label = scoreFont.render(total, 1, (255, 255, 255))
            window.blit(label, (window_width/5, window_height/6 * 4))
            label = scoreFont.render(str(total_v), 1, (0, 255, 0))
            window.blit(label, (window_width/4 * 3, window_height/6 * 4))

            events = pygame.event.get()
            txtbx.update(events)
            txtbx.draw(window)
            print(txtbx.value)



            for event in events:
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_RETURN and len(txtbx.value) > 0:
                        f = open('highscores.txt', 'a')
                        f.write(txtbx.value + ',' + str(total_v)+ '\n')
                        gameCode = 'highscore'


        if gameCode == 'lose':
            for event in pygame.event.get():
                if event.type == pygame.KEYDOWN:
                    gameCode = 'menu'
            msg = 'You were Caught!'
            label = scoreFont.render(msg, 1, (255, 255, 255))
            window.blit(label, (window_width/3, window_height/6 * 1))
            msg = '(Or fell off the Highline)'
            label = scoreFont.render(msg, 1, (255, 255, 255))
            window.blit(label, (window_width/4, window_height/6 * 2))
            msg = 'press any key to return to the main menu'
            label = scoreFont.render(msg, 1, (255, 255, 255))
            window.blit(label, (window_width/20, window_height/6 * 5))



        if gameCode == 'quit':
            pygame.quit()
            quit()

        clock.tick(frames_per_second)
        pygame.display.update()
