import os
import dearpygui.dearpygui as dpg
from function import *

dpg.create_context()

def display_file_callback(sender, data):
    fname = dpg.get_value("File_Path")
    print_limit = dpg.get_value("print_limit")
    skip_rows = dpg.get_value("skip_rows")
    encoding = dpg.get_value("encoding")
    if fname:
        dpg.set_value("File_Contents", print_lines(fname, print_limit, skip_rows, encoding))

with dpg.file_dialog(
    directory_selector=False, show=False,
    callback=lambda sender, data: dpg.set_value("File_Path", data["file_path_name"]),
    file_count=1, tag="file_dialog_tag", width=600 ,height=400
    ):
    dpg.add_file_extension("", color=(255, 150, 150, 255))
    dpg.add_file_extension(".txt", color=(255, 255, 0, 255))
    dpg.add_file_extension(".csv", color=(255, 0, 255, 255))
    dpg.add_file_extension(".*")

with dpg.window(label="Tutorial") as main_window:
    dpg.add_text("Enter the file path, or select the file using Browse:")
    dpg.add_input_int(label="Number of rows to skip", tag='skip_rows', default_value=0, width = 200)
    dpg.add_input_int(label="Number of rows to display", tag='print_limit', default_value=10, width = 200)
    dpg.add_input_text(label="File encoding", tag='encoding', default_value="utf-8", width = 200)
    dpg.add_input_text(
        label='File Path', tag='File_Path',
        callback=lambda sender, data: dpg.set_value("File_Path", data["file_path_name"]),
        default_value=r'path\to\file.txt', width=400)
    dpg.add_button(label="Browse", callback=lambda: dpg.show_item("file_dialog_tag"))
    dpg.add_button(label="Display File", callback=display_file_callback)
    dpg.add_input_text(
        label='file contents', tag="File_Contents", multiline=True,
        readonly=True, height=350)

dpg.set_primary_window(main_window, True)
dpg.create_viewport(title='csvHelper', width=1000, height=600)
dpg.setup_dearpygui()
dpg.show_viewport()
dpg.start_dearpygui()
dpg.destroy_context()