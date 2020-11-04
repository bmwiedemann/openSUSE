#
# spec file for package sigil
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


%define sigil_doc_version 2019.09.03
Name:           sigil
Version:        1.3.0
Release:        0
Summary:        WYSIWYG Ebook Editor
License:        GPL-3.0-only
Group:          Productivity/Other
URL:            https://sigil-ebook.com/
Source0:        https://github.com/Sigil-Ebook/Sigil/archive/%{version}/%{name}-%{version}.tar.gz
Source1:        https://github.com/Sigil-Ebook/Sigil/raw/master/docs/Sigil_User_Guide_%{sigil_doc_version}.epub
Source2:        %{name}.desktop
# PATCH-FIX-OPENSUSE Disabled __DATE__ and __TIME__ which is replaced later in pre section
Patch0:         %{name}-gt-0.9.0-Dialogs-About.cpp.patch
BuildRequires:  boost-devel
BuildRequires:  cmake >= 3.0
BuildRequires:  dos2unix
BuildRequires:  fdupes
BuildRequires:  gcc-c++
# upstream use Qt 5.12.3
BuildRequires:  libqt5-qtbase-devel >= 5.4.2
BuildRequires:  libqt5-qtlocation-devel >= 5.4.2
BuildRequires:  libstdc++-devel
BuildRequires:  libxerces-c-devel
BuildRequires:  libxml2-devel
BuildRequires:  libxslt-devel
BuildRequires:  make
BuildRequires:  pkgconfig
# not need for build, only check for exists
# upstream use for python3-Pillow 7.1.2
BuildRequires:  python3-Pillow >= 5.0.0
# upstream use python3-certifi 2020.6.20
BuildRequires:  python3-certifi
# upstream use python3-chardet 3.0.4
BuildRequires:  python3-chardet >= 3.0.4
# upstream use python3-css-parser 1.0.4
BuildRequires:  python3-css-parser >= 1.0.4
# upstream use python3-cssselect 1.1.0
BuildRequires:  python3-cssselect >= 1.0.3
# upstream use python3-cssutils ?
BuildRequires:  python3-cssutils >= 1.0.2
# upstream use 3.7.2
BuildRequires:  python3-devel >= 3.4
# upstream use python3-dulwich 0.20.5
BuildRequires:  python3-dulwich >= 0.20.2
# upstream use python3-html5lib >= 1.1
BuildRequires:  python3-html5lib
# upstream use for python3-lxml 4.5.1
BuildRequires:  python3-lxml >= 4.4.2
# upstream use for python3-qt5 5.12.3
BuildRequires:  python3-qt5
# upstream use for python3-regex 2020.6.8
BuildRequires:  python3-regex
# upstream use for python3-six 1.15.0
BuildRequires:  python3-six >= 1.14.0
# upstream use for python3-urllib3 1.25.9
BuildRequires:  python3-urllib3 >= 1.24
# upstream use python3-tk ?
BuildRequires:  python3-tk
BuildRequires:  unzip
BuildRequires:  update-desktop-files
BuildRequires:  zlib-devel
BuildRequires:  pkgconfig(Qt5Concurrent)
BuildRequires:  pkgconfig(Qt5Multimedia)
BuildRequires:  pkgconfig(Qt5PrintSupport)
BuildRequires:  pkgconfig(Qt5Svg)
BuildRequires:  pkgconfig(Qt5UiTools)
BuildRequires:  pkgconfig(Qt5WebChannel)
#BuildRequires:  pkgconfig(Qt5WebKit)
BuildRequires:  pkgconfig(Qt5WebEngine)
BuildRequires:  pkgconfig(Qt5WebKitWidgets)
BuildRequires:  pkgconfig(Qt5Xml)
BuildRequires:  pkgconfig(Qt5XmlPatterns)
BuildRequires:  pkgconfig(hunspell)
BuildRequires:  pkgconfig(libpcre)
BuildRequires:  pkgconfig(libusb-1.0)
BuildRequires:  pkgconfig(minizip)
Requires:       python3-Pillow
Requires:       python3-certifi
Requires:       python3-chardet
Requires:       python3-css-parser
Requires:       python3-cssselect
Requires:       python3-cssutils
Requires:       python3-dulwich
Requires:       python3-html5lib
Requires:       python3-lxml
Requires:       python3-regex
Requires:       python3-six
Requires:       python3-tk
Requires:       python3-urllib3

%description
Sigil is an editor for the EPUB format. It is designed for WYSIWYG
editing of EPUB files and for converting other formats to EPUB. It
also provides support for direct XHTML, CSS and XPGT editing. You can
use it to add any of the metadata entries supported by the EPUB
specification and create a hierarchical Table of Contents.

