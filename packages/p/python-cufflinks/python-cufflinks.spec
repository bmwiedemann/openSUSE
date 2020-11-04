#
# spec file for package python-cufflinks
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
Name:           python-cufflinks
Version:        0.17.3
Release:        0
Summary:        Productivity Tools for Plotly + Pandas
License:        MIT
URL:            https://github.com/santosjorge/cufflinks
Source:         https://files.pythonhosted.org/packages/source/c/cufflinks/cufflinks-%{version}.tar.gz
BuildRequires:  %{python_module setuptools >= 34.4.1}
BuildRequires:  fdupes
BuildRequires:  python-rpm-macros
Requires:       python-colorlover >= 0.2.1
Requires:       python-numpy >= 1.9.2
Requires:       python-pandas >= 0.19.2
Requires:       python-plotly >= 4.1.1
Requires:       python-six >= 1.9.0
Recommends:     python-ipython >= 5.3.0
Recommends:     python-ipywidgets >= 7.0.0
BuildArch:      noarch
# SECTION test requirements
BuildRequires:  %{python_module colorlover >= 0.2.1}
BuildRequires:  %{python_module ipython >= 5.3.0}
BuildRequires:  %{python_module ipywidgets >= 7.0.0}
BuildRequires:  %{python_module nose >= 1.3.7}
BuildRequires:  %{python_module numpy >= 1.9.2}
BuildRequires:  %{python_module pandas >= 0.19.2}
BuildRequires:  %{python_module plotly >= 4.1.1}
BuildRequires:  %{python_module six >= 1.9.0}
# /SECTION
%python_subpackages

%description
This library binds the plotly with pandas for plotting.

%prep
%setup -q -n cufflinks-%{version}

%build
%python_build

%install
%python_install
%python_expand %fdupes %{buildroot}%{$python_sitelib}

%files %{python_files}
%doc README.md
%license license.txt
%{python_sitelib}/*

%changelog
