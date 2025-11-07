#
# spec file for package calibre
#
# Copyright (c) 2025 SUSE LLC and contributors
#
# All modifications and additions to the file contributed by third parties
# remain the property of their copyright owners, unless otherwise agreed
# upon. The license for this file, and modifications and additions to the
# file, is the same license as for the pristine package itself (unless the
# license for the pristine package is not an Open Source License, in which
# case the license is the MIT License). An "Open Source License" is a
# license that conforms to the Open Source Definition (Version 1.9)
# published by the Open Source Initiative.

# Please submit bugfixes or comments via https://bugs.opensuse.org/
#


%define my_qtversion 6.5.3

%if 0%{suse_version} < 1600
%global pythons python311
%else
%global pythons python3
%endif

%{?sle15_python_module_pythons}
Name:           calibre
Version:        8.14.0
Release:        0
Summary:        EBook Management Application
License:        GPL-3.0-only
Group:          Productivity/Other
URL:            https://calibre-ebook.com
#Source0:        https://download.calibre-ebook.com/%%{version}/calibre-%%{version}.tar.xz
#Source1:        https://calibre-ebook.com/signatures/calibre-%%{version}.tar.xz.sig
Source0:        https://github.com/kovidgoyal/calibre/releases/download/v%{version}/%{name}-%{version}.tar.xz
Source2:        https://calibre-ebook.com/signatures/kovid.gpg#/%{name}.keyring
Source5:        https://github.com/mathjax/MathJax/archive/3.1.4/mathjax-3.1.4.tar.gz
#Source6-URL:        https://github.com/LibreOffice/dictionaries/archive/master/hyphenation-dictionaries.tar.gz
# Must be comment out because obs/osc can not download it altought it is valid, and obs rise up an error when it enable.
# Source6 is backup if upstream change something again.
Source6:        hyphenation-dictionaries.tar.gz
# Source7-URL: https://salsa.debian.org/iso-codes-team/iso-codes/-/archive/main/iso-codes-main.zip
# Must be comment out because obs/osc can not download it altought it is valid, and obs rise up an error when it enable.
# Source7 is backup if upstream change something again.
Source7:        iso-codes-main.zip
# Missing user-agent-data.json since 6.12.0.
# Fix: FileNotFoundError: [Errno 2] No such file or directory: '/usr/share/calibre/user-agent-data.json'
# Use from inside https://github.com/kovidgoyal/calibre/releases/download/v6.14.0/calibre-6.14.0-x86_64.txz
Source8:        user-agent-data.json
Source100:      %{name}-rpmlintrc
# PATCH-FIX-OPENSUSE: install locale files the openSUSE way
Patch2:         %{name}-setup.install.py.diff
# PATCH-FIX-OPENSUSE: disabling Autoupdate Searcher
Patch3:         %{name}-no-update.diff
# PATCH-FIX-OPENSUSE: disbale piper because since 8.8.0 calibre needs onnxruntime which is not in openSUSE.
Patch4:         %{name}-disable_piper.patch
ExclusiveArch:  aarch64 x86_64 riscv64
%if 0%{?suse_version} <= 1550
BuildRequires:  gcc12
BuildRequires:  gcc12-c++
%else
BuildRequires:  gcc
BuildRequires:  gcc-c++
%endif
BuildRequires:  cmake >= 3.27.6
BuildRequires:  fdupes
BuildRequires:  help2man
BuildRequires:  hicolor-icon-theme
BuildRequires:  update-desktop-files

