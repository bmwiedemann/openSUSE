#
# spec file for package python-mplcursors
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
Name:           python-mplcursors
Version:        0.3
Release:        0
Summary:        Interactive data selection cursors for Matplotlib
License:        MIT
URL:            https://github.com/anntzer/mplcursors
Source:         https://files.pythonhosted.org/packages/source/m/mplcursors/mplcursors-%{version}.tar.gz
BuildRequires:  %{python_module setuptools_scm}
BuildRequires:  %{python_module setuptools}
BuildRequires:  fdupes
BuildRequires:  python-rpm-macros
Requires:       python-matplotlib >= 2.1
BuildArch:      noarch
# SECTION test requirements
BuildRequires:  %{python_module matplotlib >= 2.1}
BuildRequires:  %{python_module pytest < 5}
# /SECTION
%python_subpackages

%description
mplcursors provides interactive data selection cursors for Matplotlib.

%prep
%setup -q -n mplcursors-%{version}

%build
%python_build

%install
%python_install
%python_expand %fdupes %{buildroot}%{$python_sitelib}

%check
%pytest

%files %{python_files}
%doc CHANGELOG.rst README.rst
%license LICENSE.txt
%{python_sitelib}/*

%changelog
