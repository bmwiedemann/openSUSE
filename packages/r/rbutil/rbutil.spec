#
# spec file for package rbutil
#
# Copyright (c) 2025 SUSE LLC
# Copyright (c) 2018-2025, Martin Hauke <mardnh@gmx.de>
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


Name:           rbutil
Version:        1.5.1
Release:        0
Summary:        Rockbox Firmware Manager
License:        GPL-2.0-only
Group:          Hardware/Other
URL:            https://www.rockbox.org/wiki/RockboxUtility
#Git-Clone:     https://git.rockbox.org/cgit/rockbox.git
Source:         rockbox-rbutil-%{version}.tar.xz
Patch0:         rbutil-no-themeeditor.patch
Patch1:         rbutil-fix-versionstring.patch
BuildRequires:  cmake
BuildRequires:  pkgconfig
BuildRequires:  pkgconfig(Qt6Core)
BuildRequires:  pkgconfig(Qt6Core5Compat)
BuildRequires:  pkgconfig(Qt6Linguist)
BuildRequires:  pkgconfig(Qt6Multimedia)
BuildRequires:  pkgconfig(Qt6Network)
BuildRequires:  pkgconfig(Qt6Svg)
BuildRequires:  pkgconfig(Qt6Test)
BuildRequires:  pkgconfig(Qt6Widgets)
BuildRequires:  pkgconfig(bzip2)
BuildRequires:  pkgconfig(libusb-1.0)
BuildRequires:  pkgconfig(speex)
BuildRequires:  pkgconfig(zlib)
%if 0%{?sle_version} >= 150500 && 0%{?sle_version} < 160000 && 0%{?is_opensuse}
BuildRequires:  gcc12
BuildRequires:  gcc12-c++
%else
BuildRequires:  gcc
BuildRequires:  gcc-c++
%endif

%description
Firmware manager for Rockbox MP3 players.

%prep
%autosetup -p1 -n rockbox-rbutil-%{version}
rm -Rv utils/rbutilqt/zlib

%build
%if 0%{?sle_version} >= 150500 && 0%{?sle_version} < 160000 && 0%{?is_opensuse}
export CC="gcc-12"
export CXX="g++-12"
%endif
#
cd utils
%cmake \
  -DCMAKE_SKIP_RPATH=ON \
  -DBUILD_SHARED_LIBS=OFF
%cmake_build

%install
install -Dm 0755 utils/build/rbutilqt/RockboxUtility %{buildroot}%{_bindir}/RockboxUtility
install -Dm 0644 utils/rbutilqt/RockboxUtility.desktop %{buildroot}%{_datadir}/applications/RockboxUtility.desktop
install -Dm 0644 docs/logo/rockbox-clef.svg %{buildroot}%{_datadir}/pixmaps/rockbox-clef.svg

%check
cd utils
%ctest --exclude-regex TestHttpGet

%files
%license docs/COPYING
%doc utils/rbutilqt/changelog.txt
%{_bindir}/RockboxUtility
%{_datadir}/applications/RockboxUtility.desktop
%{_datadir}//pixmaps/rockbox-clef.svg

%changelog
