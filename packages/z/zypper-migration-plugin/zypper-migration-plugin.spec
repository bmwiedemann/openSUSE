#
# spec file for package zypper-migration-plugin
#
# Copyright (c) 2020 SUSE LLC
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


Name:           zypper-migration-plugin
Version:        0.12.1590748670.86b0749
Release:        0
URL:            https://github.com/SUSE/zypper-migration
Requires:       zypper >= 1.11.38
Requires:       rubygem(%{rb_default_ruby_abi}:suse-connect) >= 0.3.10
BuildRoot:      %{_tmppath}/%{name}-%{version}-build
BuildRequires:  ruby-macros >= 5
BuildRequires:  zypper >= 1.11.38
Source:         zypper-migration-%{version}.tar.xz
Summary:        Zypper subcommand for online migration
License:        GPL-2.0-only
Group:          System/Packages
BuildArch:      noarch
Supplements:    packageand(zypper:SUSEConnect)

%description
Zypper subcommand for online migration to new service pack.

%prep
%setup -q -n zypper-migration-%{version}

%build

%install
mkdir -p $RPM_BUILD_ROOT/usr/lib/zypper/commands $RPM_BUILD_ROOT/%{_mandir}/man8
install -m 755 zypper-migration $RPM_BUILD_ROOT/usr/lib/zypper/commands/
install -m 644 zypper-migration.8 $RPM_BUILD_ROOT/%{_mandir}/man8/

%files
%defattr(-,root,root,-)
/usr/lib/zypper/commands
%{_mandir}/man8/*

%changelog
