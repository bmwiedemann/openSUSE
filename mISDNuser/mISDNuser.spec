#
# spec file for package mISDNuser
#
# Copyright (c) 2017 SUSE LINUX GmbH, Nuernberg, Germany.
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


Name:           mISDNuser
Version:        2.1.0
Release:        0
Summary:        Tools and library for mISDN
License:        GPL-2.0 and LGPL-2.1
Group:          Hardware/ISDN
Url:            http://misdn.org/

#Changelog:	http://misdn.org/index.php/MISDN_Release_Notes
# There seem to be no tarballs. Hence generated from git.
Source:         %name-%version.tar.xz
BuildRequires:  autoconf >= 2.63
BuildRequires:  automake
BuildRequires:  libtool >= 2
BuildRequires:  xz
BuildRoot:      %{_tmppath}/%{name}-%{version}-build

%description
This package contains libmisdn and some tools to use the mISDN driver.
mISDN is the new modular ISDN driver for Linux.

%package -n libmisdn1
Summary:        mISDN core library
Group:          System/Libraries

%description -n libmisdn1
The mISDN core library.

%package devel
Summary:        C header files for mISDN
Group:          Development/Libraries/C and C++
Requires:       libmisdn1 = %version

%description devel
This package contain the header files and libraries for
mISDNuser development.

%prep
%setup -q

%build
if [ ! -e configure ]; then
	mkdir -p m4
	autoreconf -fi
fi
export CFLAGS="%optflags -Wno-error"
export CXXFLAGS="$CFLAGS"
%configure --disable-static
make %{?_smp_mflags}

%install
%make_install
find "%buildroot/%_libdir" -type f -name "*.la" -delete;

%post -n libmisdn1 -p /sbin/ldconfig

%postun -n libmisdn1 -p /sbin/ldconfig

%files
%defattr(-,root,root)
%config %_sysconfdir/udev
%_bindir/*
%_sbindir/*

%files -n libmisdn1
%defattr(-,root,root)
%_libdir/libmisdn.so.1*

%files devel
%defattr(-,root,root)
%_includedir/mISDN/
%_libdir/*.so

%changelog
