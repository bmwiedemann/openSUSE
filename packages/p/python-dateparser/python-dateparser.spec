#
# spec file for package python-dateparser
#
# Copyright (c) 2023 SUSE LLC
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
Version:        1.1.5
Release:        0
Summary:        Date parsing library designed to parse dates from HTML pages
License:        BSD-3-Clause
URL:            https://github.com/scrapinghub/dateparser
Source:         https://files.pythonhosted.org/packages/source/d/dateparser/dateparser-%{version}.tar.gz
# PATCH-FIX-UPSTREAM mark-network-tests.patch gh#scrapinghub/dateparser#1059 mcepl@suse.com
# mark test requiring network access
Patch1:         mark-network-tests.patch
BuildRequires:  %{python_module setuptools}
BuildRequires:  fdupes
BuildRequires:  python-rpm-macros
Requires:       python-python-dateutil
Requires:       python-pytz
Requires:       python-regex
Requires:       python-tzlocal
Recommends:     convertdate
Recommends:     python-fasttext
Recommends:     python-langdetect
Recommends:     python-ruamel.yaml
BuildArch:      noarch
# SECTION test requirements
BuildRequires:  %{python_module GitPython}
BuildRequires:  %{python_module convertdate}
BuildRequires:  %{python_module fasttext}
BuildRequires:  %{python_module langdetect}
BuildRequires:  %{python_module parameterized}
BuildRequires:  %{python_module pytest}
BuildRequires:  %{python_module python-dateutil}
BuildRequires:  %{python_module pytz}
BuildRequires:  %{python_module regex}
BuildRequires:  %{python_module ruamel.yaml}
BuildRequires:  %{python_module tzlocal}
# /SECTION
Requires(post): update-alternatives
Requires(postun):update-alternatives
%python_subpackages

%description
Date parsing library designed to parse dates from HTML pages

%prep
%autosetup -p1 -n dateparser-%{version}

# not py3 compatible and weird license of the imported module
rm tests/test_hijri.py
rm dateparser/calendars/hijri*

sed -i '1{/\/usr\/bin\/env python/d;}' \
    dateparser_scripts/update_supported_languages_and_locales.py

%build
%python_build

%install
%python_install
%python_clone -a %{buildroot}%{_bindir}/dateparser-download
%python_expand %fdupes %{buildroot}%{$python_sitelib}

%check
export NO_NETWORK=1
# Requires files not shipped in PyPI sdist
ignoretestfiles="--ignore tests/test_dateparser_data_integrity.py"
# https://github.com/scrapinghub/dateparser/issues/1053
ignoretestfiles="$ignoretestfiles --ignore tests/test_search.py"
%pytest $ignoretestfiles

%post
%python_install_alternative dateparser-download

%postun
%python_uninstall_alternative dateparser-download

%files %{python_files}
%doc AUTHORS.rst README.rst
%license LICENSE
%python_alternative %{_bindir}/dateparser-download
%{python_sitelib}/dateparser
%{python_sitelib}/dateparser_cli
%{python_sitelib}/dateparser_data
%{python_sitelib}/dateparser_scripts
%{python_sitelib}/dateparser-%{version}*-info

%changelog
