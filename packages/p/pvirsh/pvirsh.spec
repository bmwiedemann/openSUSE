#
# spec file for package pvirsh
#
# Copyright (c) 2022 SUSE LLC
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

Name:           pvirsh
Version:        2.1
Release:        0
Summary:        Parallel virsh command
License:        GPL-3.0-or-later
Group:          System/Management
URL:            https://github.com/aginies/pvirsh
Source:         %{name}-%{version}.tar.gz
BuildRequires:  python-rpm-macros
BuildRequires:  %{python_module libvirt-python}
BuildRequires:  %{python_module setuptools}
BuildRequires:  %{python_module PyYAML}
BuildRequires:  fdupes
Requires:       python3-libvirt-python
Requires:       python3-PyYAML
BuildArch:      noarch
%python_subpackages

%description
Parallel virsh command to manage a selected group of Virtual Machine.
This provides an easy way to execute the same command on a selected
group of Virtual Machine.

%prep
%setup -q

%build
%python_build

%install
%python_install
# move group yaml file to /etc/pvirsh
mkdir -p %{buildroot}%{_sysconfdir}/%{name}/
mv %{buildroot}%{_datadir}/%{name}/*.yaml %{buildroot}%{_sysconfdir}/%{name}/
%python_expand %fdupes %{buildroot}%{$python_sitelib}

%files %{python_files}
%defattr(-,root,root)
%license LICENSE
%doc ChangeLog README.md AUTHORS
%{_bindir}/%{name}
%{python_sitelib}/%{name}
%{python_sitelib}/%{name}-*.egg-info
%attr(0755,root,root) %{_datadir}/%{name}/
%attr(0755,root,root) %config(noreplace) %{_sysconfdir}/%{name}
%{_mandir}/man1/%{name}.1%{ext_man}

%changelog
