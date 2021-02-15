#
# spec file for package sscep
#
# Copyright (c) 2021 SUSE LLC
# Copyright (c) 2016-2021, Martin Hauke <mardnh@gmx.de>
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


Name:           sscep
Version:        0.9.0
Release:        0
Summary:        A command line client for the SCEP protocol
License:        BSD-3-Clause-Attribution AND OpenSSL
Group:          Productivity/Networking/Diagnostic
URL:            https://github.com/certnanny/sscep
Source:         https://github.com/certnanny/sscep/archive/v%{version}.tar.gz#/%{name}-%{version}.tar.gz
BuildRequires:  cmake
BuildRequires:  gcc-c++
BuildRequires:  libopenssl-devel

%description
Simple SCEP (Simple Certificate Enrollment Protocol) client with
modifications for engine support & more.

%prep
%setup -q

%build
%cmake

%install
%cmake_install
install -Dpm 0644 sscep.conf %{buildroot}%{_sysconfdir}/sscep/sscep.conf
install -Dpm 0755 mkrequest %{buildroot}%{_bindir}

%files
%license COPYING
%doc AUTHORS ChangeLog README.md
%dir %{_sysconfdir}/sscep/
%config(noreplace) %{_sysconfdir}/sscep/sscep.conf
%{_bindir}/sscep
%{_bindir}/mkrequest

%changelog
