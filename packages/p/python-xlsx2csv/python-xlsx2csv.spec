#
# spec file for package python-xlsx2csv
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


%bcond_without libalternatives
Name:           python-xlsx2csv
Version:        0.8.6
Release:        0
Summary:        Tool to convert from xlsx to csv
License:        MIT
URL:            https://github.com/dilshod/xlsx2csv
Source:         https://files.pythonhosted.org/packages/source/x/xlsx2csv/xlsx2csv-%{version}.tar.gz
BuildRequires:  %{python_module pip >= 23 }
BuildRequires:  %{python_module setuptools_scm}
BuildRequires:  %{python_module setuptools}
BuildRequires:  alts
BuildRequires:  fdupes
Requires:       alts
Provides:       xlsx2csv = %{version}
Obsoletes:      xlsx2csv < %{version}
Conflicts:      perl-Spreadsheet-Read-scripts
BuildArch:      noarch
%python_subpackages

%description
A tool to convert xlsx files to the csv format.

%prep
%autosetup -n xlsx2csv-%{version}
sed -i -e '/^#!/d' xlsx2csv.py

%build
%pyproject_wheel
pushd man
%make_build
popd

%install
%pyproject_install
install -Dm0644 man/xlsx2csv.1 %{buildroot}%{_mandir}/man1/xlsx2csv.1
%python_clone -a %{buildroot}%{_bindir}/xlsx2csv
%python_clone -a %{buildroot}%{_mandir}/man1/xlsx2csv.1
%python_expand %fdupes %{buildroot}%{$python_sitelib}

%check
%python_expand $python ./test/run

%files %{python_files}
%license LICENSE.txt
%doc CHANGELOG README.md
%python_alternative %{_bindir}/xlsx2csv
%python_alternative %{_mandir}/man1/xlsx2csv.1%{?ext_man}
%pycache_only %{python_sitelib}/__pycache__/xlsx2csv.cpython-*.pyc
%{python_sitelib}/xlsx2csv.py
%{python_sitelib}/xlsx2csv-%{version}.dist-info

%changelog
