#
# spec file for package python-rstcheck
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
Name:           python-rstcheck
Version:        3.3.1
Release:        0
Summary:        Python module to check syntax of reStructuredText
License:        MIT
URL:            https://github.com/myint/rstcheck
Source:         https://files.pythonhosted.org/packages/source/r/rstcheck/rstcheck-%{version}.tar.gz
Source1:        https://github.com/myint/rstcheck/archive/v%{version}.tar.gz
Patch0:         test-path.patch
BuildRequires:  %{python_module Sphinx}
BuildRequires:  %{python_module docutils >= 0.7}
BuildRequires:  %{python_module setuptools}
BuildRequires:  bash
BuildRequires:  fdupes
BuildRequires:  gcc
BuildRequires:  gcc-c++
BuildRequires:  python-rpm-macros
Requires:       python-docutils >= 0.7
Requires(post): update-alternatives
Requires(postun): update-alternatives
Recommends:     bash
Recommends:     gcc
Recommends:     gcc-c++
Recommends:     python-Sphinx
BuildArch:      noarch
%ifpython3
Provides:       rstcheck = %{version}
Obsoletes:      rstcheck
%endif
%python_subpackages

%description
A Python module to check the syntax of reStructuredText and code
blocks nested within it.

%prep
%setup -q -n rstcheck-%{version}
tar --wildcards --strip-components=1 -xzf %{SOURCE1} rstcheck-%{version}/test* rstcheck-%{version}/examples
sed -i -e '/^#!\//, 1d' rstcheck.py
%patch0 -p1

%build
%python_build

%install
%python_install
%python_clone -a %{buildroot}%{_bindir}/rstcheck
%python_expand %fdupes %{buildroot}%{$python_sitelib}

%check
# LANG needed for Leap
export LANG=en_US.UTF-8
# This is testing the source copy of rstcheck.py, not the installed version,
# but at least that sanity checks the build dependencies.
#%%{python_expand # complements test-path.patch
#PYTHON=$python ./test.bash
#}

%post
%python_install_alternative rstcheck

%postun
%python_uninstall_alternative rstcheck

%files %{python_files}
%license LICENSE
%doc AUTHORS.rst README.rst
%python_alternative %{_bindir}/rstcheck
%{python_sitelib}/*

%changelog
