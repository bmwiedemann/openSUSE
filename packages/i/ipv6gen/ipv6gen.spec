#
# spec file for package ipv6gen
#
# Copyright (c) 2018 SUSE LINUX GmbH, Nuernberg, Germany.
# Copyright (c) 2016, Martin Hauke <mardnh@gmx.de>
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


Name:           ipv6gen
Version:        1.0
Release:        0
Summary:        IPv6 prefix generator
License:        GPL-2.0-only
Group:          Productivity/Networking/System
URL:            https://github.com/vladak/ipv6gen/wiki/IPv6-prefix-generator
#Git-Clone:     https://github.com/vladak/ipv6gen/wiki/IPv6-prefix-generator.git
Source:         https://github.com/vladak/ipv6gen/archive/%{version}.tar.gz#/%{name}-%{version}.tar.gz
Requires:       perl
BuildArch:      noarch

%description
ipv6gen features:
generates prefix list of certain length from given prefix
via one of the 3 methods described in RFC 3531

%prep
%setup -q

%build

%install
install -Dpm0755 ipv6gen.pl %{buildroot}%{_bindir}/ipv6gen
install -Dpm0644 ipv6gen.1 %{buildroot}%{_mandir}/man1/ipv6gen.1

%files
%license LICENSE
%doc Changelog.txt
%{_bindir}/ipv6gen
%{_mandir}/man1/ipv6gen.1%{?ext_man}

%changelog
