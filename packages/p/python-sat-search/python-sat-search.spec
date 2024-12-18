#
# spec file for package python-sat-search
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


%{?sle15_python_module_pythons}
%define packagename sat-search
Name:           python-sat-search
Version:        0.3.0
Release:        0
Summary:        A tool for discovering and downloading publicly available satellite imagery
License:        MIT
URL:            https://github.com/sat-utils/sat-search
Source:         https://files.pythonhosted.org/packages/source/s/sat-search/sat-search-%{version}.tar.gz
Source99:       https://raw.githubusercontent.com/sat-utils/sat-search/master/LICENSE
# PATCH-FIX-UPSTREAM gh#sat-utils/sat-search#136
Patch0:         use-importlib.patch
BuildRequires:  %{python_module pip}
BuildRequires:  %{python_module pytest >= 2.8.2}
BuildRequires:  %{python_module sat-stac}
BuildRequires:  %{python_module setuptools}
BuildRequires:  %{python_module wheel}
BuildRequires:  fdupes
BuildRequires:  python-rpm-macros
Requires:       python-sat-stac
Requires(post): update-alternatives
Requires(postun): update-alternatives
BuildArch:      noarch
%python_subpackages

%description
Sat-search is a Python 3 library and a command line tool for discovering
and downloading publicly available satellite imagery using a conformant
API such as sat-api.

%prep
%autosetup -p1 -n %{packagename}-%{version}
cp %{SOURCE99} .

sed -i -e '/pytest-runner/d' setup.py

%build
%pyproject_wheel

%install
%pyproject_install
for p in %{packagename} ; do
    %python_clone -a %{buildroot}%{_bindir}/$p
done
%python_expand rm -r %{buildroot}%{$python_sitelib}/test
%python_expand %fdupes %{buildroot}%{$python_sitelib}
%prepare_alternative %{packagename}

%post
%python_install_alternative %{packagename}

%postun
%python_uninstall_alternative %{packagename}

%check
# polls server for data for searching
#%%pytest

%files %{python_files}
%doc README.md
%license LICENSE
%python_alternative %{_bindir}/%{packagename}
%{python_sitelib}/satsearch
%{python_sitelib}/sat_search-%{version}.dist-info

%changelog
