#
# spec file for package python-mando
#
# Copyright (c) 2019 SUSE LINUX GmbH, Nuernberg, Germany.
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
%bcond_without  test
Name:           python-mando
Version:        0.6.4
Release:        0
Summary:        Python wrapper around argparse, a tool to create CLI apps
License:        MIT
Group:          Development/Languages/Python
URL:            https://mando.readthedocs.org/
Source:         https://files.pythonhosted.org/packages/source/m/mando/mando-%{version}.tar.gz
BuildRequires:  %{python_module setuptools}
BuildRequires:  fdupes
BuildRequires:  python-rpm-macros
Requires:       python-six
Suggests:       python-rst2ansi
BuildArch:      noarch
%if %{with test}
BuildRequires:  %{python_module pytest}
BuildRequires:  %{python_module six}
%endif
%python_subpackages

%description
Mando is a wrapper around argparse, and allows writing CLI
applications.

%prep
%setup -q -n mando-%{version}
sed -i -e '/^#!\//, 1d' mando/tests/*.py

%build
%python_build

%install
%python_install
%python_expand %fdupes %{buildroot}%{$python_sitelib}

%if %{with test}
%check
%python_exec setup.py test
%endif

%files %{python_files}
%license LICENSE
%doc README.rst
%{python_sitelib}/*

%changelog
