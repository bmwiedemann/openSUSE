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
Version:        2.1.3
Release:        0
Summary:        Tool to create XML guest configuration and prepare the host for a scenario
License:        GPL-3.0-or-later
Group:          System/Management
URL:            https://github.com/aginies/virt-scenario
Source:         %{name}-%{version}.tar.gz
BuildRequires:  %{python_module PyYAML}
BuildRequires:  %{python_module libvirt-python}
BuildRequires:  %{python_module psutil}
BuildRequires:  %{python_module pyudev}
BuildRequires:  %{python_module setuptools}
BuildRequires:  fdupes
BuildRequires:  python-rpm-macros
#Buildrequires:	pandoc
BuildArch:      noarch
Requires:       python-PyYAML
Requires:       python-curses
Requires:       python-libvirt-python
Requires:       python-psutil
Requires:       python-pyudev
Provides:       virt-scenario = %{version}
%python_subpackages

%description
A tool to generate a customized libvirt XML guest and prepare the host.
The idea is to improve the experience of usage compared to a basic setting.
This tool also simplifies the creation of secure VM (AMD SEV).

%package        gtk
Summary:        Gtk interface %{name}
Requires:       %{name} = %{version}-%{release}

%description    gtk
This is the Gtk interface for %{name}.

%prep
%autosetup

%build
%python_build

%install
%python_install
# move yaml file to /etc/virt-scenario
mkdir -p %{buildroot}%{_sysconfdir}/%{name}/vmconfig
mv %{buildroot}%{_datadir}/%{name}/*.yaml %{buildroot}%{_sysconfdir}/%{name}/
mv src/demo_api_usage.py %{buildroot}%{_datadir}/%{name}/
%python_expand %fdupes %{buildroot}%{$python_sitelib}

%files %{python_files}
%license LICENSE
%doc ChangeLog README.md
%{_bindir}/virt-scenario
%{_bindir}/virt-scenario-launch
%{_bindir}/virt-select-firmware
%{python_sitelib}/virtscenario
%{python_sitelib}/virt_select_firmware
%{python_sitelib}/virtscenario_launch
%{python_sitelib}/*.egg-info
#%attr(0644,root,root) %{_datadir}/%name
%{_mandir}/man1/%{name}.1%{ext_man}
%{_mandir}/man1/%{name}-settings.1%{ext_man}
#%attr(0644,root,root) %{_datadir}/%{name}/
%{_datadir}/%{name}/
#%attr(0644,root,root) %config(noreplace) %{_sysconfdir}/%{name}
%config(noreplace) %{_sysconfdir}/%{name}

%files gtk
%{_bindir}/virt-scenario-gtk
%{python_sitelib}/vsmygtk

%changelog
