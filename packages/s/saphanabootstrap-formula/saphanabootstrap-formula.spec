#
# spec file for package saphanabootstrap-formula
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


# See also http://en.opensuse.org/openSUSE:Specfile_guidelines

Name:           saphanabootstrap-formula
Version:        0.14.0+git.1699438512.4930943
Release:        0
Summary:        SAP HANA platform deployment formula
License:        Apache-2.0

Url:            https://github.com/SUSE/%{name}
Source0:        %{name}-%{version}.tar.gz
BuildRoot:      %{_tmppath}/%{name}-%{version}-build
BuildArch:      noarch
Requires:       habootstrap-formula
Requires:       salt-shaptools
%if 0%{?suse_version} < 1500
Recommends:     salt-formulas-configuration
%else
Requires:       salt-formulas-configuration
%endif
Suggests:       prometheus-hanadb_exporter >= 0.7.0

%define fname hana
%define fdir  %{_datadir}/salt-formulas
%define ftemplates templates

%description
SAP HANA deployment salt formula. This formula is capable to install
SAP HANA nodes, enable system replication and configure SLE-HA cluster
with the SAPHanaSR resource agent, using standalone salt or via SUSE Manager
formulas with forms, available on SUSE Manager 4.0.

In order to use the formula, salt must be available in the system. The package comes automatically
in SLE15. To use it in SLE12, salt (and it sub-components) comes from the Advanced systems management
module, which can be added running the `SUSEConnect -p sle-module-adv-systems-management/12/{{ arch }}`

%prep
%setup -q

%build

%install

mkdir -p %{buildroot}%{fdir}/states/%{fname}
mkdir -p %{buildroot}%{fdir}/metadata/%{fname}
cp -R %{fname} %{buildroot}%{fdir}/states
cp -R form.yml pillar.example %{buildroot}%{fdir}/metadata/%{fname}
if [ -f metadata.yml ]
then
  cp -R metadata.yml %{buildroot}%{fdir}/metadata/%{fname}
fi


%files
%defattr(-,root,root,-)
%if 0%{?sle_version} < 120300
%doc README.md LICENSE
%else
%doc README.md
%license LICENSE
%endif

%dir %attr(0755, root, salt) %{fdir}
%dir %attr(0755, root, salt) %{fdir}/states
%dir %attr(0755, root, salt) %{fdir}/metadata

%attr(0755, root, salt) %{fdir}/states/%{fname}
%attr(0755, root, salt) %{fdir}/states/%{fname}/%{ftemplates}
%attr(0755, root, salt) %{fdir}/metadata/%{fname}

%changelog
