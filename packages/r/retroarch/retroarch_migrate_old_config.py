#!/usr/bin/python3

import glob

config_files = glob.glob('/home/*/.config/retroarch/retroarch.cfg')

for config_file in config_files:
    fin = open(config_file, 'rt')
    data = fin.read()
    fin.close()

    # revert patched config with upstream config
    data = data.replace('assets_directory = "/usr/share/libretro/assets"', 'assets_directory = "~/.config/retroarch/assets"')
    data = data.replace('audio_filter_dir = "/usr/lib64/libretro/filters/audio"', 'audio_filter_dir = "~/.config/retroarch/filters/audio"')
    data = data.replace('cheat_database_path = "/usr/share/libretro/database/cht"', 'cheat_database_path = "~/.config/retroarch/cheats"')
    data = data.replace('content_database_path = "/usr/share/libretro/database/rdb"', 'content_database_path = "~/.config/retroarch/database/rdb"')
    data = data.replace('cursor_directory = "/usr/share/libretro/database/cursors"', 'cursor_directory = "~/.config/retroarch/database/cursors"')
    data = data.replace('joypad_autoconfig_dir = "/usr/share/libretro/autoconfig"', 'joypad_autoconfig_dir = "~/.config/retroarch/autoconfig"')
    data = data.replace('libretro_directory = "/usr/lib64/libretro"', 'libretro_directory = "~/.config/retroarch/cores"')
    data = data.replace('libretro_info_path = "/usr/share/libretro/info"', 'libretro_info_path = "~/.config/retroarch/cores"')
    data = data.replace('menu_show_core_updater = "false"', 'menu_show_core_updater = "true"')
    data = data.replace('video_filter_dir = "/usr/lib64/libretro/filters/video"', 'video_filter_dir = "~/.config/retroarch/filters/video"')
    data = data.replace('video_shader_dir = "/usr/share/libretro/shaders"', 'video_shader_dir = "~/.config/retroarch/shaders"')
    
    fout = open(config_file, 'wt')
    fout.write(data)
    fout.close()
