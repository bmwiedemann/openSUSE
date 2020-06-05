#
# spec file for package calibre
#
# Copyright (c) 2020 SUSE LLC
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


%{?!python_module:%define python_module() python-%{**} python3-%{**}}
%define skip_python2 1

Name:           calibre
Version:        4.18.0
Release:        0
Summary:        EBook Management Application
License:        GPL-3.0-only
Group:          Productivity/Other
URL:            https://calibre-ebook.com
Source0:        https://download.calibre-ebook.com/%{version}/calibre-%{version}.tar.xz
Source1:        https://calibre-ebook.com/signatures/calibre-%{version}.tar.xz.sig
Source2:        https://calibre-ebook.com/signatures/kovid.gpg#/%{name}.keyring
Source3:        %{name}.desktop
Source100:      %{name}-rpmlintrc
# PATCH-FIX-OPENSUSE: disabling unrar test
Patch1:         %{name}-python_test.patch
#
Patch2:         %{name}-setup.install.py.diff
# PATCH-FIX-OPENSUSE: disabling Autoupdate Searcher
Patch3:         %{name}-no-update.diff
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
BuildRequires:  dbus-1-python3 >= 1.2.0
BuildRequires:  hyphen-devel >= 2.8.8
BuildRequires:  libQt5Core-private-headers-devel >= 5.14.1
BuildRequires:  libQt5Gui-private-headers-devel >= 5.14.1
BuildRequires:  libQt5PlatformSupport-private-headers-devel >= 5.14.1
BuildRequires:  liberation-fonts
BuildRequires:  libicu-devel >= 4.4.0
BuildRequires:  libmtp-devel >= 1.1.5
BuildRequires:  libopenssl-devel
BuildRequires:  libpodofo-devel >= 0.8.2
BuildRequires:  libpoppler-devel >= 0.20.2
BuildRequires:  libwmf-devel >= 0.2.8
BuildRequires:  optipng >= 0.7.5
BuildRequires:  podofo >= 0.8.2
BuildRequires:  poppler-tools >= 0.20.2
BuildRequires:  xdg-utils >= 1.0.2
BuildRequires:  pkgconfig(Qt5Core) >= 5.14.1
BuildRequires:  pkgconfig(Qt5Gui) >= 5.14.1
BuildRequires:  pkgconfig(Qt5Network) >= 5.14.1
BuildRequires:  pkgconfig(Qt5WebEngineWidgets) >= 5.14.1
BuildRequires:  pkgconfig(Qt5Widgets) >= 5.14.1
BuildRequires:  pkgconfig(hunspell)
BuildRequires:  pkgconfig(python3)
BuildRequires:  pkgconfig(sqlite3)
# calibre no longer depends on ImageMagick
# but keept BuildRequires to convert icon to serveral sizes
BuildRequires:  pkgconfig(ImageMagick) >= 6.5.9
#
BuildRequires:  libjpeg-turbo
BuildRequires:  python-rpm-macros
BuildRequires:  python3-qt5-devel >= 5.13.1
BuildRequires:  pkgconfig(libjpeg)
# upstream use python-Pillow 6.0.0
BuildRequires:  %{python_module Pillow >= 5.0.0}
# upstream use python-Pygments 2.3.1
BuildRequires:  %{python_module Pygments >= 2.2.0}
# upstream use python-apsw 3.30.1-r1
BuildRequires:  %{python_module apsw >= 3.9.2}
# upstream use python-beautifulsoup4 4.7.1
BuildRequires:  %{python_module beautifulsoup4 >= 4.6.0}
BuildRequires:  %{python_module chardet >= 3.0.4}
BuildRequires:  %{python_module css-parser >= 1.0.4}
# upstream use python-dateutil 2.8.0
BuildRequires:  %{python_module dateutil >= 2.7.3}
# upstream use python-dnspython 0.16.0
BuildRequires:  %{python_module dnspython >= 1.15.0}
BuildRequires:  %{python_module dukpy-kovidgoyal >= 0.3}
# upstream use python-html5-paser 0.4.9
BuildRequires:  %{python_module html5-parser >= 0.4.6}
BuildRequires:  %{python_module html5lib >= 1.0.1}
# upstream use python-lxml 4.3.3
BuildRequires:  %{python_module lxml >= 4.0.0}
# upstream use python-mechanize 0.4.3
BuildRequires:  %{python_module mechanize >= 0.3.5}
# upstream use python-msgpack 0.6.1
BuildRequires:  %{python_module msgpack >= 0.5.6}
# upstream use python-netifaces 0.10.9
BuildRequires:  %{python_module netifaces >= 0.10.6}
BuildRequires:  %{python_module odfpy}
# upstream use python-psutil 5.6.2
BuildRequires:  %{python_module psutil >= 5.4.8}
# upstream use python-ifaddr 0.1.6
BuildRequires:  %{python_module ifaddr >= 0.1.4}
# upstream use python-regex 2019.04.14
BuildRequires:  %{python_module Markdown >= 3.1}
BuildRequires:  %{python_module feedparser >= 5.2.1}
BuildRequires:  %{python_module html2text >= 2018.1.9}
BuildRequires:  %{python_module pycrypto >= 2.6.1}
BuildRequires:  %{python_module regex >= 2017.07.28}
BuildRequires:  %{python_module setuptools >= 23.1.0}
BuildRequires:  %{python_module sip-devel >= 4.12}
# Need at buildtime too, to produce the bash completion
BuildRequires:  %{python_module qtwebengine-qt5 >= 5.13.1}
BuildRequires:  %{python_module six >= 1.10.0}
BuildRequires:  %{python_module soupsieve >= 1.9.1}
#BuildRequires:  python-unrardll >= 0.1.3
BuildRequires:  %{python_module webencodings >= 0.5.1}
# upstream use python-zeroconf 0.21.3
BuildRequires:  %{python_module zeroconf >= 0.19.1}
#
Requires:       chmlib >= 0.40
Requires:       dbus-1-python3 >= 1.2.0
Requires:       liberation-fonts
Requires:       libmtp9 >= 1.1.5
Requires:       libwmf >= 0.2.8
Requires:       optipng >= 0.7.5
Requires:       podofo >= 0.8.2
Requires:       poppler-tools >= 0.20.2
Requires:       python3
Requires:       python3-Markdown >= 3.1
Requires:       python3-Pillow >= 5.0.0
Requires:       python3-Pygments >= 2.1.3
Requires:       python3-apsw >= 3.9.2
Requires:       python3-beautifulsoup4 >= 4.6.0
Requires:       python3-chardet >= 3.0.4
Requires:       python3-css-parser >= 1.0.4
Requires:       python3-dateutil >= 2.7.3
Requires:       python3-dnspython >= 1.15.0
Requires:       python3-dukpy-kovidgoyal >= 0.3
Requires:       python3-feedparser >= 5.2.1
Requires:       python3-html2text >= 2018.1.9
Requires:       python3-html5-parser >= 0.4.6
Requires:       python3-html5lib >= 1.0.1
Requires:       python3-ifaddr >= 0.1.4
Requires:       python3-lxml >= 4.0.0
Requires:       python3-mechanize >= 0.3.5
Requires:       python3-msgpack >= 0.5.6
Requires:       python3-netifaces >= 0.10.7
Requires:       python3-odfpy
Requires:       python3-psutil >= 5.4.8
Requires:       python3-pycrypto >= 2.6.1
Requires:       python3-qt5 >= 5.13.1
Requires:       python3-qtwebengine-qt5 >= 5.13.1
Requires:       python3-regex >= 2017.07.28
Requires:       python3-setuptools >= 23.1.0
Requires:       python3-sip >= 4.12.1
Requires:       python3-six >= 1.10.0
Requires:       python3-soupsieve >= 1.9.1
#Requires:       python3-unrardll >= 0.1.3
Requires:       python3-webencodings >= 0.5.1
Requires:       python3-zeroconf >= 0.19.1
#
Requires:       sqlite3
Requires:       xdg-utils >= 1.0.2
Requires(pretrans): findutils

