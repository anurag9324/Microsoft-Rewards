from selenium import webdriver
from selenium.webdriver.common.by import By
import time
import random

# Initialize the Edge WebDriver
driver = webdriver.Edge()

# List of random words to search
words1 = ["apple", "banana", "orange", "grape", "strawberry", "kiwi", "watermelon", "pineapple", "mango", "blueberry",
          "peach", "plum", "pear", "apricot", "lemon", "lime", "cherry", "fig", "pomegranate", "raspberry",
          "avocado", "coconut", "blackberry", "cantaloupe", "cranberry", "elderberry", "grapefruit", "guava", "honeydew",
          "lychee", "melon", "nectarine", "papaya", "passionfruit", "persimmon", "tangerine", "kiwifruit", "starfruit",
          "dragonfruit", "rhubarb", "plantain", "date", "jackfruit", "kumquat", "quince", "boysenberry", "tamarind",
          "lychee", "longan", "mulberry", "gooseberry", "currant", "acai", "acorn", "anise", "artichoke", "arugula",
          "asparagus", "bamboo", "beet", "bell pepper", "black-eyed pea", "bok choy", "broccoli", "brussels sprouts",
          "cabbage", "carrot", "cauliflower", "celery", "chard", "chili pepper", "cilantro", "collard greens", "corn",
          "cucumber", "daikon", "dandelion greens", "edamame", "eggplant", "endive", "fennel", "garlic", "ginger",
          "green bean", "jalapeno", "jicama", "kale", "leek", "lentil", "lettuce", "mushroom", "okra", "onion",
          "parsley", "parsnip", "pea", "pepper", "potato", "pumpkin", "radish", "rutabaga", "shallot", "snap pea",
          "spinach", "squash", "sweet potato", "tomato", "turnip", "watercress", "zucchini", "artichoke", "asparagus",
          "beetroot", "broccoli", "carrot", "cauliflower", "celery", "cucumber", "garlic", "ginger", "kale", "leek",
          "lettuce", "mushroom", "onion", "pepper", "potato", "pumpkin", "radish", "spinach", "tomato", "turnip",
          "zucchini", "hamburger", "pizza", "spaghetti", "sandwich", "steak", "sushi", "taco", "pancake", "waffle",
          "burrito", "noodle", "quesadilla", "fried rice", "lasagna", "soup", "salad", "omelette", "muffin", "bagel",
          "croissant", "donut", "cookie", "cake", "pie", "brownie", "cupcake", "ice cream", "chocolate", "candy"]

words2 = [
    "Abacus", "Abide", "Accord", "Active", "Angel", "April", "Arcade", "Aspect", "Atom", "Avenue",
    "Back", "Badge", "Barrel", "Belief", "Blast", "Blaze", "Bounce", "Bucket", "Bump", "Button",
    "Cactus", "Calm", "Carve", "Chase", "Chord", "Claw", "Clever", "Coast", "Colon", "Compose",
    "Dance", "Dazzle", "Decide", "Delight", "Diamond", "Dimple", "Dive", "Doll", "Dragon", "Drift",
    "Earnest", "Echo", "Eclipse", "Edge", "Elect", "Elite", "Embrace", "Empire", "Endure", "Energy",
    "Fable", "Fancy", "Farmer", "Fever", "Flame", "Flash", "Flicker", "Flourish", "Fly", "Frost",
    "Galaxy", "Gather", "Gem", "Glimmer", "Glitter", "Glow", "Goddess", "Grace", "Granite", "Grove",
    "Harbor", "Harmony", "Haven", "Heart", "Heaven", "Horizon", "Hum", "Humble", "Hybrid", "Hymn",
    "Icicle", "Idea", "Ignite", "Immerse", "Ink", "Inspire", "Ivory", "Jade", "Jazz", "Jewel",
    "Karma", "Keen", "Kiss", "Kite", "Knight", "Lagoon", "Laser", "Legend", "Lime", "Lunar"
]

