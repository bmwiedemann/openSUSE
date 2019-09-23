#
# spec file for package susefirewall2-to-firewalld
#
# Copyright (c) 2018 SUSE LINUX GmbH, Nuernberg, Germany.
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


Name:           susefirewall2-to-firewalld
Version:        0.0.4
Release:        0
Summary:        Basic SuSEfirewall2 to FirewallD migration script
License:        GPL-2.0-or-later
Group:          Productivity/Networking/Other
Url:            https://github.com/openSUSE/susefirewall2-to-firewalld
Source:         https://github.com/openSUSE/%{name}/archive/%{name}-%{version}.tar.gz
Requires:       firewalld
Requires:       iptables
Recommends:     SuSEfirewall2
BuildArch:      noarch

%description
This is a simple bash script aiming to provide a basic migration path from
SuSEfirewall2 to FirewallD.

%prep
%setup -q -n %{name}-%{name}-%{version}

%build

%install
make DESTDIR=%{buildroot} install

%files
%defattr(-,root,root)
%doc README.md
%license COPYING
%{_sbindir}/susefirewall2-to-firewalld

%changelog
