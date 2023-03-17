#
# spec file for package virt-scenario
#
# Copyright (c) 2023 SUSE LLC
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

%{?!python_module:%define python_module() python3-%{**}}
%define pythons python3

Name:           virt-scenario
Version:        0.7.4
Release:        0
Summary:        Create XML guest configuration and prepare the host for a scenario
License:        GPL-3.0-or-later
Group:          System/Management
URL:            https://github.com/aginies/virt-scenario
Source:         %{name}-%{version}.tar.gz
BuildRequires:  python-rpm-macros
BuildRequires:  %{python_module setuptools}
BuildRequires:  %{python_module PyYAML}
BuildRequires:  %{python_module pyudev}
BuildRequires:  %{python_module libvirt-python}
BuildRequires:  fdupes
#Buildrequires:	pandoc
BuildArch:      noarch
Requires:	python-PyYAML
Requires:	python-pyudev
Requires:	python-curses
Requires:	python-libvirt-python
%python_subpackages

%description
Prepare a libvirt XML guest configuration and the host to run a customized guest.
Idea is to use multiple templates and concatenate them to create the
expected Guest XML file. If Host need a custom setting it will be done in second phase.

Customization to match a specific scenario is not graved in stone. The idea is to
prepare a configuration which should improved the usage compared to a basic setting.
This will **NOT guarantee** that this is perfect.

%prep
%setup -q

%build
%python_build

%install
%python_install
# move yaml file to /etc/pvirsh
mkdir -p %{buildroot}%{_sysconfdir}/%{name}/
mv %{buildroot}%{_datadir}/%{name}/*.yaml %{buildroot}%{_sysconfdir}/%{name}/
%python_expand %fdupes %{buildroot}%{$python_sitelib}


%files %{python_files}
%defattr(-,root,root)
%license LICENSE
%doc ChangeLog README.md
%{_bindir}/*
%{python_sitelib}/virtscenario
%{python_sitelib}/virt_select_firmware
%{python_sitelib}/virtscenario_launch
%{python_sitelib}/*.egg-info
%attr(0755,root,root) %{_datadir}/%name
%{_mandir}/man1/%{name}.1%{ext_man}
%attr(0755,root,root) %{_datadir}/%{name}/
%attr(0755,root,root) %config(noreplace) %{_sysconfdir}/%{name}

%changelog
