from datetime import datetime, timezone

class UTC:
    """
    Class to represent calendar UTC epochs.

    String format is Mmm DD YYYY hh:mm:ss.ssssss
    """
    STRING_FORMAT = "%b %d %Y %H:%M:%S.%f"  
    
    def __init__(self, epoch_string):
        local_datetime = datetime.strptime(epoch_string, self.STRING_FORMAT)
        utc_datetime = local_datetime.replace(tzinfo=timezone.utc)
        self.timestamp = utc_datetime.timestamp()

    def plus_seconds(self, seconds_to_add) -> "UTC":
        utc_datetime = datetime.utcfromtimestamp(self.timestamp + seconds_to_add)
        utc_string = utc_datetime.strftime(self.STRING_FORMAT)
        return UTC(utc_string)

    def to_string(self):
        utc_datetime = datetime.utcfromtimestamp(self.timestamp)
        return utc_datetime.strftime(self.STRING_FORMAT)