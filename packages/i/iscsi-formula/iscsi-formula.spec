#
# spec file for package iscsi-formula
#
# Copyright (c) 2018 SUSE LLC, Nuernberg, Germany.
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


# See also http://en.opensuse.org/openSUSE:Specfile_guidelines

Name:           iscsi-formula
Version:        1.1.1
Group:          System/Packages
Release:        0
Summary:        Configure iSCSI targets and initiator on GNU/Linux and FreeBSD

License:        Apache-2.0
Url:            https://github.com/saltstack-formulas/%{name}
Source0:        %{name}-%{version}.tar.gz
BuildRoot:      %{_tmppath}/%{name}-%{version}-build
BuildArch:      noarch
Requires:       salt-formulas-configuration

%define fname iscsi
%define fdir  %{_datadir}/salt-formulas

%description
Configure iSCSI targets and initiator on GNU/Linux and FreeBSD

%prep
%setup -q

%build

%install

mkdir -p %{buildroot}%{fdir}/states/%{fname}
mkdir -p %{buildroot}%{fdir}/metadata/%{fname}
cp -R %{fname} %{buildroot}%{fdir}/states


%files
%defattr(-,root,root,-)
%if 0%{?sle_version} < 120300
%doc docs/README.rst LICENSE
%else
%doc docs/README.rst
%license LICENSE
%endif

%dir %attr(0755, root, salt) %{fdir}
%dir %attr(0755, root, salt) %{fdir}/states
%dir %attr(0755, root, salt) %{fdir}/metadata

%attr(0755, root, salt) %{fdir}/states/%{fname}
%attr(0755, root, salt) %{fdir}/metadata/%{fname}

%changelog
