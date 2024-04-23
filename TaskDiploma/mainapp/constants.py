
class CardStatus:
    NEW = "New"
    IN_PROGRESS = "In progress"
    IN_QA = "In QA"
    READY = "Ready"
    DONE = "Done"
    STATUS_LIST = ['New', 'In progress', 'In QA', "Ready", "Done"]
    STATUS_CHOICES = (
        (NEW, "New"),
        (IN_PROGRESS, "In progress"),
        (IN_QA, "In QA"),
        (READY, "Ready"),
        (DONE, "Done"),
    )
    back = {'inprogress': 'New', 'inqa': 'In progress', 'ready': 'In QA', 'done': 'Ready'}
    next = {'new': 'In progress', 'inprogress': 'In QA', 'inqa': 'Ready', 'ready': 'Done'}

    USER_STATUS_LIST = ['New', 'In progress', 'In QA', "Ready"]
    ADMIN_STATUS_LIST = ["Ready", "Done"]

    LOWER_STATUS_DICT = {'new': 'New', 'inprogress': 'In progress', 'inqa': 'In QA', 'ready': 'Ready', 'done': 'Done'}




