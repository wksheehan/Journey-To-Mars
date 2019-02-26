from visual import *

#POSITIONS
sun = sphere(pos=vector(0,0,0), radius=30e9, color=color.yellow)
earth = sphere(pos=vector(0,150e9,0), radius=7e9, material=materials.BlueMarble)
mars = sphere(pos=vector(0,2.2794e11,0), radius=3.39e9, color=color.red)
craft = sphere(pos=vector(0,157e9,0), radius=2e9, color=color.white)

#CONSTANTS
sun.m = 1.989e30
earth.m = 5.972e24
mars.m = 6.39e23
craft.m = 5000
G = 6.67e-11

#VALUES
earth.v = vector(3e4,0,0)
mars.v = vector(24130.833,0,0)
craft.v = earth.v
earth.p = earth.m * earth.v
mars.p = mars.m * mars.v
craft.p = craft.m * craft.v

t = 0
deltat = 10000
earth.trail = curve(color=color.blue)
mars.trail = curve(color=color.red)
craft.trail1 = curve(color=color.cyan)
craft.trail2 = curve(color=color.magenta)

while True:
    rate(400)
    earth_sun = earth.pos - sun.pos
    mars_sun = mars.pos - sun.pos
    craft_earth = craft.pos - earth.pos
    craft_sun = craft.pos - sun.pos
    rhat_earth_sun = norm(earth_sun)
    rhat_mars_sun = norm(mars_sun)
    rhat_craft_earth = norm(craft_earth)
    rhat_craft_sun = norm(craft_sun)
    earth_sun_mag = earth_sun.mag
    mars_sun_mag = mars_sun.mag
    craft_earth_mag = craft_earth.mag
    craft_sun_mag = craft_sun.mag
    Fnet_earth = (-rhat_earth_sun*G*earth.m*sun.m)/earth_sun_mag**2
    Fnet_mars = (-rhat_mars_sun*G*mars.m*sun.m)/mars_sun_mag**2
    Fnet_craft = ((-rhat_craft_earth*G*craft.m*earth.m)/craft_earth_mag**2)+((-rhat_craft_sun*G*craft.m*sun.m)/craft_sun_mag**2)
    earth.p = earth.p + Fnet_earth*deltat
    mars.p = mars.p + Fnet_mars*deltat
    craft.p = craft.p + Fnet_craft*deltat
    earth.pos = earth.pos + (earth.p/earth.m)*deltat
    mars.pos = mars.pos + (mars.p/mars.m)*deltat
    craft.pos = craft.pos + (earth.p/earth.m)*deltat
    t = t + deltat
    earth.trail.append(pos=earth.pos)
    mars.trail.append(pos=mars.pos)
    while t > 30000000:
        #REPEAT EARLIER WHILE LOOP
        rate(400)
        earth_sun = earth.pos - sun.pos
        mars_sun = mars.pos - sun.pos
        craft_earth = craft.pos - earth.pos
        craft_sun = craft.pos - sun.pos
        rhat_earth_sun = norm(earth_sun)
        rhat_mars_sun = norm(mars_sun)
        rhat_craft_earth = norm(craft_earth)
        rhat_craft_sun = norm(craft_sun)
        earth_sun_mag = earth_sun.mag
        mars_sun_mag = mars_sun.mag
        craft_earth_mag = craft_earth.mag
        craft_sun_mag = craft_sun.mag
        Fnet_earth = (-rhat_earth_sun*G*earth.m*sun.m)/earth_sun_mag**2
        Fnet_mars = (-rhat_mars_sun*G*mars.m*sun.m)/mars_sun_mag**2
        earth.p = earth.p + Fnet_earth*deltat
        mars.p = mars.p + Fnet_mars*deltat
        earth.pos = earth.pos + (earth.p/earth.m)*deltat
        mars.pos = mars.pos + (mars.p/mars.m)*deltat
        t = t + deltat
        earth.trail.append(pos=earth.pos)
        mars.trail.append(pos=mars.pos)
        #CRAFT LAUNCH
        craft_mars = craft.pos-mars.pos
        rhat_craft_mars = norm(craft_mars)
        craft_mars_mag = craft_mars.mag
        Fnet_craft = vector(-50,15,0)+((-rhat_craft_earth*G*craft.m*earth.m)/craft_earth_mag**2)+((-rhat_craft_sun*G*craft.m*sun.m)/craft_sun_mag**2)+ ((-rhat_craft_mars*G*craft.m*mars.m)/craft_mars_mag**2)
        craft.p = craft.p + Fnet_craft*deltat
        craft.pos = craft.pos + (craft.p/craft.m)*deltat
        craft.trail2.append(pos=craft.pos)
        t = t + deltat
        craft_mars = craft.pos - mars.pos
        craft_mars_mag = craft_mars.mag
        while t > 39500000:
            #REPEAT EARLIER WHILE LOOP
            rate(400)
            earth_sun = earth.pos - sun.pos
            mars_sun = mars.pos - sun.pos
            craft_earth = craft.pos - earth.pos
            craft_sun = craft.pos - sun.pos
            rhat_earth_sun = norm(earth_sun)
            rhat_mars_sun = norm(mars_sun)
            rhat_craft_earth = norm(craft_earth)
            rhat_craft_sun = norm(craft_sun)
            earth_sun_mag = earth_sun.mag
            mars_sun_mag = mars_sun.mag
            craft_earth_mag = craft_earth.mag
            craft_sun_mag = craft_sun.mag
            Fnet_earth = (-rhat_earth_sun*G*earth.m*sun.m)/earth_sun_mag**2
            Fnet_mars = (-rhat_mars_sun*G*mars.m*sun.m)/mars_sun_mag**2
            earth.p = earth.p + Fnet_earth*deltat
            mars.p = mars.p + Fnet_mars*deltat
            earth.pos = earth.pos + (earth.p/earth.m)*deltat
            mars.pos = mars.pos + (mars.p/mars.m)*deltat
            t = t + deltat
            earth.trail.append(pos=earth.pos)
            mars.trail.append(pos=mars.pos)
            #CRAFT LAUNCH
            craft_mars = craft.pos-mars.pos
            rhat_craft_mars = norm(craft_mars)
            craft_mars_mag = craft_mars.mag
            Fnet_craft = ((-rhat_craft_earth*G*craft.m*earth.m)/craft_earth_mag**2)+((-rhat_craft_sun*G*craft.m*sun.m)/craft_sun_mag**2)+ ((-rhat_craft_mars*G*craft.m*mars.m)/craft_mars_mag**2)
            craft.p = craft.p + Fnet_craft*deltat
            craft.pos = craft.pos + (craft.p/craft.m)*deltat
            craft.trail1.append(pos=craft.pos)
            t = t + deltat
            craft_mars = craft.pos - mars.pos
            craft_mars_mag = craft_mars.mag
            while craft_mars_mag < mars.radius:
                rate(400)
                earth_sun = earth.pos - sun.pos
                mars_sun = mars.pos - sun.pos
                craft_earth = craft.pos - earth.pos
                craft_sun = craft.pos - sun.pos
                rhat_earth_sun = norm(earth_sun)
                rhat_mars_sun = norm(mars_sun)
                rhat_craft_earth = norm(craft_earth)
                rhat_craft_sun = norm(craft_sun)
                earth_sun_mag = earth_sun.mag
                mars_sun_mag = mars_sun.mag
                craft_earth_mag = craft_earth.mag
                craft_sun_mag = craft_sun.mag
                Fnet_earth = (-rhat_earth_sun*G*earth.m*sun.m)/earth_sun_mag**2
                Fnet_mars = (-rhat_mars_sun*G*mars.m*sun.m)/mars_sun_mag**2
                earth.p = earth.p + Fnet_earth*deltat
                mars.p = mars.p + Fnet_mars*deltat
                earth.pos = earth.pos + (earth.p/earth.m)*deltat
                mars.pos = mars.pos + (mars.p/mars.m)*deltat
                t = t + deltat
                earth.trail.append(pos=earth.pos)
                mars.trail.append(pos=mars.pos)
                #CHANGE CRAFT MOMENTUM UPDATE TO MARS'
                craft.pos = craft.pos + (mars.p/mars.m)*deltat
                craft.trail1.append(pos = craft.pos)

#CONCLUSION AND THOUGHTS

#What time you launch changes mars' position relative to earth's--does NASA take this into account everytime they send something into space? How do they know where Mars is?
#Given the launch time, how would I predict the vector velocity of the craft needed to land on mars?
#Is the speed at which the craft "lands" on mars reasonable?
#The gravitational interaction between Mars and Earth is small enough to ignore
#Earth and Mars' gravitational interaction is constantly changing because they do not have the same orbit Period
#If I gave the craft enough initial velocity to cancel out earth's gravitational force, would there be a point when earth's velocity would propel the rocket to mars?
#How do I find the earth's velocity at any point and make a velocity perpendicular to that instantaneous velocity? (kick a soccer ball perpendicular to its original motion by applying a force in the opposite parallel direction)
#Is it possible to add a z velocity? Do all the planets orbit on the same plane?
#The craft actually takes around 8 months to land on mars in this scenario
            
            
        
    
    

    
   
    
    
    

    
