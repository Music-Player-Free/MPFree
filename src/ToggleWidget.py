from PySide6.QtWidgets import QStackedWidget


class ToggleWidget(QStackedWidget):
    '''
    Child of QStackedWidget. Insert two widgets and use .toggle() to swap between them. \n
    widget1 will always be first: idx = 0.
    '''


    '''
    Implementation of stacked widget.
    StackedWidget contains widgets with indices (0,1,2...n)
    At the minute, for testing purposes, this widget has only two 
    widgets, params of init widget1, widget2.
    Since there is only 2 we can make this a toggle by using modulo 2 (guarantees idx is between 
    0 and 1). We could have used ~ (not) but I (Angus) am more familiar with mod (%).
    '''
    def __init__(self, widget1, widget2):
        # Init baseclass (QStackedWidget)
        # Use QStackedWidget.addWidget to insert widgets to toggle
        super().__init__()
        self.addWidget(widget1)
        self.addWidget(widget2)

    def toggle(self):
        '''
        Toggle between two widgets.
        '''

        # Counting 1,2,3,4 and taking the remainder mod 2 (% 2),
        # we get   1,0,1,0.
        self.setCurrentIndex((self.currentIndex()+1) % 2)
