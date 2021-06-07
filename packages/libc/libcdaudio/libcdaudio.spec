#
# spec file for package libcdaudio
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


%define lname   libcdaudio1
Name:           libcdaudio
Version:        0.99.12p2
Release:        0
Summary:        Functions to Control Operation of a CD-ROM When Playing Audio CDs
License:        GPL-2.0-or-later
Group:          Productivity/Multimedia/CD/Grabbers
URL:            http://libcdaudio.sourceforge.net/
Source:         https://sourceforge.net/projects/libcdaudio/files/libcdaudio/%{version}/libcdaudio-%{version}.tar.gz
Source98:       baselibs.conf
Patch0:         libcdaudio-max_matches.diff
Patch1:         libcdaudio-libdir.diff
Patch2:         libcdaudio-buffer-overflow.diff
Patch3:         libcdaudio-double_free.diff
Patch4:         libcdaudio-closedir.diff
Patch5:         libcdaudio-fclose.patch
Patch6:         libcdaudio-getmntinfo.patch
BuildRequires:  pkgconfig

%description
libcdaudio is a library providing functions to control
operation of a CD-ROM when playing audio CDs.  It also contains
functions for CDDB and CD index lookup.

%package -n %{lname}
Summary:        Functions to control oepration of a CD-ROM while playing audio CDs
# O/P added in 12.3
Group:          System/Libraries
Provides:       %{name} = %{version}-%{release}
Obsoletes:      %{name} < %{version}-%{release}

%description -n %{lname}
libcdaudio is a library providing functions to control
operation of a CD-ROM when playing audio CDs.  It also contains
functions for CDDB and CD index lookup.

%package devel
Summary:        Header files for libcdaudio, a library to control operation of a CD-DA
Group:          Development/Libraries/C and C++
Requires:       %{lname} = %{version}

%description devel
libcdaudio is a library providing functions to control
operation of a CD-ROM when playing audio CDs.  It also contains
functions for CDDB and CD Index lookup.

%prep
%autosetup -p0

%build
%configure --disable-static
%make_build -k

%install
%make_install
find %{buildroot} -type f -name "*.la" -delete -print

%post -n %{lname} -p /sbin/ldconfig
%postun -n %{lname} -p /sbin/ldconfig

%files -n %{lname}
%license COPYING
%{_libdir}/libcdaudio.so.1*

%files devel
%doc README
%{_bindir}/libcdaudio-config
%{_includedir}/cdaudio.h
%{_libdir}/pkgconfig/libcdaudio.pc
%{_datadir}/aclocal/libcdaudio.m4
%{_libdir}/libcdaudio.so

%changelog