# A note on BuildRequires and Requires:
#
# Requires should always be a subset of BuildRequires. If there are packages
# that are only Required
# * there is no way to check whether these packages are available in the given
#   repositories unless you install the package (the build environment only
#   contains packages from the given repositories and the project
# * the project's repository might become inconsistent, because Required
#   packages do not block a build. So a package might get published, although
#   a Required package does not build
# For those reasons put Requires also in the BuildRequires list below
BuildRequires:  chmlib-devel >= 0.40
#BuildRequires:  dbus-1-python3 >= 1.2.0
BuildRequires:  chmlib-devel >= 0.40
BuildRequires:  freetype2-devel >= 2.13.2
BuildRequires:  graphite2-devel >= 1.3.14
BuildRequires:  hyphen-devel >= 2.8.8
#upstream use:  iconv >= 1.17
BuildRequires:  liberation-fonts
BuildRequires:  libmtp-devel >= 1.1.21
# Upstream use libopenssl-devel >= 3.1.7
BuildRequires:  libopenssl-3-devel >= 3.1.4
BuildRequires:  libpoppler-devel >= 23.08.0
BuildRequires:  libstemmer-devel >= 2.2.0
BuildRequires:  libwmf-devel >= 0.2.8
%if 0%{suse_version} == 1600
BuildRequires:  (libpodofo-devel >= 0.10.3 and libpodofo-devel < 1.0.0)
%else
BuildRequires:  (libpodofo-0_10-devel >= 0.10.3 and libpodofo-0_10-devel < 1.0.0)
%endif
# upstream use: mozjpeg >= 4.1.4
BuildRequires:  optipng >= 0.7.7
BuildRequires:  poppler-tools >= 23.08.0
BuildRequires:  python-rpm-macros
BuildRequires:  qt6-core-private-devel >= %{my_qtversion}
BuildRequires:  qt6-declarative-devel >= %{my_qtversion}
BuildRequires:  qt6-gui-private-devel >= %{my_qtversion}
BuildRequires:  qt6-imageformats-devel >= %{my_qtversion}
BuildRequires:  qt6-platformsupport-private-devel >= %{my_qtversion}
BuildRequires:  qt6-wayland-devel >= %{my_qtversion}
#BuildRequires:  python311-dbus-python
BuildRequires:  xdg-utils >= 1.0.2
BuildRequires:  pkgconfig(Qt6Core) >= %{my_qtversion}
BuildRequires:  pkgconfig(Qt6Gui) >= %{my_qtversion}
BuildRequires:  pkgconfig(Qt6Network) >= %{my_qtversion}
BuildRequires:  pkgconfig(Qt6Positioning) >= %{my_qtversion}
BuildRequires:  pkgconfig(Qt6Sensors) >= %{my_qtversion}
BuildRequires:  pkgconfig(Qt6ShaderTools) >= %{my_qtversion}
BuildRequires:  pkgconfig(Qt6Svg) >= %{my_qtversion}
BuildRequires:  pkgconfig(Qt6WebChannel) >= %{my_qtversion}
BuildRequires:  pkgconfig(Qt6WebEngineCore) >= %{my_qtversion}
BuildRequires:  pkgconfig(Qt6WebEngineWidgets) >= %{my_qtversion}
BuildRequires:  pkgconfig(Qt6Widgets) >= %{my_qtversion}
BuildRequires:  pkgconfig(dbus-glib-1) >= 0.112
BuildRequires:  pkgconfig(espeak-ng)
BuildRequires:  pkgconfig(fontconfig) >= 2.14.2
BuildRequires:  pkgconfig(glib-2.0) >= 2.78.0
BuildRequires:  pkgconfig(gpg-error) >= 1.47
BuildRequires:  pkgconfig(hunspell) >= 1.7.2
###BuildRequires:  pkgconfig(icu-i18n) < 76.0
BuildRequires:  pkgconfig(icu-i18n) >= 73.2
# Upstream use 7.1
BuildRequires:  pkgconfig(libavcodec)
BuildRequires:  pkgconfig(libavdevice)
BuildRequires:  pkgconfig(libavfilter)
BuildRequires:  pkgconfig(libavformat)
BuildRequires:  pkgconfig(libavutil)
BuildRequires:  pkgconfig(libswscale)
#
BuildRequires:  pkgconfig(libffi) >= 3.4.4
BuildRequires:  libjbig-devel >= 2.1
BuildRequires:  pkgconfig(libgcrypt) >= 1.10.2
BuildRequires:  pkgconfig(libjpeg) >= 3.0.0
BuildRequires:  pkgconfig(libmspack)
BuildRequires:  pkgconfig(libopenjp2) >= 2.5.0
BuildRequires:  pkgconfig(libpng16) >= 1.6.40
BuildRequires:  pkgconfig(libtiff-4) >= 4.6.0
BuildRequires:  pkgconfig(libusb-1.0) >= 1.0.26
BuildRequires:  pkgconfig(libwebp) >= 1.3.2
# upstream use BuildRequires:  pkgconfig(ncurses) >= 6.4
BuildRequires:  pkgconfig(ncurses) >= 6.1
BuildRequires:  pkgconfig(readline) >= 8.2
BuildRequires:  pkgconfig(sqlite3) >= 3.43.0
BuildRequires:  pkgconfig(uchardet) >= 0.0.7
# calibre no longer depends on ImageMagick
# but keept BuildRequires to convert icon to serveral sizes
BuildRequires:  pkgconfig(ImageMagick) >= 6.5.9
#
BuildRequires:  jxrlib-devel >= 0.2.4
BuildRequires:  %{python_module Brotli >= 1.1.0}
BuildRequires:  %{python_module FontTools >= 4.39.3}
BuildRequires:  %{python_module Markdown >= 3.3.6}
BuildRequires:  %{python_module Pillow >= 8.4.0}
BuildRequires:  %{python_module Pygments >= 2.10.0}
BuildRequires:  %{python_module apsw >= 3.43.0.0}
BuildRequires:  %{python_module base >= 3.10}
BuildRequires:  %{python_module beautifulsoup4 >= 4.10.0}
BuildRequires:  %{python_module cchardet >= 2.1.7}
BuildRequires:  %{python_module chardet >= 4.0.0}
BuildRequires:  %{python_module css-parser >= 1.0.8}
BuildRequires:  %{python_module dateutil >= 2.8.2}
BuildRequires:  %{python_module devel >= 3.10}
BuildRequires:  %{python_module dnspython >= 2.1.0}
BuildRequires:  %{python_module feedparser >= 6.0.8}
BuildRequires:  %{python_module html2text >= 2020.1.16}
BuildRequires:  %{python_module html5-parser >= 0.4.10}
BuildRequires:  %{python_module html5lib >= 1.1}
BuildRequires:  %{python_module ifaddr >= 0.1.7}
BuildRequires:  %{python_module inflate64 >= 1.0.3}
BuildRequires:  %{python_module jeepney >= 0.7.1}
BuildRequires:  %{python_module lxml >= 5.2.1}
BuildRequires:  %{python_module lxml_html_clean}
BuildRequires:  %{python_module mechanize >= 0.4.8}
BuildRequires:  %{python_module msgpack >= 1.0.7}
BuildRequires:  %{python_module multivolumefile >= 0.2.3}
BuildRequires:  %{python_module netifaces >= 0.11.0}
BuildRequires:  %{python_module odfpy}
BuildRequires:  %{python_module packaging >= 21.3}
BuildRequires:  %{python_module ply >= 3.11}
BuildRequires:  %{python_module psutil >= 5.8.0}
BuildRequires:  %{python_module pybcj >= 1.0.1}
BuildRequires:  %{python_module pychm >= 0.8.6}
BuildRequires:  %{python_module pycryptodome >= 3.19.0}
BuildRequires:  libjpeg-turbo >= 3.0.0
##BuildRequires:  %%{python_module pykakasi >= 2.3.0}
BuildRequires:  %{python_module pyparsing >= 3.0.6}
BuildRequires:  %{python_module pyppmd >= 1.2.0}
BuildRequires:  %{python_module pyqt-builder >= 1.14.0}
BuildRequires:  %{python_module pyzstd >= 0.17.0}
BuildRequires:  %{python_module qt6-devel >= %{my_qtversion}}
BuildRequires:  %{python_module regex >= 2021.11.10}
# Upstream use: BuildRequires:  %%{python_module setuptools >= 68.2.2}
BuildRequires:  %{python_module setuptools >= 67.8.0}
BuildRequires:  %{python_module qtwebengine-qt6 >= %{my_qtversion}}
BuildRequires:  %{python_module sgmllib3k >= 1.0.0}
BuildRequires:  %{python_module sip-devel >= 6.7.5}
BuildRequires:  %{python_module six >= 1.16.0}
BuildRequires:  %{python_module soupsieve >= 2.5}
BuildRequires:  %{python_module texttable >= 1.6.7}
BuildRequires:  %{python_module toml >= 0.10.2}
BuildRequires:  %{python_module xxhash >= 3.3.0}
# Upstream use pkgconfig(libxml-2.0) >= 2.12.6
BuildRequires:  pkgconfig(libxml-2.0) >= 2.10.3
BuildRequires:  pkgconfig(libxslt) >= 1.1.39
#BuildRequires:  python-unrardll >= 0.1.5
BuildRequires:  %{python_module py7zr >= 1.0.0}
BuildRequires:  %{python_module speechd >= 0.11.5}
BuildRequires:  %{python_module webencodings >= 0.5.1}
BuildRequires:  %{python_module zeroconf >= 0.37.0}
#
Requires:       chmlib >= 0.40
#Requires:       dbus-1-python3 >= 1.2.0
Requires:       liberation-fonts
Requires:       %{python_flavor}-Brotli >= 1.1.0
Requires:       %{python_flavor}-Markdown >= 3.3.6
Requires:       %{python_flavor}-Pillow >= 8.4.0
Requires:       %{python_flavor}-Pygments >= 2.10.0
Requires:       %{python_flavor}-apsw >= 3.43.0.0
Requires:       %{python_flavor}-base >= 3.10
Requires:       %{python_flavor}-beautifulsoup4 >= 4.10.0
Requires:       %{python_flavor}-cchardet >= 2.1.7
Requires:       %{python_flavor}-chardet >= 4.0.0
Requires:       %{python_flavor}-css-parser >= 1.0.8
Requires:       %{python_flavor}-dateutil >= 2.8.2
Requires:       libjpeg-turbo >= 3.0.0
Requires:       libmtp9 >= 1.1.21
Requires:       libpng16-16 >= 1.6.40
Requires:       libwmf >= 0.2.8
Requires:       optipng >= 0.7.7
Requires:       poppler-tools >= 23.08.0
#Requires:       %%{python_flavor}-dbus-python
Requires:       %{python_flavor}-dnspython >= 2.1.0
Requires:       %{python_flavor}-FontTools >= 4.39.3
Requires:       %{python_flavor}-PyQt6-sip >= 13.5.2
Requires:       %{python_flavor}-feedparser >= 6.0.8
Requires:       %{python_flavor}-html2text >= 2020.1.16
Requires:       %{python_flavor}-html5-parser >= 0.4.10
Requires:       %{python_flavor}-html5lib >= 1.1
Requires:       %{python_flavor}-ifaddr >= 0.1.7
Requires:       %{python_flavor}-inflate64 >= 1.0.3
Requires:       %{python_flavor}-jeepney >= 0.7.1
Requires:       %{python_flavor}-lxml >= 5.2.1
Requires:       %{python_flavor}-lxml_html_clean
Requires:       %{python_flavor}-mechanize >= 0.4.8
Requires:       %{python_flavor}-msgpack >= 1.0.7
Requires:       %{python_flavor}-multivolumefile >= 0.2.3
Requires:       %{python_flavor}-netifaces >= 0.11.0
Requires:       %{python_flavor}-odfpy
Requires:       %{python_flavor}-ply >= 3.11
Requires:       %{python_flavor}-psutil >= 5.8.0
Requires:       %{python_flavor}-pybcj >= 1.0.1
Requires:       %{python_flavor}-pychm >= 0.8.6
Requires:       %{python_flavor}-pycryptodome >= 3.19.0
##Requires:       %%{python_flavor}-pykakasi >= 2.3.0
Requires:       %{python_flavor}-pyparsing >= 3.0.6
Requires:       %{python_flavor}-pyppmd >= 1.2.0
Requires:       %{python_flavor}-pyzstd >= 0.17.0
Requires:       %{python_flavor}-qt6 >= %{my_qtversion}
Requires:       %{python_flavor}-qtwebengine-qt6 >= %{my_qtversion}
Requires:       %{python_flavor}-regex >= 2021.11.10
Requires:       %{python_flavor}-sgmllib3k >= 1.0.0
Requires:       %{python_flavor}-six >= 1.16.0
Requires:       %{python_flavor}-soupsieve >= 2.5
Requires:       %{python_flavor}-texttable >= 1.6.7
Requires:       %{python_flavor}-xxhash >= 3.3.0
#Requires:       %%{python_flavor}-unrardll >= 0.1.5
Requires:       %{python_flavor}-py7zr >= 1.0.0
Requires:       %{python_flavor}-speechd >= 0.11.5
Requires:       %{python_flavor}-webencodings >= 0.5.1
Requires:       %{python_flavor}-zeroconf >= 0.37.0
#
Requires:       sqlite3 >= 3.43.0
Requires:       bzip2 >= 1.0.8
# Upstream use expat >= 2.5.0
Requires:       expat >= 2.4.4
Requires:       libsqlite3-0 >= 3.43.0
Requires:       unrar >= 6.2.11
Requires:       xdg-utils >= 1.0.2
# Upstream use xz >= 5.4.4
Requires:       xz >= 5.4.1
# upstream use zlib >= 1.3.1
Requires:       zlib >= 1.2.13

