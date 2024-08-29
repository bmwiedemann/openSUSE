#
# spec file for package python-mando
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
Name:           python-mando
Version:        0.7.1
Release:        0
Summary:        Python wrapper around argparse, a tool to create CLI apps
License:        MIT
URL:            https://mando.readthedocs.org/
Source:         https://files.pythonhosted.org/packages/source/m/mando/mando-%{version}.tar.gz
# https://github.com/rubik/mando/pull/57
Patch0:         python-mando-no-python2.patch
BuildRequires:  %{python_module pip}
BuildRequires:  %{python_module setuptools}
BuildRequires:  %{python_module wheel}
BuildRequires:  fdupes
BuildRequires:  python-rpm-macros
Suggests:       python-rst2ansi
BuildArch:      noarch
# SECTION teset requirements
BuildRequires:  %{python_module pytest}
# /SECTION
%python_subpackages

%description
Mando is a wrapper around argparse, and allows writing CLI
applications.

%prep
%autosetup -p1 -n mando-%{version}
sed -i -e '/^#!\//, 1d' mando/tests/*.py

%build
%pyproject_wheel

%install
%pyproject_install
%python_expand %fdupes %{buildroot}%{$python_sitelib}

%check
%pytest

%files %{python_files}
%license LICENSE
%doc README.rst
%{python_sitelib}/mando
%{python_sitelib}/mando-%{version}.dist-info

%changelog
