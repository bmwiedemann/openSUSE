#
# spec file for package secvarctl
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


%global make_parms OPENSSL=1 DEBUG=1
Name:           secvarctl
Version:        1.1.0+git1.1d8b86b
Release:        0
Summary:        Suite of tools to manipulate and generate Secure Boot variables on POWER
License:        Apache-2.0
URL:            https://github.com/open-power/secvarctl
Source:         %{name}-%{version}.tar.gz
BuildRequires:  openssl-devel
ExclusiveArch:  ppc64 ppc64le

%description
The purpose of this tool is to simplify and automate the process of reading and writing secure boot keys.
secvarctl allows the user to communicate, via terminal commands, with the keys efficiently.

%prep
%autosetup

%build
%make_build %{make_parms}

%install
%make_install %{make_parms}

%files
%license LICENSE
%doc README.md
%{_bindir}/secvarctl
%{_mandir}/man1/secvarctl.1%{?ext_man}

%changelog
