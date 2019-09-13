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
Version:        0.2.5
Release:        0
Summary:        SAP HANA platform deployment formula
License:        Apache-2.0

Url:            https://github.com/SUSE/%{name}
Source0:        %{name}-%{version}.tar.gz
BuildRoot:      %{_tmppath}/%{name}-%{version}-build
BuildArch:      noarch
Requires:       habootstrap-formula
Requires:       salt-shaptools
Suggests:       hanadb_exporter >= 0.3.1

# On SLE/Leap 15-SP1 and TW requires the new salt-formula configuration location.
%if ! (0%{?sle_version:1} && 0%{?sle_version} < 150100)
Requires:       salt-standalone-formulas-configuration
%endif

%define fname hana
%define fdir  %{_datadir}/salt-formulas
%define ftemplates templates

%description
SAP HANA deployment salt formula. This formula is capable to install
SAP HANA nodes, enable system replication and configure SLE-HA cluster
with the SAPHanaSR resource agent, using standalone salt or via SUSE Manager
formulas with forms, available on SUSE Manager 4.0.

%prep
%setup -q

%build

%install

# before SUMA 4.0/15-SP1, install on the standard Salt Location.
%if 0%{?sle_version:1} && 0%{?sle_version} < 150100

mkdir -p %{buildroot}/srv/salt/
cp -R %{fname} %{buildroot}/srv/salt/
cp -R %{ftemplates} %{buildroot}/srv/salt/%{fname}/

%else

# On SUMA 4.0/15-SP1, a single shared directory will be used.
mkdir -p %{buildroot}%{fdir}/states/%{fname}
mkdir -p %{buildroot}%{fdir}/metadata/%{fname}
cp -R %{fname} %{buildroot}%{fdir}/states
cp -R %{ftemplates} %{buildroot}%{fdir}/states/%{fname}
cp -R form.yml %{buildroot}%{fdir}/metadata/%{fname}
if [ -f metadata.yml ]
then
  cp -R metadata.yml %{buildroot}%{fdir}/metadata/%{fname}
fi

%endif

%if 0%{?sle_version:1} && 0%{?sle_version} < 150100
%files
%defattr(-,root,root,-)
%if 0%{?sle_version} < 120300
%doc README.md LICENSE
%else
%doc README.md
%license LICENSE
%endif
/srv/salt/%{fname}
/srv/salt/%{fname}/%{ftemplates}

%dir %attr(0755, root, salt) /srv/salt

%else

%files
%defattr(-,root,root,-)
%doc README.md
%license LICENSE
%dir %{fdir}
%dir %{fdir}/states
%dir %{fdir}/metadata
%{fdir}/states/%{fname}
%{fdir}/states/%{fname}/%{ftemplates}
%{fdir}/metadata/%{fname}

%dir %attr(0750, root, salt) %{fdir}
%dir %attr(0750, root, salt) %{fdir}/states
%dir %attr(0750, root, salt) %{fdir}/metadata

%endif

%changelog
