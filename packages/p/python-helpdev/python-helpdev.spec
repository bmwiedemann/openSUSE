#
# spec file for package python-helpdev
#
# Copyright (c) 2020 SUSE LLC
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
Name:           python-helpdev
Version:        0.7.1
Release:        0
Summary:        HelpDev - Extracts information about the Python environment easily
License:        MIT AND CC-BY-4.0
Group:          Development/Languages/Python
URL:            https://gitlab.com/dpizetta/helpdev
Source0:        https://gitlab.com/dpizetta/helpdev/-/archive/v%{version}/helpdev-v%{version}.tar.gz
BuildRequires:  %{python_module setuptools}
BuildRequires:  fdupes
BuildRequires:  python-rpm-macros
Requires:       python-importlib-metadata
Requires:       python-psutil >= 5.4.8
Requires(post): update-alternatives
Requires(postun): update-alternatives
BuildArch:      noarch
# SECTION test requirements
BuildRequires:  %{python_module importlib-metadata}
BuildRequires:  %{python_module psutil >= 5.4.8}
BuildRequires:  %{python_module pytest}
# /SECTION
%python_subpackages

%description
HelpDev - Extracts information about the Python environment easily.

%prep
%setup -q -n helpdev-v%{version}
sed -i '1{\,^#!%{_bindir}/env python,d}' helpdev/*.py
sed -i -e "s/psutil>=5.6/psutil>=5.4.8/" setup.py

%build
%python_build

%install
%python_install
%python_clone -a %{buildroot}%{_bindir}/helpdev
%python_expand %fdupes %{buildroot}%{$python_sitelib}

%check
#test_check_python_packages needs the binary
%pytest -k 'not test_check_python_packages'

%post
%python_install_alternative helpdev

%postun
%python_uninstall_alternative helpdev

%files %{python_files}
%doc README.rst
%python_alternative %{_bindir}/helpdev
%{python_sitelib}/*

%changelog
