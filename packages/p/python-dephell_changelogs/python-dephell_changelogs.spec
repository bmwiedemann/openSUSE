#
# spec file for package python-dephell_changelogs
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
%define skip_python2 1
%define modname dephell_changelogs
Name:           python-dephell_changelogs
Version:        0.0.1
Release:        0
Summary:        Pathlib for changelogss
License:        MIT
URL:            https://github.com/dephell/dephell_changelogs
Source0:        https://github.com/dephell/%{modname}/archive/v.%{version}.tar.gz#/%{modname}-%{version}.tar.gz
# Temporary measure, until dephell in %%prep actually works gh#dephell/dephell_changelogs#5
Source1:        setup.py
# PATCH-FIX-UPSTREAM add_network_markers.patch gh#dephell/dephell_changelogs#4 mcepl@suse.com
# add markers for test cases requiring network connection
Patch0:         add_network_markers.patch
BuildRequires:  %{python_module base >= 3.5}
BuildRequires:  %{python_module pip}
BuildRequires:  %{python_module requests}
BuildRequires:  %{python_module setuptools}
BuildRequires:  %{python_module wheel}
BuildRequires:  fdupes
#BuildRequires:  python-dephell-rpm-macros
BuildRequires:  python-rpm-macros
Requires:       python-attrs
BuildArch:      noarch
# SECTION test requirements
BuildRequires:  %{python_module pytest-xdist}
BuildRequires:  %{python_module pytest}
# /SECTION
%python_subpackages

%description
Dephell library providing pathlib for changelogss.

%prep
%autosetup -p1 -n %{modname}-v.%{version}

%define dephell_loglevel DEBUG
# Temporarily switched off because of gh#dephell/dephell_changelogs#5
# %%dephell_gensetup
cp -p %{SOURCE1} .

%build
%python_build

%install
%python_install
%python_expand %fdupes %{buildroot}%{$python_sitelib}

%check
%pytest -m 'not network'

%files %{python_files}
%license LICENSE
%doc README.md
%{python_sitelib}/%{modname}*

%changelog
