class Television:
    """
    Class to represent the Television objects.
    """
    MIN_CHANNEL = 0     # Minimum TV channel
    MAX_CHANNEL = 3     # Maximum TV channel

    MIN_VOLUME = 0      # Minimum TV volume
    MAX_VOLUME = 2      # Maximum TV volume

    def __init__(self) -> None:
        """
        Method to set the default state of the tv.
        :param a: starting television channel
        :param b: starting television volume
        :param c: starting television status
        """
        self.___channel: int = Television.MIN_CHANNEL
        self.___volume: int = Television.MIN_VOLUME
        self.___status: bool = False
    
    def power(self) -> None:
        """
        :param a: Status becomes true when this function gets called
        :return: Television status
        """
        self.___status: bool = not self.___status


        
    def channel_up(self) -> None:
        """
        If the status of the television is on(true) and the current channel is less than
        the max channel, then the channel goes up by one.
        If the current channel equals the max channel of 3, then the current channel becomes min
        channel of 0

        """
        if self.___status == True:
            if self.___channel < Television.MAX_CHANNEL:
                self.___channel += 1
            elif self.___channel == Television.MAX_CHANNEL: 
                self.___channel = Television.MIN_CHANNEL

        
                

    def channel_down(self) -> None:
        """
        If the status of the television is on(true) and the current channel is more than
        the min channel, then the channel goes down by one.
        If the current channel equals the min channel of 0, then the current channel becomes max
        channel of 3

        """
        if self.___status == True:
            if self.___channel > Television.MIN_CHANNEL: 
                self.___channel -= 1
            elif self.___channel == Television.MIN_CHANNEL:
                self.___channel = Television.MAX_CHANNEL

        

    def volume_up(self) -> None:
        """
        If the status of the television is on(true) and the current volume is less than
        the max volume, then the volume goes up by one.

        """
        if self.___status == True:
            if self.___volume < Television.MAX_VOLUME:
                self.___volume += 1

       
            
    def volume_down(self) -> None:
        """
        If the status of the television is on(true) and the current volume is more than
        the min volume, then the volume goes down by one.

        """
        if self.___status == True:
            if self.___volume > Television.MIN_VOLUME:
                self.___volume -= 1

                
       
    
    def __str__(self) -> str:
        """

        :return: A string that shows the tv status, current channel, and current volume
        """
        return f'TV status: Is on = {self.___status}, Channel = {self.___channel}, Volume = {self.___volume}'