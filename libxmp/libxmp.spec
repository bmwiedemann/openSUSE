#
# spec file for package libxmp
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


Name:           libxmp
%define lname	libxmp4
Version:        4.4.1
Release:        0
Summary:        Module Player library for MOD, S3M, IT and others
License:        LGPL-2.1
Group:          Development/Libraries/C and C++
Url:            http://xmp.sf.net/

#Freshcode-URL:	https://freshcode.club/projects/libxmp
#Git-Clone:	git://git.code.sf.net/p/xmp/libxmp
Source:         http://downloads.sf.net/xmp/%name-%version.tar.gz
BuildRoot:      %{_tmppath}/%{name}-%{version}-build
BuildRequires:  pkg-config

%description
libxmp is a module player library which supports many module formats,
including MOD, S3M and IT. Possible applications for libxmp include
standalone module players, module player plugins for other players,
module information extractors, background music replayers for games
and other applications, converters, etc.

%package -n %lname
Summary:        Module Player library for MOD, S3M, IT and others
Group:          System/Libraries

%description -n %lname
libxmp is a module player library which supports many module formats,
including Protacker MOD, ScreamTracker S3M and ImpulseTracker IT.

%package devel
Summary:        Development files for libxmp, a MOD/S3M/IT/etc. module player library
Group:          Development/Libraries/C and C++
Requires:       %lname = %version

%description devel
libxmp is a module player library which supports many module formats,
including MOD, S3M and IT. Possible applications for libxmp include
standalone module players, module player plugins for other players,
module information extractors, background music replayers for games
and other applications, converters, etc.

This subpackage contains headers and library development files for
libxmp.

%prep
%setup -q

%build
%configure
make %{?_smp_mflags} V=1

%install
b="%buildroot"
make install DESTDIR="$b"
mkdir -p "$b/%_mandir/man3" "$b/%_docdir/%name"
install -pm0644 docs/Changelog docs/[a-z]* "$b/%_docdir/%name/"
# Remove file due to bnc#808655, and because they are hardware-specific
# and should not have much relevance for developers anyhow.
rm -f "$b/%_docdir/%name"/{adlib*,ay*.txt}
mv "$b/%_docdir/%name/libxmp.3" "$b/%_mandir/man3/"

%check
make check %{?_smp_mflags}

%post   -n %lname -p /sbin/ldconfig
%postun -n %lname -p /sbin/ldconfig

%files -n %lname
%defattr(-,root,root)
%_libdir/libxmp.so.4*
%doc docs/COPYING.LIB

%files devel
%defattr(-,root,root)
%_includedir/xmp.h
%_libdir/libxmp.so
%_libdir/pkgconfig/libxmp.pc
%_mandir/man3/libxmp.3*
%_docdir/%name/

%changelog
