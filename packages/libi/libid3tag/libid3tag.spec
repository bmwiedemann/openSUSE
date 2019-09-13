#
# spec file for package libid3tag
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


%define lname	libid3tag0
Name:           libid3tag
Version:        0.15.1b
Release:        0
Summary:        ID3 Tag Manipulation Library
License:        GPL-2.0+
Group:          Development/Libraries/C and C++
Url:            http://www.underbit.com/products/mad/
Source0:        ftp://ftp.mars.org/pub/mpeg/%{name}-%{version}.tar.gz
Source1:        baselibs.conf
Patch0:         libid3tag-noweak.dif
Patch1:         libid3tag-gperf.dif
Patch2:         libid3tag-0.15.1b-mb.diff
Patch3:         libid3tag-automake-fix.dif
Patch4:         libid3tag-optflags.patch
Patch5:         libid3tag-visibility.patch
# PATCH-FIX-UPSTREAM fix-build-with-gperf-3.1.diff alarrosa@suse.com -- Fix build with gperf 3.1
Patch6:         fix-build-with-gperf-3.1.diff
Patch7:         libid3tag-utf16.patch
Patch8:         libid3tag-unknown-encoding.patch
BuildRequires:  gperf
BuildRequires:  libtool
BuildRequires:  pkg-config
BuildRequires:  zlib-devel
BuildRoot:      %{_tmppath}/%{name}-%{version}-build

%description
libid3tag is a library for reading and writing ID3 tags, both ID3v1 and
the various versions of ID3v2.

%package -n %{lname}
Summary:        ID3 Tag Manipulation Library
# O/P added for 12.3
Group:          System/Libraries
Obsoletes:      libid3tag < %{version}-%{release}
Provides:       libid3tag = %{version}-%{release}

%description -n %{lname}
libid3tag is a library for reading and writing ID3 tags, both ID3v1 and
the various versions of ID3v2.

%package devel
Summary:        Development package for libid3tag library
Group:          Development/Libraries/C and C++
Requires:       %{lname} = %{version}
Requires:       glibc-devel

%description devel
This package contains the header files and static libraries needed to
develop applications with libid3tag.

%prep
%setup -q
%patch0
%patch1
%patch2
%patch3
%patch4
%patch5
%if 0%{?suse_version} > 1320
%patch6 -p1
%endif
%patch7 -p1
%patch8 -p1

%build
autoreconf -fiv
%configure \
  --disable-static
make %{?_smp_mflags}
echo -e "prefix=%{_prefix}\nexec_prefix=%{_prefix}\nlibdir=%{_libdir}\nincludedir=%{_includedir}\nName: id3tag\nDescription: ID3 tag library\nRequires:\nVersion: %{version}\nLibs: -L%{_libdir} -lid3tag\nCflags: -I%{_includedir}\n" > id3tag.pc

%install
make DESTDIR=%{buildroot} install %{?_smp_mflags}
install -m 644 -D id3tag.pc %{buildroot}%{_libdir}/pkgconfig/id3tag.pc
rm -f %{buildroot}%{_libdir}/libid3tag*.*a

%post -n %{lname} -p /sbin/ldconfig

%postun -n %{lname} -p /sbin/ldconfig

%files -n %{lname}
%defattr(-,root,root)
%{_libdir}/libid3tag.so.0*

%files devel
%defattr(-,root,root)
%doc CHANGES COPYING COPYRIGHT CREDITS README TODO VERSION
%{_includedir}/*
%{_libdir}/libid3tag.so
%{_libdir}/pkgconfig/id3tag.pc

%changelog
