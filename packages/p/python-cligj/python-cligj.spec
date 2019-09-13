#
# spec file for package python-cligj
#
# Copyright (c) 2019 SUSE LINUX GmbH, Nuernberg, Germany.
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


%{?!python_module:%define python_module() python-%{**} python3-%{**}}
Name:           python-cligj
Version:        0.5.0
Release:        0
License:        BSD-3-Clause
Summary:        Click params for commmand line interfaces to GeoJSON
Url:            https://github.com/mapbox/cligj
Group:          Development/Languages/Python
# pypi source lack license and tests
Source:         https://github.com/mapbox/cligj/archive/%{version}.tar.gz#/cligj-%{version}.tar.gz
BuildRequires:  %{python_module setuptools}
BuildRequires:  fdupes
BuildRequires:  python-rpm-macros
# SECTION test requirements
BuildRequires:  %{python_module click}
BuildRequires:  %{python_module pytest}
# /SECTION
Requires:       python-click
BuildArch:      noarch


%python_subpackages

%description
Common arguments and options for GeoJSON processing commands, using Click.

%prep
%setup -q -n cligj-%{version}
# Fix script-without-shebang
chmod a-x LICENSE

%build
%python_build

%install
%python_install
%python_expand %fdupes %{buildroot}%{$python_sitelib}

%check
export LC_ALL=en_US.UTF-8
export LANG=en_US.UTF-8
%{python_expand export PYTHONPATH=%{buildroot}%{$python_sitelib}
py.test-%{$python_bin_suffix}
}

%files %{python_files}
%license LICENSE
%{python_sitelib}/*

%changelog
