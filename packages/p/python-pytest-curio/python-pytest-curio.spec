#
# spec file for package python-pytest-curio
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
%define skip_python2 1
Name:           python-pytest-curio
Version:        1.0.1
Release:        0
Summary:        Pytest support for curio
License:        Apache-2.0
URL:            https://github.com/johnnoone/pytest-curio
Source:         https://files.pythonhosted.org/packages/source/p/pytest-curio/pytest-curio-%{version}.tar.gz
Source1:        https://raw.githubusercontent.com/johnnoone/pytest-curio/master/LICENSE
BuildRequires:  %{python_module setuptools}
BuildRequires:  fdupes
BuildRequires:  python-rpm-macros
Requires:       python-curio
Requires:       python-pytest
BuildArch:      noarch
# SECTION test requirements
BuildRequires:  %{python_module curio}
BuildRequires:  %{python_module pytest}
# /SECTION
%python_subpackages

%description
Pytest support for curio.

%prep
%setup -q -n pytest-curio-%{version}
cp %{SOURCE1} .

%build
%python_build

%install
%python_install
%python_expand %fdupes %{buildroot}%{$python_sitelib}

%check
# Tests are very immature and not in sdist
# https://github.com/johnnoone/pytest-curio/tree/master/test

%files %{python_files}
%doc README.rst
%license LICENSE
%{python_sitelib}/*

%changelog
