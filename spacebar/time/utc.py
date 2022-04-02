from datetime import datetime, timezone

class UTC:
    
    STRING_FORMAT = "%b %d %Y %H:%M:%S.%f"  # Mmm DD YYYY hh:mm:ss.ssssss
    
    def __init__(self, epoch_string:str) -> None:
        """Class to represent calendar UTC epochs.

        Args:
            epoch_string:   string representing calendar date

        Attributes:
            timestamp:      posix time of calendar date

        Returns:
            None

        """
        local_datetime = datetime.strptime(epoch_string, self.STRING_FORMAT)
        utc_datetime = local_datetime.replace(tzinfo=timezone.utc)
        self.timestamp = utc_datetime.timestamp()

    def plus_seconds(self, seconds_to_add:float) -> "UTC":
        """get new UTC of self plus variable seconds
        
        Args:
            seconds_to_add:     the number of seconds to be added to self
            
        Returns:
            new UTC representing self plus seconds_to_add

        """
        utc_dt = datetime.utcfromtimestamp(self.timestamp + seconds_to_add)
        utc_string = utc_dt.strftime(self.STRING_FORMAT)
        return UTC(utc_string)

    def to_string(self) -> str:
        """get the calendar format of the UTC object
        
        Args:
            None
            
        Returns:
            string in Mmm DD YYYY hh:mm:ss.ssssss format
            
        """
        utc_datetime = datetime.utcfromtimestamp(self.timestamp)
        return utc_datetime.strftime(self.STRING_FORMAT)