%prep
%setup -q -n Sigil-%{version}
%patch0 -p 1
cp -v %{SOURCE1} .
cp -v %{SOURCE2} .
# rpmlint

#FIXME MANUAL UPDATE OF DATE REQUIRED HERE!!!!
# Fix "Your file uses  __DATE and __TIME__ this causes the package to rebuild
# when not needed warning"
# http://sourceforge.net/tracker/?func=detail&atid=102439&aid=3314371&group_id=2439
#
# We use the ChangeLog date
_date=$(date -u -r ChangeLog.txt -I)
_time=$(date -u -r ChangeLog.txt +%%T)
# Change it:
find . -type f -name About.cpp -exec sed -i "s/@DATE@/$_date/;s/@TIME@/$_time/g" {} +

sed -i 's/\r//' ChangeLog.txt README.md COPYING.txt
dos2unix src/Resource_Files/python3lib/meta*.py
dos2unix src/Resource_Files/python3lib/opf_*.py
# rpmlint:
find . -type f -exec sed -i -e 's|#!\/usr\/bin\/env python3|#!\/usr\/bin\/python3|g' {} +
find . -type f -exec sed -i -e 's|#!\/usr\/bin\/env python|#!\/usr\/bin\/python3|g' {} +

%build
export CFLAGS="%{optflags} -fno-strict-aliasing"
export CXXFLAGS="$CFLAGS"

# FIXME: you should use %%cmake macros
# With SYSTEM_LIBS=1 package does not build
cmake -G "Unix Makefiles" \
   -DCMAKE_INSTALL_PREFIX=%{_prefix} \
   -DUSE_SYSTEM_LIBS=0 \
   -DCMAKE_BUILD_TYPE=Release .

%make_build

%install
%make_install

# create a .desktop file:
mkdir -p %{buildroot}%{_datadir}/applications

# install icons for the .desktop file
install -m644 -D src/Resource_Files/icon/app_icon_16.png %{buildroot}%{_datadir}/icons/hicolor/16x16/apps/sigil.png
install -m644 -D src/Resource_Files/icon/app_icon_32.png %{buildroot}%{_datadir}/icons/hicolor/32x32/apps/sigil.png
install -m644 -D src/Resource_Files/icon/app_icon_48.png %{buildroot}%{_datadir}/icons/hicolor/48x48/apps/sigil.png
install -m644 -D src/Resource_Files/icon/app_icon_128.png %{buildroot}%{_datadir}/icons/hicolor/128x128/apps/sigil.png
install -m644 -D src/Resource_Files/icon/app_icon_256.png %{buildroot}%{_datadir}/icons/hicolor/256x256/apps/sigil.png
install -m644 %{name}.desktop %{buildroot}%{_datadir}/applications/%{name}.desktop

%suse_update_desktop_file %{name}
%fdupes -s %{buildroot}

# fix rpmlint: non-executable-script
pushd %{buildroot}%{_datadir}
grep -lr "%{_bindir}/python" | xargs chmod +x
popd

%files
%license COPYING.txt
%doc ChangeLog.txt README.md Sigil_User_Guide_%{sigil_doc_version}.epub
%{_bindir}/%{name}
%{_datadir}/applications/%{name}.desktop
%dir %{_datadir}/icons/hicolor/
%dir %{_datadir}/icons/hicolor/16x16
%dir %{_datadir}/icons/hicolor/16x16/apps
%dir %{_datadir}/icons/hicolor/32x32
%dir %{_datadir}/icons/hicolor/32x32/apps
%dir %{_datadir}/icons/hicolor/48x48
%dir %{_datadir}/icons/hicolor/48x48/apps
%dir %{_datadir}/icons/hicolor/128x128
%dir %{_datadir}/icons/hicolor/128x128/apps
%dir %{_datadir}/icons/hicolor/256x256
%dir %{_datadir}/icons/hicolor/256x256/apps
%{_datadir}/icons/hicolor/*/apps/*.png
%{_datadir}/pixmaps/*.png
%dir %{_datadir}/%{name}
%dir %{_datadir}/%{name}/translations
%{_datadir}/%{name}/translations/*
%dir %{_datadir}/%{name}/*dictionaries
%{_datadir}/%{name}/*dictionaries/*
%{_datadir}/%{name}/examples
%{_datadir}/%{name}/python3lib
%{_datadir}/%{name}/polyfills
%{_datadir}/%{name}/plugin_launchers
%dir %{_libdir}/%{name}
%{_libdir}/%{name}/*

%changelog
