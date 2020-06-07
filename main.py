import pygame, time, os, math, pygame_gui, sys, json  # Use the json so that your score saves and your game doesn't

# reset every time you leave... maybe


pygame.init()
icon = pygame.image.load('icon.png')
screen = pygame.display.set_mode((800, 600))
pygame.display.set_icon(icon)
pygame.display.set_caption("Plague-Clicker")
clock = pygame.time.Clock()  # For FPS and manager

manager = pygame_gui.UIManager((800, 600))  # Starting pygame gui

# Music

pygame.mixer_music.load('music.wav')
pygame.mixer.music.play(-1)

click_button = pygame_gui.elements.UIButton(relative_rect=pygame.Rect((350, 275), (100, 50)), text='Infect',
                                            manager=manager)

shop_textX = 0
shop_textY = 0
# First shop item

airborne_button = pygame_gui.elements.UIButton(relative_rect=pygame.Rect((660, 0), (140, 50)), text='Airborne',
                                               manager=manager)

airborneFont = pygame.font.Font("freesansbold.ttf", 16)
airbornePrice = 100
airborneCPS = 0.5


def show_airborne_text():
    airborne_text = airborneFont.render("Cost: 100 || CPS: 0.5", True, (255, 255, 255))
    screen.blit(airborne_text, (shop_textX, shop_textY))


showingAirborne = False
# -----
hardToDetectPrice = 500
hardToDetectFont = pygame.font.Font("freesansbold.ttf", 16)
hardToDetectCPS = 3


def show_hard_to_detect_text():
    hard_to_detect_text = hardToDetectFont.render("Cost: 500 || CPS: 3", True, (255, 255, 255))
    screen.blit(hard_to_detect_text, (shop_textX, shop_textY))


showing_hard_to_detect = False

quickerSpreadPrice = 5000
quicker_spread_font = pygame.font.Font("freesansbold.ttf", 16)
quicker_spreadCPS = 35


def show_quicker_spread_text():
    quicker_spread_text = quicker_spread_font.render("Cost: 5k || CPS: 35", True, (255, 255, 255))
    screen.blit(quicker_spread_text, (shop_textX, shop_textY))


showing_quicker_spread = False

epidemicPrice = 50000
epidemicFont = pygame.font.Font("freesansbold.ttf", 16)
epidemicCPS = 400


def show_epidemic_text():
    epidemic_text = epidemicFont.render("Cost: 50k || CPS: 400", True, (255, 255, 255))
    screen.blit(epidemic_text, (shop_textX, shop_textY))


showing_epidemic = False

pandemicPrice = 1000000
pandemicFont = pygame.font.Font("freesansbold.ttf", 16)
pandemicCPS = 10000


def show_pandemic_text():
    pandemic_text = pandemicFont.render("Cost: 1M || CPS: 10k", True, (255, 255, 255))
    screen.blit(pandemic_text, (shop_textX, shop_textY))


showing_pandemic = False
# -----------------------

quarterPrice = 100000000
quarterCPS = 150000
quarterFont = pygame.font.Font("freesansbold.ttf", 16)


def show_quarter_text():
    quarter_text = quarterFont.render("Cost: 100M || CPS: 150k", True, (255, 255, 255))
    screen.blit(quarter_text, (shop_textX, shop_textY))


showing_quarter = False

# --------
halfCPS = 8000000
halfPrice = 5000000000
halfFont = pygame.font.Font("freesansbold.ttf", 16)


def show_half_text():
    half_text = halfFont.render("Cost: 5B || CPS: 8M", True, (255, 255, 255))
    screen.blit(half_text, (shop_textX, shop_textY))


showing_half = False

# -------
fullPrice = 100000000000
fullFont = pygame.font.Font("freesansbold.ttf", 16)
fullCPS = 185000000


def show_full_plague_text():
    full_text = fullFont.render("Cost: 100B || CPS: 185M", True, (255, 255, 255))
    screen.blit(full_text, (shop_textX, shop_textY))


showing_fullPlague = False

# ----
planetaryCPS = 10000000000
planetaryPrice = 5000000000000
planetaryFont = pygame.font.Font("freesansbold.ttf", 16)


def show_planetary_text():
    planetary_text = planetaryFont.render("Cost: 5T || CPS: 10B", True, (255, 255, 255))
    screen.blit(planetary_text, (shop_textX, shop_textY))


showing_planetary = False

# ---
marsCPS = 3000000000000
marsPrice = 1000000000000000
marsFont = pygame.font.Font("freesansbold.ttf", 16)


def show_mars_text():
    mars_text = marsFont.render("Cost: 1QD || CPS: 3T", True, (255, 255, 255))
    screen.blit(mars_text, (shop_textX, shop_textY))