BuildRoot:      %{_tmppath}/%{name}-%{version}-build

%description
Calibre is an ebook library manager. It can view, convert and catalog
ebooks in most of the major ebook formats. It can also talk to a few
ebook reader devices. It can go out on the Internet and fetch
metadata for books. It can download newspapers and convert them
into ebooks for convenient reading.

%prep
%setup -q
%patch1 -p1
%patch2 -p1
%patch3 -p1 -b .no-update

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
find setup -type f  | xargs sed -i -e 's:#!/usr/bin/env python3:#!/usr/bin/python3:g'

cp -v %{SOURCE3}  .

%build
LANG="en_US.UTF8" \
CFLAGS="%{optflags}" \
CXXFLAGS="%{optflags}" \
OVERRIDE_CFLAGS="%{optflags}" \
CALIBRE_PY3_PORT=1 python3 setup.py build
###python setup.py build

%install
###python setup.py install \
CALIBRE_PY3_PORT=1 python3 setup.py install \
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

%suse_update_desktop_file -i -n calibre Office Viewer

%fdupes %{buildroot}/%{_prefix}

# rpmlint: wrong-script-interpreter /usr/bin/env python3
find %{buildroot}%{_bindir} -type f  | xargs sed -i -e 's:#!/usr/bin/env python3:#!/usr/bin/python3:g'
find %{buildroot}%{_libdir}/calibre -type f  | xargs sed -i -e 's:#!/usr/bin/env python3:#!/usr/bin/python3:g'

