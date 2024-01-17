#
# spec file for package procmon
#
# Copyright (c) 2023 SUSE LLC
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


Name:           procmon
Version:        1.0.1
Release:        0
Summary:        Trace the syscall activity on the system
License:        MIT
Group:          System/Monitoring
URL:            https://github.com/microsoft/ProcMon-for-Linux/
Source0:        https://github.com/Sysinternals/ProcMon-for-Linux/archive/refs/tags/%{version}.tar.gz#/%{name}-%{version}.tar.gz
# PATCH-FIX-OPENSUSE procmon-use_system_libs.patch
Patch0:         procmon-use_system_libs.patch
# PATCH-FIX-UPSTREAM procmon-no_return_in_nonvoid.patch -- aloisio@gmx.com
Patch1:         procmon-no_return_in_nonvoid.patch
# PATCH-FIX-OPENSUSE procmon-add_missing_include.patch -- aloisio@gmx.com
Patch2:         procmon-add_missing_include.patch
BuildRequires:  cmake
BuildRequires:  gcc-c++
BuildRequires:  (pkgconfig(catch2) with pkgconfig(catch2) < 3)
BuildRequires:  pkgconfig(libbcc)
BuildRequires:  pkgconfig(libedit)
BuildRequires:  pkgconfig(libelf)
BuildRequires:  pkgconfig(ncurses)
BuildRequires:  pkgconfig(sqlite3)
BuildRequires:  pkgconfig(zlib)
Requires:       kernel-devel
# on account of BPF.h
ExcludeArch:    %arm %ix86

%description
Process Monitor (Procmon) is a Linux reimagining of the classic Procmon
tool from the Sysinternals suite of tools for Windows. Procmon provides
a convenient and efficient way for Linux developers to trace the syscall
activity on the system.

%prep
%setup -q -n ProcMon-for-Linux-%{version}
%autopatch -p1

%build
%cmake
%cmake_build

%install
%cmake_install
install -Dm0644 procmon.1 %{buildroot}%{_mandir}/man1/%{name}.1

%check
%ctest

%files
%{_bindir}/%{name}
%{_mandir}/man1/%{name}.1%{?ext_man}

%changelog
