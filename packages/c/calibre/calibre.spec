#
# spec file for package calibre
#
# Copyright (c) 2024 SUSE LLC
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

%{?sle15_python_module_pythons}
Name:           calibre
Version:        7.12.0
Release:        0
Summary:        EBook Management Application
License:        GPL-3.0-only
Group:          Productivity/Other
URL:            https://calibre-ebook.com
Source0:        https://download.calibre-ebook.com/%{version}/calibre-%{version}.tar.xz
Source1:        https://calibre-ebook.com/signatures/calibre-%{version}.tar.xz.sig
Source2:        https://calibre-ebook.com/signatures/kovid.gpg#/%{name}.keyring
Source5:        https://github.com/mathjax/MathJax/archive/3.1.4/mathjax-3.1.4.tar.gz
Source6:        https://github.com/LibreOffice/dictionaries/archive/master/hyphenation-dictionaries.tar.gz
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
# Upstream use libopenssl-devel >= 3.1.3
BuildRequires:  libopenssl-3-devel >= 3.0.8
BuildRequires:  libpodofo-devel >= 0.10.1
BuildRequires:  libpoppler-devel >= 21.11.0
# upstream use: libstemmer-devel >= 2.2.0
BuildRequires:  libstemmer-devel >= 2.1.0
BuildRequires:  libwmf-devel >= 0.2.8
# upstream use: mozjpeg >= 4.0.3
BuildRequires:  optipng >= 0.7.7
BuildRequires:  podofo >= 0.10.1
BuildRequires:  poppler-tools >= 21.11.0
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
BuildRequires:  pkgconfig(glib-2.0) >= 2.70.1
BuildRequires:  pkgconfig(gpg-error) >= 1.43
BuildRequires:  pkgconfig(hunspell) >= 1.7.0
BuildRequires:  pkgconfig(icu-i18n) >= 73.2
BuildRequires:  pkgconfig(libffi) >= 3.4.4
BuildRequires:  pkgconfig(libgcrypt) >= 1.9.4
BuildRequires:  pkgconfig(libmspack)
BuildRequires:  pkgconfig(libopenjp2) >= 2.5.0
BuildRequires:  pkgconfig(libpng16) >= 1.6.40
# Upstream use pkgconfig(libusb-1.0) >= 1.0.26
BuildRequires:  pkgconfig(libusb-1.0) >= 1.0.24
# Upstream use pkgconfig(libtiff) >= 4.6.0
BuildRequires:  pkgconfig(libtiff-4) >= 4.0.9
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
# Upstream use libjpeg-turbo >= 3.0.0
BuildRequires:  libjpeg-turbo >= 2.1.5.1
BuildRequires:  python-rpm-macros
BuildRequires:  python311-Brotli >= 1.1.0
BuildRequires:  python311-FontTools >= 4.39.3
BuildRequires:  python311-Markdown >= 3.3.6
BuildRequires:  python311-Pillow >= 8.4.0
BuildRequires:  python311-Pygments >= 2.10.0
BuildRequires:  python311-apsw >= 3.43.0.0
BuildRequires:  python311-beautifulsoup4 >= 4.10.0
BuildRequires:  python311-cchardet >= 2.1.7
BuildRequires:  python311-chardet >= 4.0.0
BuildRequires:  python311-css-parser >= 1.0.8
BuildRequires:  python311-dateutil >= 2.8.2
BuildRequires:  python311-devel >= 3.10
BuildRequires:  python311-dnspython >= 2.1.0
BuildRequires:  python311-dukpy-kovidgoyal >= 0.3
BuildRequires:  python311-feedparser >= 6.0.8
BuildRequires:  python311-html2text >= 2020.1.16
BuildRequires:  python311-html5-parser >= 0.4.10
BuildRequires:  python311-html5lib >= 1.1
BuildRequires:  python311-ifaddr >= 0.1.7
BuildRequires:  python311-jeepney >= 0.7.1
BuildRequires:  python311-lxml >= 4.9.1
BuildRequires:  python311-mechanize >= 0.4.8
BuildRequires:  python311-msgpack >= 1.0.3
BuildRequires:  python311-multivolumefile >= 0.2.3
BuildRequires:  python311-netifaces >= 0.11.0
BuildRequires:  python311-odfpy
BuildRequires:  python311-packaging >= 21.3
BuildRequires:  python311-ply >= 3.11
BuildRequires:  python311-psutil >= 5.8.0
BuildRequires:  python311-pychm >= 0.8.6
BuildRequires:  python311-pycryptodome >= 3.11.0
BuildRequires:  python311-pyparsing >= 3.0.6
BuildRequires:  python311-pyppmd >= 1.1.0
BuildRequires:  python311-pyqt-builder >= 1.14.0
BuildRequires:  python311-pyzstd >= 0.15.6
BuildRequires:  python311-qt6-devel >= %{my_qtversion}
BuildRequires:  python311-regex >= 2021.11.10
# Upstream use: BuildRequires:  python311-setuptools >= 68.2.2
BuildRequires:  python311-setuptools >= 67.8.0
BuildRequires:  python311-qtwebengine-qt6 >= %{my_qtversion}
BuildRequires:  python311-sgmllib3k >= 1.0.0
BuildRequires:  python311-sip-devel >= 6.7.5
BuildRequires:  python311-six >= 1.16.0
BuildRequires:  python311-soupsieve >= 2.5
BuildRequires:  python311-texttable >= 1.6.4
BuildRequires:  python311-toml >= 0.10.2
BuildRequires:  python311-xxhash >= 3.3.0
BuildRequires:  pkgconfig(libjpeg) >= 2.1.2
BuildRequires:  pkgconfig(libwebp) >= 1.3.2
# Upstream use pkgconfig(libxml-2.0) >= 2.11.5
BuildRequires:  pkgconfig(libxml-2.0) >= 2.10.3
BuildRequires:  pkgconfig(libxslt) >= 1.1.38
#BuildRequires:  python-unrardll >= 0.1.5
BuildRequires:  python311-py7zr >= 0.20.6
%if 0%{?suse_version} > 1500
BuildRequires:  python3-speechd >= 0.11.1
%else
BuildRequires:  python311-speechd >= 0.11.1
%endif
BuildRequires:  python311-webencodings >= 0.5.1
BuildRequires:  python311-zeroconf >= 0.37.0
#
Requires:       chmlib >= 0.40
#Requires:       dbus-1-python3 >= 1.2.0
Requires:       liberation-fonts
Requires:       libmtp9 >= 1.1.21
Requires:       libpng16-16 >= 1.6.40
Requires:       libwmf >= 0.2.8
Requires:       optipng >= 0.7.5
Requires:       podofo >= 0.10.1
Requires:       poppler-tools >= 21.11.0
Requires:       python311 >= 3.10
Requires:       python311-Brotli >= 1.1.0
Requires:       python311-Markdown >= 3.3.6
Requires:       python311-Pillow >= 8.4.0
Requires:       python311-Pygments >= 2.10.0
Requires:       python311-apsw >= 3.43.0.0
Requires:       python311-beautifulsoup4 >= 4.10.0
Requires:       python311-cchardet >= 2.1.7
Requires:       python311-chardet >= 4.0.0
Requires:       python311-css-parser >= 1.0.8
Requires:       python311-dateutil >= 2.8.2
#Requires:       python311-dbus-python
Requires:       python311-dnspython >= 2.1.0
Requires:       python311-FontTools >= 4.39.3
Requires:       python311-PyQt6-sip >= 13.5.2
Requires:       python311-dukpy-kovidgoyal >= 0.3
Requires:       python311-feedparser >= 6.0.8
Requires:       python311-html2text >= 2020.1.16
Requires:       python311-html5-parser >= 0.4.10
Requires:       python311-html5lib >= 1.1
Requires:       python311-ifaddr >= 0.1.7
Requires:       python311-jeepney >= 0.7.1
Requires:       python311-lxml >= 4.9.1
Requires:       python311-mechanize >= 0.4.8
Requires:       python311-msgpack >= 1.0.3
Requires:       python311-multivolumefile >= 0.2.3
Requires:       python311-netifaces >= 0.11.0
Requires:       python311-odfpy
Requires:       python311-ply >= 3.11
Requires:       python311-psutil >= 5.8.0
Requires:       python311-pychm >= 0.8.6
Requires:       python311-pycryptodome >= 3.11.0
Requires:       python311-pyparsing >= 3.0.6
Requires:       python311-pyppmd >= 1.1.0
Requires:       python311-pyzstd >= 0.15.6
Requires:       python311-qt6 >= %{my_qtversion}
Requires:       python311-qtwebengine-qt6 >= %{my_qtversion}
Requires:       python311-regex >= 2021.11.10
Requires:       python311-sgmllib3k >= 1.0.0
Requires:       python311-six >= 1.16.0
Requires:       python311-soupsieve >= 2.5
Requires:       python311-texttable >= 1.6.4
Requires:       python311-xxhash >= 3.3.0
#Requires:       python311-unrardll >= 0.1.5
Requires:       python311-py7zr >= 0.20.6
%if 0%{?suse_version} > 1500
Requires:       python3-speechd >= 0.11.1
%else
Requires:       python311-speechd >= 0.11.1
%endif
Requires:       python311-webencodings >= 0.5.1
Requires:       python311-zeroconf >= 0.37.0
#
Requires:       sqlite3 >= 3.43.0
Requires:       bzip2 >= 1.0.8
# Upstream use expat >= 2.5.0
Requires:       expat >= 2.4.4
Requires:       libsqlite3-0 >= 3.43.0
Requires:       unrar >= 6.2.5
Requires:       xdg-utils >= 1.0.2
Requires:       xz >= 5.2.3
Requires:       zlib >= 1.2.13

