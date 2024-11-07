#
# spec file for package lsof
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


%define sover 0
Name:           lsof
Version:        4.99.3
Release:        0
Summary:        A Program That Lists Information about Files Opened by Processes
License:        Zlib
Group:          System/Monitoring
URL:            https://github.com/lsof-org/lsof
Source:         https://github.com/lsof-org/lsof/archive/refs/tags/%{version}.tar.gz#/%{name}-%{version}.tar.gz
Patch0:         lsof-4.99.3-fix-version-in-configure-ac.patch
Patch1:         0001-tests-eliminate-use-of-fgrep.patch
Patch2:         0002-linux-Maintain-original-output-for-pidfd-in-linux-6..patch
Patch3:         reproducible.patch
BuildRequires:  autoconf
BuildRequires:  automake
BuildRequires:  groff
BuildRequires:  libtool
BuildRequires:  pkgconfig
BuildRequires:  pkgconfig(libselinux)
BuildRequires:  pkgconfig(libtirpc)

%description
Lsof lists information about files opened by processes. An open file
may be a regular file, a directory, a block special file, a character
special file, an executing text reference, a library, a stream, or a
network file (Internet socket, NFS file, or UNIX domain socket.)  A
specific  file or all the files in a file system may be selected by
path.

%package -n liblsof%{sover}
Summary:        Library for listing information about files opened by process

%description -n liblsof%{sover}
This package contains a library for listing information about files opened by process.
It allows accessing the functionality of the lsof command from C functions without
spawning a subprocess.

%package devel
Summary:        Library for listing information about files opened by process
Requires:       liblsof%{sover} = %{version}

%description devel
This package contains a library for listing information about files opened by process.
It allows accessing the functionality of the lsof command from C functions without
spawning a subprocess.

This package contains the files required to build with liblsof.

%prep
%autosetup -p1

%build
autoreconf -fiv
%configure
%make_build

%install
%make_install
find %{buildroot}%{_libdir} -type f -name "*.a" -print -delete
find %{buildroot} -type f -name "*.la" -delete -print

%check
%if 0%{?qemu_user_space_build}
# Some tests are difficult to emulate by QEmu
echo exit 77 > lib/dialects/linux/tests/case-20-pty-endpoint.bash
echo exit 77 > lib/dialects/linux/tests/case-20-ux-socket-endpoint-unaccepted.bash
echo 'int main () { return 77; }' > tests/LTbasic2.c
%endif
%make_build check

%ldconfig_scriptlets -n liblsof%{sover}

%files
%license COPYING
%doc ChangeLog README 00*
%{_bindir}/lsof
%{_mandir}/man8/lsof.8%{?ext_man}

%files devel
%license COPYING
%{_includedir}/*.h
%{_libdir}/liblsof.so

%files -n liblsof%{sover}
%license COPYING
%{_libdir}/liblsof.so.%{sover}
%{_libdir}/liblsof.so.%{sover}.*

%changelog