showing_mars = False
# And so on

hard_to_detect_button = pygame_gui.elements.UIButton(relative_rect=pygame.Rect((660, 50), (140, 50)), text='Hard to '
                                                                                                           'Detect',
                                                     manager=manager)
# ^^ is the SECOND ONE

quicker_spread_button = pygame_gui.elements.UIButton(relative_rect=pygame.Rect((660, 100), (140, 50)), text='Quicker '
                                                                                                            'Spread',
                                                     manager=manager)
epidemic_button = pygame_gui.elements.UIButton(relative_rect=pygame.Rect((660, 150), (140, 50)), text='Epidemic',
                                               manager=manager)
pandemic_button = pygame_gui.elements.UIButton(relative_rect=pygame.Rect((660, 200), (140, 50)), text='Pandemic',
                                               manager=manager)
quarter_plague_button = pygame_gui.elements.UIButton(relative_rect=pygame.Rect((660, 250), (140, 50)),
                                                     text='Quarter Plague',
                                                     manager=manager)
half_plague_button = pygame_gui.elements.UIButton(relative_rect=pygame.Rect((660, 300), (140, 50)), text='Half Plague',
                                                  manager=manager)
full_plague_button = pygame_gui.elements.UIButton(relative_rect=pygame.Rect((660, 350), (140, 50)), text='Full Plague',
                                                  manager=manager)
planetary_spread_button = pygame_gui.elements.UIButton(relative_rect=pygame.Rect((660, 400), (140, 50)),
                                                       text='Planetary '
                                                            'Spread',
                                                       manager=manager)  # Spreads to different planets
mars_infections_button = pygame_gui.elements.UIButton(relative_rect=pygame.Rect((660, 450), (140, 50)),
                                                      text='Mars Infections',
                                                      manager=manager)

stats_button = pygame_gui.elements.UIButton(relative_rect=pygame.Rect((720, 550), (80, 50)), text='Stats',
                                            manager=manager)

infectionsFont = pygame.font.Font("freesansbold.ttf", 24)
infection_textX = 25
infection_textY = 530


def show_infections_count():
    global infections, infection_textX, infection_textY
    infections_text = infectionsFont.render(f'Total Infections: {round(infections)}', True, (255, 255, 255))
    screen.blit(infections_text, (infection_textX, infection_textY))


powerFont = pygame.font.Font("freesansbold.ttf", 32)
power_textX = 25
power_textY = 450


def show_click_power():
    global click_power, power_textX, power_textY
    power_text = powerFont.render(f'Click Power: {click_power}', True, (255, 255, 255))
    screen.blit(power_text, (power_textX, power_textY))


cpsFont = pygame.font.Font("freesansbold.ttf", 32)
cps_textX = 25
cps_textY = 490


def show_cps():
    global cps, cps_textX, cps_textY
    cps_text = cpsFont.render(f'CPS: {cps}', True, (255, 255, 255))
    screen.blit(cps_text, (cps_textX, cps_textY))


clickSound = pygame.mixer.Sound('click.wav')  # sound for the click
blipSound = pygame.mixer.Sound('blip.wav')
# Now we are going to make the variables for the infections, etc.
infections = 0  # Change to json later
click_power = 1
cps = 0

# Virus Stages
stageOne_once = True
stageTwo_once = True
stageThree_once = True
stageFour_once = True
stageFive_once = True
stageSix_once = True
stageSeven_once = True
stageEight_once = True
stageNine_once = True
stageTen_once = True

stageOne = False
stageTwo = False
stageThree = False
stageFour = False
stageFive = False
stageSix = False
stageSeven = False
stageEight = False
stageNine = False
stageTen = False

# Stages code
stageOneX = 375
stageOneY = 170

stageTwoX = 365
stageTwoY = 160

stageThreeX = 350
stageThreeY = 140

stageFourX = 330
stageFourY = 120

stageFiveX = 312
stageFiveY = 85

stageSixX = 290
stageSixY = 45

stageSevenX = 277
stageSevenY = 25

stageEightX = 268
stageEightY = 10

stageNineX = 263
stageNineY = 0

stageTenX = 250
stageTenY = -28

origImg = pygame.image.load('virus.png')
stageOneImg = pygame.transform.scale(origImg, (50, 50))
stageTwoImg = pygame.transform.scale(origImg, (70, 70))
stageThreeImg = pygame.transform.scale(origImg, (100, 100))
stageFourImg = pygame.transform.scale(origImg, (140, 140))
stageFiveImg = pygame.transform.scale(origImg, (180, 180))
stageSixImg = pygame.transform.scale(origImg, (220, 220))
stageSevenImg = pygame.transform.scale(origImg, (245, 245))
stageEightImg = pygame.transform.scale(origImg, (265, 265))
stageNineImg = pygame.transform.scale(origImg, (280, 280))
stageTenImg = pygame.transform.scale(origImg, (310, 310))

