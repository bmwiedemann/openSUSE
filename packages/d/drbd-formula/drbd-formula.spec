#
# spec file for package drbd-formula
#
# Copyright (c) 2021 SUSE LLC
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


%define fname drbd
%define fdir %{_datadir}/salt-formulas
# See also https://en.opensuse.org/openSUSE:Specfile_guidelines
Name:           drbd-formula
Version:        0.4.3+git.1621498620.45e1839
Release:        0
Summary:        DRBD deployment salt formula
License:        Apache-2.0
URL:            https://github.com/SUSE/%{name}
Source0:        %{name}-%{version}.tar.gz
Requires:       drbd-utils
Requires:       salt-shaptools >= 0.2.9
BuildArch:      noarch
%if 0%{?suse_version} < 1500
Recommends:     salt-formulas-configuration
%else
Requires:       salt-formulas-configuration
%endif

%description
DRBD deployment salt formula
Available on SUSE manager 4.0

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
cp -R templates %{buildroot}%{fdir}/states/%{fname}
cp -R form.yml metadata.yml pillar.example README.md %{buildroot}%{fdir}/metadata/%{fname}

%files
%doc README.md
%license LICENSE

%dir %attr(0755, root, salt) %{fdir}
%dir %attr(0755, root, salt) %{fdir}/states
%dir %attr(0755, root, salt) %{fdir}/metadata

%attr(0755, root, salt) %{fdir}/states/%{fname}
%attr(0755, root, salt) %{fdir}/states/%{fname}/templates
%attr(0755, root, salt) %{fdir}/metadata/%{fname}

%changelog
