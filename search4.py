from selenium import webdriver
from selenium.webdriver.common.by import By
import time
import random

# Initialize the Edge WebDriver
driver = webdriver.Edge()

# List of random words to search

words1 = [
    "Algorithm", "API", "Array", "Backend", "Binary", "Bit", "Boolean", "Bug", "Byte", "Cache",
    "Cloud", "Compiler", "CPU", "Cryptography", "Data", "Database", "Debugging", "Deployment",
    "DNS", "Encryption", "Firewall", "Frontend", "Function", "Git", "GUI", "HTML", "HTTP", "IDE",
    "IP Address", "JavaScript", "JSON", "Kernel", "Library", "Loop", "Machine Learning", "Malware",
    "Memory", "Module", "Network", "Node.js", "Object-Oriented", "Operating System", "Packet",
    "Parameter", "PHP", "Pixel", "Port", "Protocol", "Python", "Query", "RAM", "Recursion",
    "Repository", "Router", "SaaS", "Scripting", "SDK", "Server", "Software", "SQL", "Stack",
    "String", "Syntax", "TCP/IP", "Thread", "Token", "UI/UX", "Variable", "Version Control",
    "Virtualization", "VPN", "Webhook", "Websocket", "XML", "API Gateway", "Asynchronous",
    "Bitwise", "Blockchain", "CLI", "Containerization", "Continuous Integration", "DevOps",
    "Docker", "Ethernet", "Framework", "Hashing", "Inheritance", "JSON Web Token", "Load Balancer",
    "Microservices", "Middleware", "Multithreading", "NoSQL", "ORM", "RESTful API", "SSH",
    "SSL/TLS", "Unit Testing", "Virtual Machine", "Web Development",
    "What is the difference between an interpreted language and a compiled language?",
    "How does a binary search algorithm work?",
    "What is the purpose of an API?",
    "Explain the concept of object-oriented programming.",
    "What is a data structure and why is it important?",
    "How does recursion work in programming?",
    "What is the difference between a stack and a queue?",
    "What is a linked list and how is it different from an array?",
    "Explain the concept of inheritance in OOP.",
    "What is polymorphism in programming?",
    "How does garbage collection work in programming languages?",
    "What is a hash table and how does it work?",
    "Explain the difference between synchronous and asynchronous programming.",
    "What is a RESTful API and how does it work?",
    "How do you manage memory in C++?",
    "What is the difference between TCP and UDP?",
    "Explain the concept of a software design pattern.",
    "What is the purpose of unit testing in software development?",
    "How does a version control system like Git work?",
    "What is the difference between a database and a data warehouse?",
    "What is a virtual machine and how does it work?",
    "How does encryption work in computer security?",
    "What is the difference between SQL and NoSQL databases?",
    "Explain the concept of DevOps.",
    "What is containerization and how does Docker work?",
    "How does a compiler optimize code during the compilation process?",
    "What is the purpose of a load balancer in network architecture?",
    "What are microservices and how do they differ from monolithic applications?",
    "Explain the concept of continuous integration and continuous deployment (CI/CD).",
    "How does DNS work in networking?",
    "What is an IP address and how is it structured?",
    "Explain the role of a firewall in network security.",
    "What is the purpose of a proxy server?",
    "How does a router differ from a switch in networking?",
    "What is a subnet and why is it used?",
    "Explain the concept of cloud computing.",
    "What is a VPN and how does it secure network traffic?",
    "How does a CDN (Content Delivery Network) improve website performance?",
    "What is blockchain technology and how does it work?",
    "What is machine learning and how is it applied in IT?",
    "Explain the concept of big data and its importance.",
    "What is an IDE and why is it used in software development?",
    "What is a framework in programming?",
    "How does multithreading work in programming?",
    "What is the difference between HTTP and HTTPS?",
    "How does SSL/TLS provide security in web communication?",
    "What is a webhook and how is it used?",
    "Explain the concept of load balancing in cloud computing.",
    "What is an ORM (Object-Relational Mapping) and why is it used?",
    "What is the difference between a full-stack developer and a frontend developer?"
]

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
    "Karma", "Keen", "Kite", "Knight", "Lagoon", "Laser", "Legend", "Lime", "Lunar"
]

words3 = [
    "Magnet", "Majestic", "Mellow", "Mint", "Mirth", "Mist", "Mystic", "Nebula", "Nectar", "Nifty",
    "Ocean", "Opal", "Orbit", "Oracle", "Oasis", "Olive", "Omen", "Optic", "Oyster", "Ozone",
    "Pace", "Paddle", "Paradise", "Passion", "Peach", "Peak", "Petal", "Pilot", "Pixel", "Placid",
    "Quaint", "Quartz", "Queen", "Quest", "Quick", "Quill", "Quiver", "Quota", "Quote", "Quartz",
    "Radiant", "Rapid", "Realm", "Rebel", "Reflect", "Ripple", "River", "Roam", "Ruby",
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

def smooth_scroll_to_position(start_position, end_position, duration, steps=None):
    # Calculate step size and number of steps
    if steps is None:
        steps = abs(end_position - start_position)  # Total number of steps for pixel-perfect scrolling
    step_size = (end_position - start_position) / steps
    
    for i in range(steps):
        current_position = start_position + step_size * i
        driver.execute_script(f"window.scrollTo(0, {int(current_position)});")
        time.sleep(duration / steps)

def scroll_randomly_and_back():
    start_position = 0  # Always start from the top
    end_position = random.randint(500, 1000)  # Random end position
    
    # Calculate a reasonable duration for scrolling based on the distance
    scroll_duration = random.uniform(2, 4)  # Adjust the scrolling duration
    
    # Scroll down smoothly without skipping any pixels
    smooth_scroll_to_position(start_position, end_position, scroll_duration)

    # Scroll back up smoothly
    time.sleep(random.uniform(2, 4))  # Optional short pause before scrolling back
    smooth_scroll_to_position(end_position, start_position, scroll_duration)

# Go to the Bing search page initially
driver.get("https://www.bing.com/")

# Loop through the list of words
for _ in range(150):  # Repeat the search process 35 times
    # Randomly select a word from the list
    selected_list = random.choice(word_lists)
    word = random.choice(selected_list)

    # Print the list being used for searching
    print(f"Searching from list {word_lists.index(selected_list) + 1}")

    # Find the search box and enter the word
    search_box = driver.find_element(By.NAME, "q")
    search_box.clear()  # Clear the search box before entering the new word
    search_box.send_keys(word)
    search_box.submit()

    # Perform the scrolling smoothly
    scroll_randomly_and_back()

    # Adjust the wait time based on scroll duration to ensure smooth experience
    time.sleep(2)  # Short delay to simulate time for reviewing results

# Close the browser
driver.quit()