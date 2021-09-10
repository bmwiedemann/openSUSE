#
# spec file for package liblcf
#
# Copyright (c) 2021 SUSE LLC
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


Name:           liblcf
Version:        0.6.2
Release:        0
Summary:        RPG Maker 2000/2003 and EasyRPG game data library
License:        MIT
Group:          System/Libraries

URL:            https://easyrpg.org
Source0:        https://github.com/EasyRPG/%{name}/archive/%{version}.tar.gz#/%{name}-%{version}.tar.gz

BuildRequires:  cmake
BuildRequires:  doxygen
BuildRequires:  gcc-c++
BuildRequires:  libtool
BuildRequires:  pkgconfig
BuildRequires:  pkgconfig(expat)
BuildRequires:  pkgconfig(icu-i18n)

%description
liblcf is a library to handle RPG Maker 2000/2003 and EasyRPG game data.
It can read and write LCF and XML files.

%package -n liblcf0
Summary:        RPG Maker 2000/2003 and EasyRPG game data library
Group:          System/Libraries

%description -n liblcf0
liblcf is a library to handle RPG Maker 2000/2003 and EasyRPG game data.
It can read and write LCF and XML files.

%package -n liblcf0-devel
Summary:        RPG Maker 2000/2003 and EasyRPG game data library - development files
Group:          Development/Libraries/C and C++
Requires:       liblcf0 = %{version}

%description -n liblcf0-devel
liblcf is a library to handle RPG Maker 2000/2003 and EasyRPG game data.
It can read and write LCF and XML files.

%prep
%setup -q

%build
%cmake -DDISABLE_UPDATE_MIMEDB=ON
%cmake_build

%install
%cmake_install

%post -n liblcf0 -p /sbin/ldconfig

%postun -n liblcf0 -p /sbin/ldconfig

%files -n liblcf0
%doc README.md AUTHORS.md
%license COPYING
%{_libdir}/liblcf.so.*
%{_datadir}/mime/packages/liblcf.xml

%files -n liblcf0-devel
%{_includedir}/liblcf
%{_libdir}/liblcf.so
%{_libdir}/pkgconfig/liblcf.pc
%{_libdir}/cmake
%{_libdir}/cmake/liblcf

%changelog
