#
# spec file for package python-Delorean
#
# Copyright (c) 2018 SUSE LINUX GmbH, Nuernberg, Germany.
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
Name:           python-Delorean
Version:        1.0.0
Release:        0
Summary:        Python library for manipulating datetimes
License:        MIT
Group:          Development/Languages/Python
Url:            https://github.com/myusuf3/delorean
Source:         https://files.pythonhosted.org/packages/source/D/Delorean/Delorean-%{version}.tar.gz
BuildRequires:  %{python_module setuptools}
BuildRequires:  fdupes
BuildRequires:  python-rpm-macros
# SECTION test requirements
BuildRequires:  %{python_module Babel >= 2.1.1}
BuildRequires:  %{python_module humanize >= 0.5.1}
BuildRequires:  %{python_module mock}
BuildRequires:  %{python_module python-dateutil >= 2.4.2}
BuildRequires:  %{python_module pytz >= 2015.7}
BuildRequires:  %{python_module tzlocal >= 1.2}
# /SECTION
Requires:       python-Babel >= 2.1.1
Requires:       python-humanize >= 0.5.1
Requires:       python-python-dateutil >= 2.4.2
Requires:       python-pytz >= 2015.7
Requires:       python-tzlocal >= 1.2
BuildArch:      noarch

%python_subpackages

%description
Delorean is a library for clearing up the inconvenient truths that
arise dealing with datetimes in Python.

%prep
%setup -q -n Delorean-%{version}

%build
%python_build

%install
%python_install
%python_expand %fdupes %{buildroot}%{$python_sitelib}

%check
%{python_expand export PYTHONDONTWRITEBYTECODE=1
export PYTHONPATH=%{buildroot}%{$python_sitelib}
$python tests/delorean_tests.py
}

%files %{python_files}
%doc CHANGES.rst README.rst
%license LICENSE.txt
%{python_sitelib}/*

%changelog