Requires(pretrans): findutils

BuildRoot:      %{_tmppath}/%{name}-%{version}-build

%description
Calibre is an ebook library manager. It can view, convert and catalog
ebooks in most of the major ebook formats. It can also talk to a few
ebook reader devices. It can go out on the Internet and fetch
metadata for books. It can download newspapers and convert them
into ebooks for convenient reading.

%prep
%setup -q -a5 -a6
%patch -P 2 -p1
%patch -P 3 -p1 -b .no-update
%patch -P 4 -p1

# dos2unix newline conversion
sed -i 's/\r//' src/calibre/web/feeds/recipes/*

# remove shebangs
sed -i -e '/^#!\//, 1d' src/calibre/*/*/*/*/*.py
sed -i -e '/^#!\//, 1d' src/calibre/*/*/*/*.py
sed -i -e '/^#!\//, 1d' src/calibre/*/*/*.py
sed -i -e '/^#![ ]*\//, 1d' src/calibre/*/*.py
sed -i -e '/^#!\//, 1d' src/calibre/*.py
sed -i -e '/^#!\//, 1d' src/templite/*.py
sed -i -e '/^#!\//, 1d' src/tinycss/*.py
sed -i -e '/^#!\//, 1d' src/tinycss/*/*.py
sed -i -e '/^#!\//, 1d' resources/default_tweaks.py

