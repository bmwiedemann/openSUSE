#
# spec file for package python-pip-shims
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
%bcond_without python2
Name:           python-pip-shims
Version:        0.5.3
Release:        0
Summary:        Compatibility shims for pip versions 8 thru current
License:        ISC
URL:            https://github.com/sarugaku/pip-shims
Source:         https://github.com/sarugaku/pip-shims/archive/%{version}.tar.gz#/pip-shims-%{version}.tar.gz
BuildRequires:  %{python_module setuptools >= 40.8.0}
BuildRequires:  fdupes
BuildRequires:  python-rpm-macros
%if %{with python2}
BuildRequires:  python-backports.tempfile
%endif
Requires:       python-pip
Requires:       python-setuptools
Requires:       python-six
Requires:       python-wheel
BuildArch:      noarch
# SECTION test requirements
BuildRequires:  %{python_module pip}
BuildRequires:  %{python_module pytest}
BuildRequires:  %{python_module six}
BuildRequires:  %{python_module wheel}
# /SECTION
%python_subpackages

%description
Compatibility shims for pip versions 8 thru current.

%prep
%setup -q -n pip-shims-%{version}

%build
%python_build

%install
%python_install
%python_expand %fdupes %{buildroot}%{$python_sitelib}

%check
# Skip two online tests
# Some skipped tests fail because of missing git, however
# adding git only causes failure to fetch repositories.
# The tests are highly tied to API changes in pip
#  but they do not factualy test if the tool behave
#  so just skip them instead of having to patch them with
#  each pip release
%pytest -k 'not (test_resolution or test_wheelbuilder or test_resolve or test_get_packagefinder)'

%files %{python_files}
%license LICENSE
%doc README.rst CHANGELOG.rst docs/*.rst
%{python_sitelib}/pip_shims
%{python_sitelib}/pip_shims-%{version}*info

%changelog
