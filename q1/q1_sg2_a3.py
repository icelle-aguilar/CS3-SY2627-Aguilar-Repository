birthyear = int(input("Enter your birth year: "))
#Allows the user to input their birth year

if birthyear >= 1900:
#This is to ensure that if any year before 1900 is inputted, the input will be deemed invalid
  zodiac = ["Rat (鼠 / Shǔ)",
          "Ox (牛 / Niú)",
          "Tiger (虎 / Hǔ)",
          "Rabbit (兔 / Tù)",
          "Dragon (龙 / Lóng)",
          "Snake (蛇 / Shé)",
          "Horse (马 / Mǎ)",
          "Goat (羊 / Yáng)",
          "Monkey (猴 / Hóu)",
          "Rooster (鸡 / Jī)",
          "Dog (狗 / Gǒu)",
          "Pig (猪 / Zhū)"]
  #List of the Chinese Zodiacs
  
  zodiacnum = (birthyear - 1900) % 12
  '''1900 is subtracted from the birth year because it is our base cutoff.
  After getting the difference, it is then divided by 12 and the modulo
  operator is used to get the remainder which will determine the index that
  the Zodiac is found in.'''
  
  print(f"Your Chinese Zodiac Sign is : {zodiac[zodiacnum]}")
  #zodiac -> list, zodiacnum -> item index

else:
  print(f"/n Invalid Year, it should not be earlier than 1900")
