import csv
import turtle
import os
import glob


def graphical_setup():
    """Creates the Turtle and the Screen with the map background
       and coordinate system set to match latitude and longitude.

       :return: a tuple containing the Turtle and the Screen

    """

    import tkinter
    turtle.setup(965, 600)  # set size of window to size of map

    wn = turtle.Screen()

    # kludge to get the map shown as a background image,
    # since wn.bgpic does not allow you to position the image
    canvas = wn.getcanvas()
    turtle.setworldcoordinates(-90, 0, -17.66, 45)  # set the coordinate system to match lat/long

    map_bg_img = tkinter.PhotoImage(file="images/atlantic-basin.png")

    # additional kludge for positioning the background image
    # when setworldcoordinates is used
    canvas.create_image(-1175, -580, anchor=tkinter.NW, image=map_bg_img)

    t = turtle.Turtle()
    wn.register_shape("images/hurricane.gif")
    t.shape("images/hurricane.gif")

    return t, wn, map_bg_img


def track_storm(hurricane_data):
    """Animates the path of the storm.
    """
    (t, wn, map_bg_img) = graphical_setup()

    t.speed = (8)
    data = hurricane_data
    hurricane_data = open(f'data//{track_storm}', 'r').readlines()

    hurricane_data[0]= hurricane_data[1]

    t.penup()
    t.goto(float(hurricane_data[0].split(',')[3]), float(hurricane_data[0].split(',')[2]))
    t.pendown()

    
    #Category winds speeds were estimated from: https://www.nola.com/news/hurricane/category-4-hurricane-winds-can-rip-off-roofs-this-video-explains-how/article_2491bc82-081f-11ec-88fb-7b39be0fddea.html . Accessed on 12/2/2022.
    for h in hurricane_data:
        h = h.split(',')
        t.goto(float(h[3]), float(h[2]))
        if (int(h[4]) >= 157):
            t.color('Red')
            t.write('5')
            t.width(15)
        elif (int(h[4]) >= 130):
            t.color('Orange')
            t.write('4')
            t.width(11)
        elif (int(h[4]) >= 110):
            t.color('Yellow')
            t.write('3')
            t.width(7)
        elif (int(h[3]) >= 96):
            t.color('Green')
            t.write('2')
            t.width(3)
        elif (int(h[4]) >= 73):
            t.color('Blue')
            t.write('1')
            t.width(2)
        else:
            t.color('White')
            t.width(1)

    return t, wn, map_bg_img


def main():

    (t, wn, map_bg_img) = graphical_setup()
    hurricane_input=('data\\')+input(f'Enter Storm Name:')+('.csv')
    hurricane_data = glob.glob('data/*')
    try:
        data = open(hurricane_input, 'r'). readlines()
        data.pop(0)
        for n in data:
            h = n.split(',')
            h_lat = float(h[2])
            h_lon = float(h[3])
            winds = int(h[4])
            t.pendown()
            t.goto(h_lon, h_lat)
            if (winds >= 157):
                t.color('Red')
                t.write('5')
                t.width(15)
            elif (130 <= winds < 157):
                t.color('Orange')
                t.write('4')
                t.width(11)
            elif (110 <= winds < 130):
                t.color('Yellow')
                t.write('3')
                t.width(7)
            elif (96 <= winds < 110):
                t.color('Green')
                t.write('2')
                t.width(3)
            elif (73 <= winds < 96):
                t.color('Blue')
                t.write('1')
                t.width(2)
            else:
                t.color('White')
                t.width(1)
#See prior comment for details on the source for category wind speeds
    except:
        print('Invalid Storm Name.')
        exit(0)
    wn.exitonclick()
  

if __name__ == "__main__":
    main()
