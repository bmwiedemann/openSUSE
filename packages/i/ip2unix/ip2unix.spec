#
# spec file for package ip2unix
#
# Copyright (c) 2026 SUSE LLC and contributors
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


Name:           ip2unix
Version:        2.2.1
Release:        0
Summary:        Turn IP sockets into Unix domain sockets
License:        LGPL-3.0-only
URL:            https://github.com/nixcloud/ip2unix
Source0:        %{url}/archive/v%{version}/%{name}-%{version}.tar.gz
Patch0:         https://patch-diff.githubusercontent.com/raw/nixcloud/ip2unix/pull/35.patch#/ip2unix-2.2.1-fix_out_of_range_string_view_access.patch
BuildRequires:  asciidoc
BuildRequires:  meson >= 0.47.0
BuildRequires:  python3
BuildRequires:  python3-pytest
BuildRequires:  python3-pytest-timeout
BuildRequires:  pkgconfig(yaml-cpp) >= 0.5.0
# systemd-socket-activate is used in tests
BuildRequires:  pkgconfig(systemd)
# gcc >= 8 provides std::filesystem
%if 0%{?suse_version} < 1600
BuildRequires:  gcc13
BuildRequires:  gcc13-PIE
BuildRequires:  gcc13-c++
%else
BuildRequires:  gcc-c++
%endif

%description
Executes a program and converts IP to Unix domain sockets at runtime based on a
list of rules, either given via short command line options or via a file with a
list of rules. The first matching rule causes ip2unix to replace the current IP
socket with a Unix domain socket based on the options given. For example if a
socketPath is specified, the Unix domain socket will bind or listen to the given
path.

%prep
%autosetup -p1

%build
# Building with LTO enabled causes crashes. https://github.com/nixcloud/ip2unix/issues/33
%define _lto_cflags %{nil}
%if 0%{?suse_version} < 1600
export CC="gcc-13"
export CXX="g++-13"
%endif
%meson
%meson_build

%install
%meson_install

%check
# exclude test 'ip2unix:integration' (timeout)
test_list=$(%meson_test --list) 2> /dev/null
test_list=${test_list//ip2unix:integration}
test_list=${test_list//integration}
%meson_test $test_list

%files
%{_bindir}/%{name}
%{_libdir}/lib%{name}.so
%{_mandir}/man1/%{name}.1%{ext_man}

%changelog
