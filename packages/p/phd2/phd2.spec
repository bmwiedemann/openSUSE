#
# spec file for package phd2.spec
#
# Copyright (c) 2019 SUSE LLC
# Copyright (c) 2019-2020 Malcolm J Lewis <malcolmlewis@opensuse.org>
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


Name:           phd2
Version:        2.6.9
Release:        0
Summary:        Telescope guiding software
License:        BSD-3-Clause
Group:          Productivity/Scientific/Astronomy
URL:            https://openphdguiding.org
Source0:        %{name}-%{version}.tar.xz
BuildRequires:  cmake
BuildRequires:  gcc-c++
BuildRequires:  hicolor-icon-theme
BuildRequires:  libnova-devel
BuildRequires:  pkgconfig
BuildRequires:  update-desktop-files
BuildRequires:  wxGTK3-devel >= 3.0
BuildRequires:  pkgconfig(cfitsio)
BuildRequires:  pkgconfig(eigen3)
BuildRequires:  pkgconfig(libcurl)
BuildRequires:  pkgconfig(libindi)
BuildRequires:  pkgconfig(libusb-1.0)
BuildRequires:  pkgconfig(zlib)

%description
Telescope guiding software that simplifies the process of tracking a guide star,
letting you concentrate on other aspects of deep-sky imaging or spectroscopy.

%lang_package

%prep
%setup -q

%build
%cmake \
    -DCMAKE_BUILD_Type=Release \
    ..
%cmake_build

%install
%cmake_install
%suse_update_desktop_file %{name}
%find_lang %{name} %{?no_lang_C}

%files
%doc README.txt
%license LICENSE.txt
%{_bindir}/phd2
%{_bindir}/phd2.bin
%{_datadir}/applications/phd2.desktop
%dir /usr/lib/phd2/
/usr/lib/phd2/libtoupcam.so
%dir %{_datadir}/metainfo
%{_datadir}/metainfo/phd2.appdata.xml
%{_datadir}/phd2/
%{_datadir}/pixmaps/phd2.png

%files lang -f %{name}.lang

%changelog
