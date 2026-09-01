#
# spec file for package pvirsh
#
# Copyright (c) 2026 SUSE LLC and contributors
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


Name:           pvirsh
Version:        2.2
Release:        0
Summary:        Parallel virsh command to manage a selected group of Virtual Machine
License:        GPL-3.0-or-later
Group:          System/Management
URL:            https://github.com/aginies/pvirsh
Source:         %{name}-%{version}.tar.gz
BuildRequires:  fdupes
BuildRequires:  python-rpm-macros
BuildRequires:  python3-PyYAML
BuildRequires:  python3-libvirt-python
BuildRequires:  python3-pip
BuildRequires:  python3-setuptools
BuildRequires:  python3-wheel
Requires:       python3-PyYAML
Requires:       python3-curses
Requires:       python3-libvirt-python
BuildArch:      noarch
Provides:       python3-pvirsh = %{version}-%{release}
Obsoletes:      python3-pvirsh < %{version}-%{release}

%description
Parallel virsh command to manage a selected group of Virtual Machine.
This provides an easy way to execute the same command on a selected
group of Virtual Machine.

%prep
%autosetup -p1

%build
%python3_pyproject_wheel

%install
%python3_pyproject_install
# move group yaml file to /etc/pvirsh
mkdir -p %{buildroot}%{_sysconfdir}/%{name}/
mv %{buildroot}%{_datadir}/%{name}/*.yaml %{buildroot}%{_sysconfdir}/%{name}/
%fdupes %{buildroot}%{python3_sitelib}

%files
%license LICENSE
%doc ChangeLog README.md AUTHORS
%{_bindir}/%{name}
%{python3_sitelib}/%{name}
%{python3_sitelib}/%{name}-%{version}*-info
%attr(0755,root,root) %{_datadir}/%{name}/
%attr(0755,root,root) %config(noreplace) %{_sysconfdir}/%{name}
%{_mandir}/man1/%{name}.1%{?ext_man}

%changelog
