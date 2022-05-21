#
# spec file for package python-blurb
#
# Copyright (c) 2022 SUSE LLC
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
Name:           python-blurb
Version:        1.1.0
Release:        0
Summary:        Command-line tool to manage CPython Misc/NEWS.d entries
License:        BSD-3-Clause
Group:          Development/Languages/Python
URL:            https://github.com/python/core-workflow/tree/master/blurb
Source:         https://files.pythonhosted.org/packages/source/b/blurb/blurb-%{version}.tar.gz
BuildRequires:  %{python_module base >= 3.7}
BuildRequires:  %{python_module flit-core}
BuildRequires:  %{python_module pip}
BuildRequires:  %{python_module pytest}
BuildRequires:  %{python_module setuptools}
BuildRequires:  %{python_module wheel}
BuildRequires:  fdupes
BuildRequires:  python-rpm-macros
BuildArch:      noarch
Requires(post): update-alternatives
Requires(postun):update-alternatives
%python_subpackages

%description
Command-line tool to manage CPython Misc/NEWS.d entries.

%prep
%autosetup -p1 -n blurb-%{version}

sed -i '1{\,^#!%{_bindir}/env python,d}' blurb.py
chmod -x blurb.py

%build
%pyproject_wheel

%install
%pyproject_install
%python_clone -a %{buildroot}%{_bindir}/blurb
%python_expand %fdupes %{buildroot}%{$python_sitelib}

%check
mkdir blurb
mv tests blurb
%pytest blurb.py

%post
%python_install_alternative blurb

%postun
%python_uninstall_alternative blurb

%files %{python_files}
%doc README.rst
%license LICENSE.txt
%python_alternative %{_bindir}/blurb
%{python_sitelib}/blurb.py
%pycache_only %{python_sitelib}/__pycache__/blurb*.pyc
%{python_sitelib}/blurb-%{version}*-info

%changelog
