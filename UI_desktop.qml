import QtQuick
import QtQuick.Controls
import QtQuick.Layouts
import my.slots.name 1.0

Window {
    width: Screen.desktopAvailableWidth
    height: Screen.desktopAvailableHeight
    visible: true
    title: "Hello World"

    Bridge {
        id: slots
    }


    RowLayout{
        anchors.fill: parent
        id: bottom_bar
        Layout.alignment: Qt.AlignBottom
        Button{
            id: play_button
            Layout.alignment: Qt.AlignHCenter
            text:  "play/pause"
            onClicked: slots.toggle_play_pause()
        }
    }
}
