#!/Arun/Lavnaya/marriage

# This is just a code. Dot try running it.
#You cannot import god and blessings :-)


"""
.. module:: invitation.shy
    :synopsis: We fell in love on each other by pushed by our parents
    :aim:: Get married
    :purpose:: Invite all of our friends

.. module authors:: Arun.R & Lavnaya.G
.. target date:: 02.July.2019

"""

from god import blessings
from friends import wishes, greetings, gifts, kindals, joyful, help, etc
from family.parents import Rajendiran_Jayalakshmi, Ganesan_Manimegalai as appa_amma
from family.brothers import Dinesh_Saranya as Software_Engineer
from family.sister import Gopi_Sharmila
from family.relations import *

class Love(love):

    def __init__(self, partner):
        self.__romance__(partner)
        self.__duet__(partner)
        self.__fight__(partner)

    def __romance__(self, partner):
        # Do romance for infinity times without any break
        while True:        
            # Make self to love partner
            self = do_love(partner)
            # Exchange our loves 
            self, partner = partner, self

    def __duet__(self, partner):
        self.songs_60s_to_90s(partner)

    def __fight__(self, partner):
        pass

class Marriage(Love, friends, parents, siblings, relativies):

    def __init__(self):
        self.time = " 6.00 am to 7.00 am "
        self.date = " 02-07-2018 "
        self.place = " Narasima Swamy temple , Sholinghur "
        self.place += " Near by Arakonnam railway station "
        Love.do_marriage(arranged_by = parents, with_supports = siblings,
                          manage_by = relativies, with_love_of = friends)


class Reception(Love, friends):

    def __init__(self):        
        place = self.place
        self.party(You)

    def party(self, friends):
        # Celebrate happiness with you
        you = friends.best

        print " Reception Date ", " 01-07-2019 "
        print " Party Time ", " 6.30 pm to 9.30 pm "

        if you in Marriage:
            treat_to(you)
            photo_clips_with_us()

        elif you in Reception:
            party_to(you)
            photo_clips_with_us()

        else:
            fight_with(you)


def welcome(you):

    print " With Blessings of ", Love.love.angel

    print " We 'Lavanya Arun' invite ", you, """ to our marriage and
                        reception with immense pleasure.
                      Your presence is most important to us.
            We are waiting for the moment to join with our life partner
               in front of our parents, brothers, relativies and most
                        importantly friends (you)... """

    print " We thank ", love.angel, " to tighed us together in this brith too "

    print " Once again welcome you to ", Marriage(2 July 2019)
    print " and ", Reception(you), " too..."

    if you:
        print ":) :-) :P :D :} :-] :D :P :-) :) " * 10000000000000000000000000
    else:
        print ":( :-( :( :-( :=( :-{ :-[ :{ :(  " * 10000000000000000000000000


if __name__ == 'main':
    
    # Invitation begins here
    import love
    from mylife.partner import shyness, smile, love, happy, friendship, *
    from myself import shyness, smile
    from future import children
    
    welcome(invitation.cover.your_name)
