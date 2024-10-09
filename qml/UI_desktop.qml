import QtQuick
import QtQuick.Controls
import QtQuick.Layouts
import my.slots.name 1.0

Window {
    width: Screen.desktopAvailableWidth
    height: Screen.desktopAvailableHeight
    visible: true
    title: "Hello World"

    Media_Controls {
        id: media_controller
    }

    RowLayout{
        anchors.fill: parent
        id: media_control_bar
        Layout.alignment: Qt.AlignBottom

        Button{
            id: previous_button
            Layout.alignment: Qt.AlignHCenter
            text:  "previous"
            onClicked: media_controller.previous()
        }

        Button{
            id: play_button
            Layout.alignment: Qt.AlignHCenter
            text:  "play/pause"
            onClicked: media_controller.toggle_play_pause()
        }

        Button{
            id: skip_button
            Layout.alignment: Qt.AlignHCenter
            text:  "next"
            onClicked: media_controller.skip()
        }
    }
}
