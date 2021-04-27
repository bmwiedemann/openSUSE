#
# spec file for package python-snuggs
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
%define         skip_python36 1
Name:           python-snuggs
Version:        1.4.7
Release:        0
Summary:        S-expressions tool for Numpy
License:        MIT
Group:          Development/Languages/Python
URL:            https://github.com/mapbox/snuggs
Source:         https://files.pythonhosted.org/packages/source/s/snuggs/snuggs-%{version}.tar.gz
BuildRequires:  %{python_module setuptools}
BuildRequires:  fdupes
BuildRequires:  python-rpm-macros
Requires:       python-numpy
Requires:       python-pyparsing
BuildArch:      noarch
# SECTION test requirements
BuildRequires:  %{python_module hypothesis}
BuildRequires:  %{python_module numpy}
BuildRequires:  %{python_module pyparsing}
BuildRequires:  %{python_module pytest}
# /SECTION
%python_subpackages

%description
Snuggs are s-expressions for Numpy.

%prep
%setup -q -n snuggs-%{version}

%build
%python_build

%install
%python_install
%python_expand %fdupes %{buildroot}%{$python_sitelib}

%check
%python_expand pytest-%{$python_bin_suffix} test_snuggs.py

%files %{python_files}
%doc AUTHORS.txt CHANGES.txt README.rst
%license LICENSE
%{python_sitelib}/*

%changelog
