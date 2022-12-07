#
# spec file for package xournalpp
#
# Copyright (c) 2022 SUSE LLC
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


Name:           xournalpp
Version:        1.1.3
Release:        0
Summary:        Notetaking software designed around a tablet
License:        GPL-2.0-or-later
Group:          Productivity/Office/Other
URL:            https://github.com/xournalpp/xournalpp
Source0:        https://github.com/xournalpp/xournalpp/archive/refs/tags/v%{version}.tar.gz#/%{name}-%{version}.tar.gz
BuildRequires:  cmake
BuildRequires:  fdupes
BuildRequires:  hicolor-icon-theme
BuildRequires:  pkgconfig
BuildRequires:  texlive-latex-bin
BuildRequires:  update-desktop-files
BuildRequires:  pkgconfig(glib-2.0)
BuildRequires:  pkgconfig(gthread-2.0)
BuildRequires:  pkgconfig(gtk+-3.0)
BuildRequires:  pkgconfig(librsvg-2.0)
BuildRequires:  pkgconfig(libxml-2.0)
BuildRequires:  pkgconfig(libzip)
BuildRequires:  pkgconfig(lua)
BuildRequires:  pkgconfig(poppler-glib)
BuildRequires:  pkgconfig(portaudiocpp)
BuildRequires:  pkgconfig(sndfile)
BuildRequires:  pkgconfig(zlib)
Recommends:     webp-pixbuf-loader
Recommends:     tex(scontents.tex)
Recommends:     tex(standalone.tex)
%if 0%{?suse_version} < 1550
BuildRequires:  gcc9-c++
%else
BuildRequires:  gcc-c++
%endif

%description
Xournal++ is a hand note taking software.
It supports pen input, e.g. Wacom tablets.

%lang_package

%prep
%autosetup -p1

%build
%cmake -DENABLE_MATHTEX=ON \
%if 0%{?suse_version} < 1550
       -DCMAKE_CXX_COMPILER="%{_bindir}/g++-9" \
%endif
       %{nil}
%cmake_build

%install
%cmake_install
%find_lang xournalpp %{no_lang_C}

%fdupes %{buildroot}%{_datadir}

%files
%license LICENSE
%doc AUTHORS README.md
%{_bindir}/xournalpp-thumbnailer
%{_bindir}/xournalpp
%{_datadir}/applications/*.desktop
%{_datadir}/icons/hicolor/scalable/mimetypes/*.svg
%{_datadir}/icons/hicolor/*/apps/*
%{_datadir}/metainfo/*.appdata.xml
%{_datadir}/mime/packages/*.xml
%dir %{_datadir}/mimelnk
%dir %{_datadir}/mimelnk/application
%{_datadir}/mimelnk/application/*.desktop
%dir %{_datadir}/thumbnailers
%{_datadir}/thumbnailers/*.thumbnailer
%{_datadir}/xournalpp/

%files lang -f xournalpp.lang

%changelog
