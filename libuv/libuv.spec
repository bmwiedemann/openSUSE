#
# spec file for package libuv
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


%define somajor 1
Name:           libuv
Version:        1.30.1
Release:        0
Summary:        Asychronous I/O support library
License:        MIT
Group:          Development/Libraries/C and C++
URL:            http://libuv.org
# Using URL from upstream project fails due to ipv6 redirect
# Source0:      http://dist.libuv.org/dist/v%{version}/libuv-v%{version}.tar.gz
# Source1:      http://dist.libuv.org/dist/v%{version}/libuv-v%{version}.tar.gz.sign
# Source2:      %{name}.keyring
Source0:        https://github.com/libuv/libuv/archive/v%{version}.tar.gz#/%{name}-%{version}.tar.gz
Patch1:         fix_tests.patch
BuildRequires:  autoconf
BuildRequires:  automake
BuildRequires:  libtool
BuildRequires:  pkgconfig

%description
libuv is a support library with a focus on asynchronous I/O. It was
primarily developed for use by Node.js, but it is also used by
Mozilla's Rust language, Luvit, Julia, pyuv, and others.

%package     -n libuv%{somajor}
Summary:        Asychronous I/O support library
Group:          System/Libraries

%description -n libuv%{somajor}
libuv is a support library with a focus on asynchronous I/O. It was
primarily developed for use by Node.js, but it is also used by
Mozilla's Rust language, Luvit, Julia, pyuv, and others.

%package        devel
Summary:        Development libraries for libuv
Group:          Development/Libraries/C and C++
BuildRequires:  glibc-devel
Requires:       libuv%{somajor} = %{version}

%description    devel
Development files for libuv.

libuv is a support library with a focus on asynchronous I/O. It was
primarily developed for use by Node.js, but it is also used by
Mozilla's Rust language, Luvit, Julia, pyuv, and others.

%prep
%setup -q
%patch1 -p1

%build
./autogen.sh
%configure \
  --disable-static
make %{?_smp_mflags} V=1

%install
%make_install
find %{buildroot} -type f -name "*.la" -delete -print

%check
make %{?_smp_mflags} check

%post -n libuv%{somajor} -p /sbin/ldconfig
%postun -n libuv%{somajor} -p /sbin/ldconfig

%files -n libuv%{somajor}
%{_libdir}/libuv.so.%{somajor}*

%files devel
%doc AUTHORS CONTRIBUTING.md ChangeLog README.md
%license LICENSE
%{_libdir}/libuv.so
%{_includedir}/uv*
%{_libdir}/pkgconfig/libuv.pc

%changelog