Requires(pretrans):findutils

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
rm -f src/calibre/utils/lzx/mspack.h
sed -i 's| calibre/utils/lzx/mspack.h||' setup/extensions.json

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
CALIBRE_PY3_PORT=1 python3.11 setup.py build

#python3.11 setup.py iso639
#python3.11 setup.py iso3166
#python3.11 setup.py translations
python3.11 setup.py gui

#%%{__python3} setup.py resources \
#	--path-to-liberation_fonts %%{_datadir}/fonts/truetype \
#	--system-liberation_fonts \
#	--path-to-hyphenation `pwd`/dictionaries-master \
#	--path-to-mathjax `pwd`/MathJax-3.1.4
#%%{__python311} setup.py man_pages

%install
###python setup.py install \
CALIBRE_PY3_PORT=1 python3.11 setup.py install \
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
find %{buildroot}%{_bindir} -type f  | xargs sed -i -e 's:#!/usr/bin/env python3:#!/usr/bin/python3.11:g'
find %{buildroot}%{_libdir}/calibre -type f  | xargs sed -i -e 's:#!/usr/bin/env python3:#!/usr/bin/python3.11:g'

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
%if 0%{?suse_version} > 1600
    --exclude-test-name test_fts_basic              # rise up build error
%endif
)

CALIBRE_PY3_PORT=1 SKIP_QT_BUILD_TEST=1 python3.11 setup.py test "${TEST_EXCLUDE[@]}"
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
