#
# spec file for package python-pan-python
#
# Copyright (c) 2020 SUSE LLC
# Copyright (c) 2017-2019, Martin Hauke <mardnh@gmx.de>
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


%{?!python_module:%define python_module() python-%{**} python3-%{**}}
Name:           python-pan-python
Version:        0.16.0
Release:        0
Summary:        Multi-tool set for Palo Alto Networks PAN-OS, Panorama, WildFire and AutoFocus
License:        ISC
Group:          Development/Languages/Python
URL:            https://github.com/kevinsteves/pan-python
Source:         https://files.pythonhosted.org/packages/source/p/pan-python/pan-python-%{version}.tar.gz
BuildRequires:  %{python_module setuptools}
BuildRequires:  fdupes
BuildRequires:  python-rpm-macros
Requires(post): update-alternatives
Requires(postun): update-alternatives
BuildArch:      noarch
# SECTION test requirements
#BuildRequires:  %%{python_module pytest}
# /SECTION
%python_subpackages

%description
pan-python is a Python package for Palo Alto Networks' Next-Generation
Firewalls, WildFire and AutoFocus.  It provides:
 - a Python and command line interface to the PAN-OS and Panorama XML API
 - a command line program for managing PAN-OS XML configurations
 - a Python and command line interface to the WildFire API
 - a Python and command line interface to the AutoFocus API

%prep
%setup -q -n pan-python-%{version}

%build
%python_build

%install
%python_install
# remove .py suffix from binaries
cd %{buildroot}/%{_bindir}
for f in panxapi panconf panlicapi panwfapi panafapi; do mv "$f.py" "$f"; done
#
%python_clone -a %{buildroot}%{_bindir}/panxapi
%python_clone -a %{buildroot}%{_bindir}/panwfapi
%python_clone -a %{buildroot}%{_bindir}/panlicapi
%python_clone -a %{buildroot}%{_bindir}/panconf
%python_clone -a %{buildroot}%{_bindir}/panafapi
%python_expand %fdupes %{buildroot}%{$python_sitelib}
# remove unneeded files
rm -f %{buildroot}%{_bindir}/_current_flavor

%check
# Upstream does not have any tests yet
#%%pytest

%post
%python_install_alternative panxapi
%python_install_alternative panwfapi
%python_install_alternative panlicapi
%python_install_alternative panconf
%python_install_alternative panafapi

%postun
%python_uninstall_alternative panxapi
%python_uninstall_alternative panwfapi
%python_uninstall_alternative panlicapi
%python_uninstall_alternative panconf
%python_uninstall_alternative panafapi

%files %{python_files}
%license LICENSE.txt
%doc AUTHORS.rst HISTORY.rst README.rst
%python_alternative %{_bindir}/panafapi
%python_alternative %{_bindir}/panconf
%python_alternative %{_bindir}/panlicapi
%python_alternative %{_bindir}/panwfapi
%python_alternative %{_bindir}/panxapi
%{python_sitelib}/*

%changelog
