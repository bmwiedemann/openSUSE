#
# spec file for package goshs
#
# Copyright (c) 2021-2025, Martin Hauke <mardnh@gmx.de>
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

Name:           goshs
Version:        1.1.1
Release:        0
Summary:        A simple HTTP server
License:        MIT
Group:          Productivity/Networking/Web/Servers
URL:            https://goshs.de/
#Git-Clone:     https://github.com/patrickhener/goshs.git
Source:         https://github.com/patrickhener/goshs/archive/refs/tags/v%{version}.tar.gz#/%{name}-%{version}.tar.gz
Source1:        vendor.tar.gz
BuildRequires:  go >= 1.24.1
BuildRequires:  golang-packaging
# shared-mime-info needed for tests
BuildRequires:  shared-mime-info
%{go_provides}

%description
goshs is a replacement for Python's SimpleHTTPServer.
It allows uploading and downloading via HTTP/S with either
self-signed certificate or user provided certificate and
you can use HTTP basic auth.

%prep
%autosetup -p 1 -a 1

%build
%{goprep} github.com/patrickhener/goshs
%{gobuild} -mod=vendor .

%install
%{goinstall}

%check
make run-unit-no-network

%files
%license LICENSE
%doc README.md
%doc example/goshs.json.example
%{_bindir}/goshs

%changelog
