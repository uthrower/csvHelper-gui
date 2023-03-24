import ctypes
import os
import dearpygui.dearpygui as dpg
from function import *

ctypes.windll.shcore.SetProcessDpiAwareness(2)

dpg.create_context()


def display_file_callback(sender, data):
    fname = dpg.get_value("File_Path")
    print_limit = dpg.get_value("print_limit")
    skip_rows = dpg.get_value("skip_rows")
    encoding = dpg.get_value("encoding")
    if fname:
        dpg.set_value("File_Contents", print_lines(fname, print_limit, skip_rows, encoding))


def convert_encoding_callback(sender, data):
    fname = dpg.get_value("File_Path")
    frm_encoding = dpg.get_value("frm_encoding")
    to_encoding = dpg.get_value("to_encoding")
    if fname:
        convert_encoding(fname, frm_encoding, to_encoding)
        print('success~')


with dpg.font_registry():
    default_font = dpg.add_font(r"Desktop\gui\fonts\JetBrainsMonoNL-SemiBold.ttf", 20)
    dpg.add_font(r"Desktop\gui\fonts\JetBrainsMono-Bold.ttf", 20)
    dpg.add_font(r"Desktop\gui\fonts\JetBrainsMonoNL-Regular.ttf", 20)
    dpg.add_font(r"Desktop\gui\fonts\JetBrainsMonoNL-Thin.ttf", 20)
    dpg.add_font(r"Desktop\gui\fonts\JetBrainsMono-Regular.ttf", 20)
    dpg.add_font(r"Desktop\gui\fonts\ProggySquare.ttf", 20)
    # with dpg.font(r"Desktop\gui\fonts\JetBrainsMono-Bold.ttf", 20) as default_font:
    #     dpg.add_font_range_hint(dpg.mvFontRangeHint_Japanese)


with dpg.file_dialog(
    directory_selector=False, show=False,
    callback=lambda sender, data: dpg.set_value("File_Path", data["file_path_name"]),
    file_count=1, tag="file_dialog_tag", width=600 ,height=400
    ):
    dpg.add_file_extension("", color=(255, 150, 150, 255))
    dpg.add_file_extension(".csv", color=(255, 0, 255, 255))
    dpg.add_file_extension(".txt", color=(255, 255, 0, 255))
    dpg.add_file_extension(".*")


with dpg.window(label="Tutorial") as main_window:
    dpg.add_text("Enter the file path, or select the file using Browse:")
    dpg.add_input_int(label="Number of rows to skip", tag='skip_rows', default_value=0, width = 200)
    dpg.add_input_int(label="Number of rows to display", tag='print_limit', default_value=10, width = 200)
    dpg.add_input_text(label="File encoding", tag='encoding', default_value="utf-8", width = 200)
    dpg.add_input_text(
        label='File Path', tag='File_Path',
        callback=lambda sender, data: dpg.set_value("File_Path", data["file_path_name"]),
        default_value=r'path\to\file.txt', width=800)
    dpg.add_button(label="Browse", callback=lambda: dpg.show_item("file_dialog_tag"))
    dpg.add_button(label="Display File", callback=display_file_callback)
    dpg.add_input_text(
        label='', tag="File_Contents", multiline=True,
        readonly=True, height=300, width=800)
    dpg.add_button(label="I want to change the encoding of this file!", callback=lambda: dpg.show_item("change_encode"))

    dpg.bind_font(default_font)


with dpg.window(tag="change_encode", show=False, pos=[200,100], width=600, height=400):
    dpg.add_input_text(label="From encoding", tag='frm_encoding', default_value='utf-8', width = 200)
    dpg.add_input_text(label="To encoding", tag='to_encoding', default_value='utf-16', width = 200)
    dpg.add_button(label="Convert!", callback=convert_encoding_callback)

dpg.set_primary_window(main_window, True)
dpg.create_viewport(title='csvHelper', width=1000, height=700, x_pos=1000, y_pos=500)
dpg.setup_dearpygui()
dpg.show_viewport()
# dpg.start_dearpygui()
while dpg.is_dearpygui_running():
    dpg.get_value("encoding")
    dpg.render_dearpygui_frame()
dpg.destroy_context()