words3 = [
    "Magnet", "Majestic", "Mellow", "Mint", "Mirth", "Mist", "Mystic", "Nebula", "Nectar", "Nifty",
    "Ocean", "Opal", "Orbit", "Oracle", "Oasis", "Olive", "Omen", "Optic", "Oyster", "Ozone",
    "Pace", "Paddle", "Paradise", "Passion", "Peach", "Peak", "Petal", "Pilot", "Pixel", "Placid",
    "Quaint", "Quartz", "Queen", "Quest", "Quick", "Quill", "Quiver", "Quota", "Quote", "Quartz",
    "Radiant", "Rapid", "Realm", "Rebel", "Reflect", "Ripple", "River", "Roam", "Rosy", "Ruby",
    "Sage", "Sapphire", "Savor", "Scenic", "Secret", "Serene", "Shadow", "Shimmer", "Silk", "Skylark",
    "Tale", "Talisman", "Tango", "Teal", "Tender", "Terrain", "Thrill", "Tidal", "Tint", "Tranquil",
    "Umbra", "Unique", "Unity", "Uplift", "Urban", "Utopia", "Valiant", "Vast", "Vivid", "Vortex",
    "Wander", "Wave", "Whisper", "Willow", "Wish", "Wonder", "Worthy", "Woven", "Wreath", "Wrinkle",
    "Xanadu", "Xenon", "Xylophone", "Xylitol", "X-ray", "Xerox", "Xylograph", "Xyst", "Xenophobia", "Xenial"
]

words4 = [
    "Yarn", "Yearn", "Yellow", "Yonder", "Youth", "Yacht", "Yield", "Yoga", "Yonder", "Yule",
    "Zap", "Zenith", "Zest", "Zigzag", "Zephyr", "Zeal", "Zen", "Zephyr", "Zero", "Zebra",
    "Alchemy", "Aloof", "Bamboo", "Bounty", "Bravo", "Cosmic", "Crescent", "Crucible", "Cynosure", "Chivalry",
    "Dainty", "Divine", "Dynamo", "Effervescent", "Elysian", "Ethereal", "Eureka", "Fervent", "Fervor", "Fusion",
    "Gentle", "Gossamer", "Gusto", "Halcyon", "Harmonious", "Haven", "Illustrious", "Incandescent", "Ineffable", "Ingenious",
    "Jovial", "Jubilant", "Juncture", "Juxtapose", "Kaleidoscope", "Kismet", "Labyrinth", "Lavish", "Luminous", "Majesty",
    "Noble", "Nostalgic", "Novel", "Nurturing", "Omnipotent", "Opulent", "Panacea", "Paragon", "Patina", "Pinnacle",
    "Quixotic", "Resplendent", "Reverie", "Serenity", "Sublime", "Succulent", "Sumptuous", "Surreal", "Tranquility", "Utopian"
]

word_lists = [words1, words2, words3, words4]

def scroll_randomly():
    for _ in range(random.randint(5, 10)):
        scroll_distance = random.randint(-1000, 1000)  # Random scroll distance
        driver.execute_script(f"window.scrollBy(0, {scroll_distance});")
        time.sleep(random.uniform(1, 3))  # Random delay between scrolls

# Loop through the list of words
for _ in range(35):  # Repeat the search process 35 times
    # Randomly select a word from the list
    selected_list = random.choice(word_lists)
    word = random.choice(selected_list)

    # Print the list being used for searching
    print(f"Searching from list {word_lists.index(selected_list) + 1}")

    # Go to the Google search page
    driver.get("https://www.bing.com/")

    # Search for the word
    search_box = driver.find_element(By.NAME, "q")
    search_box.send_keys(word)
    search_box.submit()

    # Add a delay of 15 seconds
    time.sleep(5)

    # Scroll randomly on the webpage
    scroll_randomly()

# Close the browser
driver.quit()
