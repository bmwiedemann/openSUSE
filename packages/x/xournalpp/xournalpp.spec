#
# spec file for package xournalpp
#
# Copyright (c) 2026 SUSE LLC and contributors
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
Version:        1.3.2
Release:        0
Summary:        Notetaking software designed around a tablet
License:        GPL-2.0-or-later
Group:          Productivity/Office/Other
URL:            https://github.com/xournalpp/xournalpp
Source0:        https://github.com/xournalpp/xournalpp/archive/refs/tags/v%{version}.tar.gz#/%{name}-%{version}.tar.gz
BuildRequires:  cmake
BuildRequires:  fdupes
BuildRequires:  gcc-c++
BuildRequires:  help2man
BuildRequires:  hicolor-icon-theme
BuildRequires:  pkgconfig
BuildRequires:  texlive-latex-bin
BuildRequires:  pkgconfig(glib-2.0)
BuildRequires:  pkgconfig(gthread-2.0)
BuildRequires:  pkgconfig(gtk+-3.0)
BuildRequires:  pkgconfig(gtksourceview-4)
BuildRequires:  pkgconfig(libqpdf) >= 10.6.0
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

%description
Xournal++ is a hand note taking software.
It supports pen input, e.g. Wacom tablets.

%lang_package

%prep
%autosetup -p1

%build
%cmake \
  -DDISTRO_CODENAME="openSUSE Linux" \
  -DENABLE_CPPTRACE=OFF \
  -DMAN_COMPRESS=OFF \
  %{nil}
%cmake_build

%install
%cmake_install
%find_lang xournalpp %{no_lang_C}
%fdupes %{buildroot}%{_datadir}

%files
%license LICENSE
%doc AUTHORS README.md
%{_bindir}/xournalpp
%{_bindir}/xournalpp-thumbnailer
%{_bindir}/xournalpp-wrapper
%{_datadir}/applications/*.desktop
%{_datadir}/icons/hicolor/scalable/mimetypes/*.svg
%{_datadir}/icons/hicolor/*/apps/*
%{_datadir}/metainfo/*.appdata.xml
%{_datadir}/mime/packages/*.xml
%dir %{_datadir}/thumbnailers
%{_datadir}/thumbnailers/*.thumbnailer
%{_datadir}/xournalpp/
%{_mandir}/man1/xournalpp*.1%{?ext_man}

%files lang -f xournalpp.lang

%changelog
