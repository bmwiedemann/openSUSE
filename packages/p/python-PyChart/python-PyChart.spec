#
# spec file for package python-PyChart
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
#


%{?!python_module:%define python_module() python-%{**} python3-%{**}}
Name:           python-PyChart
Version:        1.39
Release:        0
Summary:        Python Chart Generator
Group:          Development/Languages/Python
License:        GPL-2.0-or-later
URL:            http://home.gna.org/pychart/
Source:         PyChart-%{version}.tar.gz
BuildRequires:  python-rpm-macros
BuildRequires:  fdupes
BuildRequires:  %{python_module setuptools}
BuildArch:      noarch
%python_subpackages

%description
Pychart is a Python library for creating high-quality
charts in Postscript, PDF, PNG, and SVG.
It produces line plots, bar plots, range-fill plots, and pie
charts.

%prep
%setup -q -n PyChart-%{version}
find demos/ -exec sed -i 's/\r$//' {} \;

%build
%python_build

%install
%python_install
%python_expand %fdupes %{buildroot}%{$python_sitelib}

%files %{python_files}
%license COPYING
%doc README demos
%{python_sitelib}/*

%changelog
