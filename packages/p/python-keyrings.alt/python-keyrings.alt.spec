#
# spec file for package python-keyrings.alt
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


%define keyring_ver 18.0.0
%define skip_python2 1
%{?!python_module:%define python_module() python-%{**} python3-%{**}}
Name:           python-keyrings.alt
Version:        4.0.2
Release:        0
Summary:        Alternate keyring implementations
License:        MIT
Group:          Development/Languages/Python
URL:            https://github.com/jaraco/keyrings.alt
Source:         https://files.pythonhosted.org/packages/source/k/keyrings.alt/keyrings.alt-%{version}.tar.gz
BuildRequires:  %{python_module setuptools_scm >= 3.4.1}
BuildRequires:  %{python_module setuptools}
BuildRequires:  %{python_module toml}
BuildRequires:  fdupes
BuildRequires:  python-rpm-macros
BuildArch:      noarch
# SECTION test requirements
BuildRequires:  %{python_module fs >= 0.5}
BuildRequires:  %{python_module gobject}
BuildRequires:  %{python_module keyring >= 20}
BuildRequires:  %{python_module pycryptodomex}
BuildRequires:  %{python_module pytest >= 3.5}
BuildRequires:  typelib(GnomeKeyring)
# /SECTION
%python_subpackages

%description
Alternate keyring backend implementations for use with the
keyring package.

%prep
%setup -q -n keyrings.alt-%{version}
sed -i -e 's/--flake8//' -e 's/--black//' -e 's/--cov//' pytest.ini

%build
%python_build

%install
%python_install
%python_expand %fdupes %{buildroot}%{$python_sitelib}

%check
%pytest

%files %{python_files}
%doc CHANGES.rst README.rst
%license LICENSE
%{python_sitelib}/*

%changelog
