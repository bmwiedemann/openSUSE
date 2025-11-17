#
# spec file for package tsctp
#
# Copyright (c) 2025 SUSE LLC and contributors
# Copyright (c) 2020-2025, Martin Hauke <mardnh@gmx.de>
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


Name:           tsctp
Version:        0.8.4
Release:        0
Summary:        SCTP test tool
License:        BSD-3-Clause
Group:          Productivity/Networking/Diagnostic
#Git-Clone:     https://github.com/dreibh/tsctp
URL:            https://www.nntb.no/~dreibh/tsctp/
Source:         https://www.uni-due.de/~be0001/tsctp/download/%{name}-%{version}.tar.xz
Source1:        https://www.uni-due.de/~be0001/tsctp/download/%{name}-%{version}.tar.xz.asc
Source2:        %{name}.keyring
BuildRequires:  cmake
BuildRequires:  lksctp-tools-devel

%description
TSCTP is an SCTP test tool. Its purpose is to perform basic SCTP
functionality tests to check implementations interoperability and
to verify that the SCTP stack is working.

%prep
%autosetup

%build
%cmake
%cmake_build

%install
%cmake_install

%files
%license COPYING-BSD
%doc AUTHORS ChangeLog README.md
%{_bindir}/tsctp
%{_mandir}/man1/tsctp.1%{?ext_man}
%{_datadir}/bash-completion/

%changelog
