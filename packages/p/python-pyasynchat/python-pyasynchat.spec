#
# spec file for package python-pyasynchat
#
# Copyright (c) 2025 SUSE LLC
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


%{?sle15_python_module_pythons}
Name:           python-pyasynchat
Version:        1.0.4
Release:        0
Summary:        Make asynchat available for Python 312 onwards
License:        PSF-2.0
URL:            https://github.com/simonrob/pyasynchat
Source:         https://files.pythonhosted.org/packages/source/p/pyasynchat/pyasynchat-%{version}.tar.gz
BuildRequires:  python-rpm-macros
BuildRequires:  %{python_module pip}
BuildRequires:  %{python_module setuptools}
BuildRequires:  %{python_module wheel}
# SECTION test requirements
BuildRequires:  %{python_module pyasyncore >= 1.0.2}
BuildRequires:  %{python_module testsuite}
# /SECTION
BuildRequires:  fdupes
Requires:       python-pyasyncore >= 1.0.2
BuildArch:      noarch
%python_subpackages

%description
Make asynchat available for Python 3.12 onwards

%prep
%autosetup -p1 -n pyasynchat-%{version}
chmod -x README.md LICENSE

%build
%pyproject_wheel

%install
%pyproject_install
%python_expand %fdupes %{buildroot}%{$python_sitelib}

%check
%pyunittest -v tests/test_asynchat.py

%files %{python_files}
%doc README.md
%license LICENSE
%{python_sitelib}/asynchat
%{python_sitelib}/pyasynchat-%{version}.dist-info

%changelog
