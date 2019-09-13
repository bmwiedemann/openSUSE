#
# spec file for package giflib
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

# Please submit bugfixes or comments via https://bugs.opensuse.org/
#


%define lname   libgif7
Name:           giflib
Version:        5.1.4
Release:        0
Summary:        A Library for Working with GIF Images
License:        MIT
Group:          Development/Libraries/C and C++
Url:            http://giflib.sf.net/
Source:         http://downloads.sf.net/giflib/%{name}-%{version}.tar.bz2
Source2:        baselibs.conf
Patch1:         giflib-visibility.patch
Patch2:         giflib-automake-1_13.patch
Patch3:         giflib-CVE-2016-3977.patch
Patch4:         fix-autoconf11.patch
BuildRequires:  libtool >= 2
BuildRoot:      %{_tmppath}/%{name}-%{version}-build

%description
This Library allows manipulating GIF Image files. Since the LZW patents
have expired, giflib can again be used instead of libungif.

%package -n %{lname}
Summary:        A Library for Working with GIF Images
Group:          System/Libraries

%description -n %{lname}
This Library allows manipulating GIF Image files. Since the LZW patents
have expired, giflib can again be used instead of libungif.

%package progs
Summary:        Tools for Working with the GIF Library
Group:          Productivity/Graphics/Convertors
Provides:       ungif = %{version}
Obsoletes:      ungif < %{version}

%description progs
A tool for converting GIFs to various formats.

%package devel
Summary:        Library for Working with GIF Images - Files Mandatory for Development
Group:          Development/Libraries/C and C++
Requires:       %{lname} = %{version}

%description devel
This Library allows manipulating GIF Image files. Since the LZW patents
have expired, giflib can again be used instead of libungif.

%prep
%setup -q
for file in `find util -name "*.c"`; do
	touch -r $file $file.stamp
done
%patch1 -p1
%patch2 -p1
%patch3 -p1
%if 0%{?suse_version} <= 1110
%patch4 -p1
%endif

# USE __TIMESTAMP__ instead of __DATE__ , __TIME__
# this change is pointless unless we preserve the original
# file modification time
for file in `find util -name "*.c"`; do
	sed -i -e s@'__DATE__ ",   " __TIME__'@__TIMESTAMP__@g $file;
    touch -r $file.stamp $file;
    rm -v $file.stamp
done

mkdir -p m4; autoreconf -fiv

%build
%configure \
    --disable-silent-rules \
    --disable-static \
    --with-pic \
    --x-libraries=%{_libdir}
make %{?_smp_mflags}

%install
make DESTDIR=%{buildroot} install %{?_smp_mflags}
find %{buildroot} -type f -name "*.la" -delete -print
find doc -name "Makefile*" -print -delete

%post -n %{lname} -p /sbin/ldconfig

%postun -n %{lname} -p /sbin/ldconfig

%files -n %{lname}
%defattr(-,root,root)
%license COPYING
%{_libdir}/lib*.so.*

%files devel
%defattr(-,root,root)
%{_includedir}/gif_lib.h
%{_libdir}/lib*.so

%files progs
%defattr(-,root,root)
%license COPYING
%doc NEWS README doc
%{_bindir}/*

%changelog
