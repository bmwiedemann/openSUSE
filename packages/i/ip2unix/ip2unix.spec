#
# spec file for package ip2unix
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


Name:           ip2unix
Version:        2.1.4
Release:        0
Summary:        Turn IP sockets into Unix domain sockets
License:        LGPL-3.0-only
URL:            https://github.com/nixcloud/ip2unix/
Source0:        https://github.com/nixcloud/ip2unix/archive/v%{version}.tar.gz#/%{name}-%{version}.tar.gz
Patch0:         gcc-12.patch
Patch1:         gcc-13.patch
BuildRequires:  asciidoc
BuildRequires:  gcc-c++
BuildRequires:  meson >= 0.46.0
BuildRequires:  python3
BuildRequires:  python3-pytest
BuildRequires:  pkgconfig(yaml-cpp) >= 0.5.0
# systemd-socket-activate is used in tests
BuildRequires:  pkgconfig(systemd)

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

%meson
%meson_build

%install
%meson_install

%check
%meson_test

%files
%{_bindir}/%{name}
%{_libdir}/lib%{name}.so
%{_mandir}/man1/%{name}.1%{ext_man}

%changelog
