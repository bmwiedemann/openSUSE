#
# spec file for package libuv
#
# Copyright (c) 2024 SUSE LLC
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
Version:        1.48.0
Release:        0
Summary:        Asychronous I/O support library
License:        MIT
URL:            https://libuv.org
Source0:        https://dist.libuv.org/dist/v%{version}/libuv-v%{version}.tar.gz
Source1:        https://dist.libuv.org/dist/v%{version}/libuv-v%{version}.tar.gz.sign
# https://github.com/libuv/libuv/blob/v1.x/MAINTAINERS.md
Source2:        %{name}.keyring
Source3:        baselibs.conf
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

%description -n libuv%{somajor}
libuv is a support library with a focus on asynchronous I/O. It was
primarily developed for use by Node.js, but it is also used by
Mozilla's Rust language, Luvit, Julia, pyuv, and others.

%package        devel
Summary:        Development libraries for libuv
BuildRequires:  glibc-devel
Requires:       libuv%{somajor} = %{version}

%description    devel
Development files for libuv.

libuv is a support library with a focus on asynchronous I/O. It was
primarily developed for use by Node.js, but it is also used by
Mozilla's Rust language, Luvit, Julia, pyuv, and others.

%prep
%autosetup -p1 -n %{name}-v%{version}

%build
./autogen.sh
%configure \
  --disable-static
%make_build

%install
%make_install
find %{buildroot} -type f -name "*.la" -delete -print

%check
%if !0%{?qemu_user_space_build}
%make_build check
%endif

%post -n libuv%{somajor} -p /sbin/ldconfig
%postun -n libuv%{somajor} -p /sbin/ldconfig

%files -n libuv%{somajor}
%license LICENSE
%{_libdir}/libuv.so.%{somajor}*

%files devel
%doc AUTHORS CONTRIBUTING.md ChangeLog README.md
%license LICENSE
%{_libdir}/libuv.so
%{_includedir}/uv*
%{_libdir}/pkgconfig/libuv.pc

%changelog
