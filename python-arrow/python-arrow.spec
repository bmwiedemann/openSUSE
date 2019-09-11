#
# spec file for package python-arrow
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
%bcond_without python2
Name:           python-arrow
Version:        0.14.4
Release:        0
Summary:        Better dates and times for Python
License:        Apache-2.0
Group:          Development/Languages/Python
URL:            https://github.com/crsmithdev/arrow
Source:         https://files.pythonhosted.org/packages/source/a/arrow/arrow-%{version}.tar.gz
BuildRequires:  %{python_module chai}
BuildRequires:  %{python_module nose}
BuildRequires:  %{python_module python-dateutil}
BuildRequires:  %{python_module pytz}
BuildRequires:  %{python_module simplejson}
BuildRequires:  fdupes
BuildRequires:  python-rpm-macros
Requires:       python-python-dateutil
BuildArch:      noarch
%if %{with python2}
BuildRequires:  python-backports.functools_lru_cache
%endif
%ifpython2
Requires:       python-backports.functools_lru_cache
%endif
%python_subpackages

%description
Arrow is a Python library that offers a sensible, human-friendly
approach to creating, manipulating, formatting and converting dates,
times, and timestamps.  It implements and updates the datetime type,
plugging gaps in functionality, and provides an intelligent module
API that supports many common creation scenarios.  Simply put, it
helps you work with dates and times with fewer imports and a lot
less code.

Arrow is heavily inspired by moment.js and requests.

%prep
%setup -q -n arrow-%{version}
rm -rf arrow.egg-info

%build
%python_build

%install
%python_install
%python_expand %fdupes %{buildroot}%{$python_sitelib}

%check
%python_expand PYTHONPATH=%{buildroot}%{$python_sitelib} nosetests-%{$python_bin_suffix} -v

%files %{python_files}
%license LICENSE
%doc README.rst HISTORY.md
%dir %{python_sitelib}/arrow
%{python_sitelib}/arrow/*
%dir %{python_sitelib}/arrow-%{version}-py*.egg-info
%{python_sitelib}/arrow-%{version}-py*.egg-info

%changelog
