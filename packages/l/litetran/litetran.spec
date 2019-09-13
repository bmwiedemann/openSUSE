#
# spec file for package litetran
#
# Copyright (c) 2018 SUSE LINUX GmbH, Nuernberg, Germany.
#
# All modifications and additions to the file contributed by third parties
# remain the property of their copyright owners, unless otherwise agreed
# upon. The license for this file, and modifications and additions to the
# file, is the same license as for the pristine package itself (unless the
# license for the pristine package is not an Open Source License, in which
# case the license is the MIT License). An "Open Source License" is a
# license that conforms to the Open Source Definition (Version 1.9)
# published by the Open Source Initiative.

# Please submit bugfixes or comments via http://bugs.opensuse.org/
#


Name:           litetran
Version:        1.3+git20161111
Release:        0
Summary:        A translator on Qt
License:        GPL-3.0-or-later
Group:          Productivity/Networking/Web/Frontends
URL:            https://bitbucket.org/gfarniev/litetran
Source:         %{name}-%{version}.tar.xz
# PATCH-FIX-OPENSUSE litetran-fix-qt-5.11.patch -- Fix Qt 5.11+ compatibility.
Patch0:         %{name}-fix-qt-5.11.patch
BuildRequires:  cmake
BuildRequires:  libqt5-linguist-devel
BuildRequires:  pkgconfig
BuildRequires:  update-desktop-files
BuildRequires:  pkgconfig(Qt5Gui) >= 5.2
BuildRequires:  pkgconfig(Qt5Multimedia) >= 5.2
BuildRequires:  pkgconfig(Qt5Network) >= 5.2
BuildRequires:  pkgconfig(Qt5Widgets) >= 5.2
BuildRequires:  pkgconfig(Qt5X11Extras) >= 5.2

%description
LiteTran is a GUI for text translation (like Yandex.Translate).

 * Translate by text selection: select text, press the key combination
   (Ctrl+Shift+T by default), and get the translation result in
   a pop-up. It will not be necessary to open a web browser for
   translation.
 * Text speech (up to 100 characters).
 * 37 supported languages.

%prep
%setup -q
%patch0 -p1

%build
%cmake
make %{?_smp_mflags} V=1

%install
%cmake_install

%if 0%{?suse_version} < 1500
%post
%desktop_database_post

%postun
%desktop_database_postun
%endif

%files
%if 0%{?suse_version} >= 1500
%license LICENSE.txt
%else
%doc LICENSE.txt
%endif
%doc README.md RELNOTES.txt
%{_bindir}/%{name}
%{_datadir}/%{name}/
%{_datadir}/applications/%{name}.desktop
%{_datadir}/pixmaps/%{name}.png

%changelog
