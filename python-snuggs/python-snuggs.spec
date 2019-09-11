#
# spec file for package python-snuggs
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

# Please submit bugfixes or comments via http://bugs.opensuse.org/


%{?!python_module:%define python_module() python-%{**} python3-%{**}}
Name:           python-snuggs
Version:        1.4.3
Release:        0
License:        MIT
Summary:        S-expressions tool for Numpy
Url:            https://github.com/mapbox/snuggs
Group:          Development/Languages/Python
Source:         https://files.pythonhosted.org/packages/source/s/snuggs/snuggs-%{version}.tar.gz
BuildRequires:  python-rpm-macros
BuildRequires:  %{python_module setuptools}
# SECTION test requirements
BuildRequires:  %{python_module numpy}
BuildRequires:  %{python_module pyparsing}
BuildRequires:  %{python_module pytest}
# /SECTION
BuildRequires:  fdupes
Requires:       python-numpy
Requires:       python-pyparsing
BuildArch:      noarch

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
