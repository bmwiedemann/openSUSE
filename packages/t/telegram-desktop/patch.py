#!/usr/bin/env python3

import json
import re
from shutil import copyfile

def remove_trailing_commas(json_like):
    """
    Removes trailing commas from *json_like* and returns the result.  Example::
        >>> remove_trailing_commas('{"foo":"bar","baz":["blah",],}')
        '{"foo":"bar","baz":["blah"]}'
    """
    trailing_object_commas_re = re.compile(
        r'(,)\s*}(?=([^"\\]*(\\.|"([^"\\]*\\.)*[^"\\]*"))*[^"]*$)')
    trailing_array_commas_re = re.compile(
        r'(,)\s*\](?=([^"\\]*(\\.|"([^"\\]*\\.)*[^"\\]*"))*[^"]*$)')
    # Fix objects {} first
    objects_fixed = trailing_object_commas_re.sub("}", json_like)
    # Now fix arrays/lists [] and return the result
    return trailing_array_commas_re.sub("]", objects_fixed)

def find_first_prime(str, ch):
    for i,c in enumerate(str):
        if c == ch:
            return i

def find_last_prime(str, ch):
    for i,c in enumerate(str[::-1]):
        if c == ch:
            return len(str)-1-i

def is_inserted_doublequote(line, i):
    if i >= len(line):
        return False
    if line[i] == "\"":
        if i == 0:
            return True
        elif (not line[i-1] == "\\"):
            return True
        return False
    return False

def transform_back(proper_json):
    gyp_str = ""
    for line in proper_json.splitlines():
        temp = '%s' % line
        # remove double quotes in the middle
        temp = temp.replace("'\": [[ \"'", "': [[ '")
        temp = temp.replace("'\": [ \"'", "': [ '")
        temp = temp.replace("'\": \"'", "': '")
        # remove all other double quotes
        for i,s in enumerate(temp):
            if is_inserted_doublequote(temp, i):
                if i == 0:
                    temp = temp[1:]
                else:
                    temp = temp[:i] + temp[i+1:]
        # replace \" to "
        temp = temp.replace("\\\"", "\"")
        # replace all double backslashes with single backslash
        temp = temp.replace("\\\\", "\\")
        gyp_str += temp + "\n"
    return gyp_str

def read_file_to_proper_json(f):
    json_like = ""
    for line in f: # read it all in
        stripped_line = line.strip()
        if not stripped_line.startswith("#"):
            if stripped_line.find("'") != -1:
                # step 1: replace all " with \"
                stripped_line = stripped_line.replace("\\'", "\\\\'")
                stripped_line = stripped_line.replace("\"", "\\\"")
                first = find_first_prime(stripped_line, "'")
                last = find_last_prime(stripped_line, "'")
                # step 2: insert " before the first ' and after the last '
                first_str = stripped_line[0:first]
                mid_str = stripped_line[first:last+1]
                last_str = stripped_line[last+1:]
                final_str = first_str + "\"" + mid_str + "\"" + last_str
                line = final_str
                # add double quotes for single quotes in the middle
                line = line.replace("': '", "'\": \"'")
                line = line.replace("': [ '", "'\": [ \"'")
                line = line.replace("': [[ '", "'\": [[ \"'")
                json_like += line
            else:
                json_like += line
    proper_json = remove_trailing_commas(json_like)
    return proper_json

def load_json(filename):
    return json.loads(read_file_to_proper_json(open(filename)))

def save_json(jsonobj, filename):
    j = transform_back(jsonobj)
    # backup = filename + ".orig"
    # copyfile(filename, backup)
    f = open(filename, 'w')
    f.write(j)
    return

def process_telegram_linux(jsonobj):
    child = jsonobj["'conditions'"][0][1]["'variables'"]["'pkgconfig_libs'"]
    child.append("'liblzma'")
    child.append("'openal'")
    child.append("'libavformat'")
    child.append("'libavcodec'")
    child.append("'libswresample'")
    child.append("'libswscale'")
    child.append("'libavutil'")
    child.append("'opus'")
    child.append("'libva-x11'")
    child.append("'libva-drm'")
    child.append("'libva'")
    child.append("'libdrm'")
    child.append("'zlib'")
    child.append("'minizip'")
    child.append("'openssl'")

    child = jsonobj["'conditions'"][0][1]["'libraries'"]
    child.remove("'-lcomposeplatforminputcontextplugin'")
    child.remove("'-lfcitxplatforminputcontextplugin'")
    child.remove("'-lhimeplatforminputcontextplugin'")
    child.remove("'-libusplatforminputcontextplugin'")
    child.remove("'-lnimfplatforminputcontextplugin'")

    child = jsonobj["'conditions'"][0][1]["'cflags_cc'"]
    child.append("'<!(pkg-config --cflags <@(pkgconfig_libs))'")
    
    child = jsonobj["'conditions'"][0][1]["'ldflags'"]
    child.remove("'-Wl,-Bstatic'")
    
    return json.dumps(jsonobj)

