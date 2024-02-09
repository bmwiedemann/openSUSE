#
# spec file for package python-pyasyncore
#
# Copyright (c) 2024 SUSE LLC
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

%define pythons python312
Name:           python-pyasyncore
Version:        1.0.3
Release:        0
Summary:        Make asyncore available for Python 312 onwards
License:        PSF-2.0
URL:            https://github.com/simonrob/pyasyncore
Source:         https://files.pythonhosted.org/packages/source/p/pyasyncore/pyasyncore-%{version}.tar.gz
BuildRequires:  python-rpm-macros
BuildRequires:  %{python_module base >= 3.12}
BuildRequires:  %{python_module pip}
BuildRequires:  %{python_module setuptools}
BuildRequires:  %{python_module wheel}
BuildRequires:  fdupes
Requires:       python-base >= 3.12
BuildArch:      noarch
%python_subpackages

%description
Make asyncore available for Python 3.12 onwards

%prep
%autosetup -p1 -n pyasyncore-%{version}

%build
%pyproject_wheel

%install
%pyproject_install
%python_expand %fdupes %{buildroot}%{$python_sitelib}

# no tests available

%files %{python_files}
%doc README.md
%license LICENSE
%{python_sitelib}/asyncore
%{python_sitelib}/pyasyncore-%{version}.dist-info

%changelog
