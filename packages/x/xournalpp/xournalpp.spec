#
# spec file for package xournalpp
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


Name:           xournalpp
Version:        1.0.18
Release:        0
Summary:        Notetaking software designed around a tablet
License:        GPL-2.0-or-later
Group:          Productivity/Office/Other
URL:            https://github.com/xournalpp/xournalpp
Source0:        https://github.com/xournalpp/xournalpp/archive/%{version}.tar.gz#/%{name}-%{version}.tar.gz
# PATCH-FIX-UPSTREAM xournalpp-fix-desktop-categories.patch badshah400@gmail.com -- Fix desktop categories with additional keywords to prevent "No sufficient Category definition" error from brp-desktop.
Patch0:         xournalpp-fix-desktop-categories.patch
# PATCH-FIX-UPSTREAM xournalpp-fix-exporting-pdf-with-references.patch gh#xournalpp/xournalpp#2236 badshah400@gmail.com -- Fix PDF export when references exist in the document.
Patch1:         xournalpp-fix-exporting-pdf-with-references.patch
BuildRequires:  cmake
BuildRequires:  fdupes
BuildRequires:  gcc-c++
BuildRequires:  hicolor-icon-theme
BuildRequires:  pkgconfig
BuildRequires:  texlive-latex-bin
BuildRequires:  pkgconfig(glib-2.0)
BuildRequires:  pkgconfig(gthread-2.0)
BuildRequires:  pkgconfig(gtk+-3.0)
BuildRequires:  pkgconfig(libxml-2.0)
BuildRequires:  pkgconfig(libzip)
BuildRequires:  pkgconfig(poppler-glib)
BuildRequires:  pkgconfig(portaudiocpp)
BuildRequires:  pkgconfig(sndfile)
BuildRequires:  pkgconfig(zlib)
Recommends:     tex(standalone.tex)

%description
Xournal++ is a hand note taking software.
It supports pen input, e.g. Wacom tablets.

%lang_package

%prep
%setup -q
%patch0 -p1
%patch1 -p1

%build
%cmake

%install
%cmake_install

# REMOVE UNNECESSARY SCRIPTS update-icon-cache IS TAKEN CARE OF BY RPM FILE TRIGGERS
rm %{buildroot}%{_datadir}/%{name}/ui/*/hicolor/update-icon-cache.sh

%find_lang xournalpp %{no_lang_C}

%fdupes %{buildroot}%{_datadir}

%files
%license LICENSE
%doc AUTHORS README.md
%{_bindir}/xournal-thumbnailer
%{_bindir}/xournalpp
%{_datadir}/applications/*.xournalpp.desktop
%{_datadir}/icons/hicolor/scalable/mimetypes/*.svg
%{_datadir}/mime/packages/*.xml
%dir %{_datadir}/metainfo
%{_datadir}/metainfo/*.appdata.xml
%dir %{_datadir}/mimelnk
%dir %{_datadir}/mimelnk/application
%{_datadir}/mimelnk/application/*.desktop
%{_datadir}/xournalpp/
%{_datadir}/icons/hicolor/*/apps/*
%dir %{_datadir}/thumbnailers
%{_datadir}/thumbnailers/*.thumbnailer

%files lang -f xournalpp.lang

%changelog
