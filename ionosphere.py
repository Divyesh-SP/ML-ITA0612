# ionosphere.py

def estimate_virtual_height(frequency):

    if frequency < 5:
        return 350

    elif frequency < 10:
        return 320

    elif frequency < 15:
        return 300

    elif frequency < 20:
        return 280

    elif frequency < 25:
        return 260

    else:
        return 240