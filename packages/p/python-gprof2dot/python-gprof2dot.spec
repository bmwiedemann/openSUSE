#
# spec file for package python-gprof2dot
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
Name:           python-gprof2dot
Version:        2017.9.19
Release:        0
%define gitver  2017.09.19
Summary:        Script to generate a dot graph from the output of several profilers
License:        LGPL-3.0-or-later
Group:          Development/Languages/Python
Url:            https://github.com/jrfonseca/gprof2dot
Source:         https://files.pythonhosted.org/packages/source/g/gprof2dot/gprof2dot-%{version}.tar.gz
Source10:       https://raw.githubusercontent.com/jrfonseca/gprof2dot/%{gitver}/LICENSE.txt
BuildRequires:  %{python_module setuptools}
BuildRequires:  fdupes
BuildRequires:  python-rpm-macros
BuildArch:      noarch

%python_subpackages

%description
GProf2Dot.py is a Python script to convert the output from many
profilers into a dot graph.

%prep
%setup -q -n gprof2dot-%{version}
cp %{SOURCE10} .
sed -i -e '/^#!\//, 1d' gprof2dot.py 

%build
%python_build

%install
%python_install
%python_expand %fdupes %{buildroot}%{$python_sitelib}

%files %{python_files}
%license LICENSE.txt
%python3_only %{_bindir}/gprof2dot
%{python_sitelib}/*

%changelog