# these are provided as separate packages
rm -r %{buildroot}%{_libdir}/%{name}/odf

# Also the Liberation fonts are provided as separate
# packages, but a symbolic link to each is needed.
for font in %{buildroot}%{_datadir}/%{name}/fonts/liberation/*.ttf
do
    rm ${font}
    ln -s %{_datadir}/fonts/truetype/$(basename ${font}) %{buildroot}%{_datadir}/%{name}/fonts/liberation/
done

# appdata file references calibre-gui.desktop, and .appdata.xml file should necessarily have matching name with .desktop file in order for the app to show up in Software Centres
mv %{buildroot}%{_datadir}/applications/calibre.desktop %{buildroot}%{_datadir}/applications/calibre-gui.desktop

# Remove all appdata.xml files but the main one, we do not install the corresponding .desktop files
rm %{buildroot}%{_datadir}/metainfo/calibre-ebook-{edit,viewer}.appdata.xml
# Remove unneeded desktop files
rm %{buildroot}%{_datadir}/applications/calibre-ebook-{edit,viewer}.desktop
rm %{buildroot}%{_datadir}/applications/calibre-lrfviewer.desktop

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
CALIBRE_PY3_PORT=1 SKIP_QT_BUILD_TEST=1 python3 setup.py test

%post
%desktop_database_post
%icon_theme_cache_post

%postun
%desktop_database_postun
%icon_theme_cache_postun

%files
# -f %%{name}.lang  -f iso639.lang
%license COPYRIGHT LICENSE LICENSE.rtf
%{_bindir}/*
%{_datadir}/applications/%{name}-gui.desktop
%dir %{_datadir}/icons/hicolor/512x512
%dir %{_datadir}/icons/hicolor/512x512/apps
%{_datadir}/icons/hicolor/*/apps/*.png
%{_datadir}/icons/hicolor/*/mimetypes/*.png
%{_datadir}/mime/packages/calibre-mimetypes.xml
%{_datadir}/%{name}/
%{_libdir}/%{name}/
%dir %{_datadir}/metainfo
%{_datadir}/metainfo/%{name}-gui.appdata.xml
%{_datadir}/bash-completion/completions/%{name}*
%{_datadir}/bash-completion/completions/*ebook*
%{_datadir}/bash-completion/completions/lrf*
%{python_sitelib}/init_calibre.py

%changelog
