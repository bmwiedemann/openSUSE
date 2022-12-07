#
# spec file for package libbluray
#
# Copyright (c) 2022 SUSE LLC
# Copyright (c) 2011 Dominique Leuenberger, Amsterdam, The Netherlands
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


%define         sover 2
Name:           libbluray
Version:        1.3.4
Release:        0
Summary:        Library to access Blu-Ray disk
License:        LGPL-2.1-or-later
Group:          Productivity/Multimedia/Other
URL:            https://www.videolan.org/developers/libbluray.html
Source0:        https://download.videolan.org/pub/videolan/%{name}/%{version}/%{name}-%{version}.tar.bz2
Source99:       baselibs.conf
Patch0:         libbluray-pkgconfig.patch
BuildRequires:  ant
BuildRequires:  java-devel >= 1.8
BuildRequires:  libtool
BuildRequires:  pkgconfig
BuildRequires:  pkgconfig(fontconfig)
BuildRequires:  pkgconfig(freetype2)
BuildRequires:  pkgconfig(libxml-2.0) >= 2.6

%description
This library is written for the purpose of playing Blu-ray movies. It is
intended for software that want to support Blu-ray playback (such as VLC and
MPlayer). We, the authors of this library, do not condone nor endorse piracy.

%package -n libbluray%{sover}
Summary:        Library to access Blu-Ray disk
Group:          System/Libraries

%description -n libbluray%{sover}
This library is written for the purpose of playing Blu-ray movies. It is
intended for software that want to support Blu-ray playback (such as VLC and
MPlayer). We, the authors of this library, do not condone nor endorse piracy.

%package tools
Summary:        Library to access Blu-Ray disk - Utilities
Group:          Productivity/Multimedia/Other

%description tools
This library is written for the purpose of playing Blu-ray movies. It is
intended for software that want to support Blu-ray playback (such as VLC and
MPlayer). We, the authors of this library, do not condone nor endorse piracy.

%package devel
Summary:        Library to access Blu-Ray disks - Development files
Group:          Development/Languages/C and C++
Requires:       libbluray%{sover} = %{version}

%description devel
This library is written for the purpose of playing Blu-ray movies. It is
intended for software that want to support Blu-ray playback (such as VLC and
MPlayer). We, the authors of this library, do not condone nor endorse piracy.

%package bdj
Summary:        Library to access Blu-Ray disk - BD-J support
Group:          Development/Libraries/Java
Requires:       jpackage-utils
%if %{?pkg_vcmp:%pkg_vcmp java-devel >= 9}%{!?pkg_vcmp:0}
Requires:       java >= 9
%else
Requires:       java >= 1.8
%endif
%if 0%{?suse_version} > 1110
BuildArch:      noarch
%endif

%description bdj
This library is written for the purpose of playing Blu-ray movies. It is
intended for software that want to support Blu-ray playback (such as VLC and
MPlayer). We, the authors of this library, do not condone nor endorse piracy.

%prep
%autosetup -p1

%build
%configure \
    --disable-static \
    --enable-bdjava \
    --enable-udf
%make_build

%install
%make_install
find %{buildroot} -type f -name "*.la" -delete -print

%post -n libbluray%{sover} -p /sbin/ldconfig
%postun -n libbluray%{sover} -p /sbin/ldconfig

%files tools
%{_bindir}/bd_info
%{_bindir}/bd_list_titles
%{_bindir}/bd_splice

%files -n libbluray%{sover}
%license COPYING
%{_libdir}/libbluray.so.*

%files devel
%{_includedir}/%{name}/
%{_libdir}/libbluray.so
%{_libdir}/pkgconfig/libbluray.pc

%files bdj
%{_javadir}/libbluray-awt-j2se-%{version}.jar
%{_javadir}/libbluray-j2se-%{version}.jar

%changelog
