#
# spec file for package drbd-formula
#
# Copyright (c) 2019 SUSE LLC
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


# See also https://en.opensuse.org/openSUSE:Specfile_guidelines

Name:           drbd-formula
Version:        0.3.10+git.1591284159.484cfdd
Release:        0
Summary:        DRBD deployment salt formula
License:        Apache-2.0
URL:            https://github.com/SUSE/%{name}
Source0:        %{name}-%{version}.tar.gz
Requires:       drbd-utils
Requires:       salt-shaptools >= 0.2.9
Requires:       salt-formulas-configuration
BuildArch:      noarch
BuildRoot:      %{_tmppath}/%{name}-%{version}-build

%define fname drbd
%define fdir %{_datadir}/salt-formulas
%define ftemplates templates

%description
DRBD deployment salt formula
Available on SUSE manager 4.0

%prep
%setup -q

%build

%install
mkdir -p %{buildroot}%{fdir}/states/%{fname}
mkdir -p %{buildroot}%{fdir}/metadata/%{fname}
cp -R %{fname} %{buildroot}%{fdir}/states
cp -R examples %{buildroot}%{fdir}/states/%{fname}/%{ftemplates}/
cp -R form.yml metadata.yml pillar.example README.md %{buildroot}%{fdir}/metadata/%{fname}

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
