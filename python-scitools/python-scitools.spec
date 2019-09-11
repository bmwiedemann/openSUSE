#
# spec file for package python-scitools
#
# Copyright (c) 2018 SUSE LINUX GmbH, Nuernberg, Germany.
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
#


%define skip_python3 1

%{?!python_module:%define python_module() python-%{**} python3-%{**}}
%define modname scitools

Name:           python-%{modname}
Version:        0.9.0
Release:        0
Summary:        A Python package containing lots of useful tools for scientific
License:        BSD-3-Clause AND GPL-2.0-or-later
Group:          Development/Libraries/Python
URL:            https://github.com/hplgit/scitools
Source0:        https://github.com/hplgit/%{modname}/archive/%{modname}-%{version}.tar.gz
BuildArch:      noarch
BuildRequires:  %{python_module devel}
BuildRequires:  %{python_module matplotlib}
BuildRequires:  fdupes
BuildRequires:  gnuplot
BuildRequires:  python-rpm-macros
Requires:       python-numpy
%python_subpackages

%description
SciTools is a Python package containing lots of useful tools for
scientific computing in Python. The package is built on top of other
widely used packages such as NumPy, SciPy, ScientificPython, Gnuplot,
etc.

%prep
%setup -q -n %{modname}-%{modname}-%{version}

%build
%python_build
find . -name "*.py" -exec sed -i "/#!\/usr\/bin.*/d" {} \;

%install
%python_install
%python_expand %fdupes %{buildroot}%{$python_sitelib}

%files %{python_files}
%license LICENSE
%doc ChangeLog README
%{_bindir}/scitools
%{_mandir}/man1/scitools.1%{?ext_man}
%{python_sitelib}/scitools/
%{python_sitelib}/SciTools-%{version}-py%{python_version}.egg-info

%changelog
