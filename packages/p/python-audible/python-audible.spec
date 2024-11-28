#
# spec file for package python-audible
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


%{?sle15_python_module_pythons}
Name:           python-audible
Version:        0.10.0
Release:        0
Summary:        A(Sync) Interface for internal Audible API
License:        AGPL-3.0-only
URL:            https://github.com/mkb79/audible
Source:         https://files.pythonhosted.org/packages/source/a/audible/audible-%{version}.tar.gz
# PATCH-FIX-OPENSUSE remove-python-restriction.patch
Patch1:         remove-python-restriction.patch
BuildRequires:  %{python_module Pillow}
BuildRequires:  %{python_module beautifulsoup4}
BuildRequires:  %{python_module httpx >= 0.20.0}
BuildRequires:  %{python_module pbkdf2}
BuildRequires:  %{python_module pip}
BuildRequires:  %{python_module poetry-core}
BuildRequires:  %{python_module pyaes}
BuildRequires:  %{python_module rsa}
BuildRequires:  %{python_module setuptools}
BuildRequires:  %{python_module wheel}
BuildRequires:  fdupes
BuildRequires:  python-rpm-macros
Requires:       python-Pillow
Requires:       python-beautifulsoup4
Requires:       python-httpx >= 0.20.0
Requires:       python-pbkdf2
Requires:       python-pyaes
Requires:       python-rsa
Suggests:       python-sphinx
Suggests:       python-sphinx_rtd_theme
Suggests:       python-sphinxcontrib-httpdomain
Suggests:       python-sphinx-autodoc-typehints
BuildArch:      noarch
%python_subpackages

%description
A(Sync) Interface for internal Audible API written in pure Python.

%prep
%autosetup -n audible-%{version}

%build
%pyproject_wheel

%install
%pyproject_install
%python_expand %fdupes %{buildroot}%{$python_sitelib}

%files %{python_files}
%doc README.md
%license LICENSE
%{python_sitelib}/audible
%{python_sitelib}/audible-%{version}*-info

%changelog
