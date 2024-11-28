#
# spec file for package pentobi
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


Name:           pentobi
Version:        25.2
Release:        0
Summary:        Program to play the board game Blokus
License:        GPL-3.0-only
Group:          Amusements/Games/Strategy/Other
URL:            https://pentobi.sourceforge.net/
Source:         https://downloads.sourceforge.net/%{name}/%{name}-%{version}.tar.xz
BuildRequires:  cmake >= 3.18
BuildRequires:  docbook-xsl-stylesheets
BuildRequires:  extra-cmake-modules
BuildRequires:  itstool
BuildRequires:  kio-devel
BuildRequires:  libxslt-tools
BuildRequires:  pkgconfig
BuildRequires:  qt6-linguist-devel
BuildRequires:  rsvg-convert
BuildRequires:  pkgconfig(Qt6Concurrent)
BuildRequires:  pkgconfig(Qt6Core) >= 6.4
BuildRequires:  pkgconfig(Qt6QuickControls2)
BuildRequires:  pkgconfig(Qt6WebView)
BuildRequires:  pkgconfig(Qt6Widgets)
BuildRequires:  pkgconfig(appstream)
Requires(post): hicolor-icon-theme
Requires(post): update-desktop-files
Requires(postun): hicolor-icon-theme
Requires(postun): update-desktop-files
# unresolvable: nothing provides pkgconfig(Qt6WebView)
ExclusiveArch:  x86_64 aarch64
%if 0%{?sle_version} >= 150500 && 0%{?sle_version} < 160000 && 0%{?is_opensuse}
BuildRequires:  gcc12
BuildRequires:  gcc12-c++
%else
BuildRequires:  gcc-c++
%endif

%description
Pentobi is a computer opponent for the board game Blokus with
support for Classic, Duo, Junior, Trigon, and Nexos game variants.
Different levels of playing strength are available. Pentobi can
save and load games along with comments and move variations.

%prep
%setup -q

%build
%if 0%{?sle_version} >= 150500 && 0%{?sle_version} < 160000 && 0%{?is_opensuse}
export CC="gcc-12"
export CXX="g++-12"
%endif
%cmake -DCMAKE_BUILD_TYPE=Release -DCMAKE_SKIP_INSTALL_RPATH:BOOL=ON .
%make_jobs VERBOSE=1

%install
%cmake_install

%files
%license LICENSE.md
%doc AUTHORS.md NEWS.md README.md
%{_bindir}/pentobi
%{_datadir}/applications/io.sourceforge.pentobi.desktop
%{_datadir}/icons/hicolor/*/*/*
%{_datadir}/mime/packages/*.xml
%{_datadir}/metainfo/io.sourceforge.pentobi.appdata.xml

%changelog
