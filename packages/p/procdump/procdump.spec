#
# spec file for package procdump
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


Name:           procdump
Version:        1.3
Release:        0
Summary:        Process coredump emitter using performance triggers
License:        MIT
URL:            https://github.com/Microsoft/ProcDump-for-Linux
Source0:        https://github.com/Microsoft/ProcDump-for-Linux/archive/%{version}.tar.gz#/%{name}-%{version}.tar.gz
BuildRequires:  pkgconfig(zlib)

%description
A Linux version of the eponymous ProcDump tool from the Windows Sysinternals
suite. It can create core dumps of processes based on performance triggers.

%prep
%autosetup -p1 -n ProcDump-for-Linux-%{version}

%build
export CFLAGS="%{optflags}"
# build is not always parallel-safe
make

%install
%make_install

%files
%license LICENSE
%doc README.md
%{_bindir}/%{name}
%{_mandir}/man1/%{name}.1%{ext_man}

%changelog