def process_qt(jsonobj):
    child = jsonobj["'variables'"]["'variables'"]["'variables'"]["'variables'"]["'variables'"]["'conditions'"][0]
    child[2]["'qt_version%'"] = "'<!(qmake-qt5 --version | sed -n 2p | grep -Po \"\d+\.\d+\.\d+\")'"
    child = jsonobj["'variables'"]["'variables'"]["'variables'"]["'variables'"]["'qt_libs'"];
    child.remove("'qtharfbuzzng'")
    child.remove("'qwebp'")
    child.remove("'Qt5PrintSupport'")
    child.remove("'Qt5PlatformSupport'")
    child = jsonobj["'variables'"]["'variables'"]["'variables'"]["'variables'"]["'conditions'"][0][2];
    child["'linux_path_qt%'"] = "'/usr/lib64/qt5'"
    child = jsonobj["'variables'"]["'variables'"]["'variables'"]["'conditions'"][0][1]["'qt_libs'"]; # build_win
    child.remove("'qtpcre'")
    child = jsonobj["'variables'"]["'variables'"]["'variables'"]["'conditions'"][2][1]["'qt_libs'"]; # build_mac not build_macold
    child.remove("'qtpcre'")
    # build_linux
    child = jsonobj["'variables'"]["'variables'"]["'variables'"]["'conditions'"][3][1];
    child["'qt_lib_prefix'"] = "''"
    child["'qt_lib_debug_postfix'"] = "''"
    child["'qt_lib_release_postfix'"] = "''"

    child = jsonobj["'variables'"]["'variables'"]["'variables'"]["'conditions'"][3][1]["'qt_libs'"];
    child.remove("'qxcb'")
    child.remove("'Qt5XcbQpa'")
    child.remove("'qconnmanbearer'")
    child.remove("'qgenericbearer'")
    child.remove("'qnmbearer'")
    child.remove("'qtpcre'")
    child.remove("'Xi'")
    child.remove("'Xext'")
    child.remove("'Xfixes'")
    child.remove("'SM'")
    child.remove("'ICE'")
    child.remove("'fontconfig'")
    child.remove("'expat'")
    child.remove("'freetype'")
    child.remove("'z'")
    child.remove("'xcb-shm'")
    child.remove("'xcb-xfixes'")
    child.remove("'xcb-render'")
    child.remove("'xcb-static'")

    child = jsonobj["'variables'"]
    del child["'linux_path_xkbcommon%'"]
    del child["'linux_lib_ssl%'"]
    del child["'linux_lib_crypto%'"]
    del child["'linux_lib_icu%'"]

    child = jsonobj["'include_dirs'"]
    del child[:]
    child.append("'/usr/include/ffmpeg'")
    child.append("'/usr/include/qt5'")
    child.append("'/usr/include/qt5/QtCore'")
    child.append("'/usr/include/qt5/QtGui'")
    child.append("'/usr/include/qt5/QtDBus'")
    child.append("'/usr/include/qt5/QtGui/<(qt_version)'")
    child.append("'/usr/include/qt5/QtCore/<(qt_version)'")
    child.append("'/usr/include/qt5/QtGui/<(qt_version)/QtGui'")
    child.append("'/usr/include/qt5/QtCore/<(qt_version)/QtCore'")

    child = jsonobj["'conditions'"][0][1]["'libraries'"]
    child.remove("'<(linux_path_xkbcommon)/lib/libxkbcommon.a'")
    child.remove("'<(linux_lib_ssl)'")
    child.remove("'<(linux_lib_crypto)'")
    child.remove("'<!@(python -c \"for s in \\'<(linux_lib_icu)\\'.split(\\' \\'): print(s)\")'")
    child.remove("'-lxcb'")
    child.remove("'-lX11-xcb'")
    child.remove("'-ldbus-1'")
    child.remove("'-lgthread-2.0'")
    child.append("'-ljpeg'")
    child.append("'-lGL'")
    child.append("'-lfreetype'")
    child.append("'-lcrypto'")
    child.append("'-lfontconfig'")
    child.append("'-lXi'")
    child.append("'-lSM'")
    child.append("'-lICE'")
    child.append("'-lproxy'")
    child.append("'-lz'")
    child.append("'<!(pkg-config 2> /dev/null --libs xkbcommon xkbcommon-x11)'")
    child.append("'<!(pkg-config 2> /dev/null --libs libpcre16)'")
    child.append("'<!(pkg-config 2> /dev/null --libs zlib)'")
    child.append("'<!(pkg-config 2> /dev/null --libs libpng16)'")
    child.append("'<!(pkg-config 2> /dev/null --libs libwebp)'")
    child.append("'<!(pkg-config 2> /dev/null --libs harfbuzz)'")
    child.append("'<!(pkg-config 2> /dev/null --libs xcb-shm xcb-xfixes xcb-render xcb-renderutil xcb-sync xcb-randr xcb-xinerama xcb-xkb xcb-icccm xcb-image xcb-shape xcb-keysyms xcb-util)'")
    child = jsonobj["'conditions'"][0][1]["'ldflags'"]
    child.remove("'-static-libstdc++'")
    return json.dumps(jsonobj)

