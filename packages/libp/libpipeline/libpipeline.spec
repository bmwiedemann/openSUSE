#
# spec file for package libpipeline
#
# Copyright (c) 2022 SUSE LLC
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


%define lname   libpipeline1
Name:           libpipeline
Version:        1.5.7
Release:        0
Summary:        A pipeline manipulation library
License:        GPL-3.0-or-later
Group:          System/Libraries
URL:            https://www.nongnu.org/libpipeline/
Source0:        https://download.savannah.nongnu.org/releases/%{name}/%{name}-%{version}.tar.gz
Source1:        https://download.savannah.nongnu.org/releases/%{name}/%{name}-%{version}.tar.gz.asc
Source2:        %{name}.keyring
BuildRequires:  pkgconfig

%description
libpipeline is a C library for setting up and running pipelines of
processes, without needing to involve shell command-line parsing which
is often error-prone and insecure. This alleviates programmers of the
need to laboriously construct pipelines using lower-level primitives
such as fork(2) and execve(2).

%package -n %{lname}
Summary:        A pipeline manipulation library
Group:          System/Libraries

%description -n %{lname}
libpipeline is a C library for setting up and running pipelines of
processes, without needing to involve shell command-line parsing which
is often error-prone and insecure. This alleviates programmers of the
need to laboriously construct pipelines using lower-level primitives
such as fork(2) and execve(2).

%package devel
Summary:        A pipeline manipulation library
Group:          Development/Libraries/C and C++
Requires:       %{lname} = %{version}
Provides:       pkgconfig(%{name}) = %{version}

%description devel
libpipeline is a C library for setting up and running pipelines of
processes, without needing to involve shell command-line parsing which
is often error-prone and insecure. This alleviates programmers of the
need to laboriously construct pipelines using lower-level primitives
such as fork(2) and execve(2).

%prep
%setup -q

%build
export CFLAGS="%{optflags} $(getconf LFS_CFLAGS)"
%configure \
  --enable-shared \
  --enable-threads=posix \
  --disable-rpath	\
  --enable-socketpair-pipe \
  --with-pic=yes \
  --with-gnu-ld
%make_build

%install
%make_install
rm -vf %{buildroot}%{_libdir}/libpipeline.la

%post -n %{lname} -p /sbin/ldconfig
%postun -n %{lname} -p /sbin/ldconfig

%files -n %{lname}
%defattr(-,root,root,0755)
%{_libdir}/libpipeline.so.*

%files devel
%defattr(-,root,root,0755)
%license COPYING
%doc ChangeLog README.md
%{_libdir}/libpipeline.so
%{_libdir}/pkgconfig/libpipeline.pc
%{_includedir}/pipeline.h
%{_mandir}/man3/*.3%{?ext_man}

%changelog
