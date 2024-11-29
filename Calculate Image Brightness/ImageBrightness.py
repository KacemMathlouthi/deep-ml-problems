def calculate_brightness(img):
	# checking if the list is empty
    if not img or not img[0]:
        return -1
    
    n = len(img)
    m = len(img[0])

    # checking that all rows have the same length
    for row in img:
        if len(row) != m:
            return -1
        
    brightness = 0

    for i in range(n):
        for j in range(m):
            #checking that all pixels are valid
            if img[i][j] > 255 or img[i][j] < 0:
                return -1
            brightness += img[i][j]
    brightness = brightness/(m*n)
    return brightness
