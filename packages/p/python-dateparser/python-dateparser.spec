#
# spec file for package python-dateparser
#
# Copyright (c) 2021 SUSE LLC
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
Name:           python-dateparser
Version:        1.0.0
Release:        0
Summary:        Date parsing library designed to parse dates from HTML pages
License:        BSD-3-Clause
URL:            https://github.com/scrapinghub/dateparser
Source:         https://files.pythonhosted.org/packages/source/d/dateparser/dateparser-%{version}.tar.gz
BuildRequires:  %{python_module setuptools}
BuildRequires:  fdupes
BuildRequires:  python-rpm-macros
Requires:       python-python-dateutil
Requires:       python-pytz
Requires:       python-regex
Requires:       python-tzlocal
Recommends:     convertdate
Recommends:     python-jdatetime
Recommends:     python-ruamel.yaml
BuildArch:      noarch
# SECTION test requirements
BuildRequires:  %{python_module GitPython}
BuildRequires:  %{python_module convertdate}
BuildRequires:  %{python_module coverage}
BuildRequires:  %{python_module jdatetime}
BuildRequires:  %{python_module mock}
BuildRequires:  %{python_module parameterized}
BuildRequires:  %{python_module pytest}
BuildRequires:  %{python_module python-dateutil}
BuildRequires:  %{python_module pytz}
BuildRequires:  %{python_module regex}
BuildRequires:  %{python_module ruamel.yaml}
BuildRequires:  %{python_module six}
BuildRequires:  %{python_module tzlocal}
# /SECTION
%python_subpackages

%description
Date parsing library designed to parse dates from HTML pages

%prep
%setup -q -n dateparser-%{version}
# not py3 compatible and weird license of the imported module
rm tests/test_hijri.py
rm dateparser/calendars/hijri*
# Requires files not shipped in PyPi tarball
rm tests/test_dateparser_data_integrity.py

%build
%python_build

%install
%python_install
%python_expand %fdupes %{buildroot}%{$python_sitelib}

%check
%pytest

%files %{python_files}
%doc AUTHORS.rst README.rst
%license LICENSE
%dir %{python_sitelib}/dateparser
%{python_sitelib}/dateparser/*
%dir %{python_sitelib}/dateparser_data
%{python_sitelib}/dateparser_data/*
%dir %{python_sitelib}/dateparser_scripts
%{python_sitelib}/dateparser_scripts/*
%{python_sitelib}/dateparser-%{version}-py*.egg-info

%changelog
