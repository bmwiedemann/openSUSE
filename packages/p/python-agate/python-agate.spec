#
# spec file for package python-agate
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
Name:           python-agate
Version:        1.6.1
Release:        0
Summary:        Data analysis library optimized for humans instead of machines
License:        MIT
Group:          Development/Languages/Python
URL:            https://github.com/wireservice/agate
Source:         https://github.com/wireservice/agate/archive/%{version}.tar.gz
BuildRequires:  %{python_module Babel >= 2.0}
BuildRequires:  %{python_module future}
BuildRequires:  %{python_module isodate >= 0.5.4}
BuildRequires:  %{python_module leather >= 0.3.2}
BuildRequires:  %{python_module lxml >= 0.3.2}
BuildRequires:  %{python_module parsedatetime >= 2.1}
BuildRequires:  %{python_module pytest}
BuildRequires:  %{python_module python-slugify >= 1.2.1}
BuildRequires:  %{python_module pytimeparse >= 1.1.5}
BuildRequires:  %{python_module setuptools}
BuildRequires:  %{python_module six >= 1.9.0}
BuildRequires:  fdupes
BuildRequires:  python-rpm-macros
Requires:       python-Babel >= 2.0
Requires:       python-future
Requires:       python-isodate >= 0.5.4
Requires:       python-leather >= 0.3.2
Requires:       python-parsedatetime >= 2.1
Requires:       python-python-slugify >= 1.2.1
Requires:       python-pytimeparse >= 1.1.5
Requires:       python-six >= 1.9.0
BuildArch:      noarch
%python_subpackages

%description
Agate is a Python data analysis library that is optimized for humans
instead of machines. It is an alternative to numpy and pandas that
solves real-world problems with readable code.

Agate was previously known as journalism.

%prep
%setup -q -n agate-%{version}
find agate -name "*.py" -exec sed -i -e '/^#!\//, 1d' {} \;

%build
%python_build

%install
%python_install
%python_expand %fdupes %{buildroot}%{$python_sitelib}

%check
export LANG=en_US.UTF-8
%pytest -k 'not test_join'

%files %{python_files}
%doc CHANGELOG.rst README.rst
%license COPYING
%{python_sitelib}/*

%changelog
