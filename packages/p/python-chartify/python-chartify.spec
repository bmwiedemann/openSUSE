#
# spec file for package python-chartify
#
# Copyright (c) 2021 SUSE LLC
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
# NEP29: TW does not have python36-scipy anymore
%define         skip_python36 1
Name:           python-chartify
Version:        3.0.3
Release:        0
Summary:        Python library for plotting charts
License:        Apache-2.0
URL:            https://github.com/spotify/chartify
Source:         https://github.com/spotify/chartify/archive/%{version}.tar.gz#/chartify-%{version}.tar.gz
BuildRequires:  %{python_module setuptools}
BuildRequires:  fdupes
BuildRequires:  python-rpm-macros
Requires:       python-Pillow >= 6.2.0
Requires:       python-bokeh >= 2.0.0
Requires:       python-ipykernel >= 5.0
Requires:       python-ipython >= 7.0
Requires:       python-pandas >= 1.0.0
Requires:       python-scipy >= 1.0.0
# ignoring https://github.com/SeleniumHQ/selenium/issues/5296
Requires:       python-selenium >= 3.7.0
BuildArch:      noarch
# SECTION test requirements
BuildRequires:  %{python_module Pillow >= 6.2.0}
BuildRequires:  %{python_module bokeh >= 2.0.0}
BuildRequires:  %{python_module ipykernel >= 5.0}
BuildRequires:  %{python_module ipython >= 7.0}
BuildRequires:  %{python_module pandas >= 1.0.0}
BuildRequires:  %{python_module pytest}
BuildRequires:  %{python_module scipy >= 1.0.0}
BuildRequires:  %{python_module selenium >= 3.7.0}
# /SECTION
%python_subpackages

%description
Chartify is a Python library for creating charts.

%prep
%setup -q -n chartify-%{version}
rm tox.ini

%build
%python_build

%install
%python_install
%python_expand %fdupes %{buildroot}%{$python_sitelib}

%check
%pytest

%files %{python_files}
%doc AUTHORS.rst README.rst
%license LICENSE
%{python_sitelib}/*

%changelog
