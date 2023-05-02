#
# spec file for package sshping
#
# Copyright (c) 2023, Martin Hauke <mardnh@gmx.de>
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


Name:           sshping
Version:        0.1.4+git20230317
Release:        0
Summary:        SSH server auditing
License:        MIT
Group:          Productivity/Networking/Diagnostic
URL:            https://github.com/spook/sshping
Source:         %{name}-%{version}.tar.xz
BuildRequires:  cmake
BuildRequires:  gcc-c++
BuildRequires:  pkgconfig
BuildRequires:  pkgconfig(libssh)

%description
Utility to test the performance of interactive ssh sessions or scp file
transfers. It uses ssh to log into a remote system, then runs two tests: the
first test sends one character at a time, waiting for each character to be
returned while it records the latency time for each. The second test sends a
dummy file over scp to /dev/null on the remote system.

%prep
%setup -q

%build
%cmake
%cmake_build

%install
%cmake_install

%files
%license LICENSE
%doc README.md
%{_bindir}/sshping
%{_mandir}/man8/sshping.8%{?ext_man}

%changelog
