from datetime import datetime, timedelta
def getDate(left: int):
    return (datetime.now() - timedelta(days=left)).strftime("%Y-%m-%d")