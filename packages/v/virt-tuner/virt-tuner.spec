#
# spec file for package specRPM_CREATION_NAME
#
# Copyright (c) specCURRENT_YEAR SUSE LINUX GmbH, Nuernberg, Germany.
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

%{?!python_module:%define python_module() python3-%{**}}
%define pythons python3

Name:           virt-tuner
Version:        0.0.1
Release:        0
Summary:        Virtual Machine definition tuner
License:        GPL-3.0-or-later
Group:          Productivity/Other
Url:            https://github.com/cbosdo/virt-tuner
Source:         %{name}-%{version}.tar.gz
BuildRequires:  %{python_module setuptools} 
BuildRequires:  %{python_module libvirt-python}
BuildRequires:  fdupes
Requires:       python-libvirt-python
Requires(post): update-alternatives
Requires(postun): update-alternatives
BuildArch:      noarch
%python_subpackages

%description
Helps tuning the libvirt XML definition of a virtual machine for specific use cases.

%prep
%setup -q

%build
%python_build

%install
%python_install
%python_clone -a %{buildroot}%{_bindir}/virt-tuner
%python_clone -a %{buildroot}%{_mandir}/man1/virt-tuner.1
%fdupes %{buildroot}%{_prefix}

%post
%python_install_alternative virt-tuner virt-tuner.1

%postun
%python_uninstall_alternative virt-tuner virt-tuner.1

%files %{python_files}
%license LICENSE
%doc ChangeLog README.md AUTHORS
%python_alternative %{_bindir}/virt-tuner
%{python_sitelib}/virt_tuner
%{python_sitelib}/virt_tuner-*.egg-info
%python_alternative %{_mandir}/man1/virt-tuner.1%{ext_man}

%changelog

