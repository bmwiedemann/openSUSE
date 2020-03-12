#
# spec file for package python-panflute
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
Name:           python-panflute
Version:        1.12.5
Release:        0
Summary:        Pandoc filters package for Python
License:        BSD-3-Clause
Group:          Development/Languages/Python
URL:            https://github.com/sergiocorreia/panflute
Source:         https://files.pythonhosted.org/packages/source/p/panflute/panflute-%{version}.tar.gz
BuildRequires:  %{python_module setuptools}
BuildRequires:  fdupes
BuildRequires:  python-rpm-macros
# SECTION test requirements
BuildRequires:  %{python_module PyYAML}
BuildRequires:  %{python_module click}
BuildRequires:  %{python_module future}
BuildRequires:  %{python_module pytest-cov}
BuildRequires:  %{python_module pytest}
BuildRequires:  python-configparser
BuildRequires:  python-shutilwhich
# /SECTION
Requires:       python-PyYAML
Requires:       python-click
Requires:       python-future
%ifpython2
Requires:       python-shutilwhich
%endif
BuildArch:      noarch

%python_subpackages

%description
Panflute is a Python package for writing Pandoc filters.

%prep
%setup -q -n panflute-%{version}

%build
%python_build

%install
%python_install
%python_expand %fdupes %{buildroot}%{$python_sitelib}
sed -i 's|shutilwhich||' %{buildroot}%{python3_sitelib}/panflute-*.egg-info/requires.txt

%files %{python_files}
%doc README.md
%license LICENSE
%python3_only %{_bindir}/panflute
%python3_only %{_bindir}/panfl
%{python_sitelib}/*

%changelog
