#
# spec file for package sshamble
#
# Copyright (c) 2025 SUSE LLC and contributors
# Copyright (c) 2024-2025, Martin Hauke <mardnh@gmx.de>
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


Name:           sshamble
Version:        0.3.3
Release:        0
Summary:        Security testing toolset for SSH
License:        BSD-2-Clause
Group:          Productivity/Security
URL:            https://SSHamble.com/
#Git-Clone:     https://github.com/runZeroInc/sshamble.git
Source:         https://github.com/runZeroInc/sshamble/archive/refs/tags/v%{version}.tar.gz#/%{name}-%{version}.tar.gz
Source1:        vendor.tar.gz
BuildRequires:  go
BuildRequires:  golang-packaging >= 1.22.5
%{go_provides}

%description
SSHamble simulates potential attack scenarios, including
unauthorized remote access due to unexpected state transitions,
remote command execution in post-session login implementations
and information leakage through unlimited high-speed authentication
requests.

The SSHamble interactive shell provides raw access to SSH requests in
the post-session (but pre-execution) environment, allowing for simple
esting of environment controls, signal processing, port forwarding,
and more.

%prep
%autosetup -p 1 -a 1

%build
%{goprep} github.com/runZeroInc/sshamble
%{gobuild} -mod=vendor .

%install
%{goinstall}

%files
%license LICENSE.md
%doc README.md SECURITY.md
%{_bindir}/sshamble

%changelog
