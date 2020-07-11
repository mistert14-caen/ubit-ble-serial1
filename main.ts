// evenements
bluetooth.onBluetoothConnected(function () {
    basic.showIcon(IconNames.Yes)
    basic.pause(100)
    basic.clearScreen()
})
bluetooth.onBluetoothDisconnected(function () {
    basic.showIcon(IconNames.No)
})
input.onButtonPressed(Button.A, function () {
    bluetooth.uartWriteString("BtnA\n")
    serial.writeString("" + ("BtnA\r\n"))
})
input.onButtonPressed(Button.B, function () {
    bluetooth.uartWriteString("BtnB\n")
    serial.writeString("" + ("BtnB\r\n"))
})
bluetooth.onUartDataReceived(serial.delimiters(Delimiters.NewLine), function () {
    s = bluetooth.uartReadUntil(serial.delimiters(Delimiters.NewLine))
    serial.writeString("" + s + serial.NEW_LINE)
    basic.showIcon(IconNames.Heart)
    basic.pause(30)
    basic.clearScreen()
})
let s = ""
servos.P2.setAngle(0)
input.setAccelerometerRange(AcceleratorRange.EightG)
serial.redirectToUSB()
serial.setBaudRate(BaudRate.BaudRate115200)
bluetooth.startUartService()
basic.showIcon(IconNames.No)
