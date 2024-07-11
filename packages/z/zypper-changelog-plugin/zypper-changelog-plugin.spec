#
# spec file for package zypper-changelog-plugin
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


Name:           zypper-changelog-plugin
Version:        0.5
Release:        0
Summary:        Changelog listing tool
License:        GPL-2.0-only
Group:          System/Packages
URL:            https://github.com/bzoltan1/zypper-changelog-plugin.git
Source:         zypper-changelog-plugin-0.5.tar.gz
Requires:       /usr/bin/python3
Requires:       python3-requests
Requires:       python3-rpm
Requires:       zstd
BuildArch:      noarch

%description
This tool is to show the changelog of packages in the repository

%prep
%setup -q

%build

%install
mkdir -p %{buildroot}%{_bindir}/
install -m 755 zypper-changelog %{buildroot}%{_bindir}/zypper-changelog
mkdir -p %{buildroot}/usr/lib/zypper/commands %{buildroot}/%{_mandir}/man8
install -m 644 zypper-changelog.8 %{buildroot}/%{_mandir}/man8/

%files
%license LICENSE
%doc README.md
%{_bindir}/zypper-changelog
%{_mandir}/man8/*

%changelog
