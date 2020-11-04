#
# spec file for package python-gwosc
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


%define modname gwosc
# Disable python2 until py2 tests are fixed
%define         skip_python2 1
Name:           python-gwosc
Version:        0.5.6
Release:        0
Summary:        Python interface to the Gravitational-Wave Open Data Center archive
License:        MIT
URL:            https://gwosc.readthedocs.io/en/latest/
# Don't use sources directly from github, see https://github.com/gwpy/gwosc/issues/55
Source:         https://pypi.io/packages/source/g/%{modname}/%{modname}-%{version}.tar.gz
BuildRequires:  %{python_module setuptools}
BuildRequires:  fdupes
BuildRequires:  python-rpm-macros
# SECTION For tests
BuildRequires:  %{python_module pytest}
BuildRequires:  %{python_module requests-mock}
# /SECTION
%python_subpackages

%description
The gwosc package provides an interface to querying the open data
releases hosted on https://gw-openscience.org from the GEO, LIGO, and
Virgo gravitational-wave observatories.

%prep
%setup -q -n %{modname}-%{version}

%build
%python_build

%install
%python_install

%python_expand %fdupes %{buildroot}%{$python_sitelib}/%{modname}/

%check
# requests_mock too old for 15.1
%if 0%{?suse_version} == 1500 && 0%{?sle_version} == 150100
%pytest -k "not remote and not test_fetch_json_local"
%else
%pytest -k "not remote"
%endif

%files %{python_files}
%license LICENSE
%doc README.md
%{python_sitelib}/%{modname}
%{python_sitelib}/%{modname}-%{version}-py%{python_version}.egg-info/

%changelog