lvl_up_sound = pygame.mixer.Sound('virusUp.wav')


def stage(x, y, img):
    screen.blit(img, (x, y))


success_sound = pygame.mixer.Sound('success.wav')
insufficient_sound = pygame.mixer.Sound('insufficient.wav')

local_high = 0
show_stats = True

running = True

while running:
    screen.fill((0, 0, 0))

    time_delta = clock.tick(60) / 1000.0

    for event in pygame.event.get():

        if event.type == pygame.QUIT:
            running = False
            sys.exit()

        if event.type == pygame.USEREVENT:
            if event.user_type == pygame_gui.UI_BUTTON_PRESSED:
                if event.ui_element == stats_button:
                    if show_stats:
                        show_stats = False
                    else:
                        show_stats = True
                if event.ui_element == click_button:
                    infections += click_power
                    # Add something somehow so that there is a delay when clicking.
                    pygame.mixer.Sound.play(clickSound)
                if event.ui_element == airborne_button:
                    if infections >= airbornePrice:
                        infections -= airbornePrice
                        cps += airborneCPS
                        pygame.mixer.Sound.play(success_sound)
                    else:
                        pygame.mixer.Sound.play(insufficient_sound)
                if event.ui_element == hard_to_detect_button:
                    if infections >= hardToDetectPrice:
                        infections -= hardToDetectPrice
                        cps += hardToDetectCPS
                        pygame.mixer.Sound.play(success_sound)
                    else:
                        pygame.mixer.Sound.play(insufficient_sound)
                if event.ui_element == quicker_spread_button:
                    if infections >= quickerSpreadPrice:
                        infections -= quickerSpreadPrice
                        cps += quicker_spreadCPS
                        pygame.mixer.Sound.play(success_sound)
                    else:
                        pygame.mixer.Sound.play(insufficient_sound)
                if event.ui_element == epidemic_button:
                    if infections >= epidemicPrice:
                        infections -= epidemicPrice
                        cps += epidemicCPS
                        pygame.mixer.Sound.play(success_sound)
                    else:
                        pygame.mixer.Sound.play(insufficient_sound)
                if event.ui_element == pandemic_button:
                    if infections >= pandemicPrice:
                        infections -= pandemicPrice
                        cps += pandemicCPS
                        pygame.mixer.Sound.play(success_sound)
                    else:
                        pygame.mixer.Sound.play(insufficient_sound)
                if event.ui_element == quarter_plague_button:
                    if infections >= quarterPrice:
                        infections -= quarterPrice
                        cps += quarterCPS
                        pygame.mixer.Sound.play(success_sound)
                    else:
                        pygame.mixer.Sound.play(insufficient_sound)
                if event.ui_element == half_plague_button:
                    if infections >= halfPrice:
                        infections -= halfPrice
                        cps += halfCPS
                        pygame.mixer.Sound.play(success_sound)
                    else:
                        pygame.mixer.Sound.play(insufficient_sound)
                if event.ui_element == full_plague_button:
                    if infections >= fullPrice:
                        infections -= fullPrice
                        cps += fullCPS
                        pygame.mixer.Sound.play(success_sound)
                    else:
                        pygame.mixer.Sound.play(insufficient_sound)
                if event.ui_element == planetary_spread_button:
                    if infections >= planetaryPrice:
                        infections -= planetaryPrice
                        cps += planetaryCPS
                        pygame.mixer.Sound.play(success_sound)
                    else:
                        pygame.mixer.Sound.play(insufficient_sound)
                if event.ui_element == mars_infections_button:
                    if infections >= marsPrice:
                        infections -= marsPrice
                        cps += marsCPS
                        pygame.mixer.Sound.play(success_sound)
                    else:
                        pygame.mixer.Sound.play(insufficient_sound)
            if event.user_type == pygame_gui.UI_BUTTON_ON_HOVERED:
                # Menu sound
                if event.ui_element != click_button and event.ui_element != stats_button:
                    pygame.mixer.Sound.play(blipSound)
                if event.ui_element == airborne_button:
                    showingAirborne = True
                if event.ui_element == hard_to_detect_button:
                    showing_hard_to_detect = True
                if event.ui_element == quicker_spread_button:
                    showing_quicker_spread = True
                if event.ui_element == epidemic_button:
                    showing_epidemic = True
                if event.ui_element == pandemic_button:
                    showing_pandemic = True
                if event.ui_element == quarter_plague_button:
                    showing_quarter = True
                if event.ui_element == half_plague_button:
                    showing_half = True
                if event.ui_element == full_plague_button:
                    showing_fullPlague = True
                if event.ui_element == planetary_spread_button:
                    showing_planetary = True
                if event.ui_element == mars_infections_button:
                    showing_mars = True
            if event.user_type == pygame_gui.UI_BUTTON_ON_UNHOVERED:
                if event.ui_element == airborne_button:
                    showingAirborne = False
                if event.ui_element == hard_to_detect_button:
                    showing_hard_to_detect = False
                if event.ui_element == quicker_spread_button:
                    showing_quicker_spread = False
                if event.ui_element == epidemic_button:
                    showing_epidemic = False
                if event.ui_element == pandemic_button:
                    showing_pandemic = False
                if event.ui_element == quarter_plague_button:
                    showing_quarter = False
                if event.ui_element == half_plague_button:
                    showing_half = False
                if event.ui_element == full_plague_button:
                    showing_fullPlague = False
                if event.ui_element == planetary_spread_button:
                    showing_planetary = False
                if event.ui_element == mars_infections_button:
                    showing_mars = False

        manager.process_events(event)
    manager.update(time_delta)

    keys = pygame.key.get_pressed()
    manager.draw_ui(screen)

    if showingAirborne:
        show_airborne_text()
    if showing_hard_to_detect:
        show_hard_to_detect_text()
    if showing_quicker_spread:
        show_quicker_spread_text()
    if showing_epidemic:
        show_epidemic_text()
    if showing_pandemic:
        show_pandemic_text()
    if showing_quarter:
        show_quarter_text()
    if showing_half:
        show_half_text()
    if showing_fullPlague:
        show_full_plague_text()
    if showing_planetary:
        show_planetary_text()
    if showing_mars:
        show_mars_text()

    infections += cps / 60  # 60 FPS and CPS is clicks per second so you have to do this.

    show_infections_count()
    if show_stats:
        show_click_power()
        show_cps()

    if infections >= local_high:
        local_high = round(infections)  # Use this for stages.
    #   print(local_high) -> debug

    if local_high >= airbornePrice and stageOne_once:
        stageOne = True
        stageOne_once = False
    if local_high >= hardToDetectPrice and stageTwo_once:
        pygame.mixer.Sound.play(lvl_up_sound)
        stageOne = False
        stageTwo = True
        stageTwo_once = False
    if local_high >= quickerSpreadPrice and stageThree_once:
        pygame.mixer.Sound.play(lvl_up_sound)
        stageTwo = False
        stageThree = True
        stageThree_once = False
    if local_high >= epidemicPrice and stageFour_once:
        pygame.mixer.Sound.play(lvl_up_sound)
        stageThree = False
        stageFour = True
        stageFour_once = False
    if local_high >= pandemicPrice and stageFive_once:
        pygame.mixer.Sound.play(lvl_up_sound)
        stageFour = False
        stageFive = True
        stageFive_once = False
    if local_high >= quarterPrice and stageSix_once:
        pygame.mixer.Sound.play(lvl_up_sound)
        stageFive = False
        stageSix = True
        stageSix_once = False
    if local_high >= halfPrice and stageSeven_once:
        pygame.mixer.Sound.play(lvl_up_sound)
        stageSix = False
        stageSeven = True
        stageSeven_once = False
    if local_high >= fullPrice and stageEight_once:
        pygame.mixer.Sound.play(lvl_up_sound)
        stageSeven = False
        stageEight = True
        stageEight_once = False
    if local_high >= planetaryPrice and stageNine_once:
        pygame.mixer.Sound.play(lvl_up_sound)
        stageEight = False
        stageNine = True
        stageNine_once = False
    if local_high >= marsPrice and stageTen_once:
        pygame.mixer.Sound.play(lvl_up_sound)
        stageNine = False
        stageTen = True
        stageTen_once = False

    if stageOne:
        stage(stageOneX, stageOneY, stageOneImg)
    if stageTwo:
        stage(stageTwoX, stageTwoY, stageTwoImg)
    if stageThree:
        stage(stageThreeX, stageThreeY, stageThreeImg)
    if stageFour:
        stage(stageFourX, stageFourY, stageFourImg)
    if stageFive:
        stage(stageFiveX, stageFiveY, stageFiveImg)
    if stageSix:
        stage(stageSixX, stageSixY, stageSixImg)
    if stageSeven:
        stage(stageSevenX, stageSevenY, stageSevenImg)
    if stageEight:
        stage(stageEightX, stageEightY, stageEightImg)
    if stageNine:
        stage(stageNineX, stageNineY, stageNineImg)
    if stageTen:
        stage(stageTenX, stageTenY, stageTenImg)

    pygame.display.update()
