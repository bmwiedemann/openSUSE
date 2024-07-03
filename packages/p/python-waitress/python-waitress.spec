#
# spec file for package python-waitress
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


%global flavor @BUILD_FLAVOR@%{nil}
%if "%{flavor}" == "doc"
%define psuffix -doc
%endif
%if "%{flavor}" == ""
%define psuffix %{nil}
%endif
%{?!python_module:%define python_module() python-%{**} python3-%{**}}
%if 0%{?suse_version} > 1500
%bcond_without libalternatives
%else
%bcond_with libalternatives
%endif
%{?sle15_python_module_pythons}
Name:           python-waitress%{psuffix}
Version:        3.0.0
Release:        0
Summary:        Waitress WSGI server
License:        ZPL-2.1
Group:          Development/Languages/Python
URL:            https://github.com/Pylons/waitress
Source:         https://files.pythonhosted.org/packages/source/w/waitress/waitress-%{version}.tar.gz
# intersphinx inventories, as fetched with fetch-intersphinx-inventories.sh
# https://docs.python.org/3/objects.inv -> python3.inv
Source1:        python3.inv
Source2:        fetch-intersphinx-inventories.sh
BuildRequires:  %{python_module pip}
BuildRequires:  %{python_module setuptools}
BuildRequires:  %{python_module wheel}
BuildRequires:  fdupes
BuildRequires:  python-rpm-macros >= 20210929
BuildArch:      noarch
%if "%{flavor}" == ""
BuildRequires:  %{python_module pytest}
%if %{with libalternatives}
BuildRequires:  alts
Requires:       alts
%else
Requires(post): update-alternatives
Requires(postun): update-alternatives
%endif
%else
# Documentation requirements
%if 0%{?suse_version} > 1500
BuildRequires:  python3-Sphinx
BuildRequires:  python3-docutils
BuildRequires:  python3-pylons-sphinx-themes
BuildRequires:  python3-waitress = %{version}
Recommends:     python3-waitress = %{version}
%else
BuildRequires:  %{python_module Sphinx}
BuildRequires:  %{python_module docutils}
BuildRequires:  %{python_module pylons-sphinx-themes}
BuildRequires:  %{python_module waitress = %{version}}
Recommends:     python-waitress = %{version}
%endif
%endif
%python_subpackages

%if "%{flavor}" == ""
%description
Waitress is a pure-Python WSGI server. It has no dependencies except
ones which live in the Python standard library. It supports HTTP/1.0
and HTTP/1.1.

For more information, see the "docs" directory of the Waitress package or
http://docs.pylonsproject.org/projects/waitress/en/latest/ .

%prep
%setup -q -n waitress-%{version}
sed -i '/addopts/d' setup.cfg

%build
%pyproject_wheel

%install
%pyproject_install
%python_clone -a %{buildroot}%{_bindir}/waitress-serve
%python_expand %fdupes %{buildroot}%{$python_sitelib}

%check
# disable one test, that requires network
%pytest -k 'not test_service_port'

%pre
# If libalternatives is used: Removing old update-alternatives entries.
%python_libalternatives_reset_alternative waitress-serve

%post
%python_install_alternative waitress-serve

%postun
%python_uninstall_alternative waitress-serve

%files %{python_files}
%license LICENSE.txt
%doc COPYRIGHT.txt README.rst
%python_alternative %{_bindir}/waitress-serve
%{python_sitelib}/waitress
%{python_sitelib}/waitress-%{version}.dist-info

%else

# doc flavor
%description
This package contains documentation files for %{name}.

%prep
%setup -q -n waitress-%{version}
# python3.inv
cp %{SOURCE1} docs/

%build
sphinx-build -b html docs build/sphinx/html && rm -r build/sphinx/html/.{buildinfo,doctrees}

%files %{python_files}
%license LICENSE.txt
%doc build/sphinx/html
%endif

%changelog
