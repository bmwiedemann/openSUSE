#
# spec file for package python-LTTL
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
Name:           python-LTTL
Version:        2.0.12
Release:        0
Summary:        Library for text processing and analysis
License:        GPL-3.0-only
URL:            https://github.com/axanthos/LTTL
Source:         https://files.pythonhosted.org/packages/source/L/LTTL/LTTL-%{version}.zip
BuildRequires:  %{python_module setuptools}
BuildRequires:  fdupes
BuildRequires:  python-rpm-macros
BuildRequires:  unzip
Requires:       python-future
Requires:       python-numpy
Requires:       python-scipy
BuildArch:      noarch
# SECTION test requirements
BuildRequires:  %{python_module future}
BuildRequires:  %{python_module numpy}
BuildRequires:  %{python_module pytest}
BuildRequires:  %{python_module scipy}
# /SECTION
%python_subpackages

%description
LangTech Text Library (LTTL) for text processing and analysis

%prep
%setup -q -n LTTL-%{version}
sed -i 's/\r$//' README.rst

%build
%python_build

%install
%python_install
%python_expand %fdupes %{buildroot}%{$python_sitelib}

%check
%pytest

%files %{python_files}
%doc README.rst
%license LICENSE
%{python_sitelib}/*

%changelog