# remove the executable flag from files
find src/calibre -name "*.py" -type f -exec chmod -x {} +
chmod -x recipes/*.recipe

# rpmlint: wrong-script-interpreter /usr/bin/env python3
##find setup -type f  | xargs sed -i -e 's|#!/usr/bin/env python|#!/usr/bin/python3|g'

# use system mspack (mga#15218)
##rm -f src/calibre/utils/lzx/mspack.h
##sed -i 's| calibre/utils/lzx/mspack.h||' setup/extensions.json

%build
%if 0%{?suse_version} <= 1500
export CC=gcc-12
export CXX=g++-12
%endif
export \
LANG="en_US.UTF8" \
CFLAGS="%{optflags}" \
CXXFLAGS="%{optflags}"

###python setup.py build
CALIBRE_PY3_PORT=1 python%python_bin_suffix setup.py build

#python%%python_bin_suffix setup.py iso639
#python%%python_bin_suffix setup.py iso3166
#python%%python_bin_suffix setup.py translations
python%python_bin_suffix setup.py gui

#%%{__python3} setup.py resources \
#	--path-to-liberation_fonts %%{_datadir}/fonts/truetype \
#	--system-liberation_fonts \
#	--path-to-hyphenation `pwd`/dictionaries-master \
#	--path-to-mathjax `pwd`/MathJax-3.1.4
#%%{__python%%python_bin_suffix} setup.py man_pages

%install
###python setup.py install \
CALIBRE_PY3_PORT=1 python%python_bin_suffix setup.py install \
   --prefix=%{_prefix} \
   --root=%{buildroot}%{_prefix} \
   --staging-bindir=%{buildroot}%{_bindir} \
   --staging-libdir=%{buildroot}%{_libdir} \
   --staging-sharedir=%{buildroot}%{_datadir} \
   --staging-mandir=%{buildroot}%{_mandir} \
   --libdir=%{_libdir}

# GENERATE AND INSTALL HIRES ICONS INTO HICOLOR DIR (PRESENT ICON LOOKS BLURRED ON HiDPI)
for i in 24 32 48 64 128 256 512
do
  mkdir -p %{buildroot}%{_datadir}/icons/hicolor/${i}x${i}/apps
  convert -strip icons/calibre.png \
          -resize ${i}x${i} %{buildroot}%{_datadir}/icons/hicolor/${i}x${i}/apps/%{name}.png
done

%suse_update_desktop_file -i -n -N "Calibre E-Book Management" -G "Calibre E-Book library management" calibre-gui
%suse_update_desktop_file -i -n -N "Calibre E-Book Editor" -G "Calibre Editor for E-Books" calibre-ebook-edit
%suse_update_desktop_file -i -n -N "Calibre E-Book Viewer" -G "Calibre Viewer for E-Books" calibre-ebook-viewer
%suse_update_desktop_file -i -n -N "Calibre LRF Viewer" -G "Calibre Viewer for LRF files" calibre-lrfviewer

# rpmlint: wrong-script-interpreter /usr/bin/env python3
find %{buildroot}%{_bindir} -type f  | xargs sed -i -e 's:#!/usr/bin/env python3:#!/usr/bin/python%python_bin_suffix:g'
find %{buildroot}%{_libdir}/calibre -type f  | xargs sed -i -e 's:#!/usr/bin/env python3:#!/usr/bin/python%python_bin_suffix:g'

# these are provided as separate packages
rm -r %{buildroot}%{_libdir}/%{name}/odf

# Also the Liberation fonts are provided as separate
# packages, but a symbolic link to each is needed.
for font in %{buildroot}%{_datadir}/%{name}/fonts/liberation/*.ttf
do
    rm ${font}
    ln -s %{_datadir}/fonts/truetype/$(basename ${font}) %{buildroot}%{_datadir}/%{name}/fonts/liberation/
done

# Fix missing user-agent-data.json
# With version 6.15.0 it is available again. So we use it again from source but let the code in.
#install -Dm 0644 %%{SOURCE8} %%{buildroot}%%{_datadir}/%%{name}/user-agent-data.json

%fdupes %{buildroot}%{_prefix}

# bsc#1022710, bsc#1104597: fix upgrade
# liberation had become a symlink in Leap and RPM does not like to overwrite a directory with a symlink (or vice versa).
# Later, liberation became a directory again.
# This scriptlet supports both upgrade scenarios.  Sort of.
# When converting from a link into a directory, it will complain about conflicting files with liberation-fonts.

%pretrans -p <lua>
path = "%{_datadir}/%{name}/fonts/liberation"
st = posix.stat(path)
if st and st.type == "link" then
   os.remove(path)
end
-- This depends on the assumption that the directory should only contain symbolic links.
if st and st.type == "directory" then
  os.execute("find " .. path .. " -type f -delete")
end

%check
# don't know why Leap rise up an error. Does anyone know the reason?
%if 0%{?suse_version} > 1500
TEST_EXCLUDE=(
    --exclude-test-name unrar                       # is not in openSUSE oss
    --exclude-test-name zeroconf                    # rise up build error
%if 0%{?suse_version} >= 1600
    --exclude-test-name test_fts_basic              # rise up build error
    --exclude-test-name test_websocket_basic        # rise up build error
    --exclude-test-name test_piper                  # rise up build error
    --exclude-test-name test_plugins                # rise up build error since disable_piper.patch
    --exclude-test-name test_pykakasi               # is not in openSUSE oss
    --exclude-test-name test_import_of_all_python_modules # rise up build error because of pykakasi
%endif
)

CALIBRE_PY3_PORT=1 SKIP_QT_BUILD_TEST=1 python%python_bin_suffix setup.py test "${TEST_EXCLUDE[@]}"
%endif

%if 0%{?suse_version} <= 1320
%post
%desktop_database_post
%icon_theme_cache_post

%postun
%desktop_database_postun
%icon_theme_cache_postun
%endif

%files
# -f %%{name}.lang  -f iso639.lang
%license COPYRIGHT LICENSE LICENSE.rtf
%{_bindir}/*
%{_datadir}/applications/%{name}-gui.desktop
%{_datadir}/applications/%{name}-ebook-edit.desktop
%{_datadir}/applications/%{name}-ebook-viewer.desktop
%{_datadir}/applications/%{name}-lrfviewer.desktop
%dir %{_datadir}/icons/hicolor/512x512
%dir %{_datadir}/icons/hicolor/512x512/apps
%{_datadir}/icons/hicolor/*/apps/*.png
%{_datadir}/icons/hicolor/*/mimetypes/*.png
%{_datadir}/mime/packages/calibre-mimetypes.xml
%{_datadir}/%{name}/
%{_datadir}/%{name}/user-agent-data.json
%{_libdir}/%{name}/
%dir %{_datadir}/metainfo
%{_datadir}/metainfo/%{name}-gui.metainfo.xml
%{_datadir}/metainfo/%{name}-ebook-edit.metainfo.xml
%{_datadir}/metainfo/%{name}-ebook-viewer.metainfo.xml
%{_datadir}/bash-completion/completions/%{name}*
%{_datadir}/bash-completion/completions/*ebook*
%{_datadir}/bash-completion/completions/lrf*
%{python_sitearch}/init_calibre.py

%changelog
