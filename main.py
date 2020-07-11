# evenements

def on_bluetooth_connected():
    basic.show_icon(IconNames.YES)
    basic.pause(100)
    basic.clear_screen()
bluetooth.on_bluetooth_connected(on_bluetooth_connected)

def on_bluetooth_disconnected():
    basic.show_icon(IconNames.NO)
bluetooth.on_bluetooth_disconnected(on_bluetooth_disconnected)

def on_button_pressed_a():
    bluetooth.uart_write_string("BtnA\n")
    serial.write_string("" + ("BtnA\r\n"))
input.on_button_pressed(Button.A, on_button_pressed_a)

def on_button_pressed_b():
    bluetooth.uart_write_string("BtnB\n")
    serial.write_string("" + ("BtnB\r\n"))
input.on_button_pressed(Button.B, on_button_pressed_b)

def on_uart_data_received():
    global s
    s = bluetooth.uart_read_until(serial.delimiters(Delimiters.NEW_LINE))
    serial.write_string("" + s + serial.NEW_LINE)
    basic.show_icon(IconNames.HEART)
    basic.pause(30)
    basic.clear_screen()
bluetooth.on_uart_data_received(serial.delimiters(Delimiters.NEW_LINE),
    on_uart_data_received)

s = ""
input.set_accelerometer_range(AcceleratorRange.EIGHT_G)
serial.redirect_to_usb()
serial.set_baud_rate(BaudRate.BAUD_RATE115200)
bluetooth.start_uart_service()
basic.show_icon(IconNames.NO)