def process_settings_linux(jsonobj):
    child = jsonobj["'conditions'"][0][1]["'variables'"]["'linux_common_flags'"]
    child.append("'-Wno-implicit-fallthrough'")
    child.remove("'-Werror'")
    child = jsonobj["'conditions'"][0][1]["'defines'"]
    child.remove("'QT_STATICPLUGIN'")
    return json.dumps(jsonobj)

def process_telegram(jsonobj):
    child = jsonobj["'targets'"][0]
    child["'dependencies'"].remove("'utils.gyp:Updater'")
    child = jsonobj["'targets'"][0]["'defines'"]
    child.append("'__STDC_FORMAT_MACROS'")
    child.append("'TDESKTOP_DISABLE_AUTOUPDATE'")
    child.append("'TDESKTOP_DISABLE_REGISTER_CUSTOM_SCHEME'")
    child.append("'TDESKTOP_DISABLE_UNITY_INTEGRATION'")
    # child.append("'TDESKTOP_DISABLE_GTK_INTEGRATION'")
    child.append("'TDESKTOP_DISABLE_OPENAL_EFFECTS'")
    child.remove("'AL_LIBTYPE_STATIC'")
    child = jsonobj["'targets'"][0]["'include_dirs'"]
    child.remove("'<(libs_loc)/breakpad/src'")
    child.remove("'<(libs_loc)/lzma/C'")
    child.remove("'<(libs_loc)/zlib'")
    child.remove("'<(libs_loc)/ffmpeg'")
    child.remove("'<(libs_loc)/openal-soft/include'")
    child.remove("'<(libs_loc)/opus/include'")
    # child.remove("'<(libs_loc)/range-v3/include'")
    child.remove("'<(minizip_loc)'")
    child.remove("'<(sp_media_key_tap_loc)'")
    child.append("'<(libs_loc)/breakpad/include/breakpad'")
    child.append("'/usr/include/minizip'")
    child.append("'/usr/include/ffmpeg'")
    return json.dumps(jsonobj)

def process_libffmpeg(jsonobj):
    include_dirs = jsonobj["'targets'"][0]["'include_dirs'"]
    include_dirs.remove("'<(libs_loc)/ffmpeg'")
    include_dirs.append("'/usr/include/ffmpeg'")
    return json.dumps(jsonobj)

def process(filename, op):
    json = load_json(filename)
    json = op(json)
    save_json(json, filename)

tl_path = './Telegram/gyp/telegram/linux.gypi'
tg_srcs = './Telegram/gyp/telegram/sources.txt'
settings_path = './Telegram/gyp/common/linux.gypi'
tg_path = './Telegram/gyp/telegram/telegram.gypi'
qt_path = './Telegram/gyp/modules/qt.gypi'
moc_path = './Telegram/gyp/modules/qt_moc.gypi'
rcc_path = './Telegram/gyp/modules/qt_rcc.gypi'
libffmpeg_path="./Telegram/gyp/lib_ffmpeg.gyp"

print("Patching %s ..." % tl_path)
process(tl_path, process_telegram_linux)
print("Patching %s ..." % settings_path)
process(settings_path, process_settings_linux)
print("Patching %s ..." % qt_path)
process(qt_path, process_qt)
print("Patching %s ..." % tg_path)
process(tg_path, process_telegram)
print("Patching %s ..." % libffmpeg_path)
process(libffmpeg_path, process_libffmpeg)

print("Patching complete!")
