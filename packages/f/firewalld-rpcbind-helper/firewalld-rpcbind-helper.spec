#
# spec file for package firewalld-rpcbind-helper
#
# Copyright (c) 2019 SUSE LINUX GmbH, Nuernberg, Germany.
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


%define main_script firewall-rpc-helper.py
Name:           firewalld-rpcbind-helper
Version:        0.21
Release:        0
Summary:        Tool for static port assignment of NFSv3, ypserv, ypbind services
License:        GPL-2.0-or-later
Group:          Productivity/Networking/Security
Url:            https://github.com/mgerstner/firewalld-rpcbind-helper
Source0:        https://github.com/mgerstner/firewalld-rpcbind-helper/archive/v%{version}.tar.gz
Requires:       python3
Recommends:     firewalld
BuildArch:      noarch

%description
This is a helper utility for the configuration of static NFSv3, ypserv and
ypbind network ports for use with firewalld.

%prep
%setup -q

%build
# nothing

%install
mkdir -p %{buildroot}/%{_bindir}
mkdir -p %{buildroot}/%{_docdir}/%{name}
cp %{main_script} %{buildroot}/%{_bindir}/%{main_script}

%files
%doc README.md
%license LICENSE
%{_bindir}/%{main_script}

%changelog
