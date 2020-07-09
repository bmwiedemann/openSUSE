#
# spec file for package python-chart-studio
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
%define         skip_python2 1
Name:           python-chart-studio
Version:        1.1.0
Release:        0
Summary:        Utilities for Chart Studio
License:        MIT
Group:          Development/Languages/Python
URL:            https://plot.ly/python/
Source:         https://files.pythonhosted.org/packages/source/c/chart-studio/chart-studio-%{version}.tar.gz
BuildRequires:  %{python_module devel}
BuildRequires:  %{python_module setuptools}
BuildRequires:  python-rpm-macros
# SECTION test requirements
BuildRequires:  %{python_module plotly}
BuildRequires:  %{python_module requests}
BuildRequires:  %{python_module retrying >= 1.3.3}
BuildRequires:  %{python_module six}
# /SECTION
BuildRequires:  fdupes
Requires:       python-plotly
Requires:       python-requests
Requires:       python-retrying >= 1.3.3
Requires:       python-six
BuildArch:      noarch

%python_subpackages

%description
Utilities for interfacing with plotly's Chart Studio

%prep
%setup -q -n chart-studio-%{version}

%build
%python_build

%install
%python_install
%python_expand %fdupes %{buildroot}%{$python_sitelib}

%check
# no tests in PyPI tarball, github "release tarball" is not suitable for build

%files %{python_files}
%doc README.md
%{python_sitelib}/*

%changelog
