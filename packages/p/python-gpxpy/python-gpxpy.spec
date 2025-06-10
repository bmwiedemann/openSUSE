#
# spec file for package python-gpxpy
#
# Copyright (c) 2025 SUSE LLC
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
Name:           python-gpxpy
Version:        1.6.2
Release:        0
Summary:        GPX file parser and GPS track manipulation library
License:        Apache-2.0
Group:          Development/Languages/Python
URL:            https://github.com/tkrajina/gpxpy
Source:         https://files.pythonhosted.org/packages/source/g/gpxpy/gpxpy-%{version}.tar.gz
BuildRequires:  %{python_module pip}
BuildRequires:  %{python_module setuptools}
BuildRequires:  %{python_module wheel}
BuildRequires:  alts
BuildRequires:  fdupes
BuildRequires:  python-rpm-macros
Requires:       alts
BuildArch:      noarch
%python_subpackages

%description
A Python library for parsing and manipulating GPX files.
GPX is an XML based format for GPS tracks.

%prep
%setup -q -n gpxpy-%{version}

%build
%pyproject_wheel

%install
%pyproject_install
%python_clone -a %{buildroot}%{_bindir}/gpxinfo
%python_expand %fdupes %{buildroot}%{$python_sitelib}

%check
%pyunittest discover -v

%pre
%python_libalternatives_reset_alternative gpxinfo

%files %{python_files}
%license LICENSE.txt
%doc README.md
%python_alternative %{_bindir}/gpxinfo
%{python_sitelib}/gpxpy
%{python_sitelib}/gpxpy-%{version}*-info

%changelog
