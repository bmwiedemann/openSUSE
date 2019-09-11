#
# spec file for package libsigsegv
#
# Copyright (c) 2019 SUSE LINUX GmbH, Nuernberg, Germany.
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


%define somajor	2
%define lname	  libsigsegv%{somajor}
Name:           libsigsegv
Version:        2.12
Release:        0
Summary:        Library for Handling Page Faults in User Mode
License:        GPL-2.0-or-later
Group:          System/Libraries
Url:            https://www.gnu.org/software/libsigsegv/
Source0:        https://ftp.gnu.org/pub/gnu/libsigsegv/libsigsegv-%{version}.tar.gz
Source1:        https://ftp.gnu.org/pub/gnu/libsigsegv/libsigsegv-%{version}.tar.gz.sig
Source2:        https://savannah.gnu.org/project/memberlist-gpgkeys.php?group=%{name}&download=1#/%{name}.keyring
Patch0:         libsigsegv-2.12-lto.dif
BuildRequires:  pkgconfig

%define add_optflags(a:f:t:p:w:W:d:g:O:A:C:D:E:H:i:M:n:P:U:u:l:s:X:B:I:L:b:V:m:x:c:S:E:o:v:) \
%global optflags %{optflags} %{**}

%description
This is a library for handling page faults in user mode. A page fault occurs
when a program tries to access to a region of memory that is currently not
available.

%package -n %{lname}
Summary:        Library for Handling Page Faults in User Mode
Group:          System/Libraries

%description -n %{lname}
This is a library for handling page faults in user mode. A page fault occurs
when a program tries to access to a region of memory that is currently not
available.

%package devel
Summary:        Library for Handling Page Faults in User Mode
Group:          Development/Libraries/C and C++
Requires:       %{lname} = %{version}-%{release}

%description devel
This is a library for handling page faults in user mode. A page fault occurs
when a program tries to access to a region of memory that is currently not
available.

%package doc
Summary:        Library for Handling Page Faults in User Mode
Group:          Documentation/Other

%description doc
This is a library for handling page faults in user mode. A page fault occurs
when a program tries to access to a region of memory that is currently not
available.

%prep
%setup -q
%patch0 -b .p0

%build
%add_optflags -g3 -D_DEFAULT_SOURCE -D_XOPEN_SOURCE
%if 0%(case "%optflags" in (*-flto*) echo 1;; esac)
%add_optflags -ffat-lto-objects
%endif
%configure \
	--with-gnu-ld   \
	--enable-shared \
	--enable-static
sed -ri 's@^((old_striplib|striplib)=)".*"@\1""@' libtool
sed -ri 's@^(hardcode_libdir_flag_spec=)".*"@\1""@' libtool
mkdir bin/
ln -sf /bin/true bin/strip
PATH=${PWD}/bin:$PATH; export PATH
make %{?_smp_mflags}

%install
%make_install
rm "%{buildroot}%{_libdir}/libsigsegv.la"

%check
%if 0%{?qemu_user_space_build:1}
# qemu does not support stack overflows well ;)
make %{?_smp_mflags} check TESTS='sigsegv1 sigsegv2 sigsegv3'
%else
make %{?_smp_mflags} check
%endif

%post   -n %{lname} -p /sbin/ldconfig
%postun -n %{lname} -p /sbin/ldconfig

%files doc
%if %{defined license}
%license COPYING
%doc AUTHORS ChangeLog* NEWS PORTING README
%else
%doc AUTHORS COPYING ChangeLog* NEWS PORTING README
%endif

%files -n %{lname}
%{_libdir}/libsigsegv.so.%{somajor}*

%files devel
%{_includedir}/sigsegv.h
%{_libdir}/libsigsegv.so
%{_libdir}/libsigsegv.a

%changelog
