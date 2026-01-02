#
# spec file for package python-dateparser
#
# Copyright (c) 2026 SUSE LLC and contributors
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


%if 0%{?suse_version} > 1500
%bcond_without libalternatives
%else
%bcond_with libalternatives
%endif
%{?sle15_python_module_pythons}
Name:           python-dateparser
Version:        1.2.2
Release:        0
Summary:        Date parsing library designed to parse dates from HTML pages
License:        BSD-3-Clause
URL:            https://github.com/scrapinghub/dateparser
Source:         https://files.pythonhosted.org/packages/source/d/dateparser/dateparser-%{version}.tar.gz
# PATCH-FIX-UPSTREAM mark-network-tests.patch gh#scrapinghub/dateparser#1059 mcepl@suse.com
# mark test requiring network access
Patch1:         mark-network-tests.patch
# PATCH-FIX-UPSTREAM https://github.com/scrapinghub/dateparser/pull/1294 use current year in test_search_dates_with_prepositions
Patch2:         happy-new-year.patch
BuildRequires:  %{python_module pip}
BuildRequires:  %{python_module wheel}
BuildRequires:  fdupes
BuildRequires:  python-rpm-macros
Requires:       python-python-dateutil >= 2.7.0
Requires:       python-pytz >= 2024.2
Requires:       python-regex >= 2024.9.11
Requires:       python-tzlocal >= 0.2
Recommends:     python-convertdate
Recommends:     python-fasttext
Recommends:     python-langdetect
Recommends:     python-ruamel.yaml
BuildArch:      noarch
%if %{with libalternatives}
BuildRequires:  alts
Requires:       alts
%else
Requires(post): update-alternatives
Requires(postun): update-alternatives
%endif
# SECTION test requirements
BuildRequires:  %{python_module convertdate}
BuildRequires:  %{python_module fasttext}
BuildRequires:  %{python_module langdetect}
BuildRequires:  %{python_module parameterized}
BuildRequires:  %{python_module pytest}
BuildRequires:  %{python_module python-dateutil >= 2.7.0}
BuildRequires:  %{python_module pytz >= 2024.2}
BuildRequires:  %{python_module regex >= 2024.9.11}
BuildRequires:  %{python_module ruamel.yaml}
BuildRequires:  %{python_module tzlocal >= 0.2}
# /SECTION
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
%pyproject_wheel

%install
%pyproject_install
%python_clone -a %{buildroot}%{_bindir}/dateparser-download
%python_expand %fdupes %{buildroot}%{$python_sitelib}

%check
export NO_NETWORK=1
# Requires files not shipped in PyPI sdist
ignoretestfiles="--ignore tests/test_dateparser_data_integrity.py"
# overflow on 32bit
donttest="(not test_timezone_offset_calculation)"
%pytest -k "$donttest" $ignoretestfiles

%pre
%python_libalternatives_reset_alternative dateparser-download

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
