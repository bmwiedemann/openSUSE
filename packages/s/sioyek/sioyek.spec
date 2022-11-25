#
# spec file for package sioyek
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


Name:           sioyek
Version:        1.5.0
Release:        0
Summary:        PDF Viewer for research papers and technical books
License:        GPL-3.0-or-later
Group:          Productivity/Office/Other
URL:            https://github.com/ahrm/sioyek
Source0:        https://github.com/ahrm/sioyek/archive/refs/tags/v%{version}.tar.gz#/%{name}-%{version}.tar.gz
Patch0:         0000-mupdf-1.20-compat-issue.patch
Patch1:         0001-parse-mupdf-1.20-links.patch
BuildRequires:  c++_compiler
BuildRequires:  binutils
BuildRequires:  libQt5Gui-devel
BuildRequires:  libQt5OpenGL-devel
BuildRequires:  libQt5OpenGLExtensions-devel-static
BuildRequires:  libqt5-qt3d-devel
BuildRequires:  libqt5-qt3d-tools
BuildRequires:  libqt5-qtbase-common-devel
BuildRequires:  mupdf-devel-static
BuildRequires:  openjpeg2-devel
BuildRequires:  pkgconfig(freetype2)
BuildRequires:  pkgconfig(gumbo)
BuildRequires:  pkgconfig(harfbuzz)
BuildRequires:  pkgconfig(jbig2dec)
BuildRequires:  pkgconfig(libjpeg)
BuildRequires:  pkgconfig(mujs)
BuildRequires:  pkgconfig(zlib)

%description
Sioyek is a PDF viewer designed for reading research papers and technical books.

%prep
%autosetup -p1

%build
# We really cannot use the qt5 macros here because the builds fail
# RPM build flags cannot really be used here also since they make the builds fail
export QMAKE=/usr/bin/qmake-qt5
$QMAKE  pdf_viewer_build_config.pro
%make_build

%install
# The install paths in the config file does not correspond to
# the usual paths of installation in openSUSE
mkdir -p %{buildroot}%{_datadir}/%{name}/shaders/
cp -v pdf_viewer/shaders/* %{buildroot}%{_datadir}/%{name}/shaders/

install -Dm755 %{name} -t "%{buildroot}%{_bindir}/"

install -Dm644 pdf_viewer/prefs.config -t "%{buildroot}%{_sysconfdir}/%{name}/"
install -Dm644 pdf_viewer/keys.config -t "%{buildroot}%{_sysconfdir}/%{name}/"
install -Dm644 resources/%{name}-icon-linux.png -t "%{buildroot}%{_datadir}/icons/pixmaps/"
install -Dm644 resources/%{name}.desktop -t "%{buildroot}%{_datadir}/applications/"
install -Dm644 resources/%{name}.1 -t "%{buildroot}%{_mandir}/man1/"

install -Dm644 tutorial.pdf -t "%{buildroot}%{_datadir}/%{name}/"

%files
%{_bindir}/%{name}
%{_datadir}/applications/%{name}.desktop
%{_mandir}/man1/%{name}.1%{?ext_man}

%dir %{_datadir}/%{name}
%{_datadir}/%{name}/*
%dir %{_datadir}/icons/pixmaps
%{_datadir}/icons/pixmaps/%{name}-icon-linux.png

%dir %{_sysconfdir}/%{name}
%config(noreplace) %{_sysconfdir}/%{name}/prefs.config
%config(noreplace) %{_sysconfdir}/%{name}/keys.config

%license LICENSE
%doc README.md

%changelog

