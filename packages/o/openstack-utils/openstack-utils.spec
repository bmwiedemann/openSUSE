#
# spec file for package openstack-utils
#
# Copyright (c) 2014 SUSE LINUX Products GmbH, Nuernberg, Germany.
#
# All modifications and additions to the file contributed by third parties
# remain the property of their copyright owners, unless otherwise agreed
# upon. The license for this file, and modifications and additions to the
# file, is the same license as for the pristine package itself (unless the
# license for the pristine package is not an Open Source License, in which
# case the license is the MIT License). An "Open Source License" is a
# license that conforms to the Open Source Definition (Version 1.9)
# published by the Open Source Initiative.

# Please submit bugfixes or comments via http://bugs.opensuse.org/
#


Name:           openstack-utils
Version:        2014.1.3+git.1409246608.bd34653
Release:        0
Summary:        Helper utilities for OpenStack service
License:        Apache-2.0
Group:          Development/Libraries/Python
Url:            https://github.com/fedora-openstack/openstack-utils
Source:         %{name}-%{version}.tar.gz
Patch1:         fix-db.patch
BuildRoot:      %{_tmppath}/%{name}-%{version}-build
BuildArch:      noarch
Requires:       crudini

%description
Utilities to aid the setup and configuration of OpenStack packages.

 - openstack-config - Manipulate the openstack ini files
 - openstack-db - Setup or delete the database for a specified service
 - openstack-status - Give an overview of the status of installed services

%prep
%setup -q
%patch1 -p0

%build

%install
install -d %{buildroot}%{_bindir}
install -m755 utils/* %{buildroot}%{_bindir}
install -d %{buildroot}%{_mandir}/man1
install -m644 man/*.1 %{buildroot}/%{_mandir}/man1

%files
%defattr(-,root,root)
%doc README.md NEWS LICENSE
%{_bindir}/openstack-config
%{_bindir}/openstack-db
%{_bindir}/openstack-service
%{_bindir}/openstack-status
%{_mandir}/man1/openstack-config.1%{?ext_man}
%{_mandir}/man1/openstack-db.1%{?ext_man}
%{_mandir}/man1/openstack-service.1.gz
%{_mandir}/man1/openstack-status.1%{?ext_man}

%changelog
