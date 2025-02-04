#
# spec file for package python-numpydoc
#
# Copyright (c) 2025 SUSE LLC
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


Name:           python-numpydoc
Version:        1.8.0
Release:        0
Summary:        Sphinx extension to support docstrings in Numpy format
License:        BSD-3-Clause
Group:          Development/Languages/Python
URL:            https://github.com/numpy/numpydoc
Source:         https://files.pythonhosted.org/packages/source/n/numpydoc/numpydoc-%{version}.tar.gz
# https://docs.python.org/3/objects.inv (changes from time to time, accessed 2024-02-29)
Source1:        python-objects.inv
# PATCH-FIX-UPSTREAM numpydoc-pr523-py312deprecation.patch gh#numpy/numpydoc#523
Patch0:         numpydoc-pr523-py312deprecation.patch
# PATCH-FIX-UPSTREAM https://github.com/numpy/numpydoc/pull/586 MAINT: Add _exception_on_warning to MockApp
Patch1:         mockapp.patch
BuildRequires:  %{python_module Sphinx >= 5}
BuildRequires:  %{python_module base >= 3.8}
BuildRequires:  %{python_module pip}
BuildRequires:  %{python_module setuptools}
BuildRequires:  %{python_module tabulate >= 0.8.10}
BuildRequires:  %{python_module wheel}
BuildRequires:  fdupes
BuildRequires:  python-rpm-macros
Requires(post): update-alternatives
Requires(postun): update-alternatives
Requires:       python-Sphinx >= 5
Requires:       python-tabulate >= 0.8.10
BuildArch:      noarch
# SECTION test requirements
BuildRequires:  %{python_module pytest}
BuildRequires:  %{python_module matplotlib}
# /SECTION
%python_subpackages

%description
Numpy's documentation uses several custom extensions to Sphinx.  These
are shipped in this numpydoc package, in case you want to make use
of them in third-party projects.

%prep
%autosetup -p1 -n numpydoc-%{version}
# remove interpreter line. This script has no main section
sed -i '1 {/env python/ d}' numpydoc/validate.py
# don't check coverage
sed -i 's/--cov[^ ]*//g' pyproject.toml
# provide the python doc inventory locally
sed -i "\|https://docs.python.org/3| s|None|'%{SOURCE1}'|" numpydoc/tests/tinybuild/conf.py

%build
%pyproject_wheel

%install
%pyproject_install
%python_clone -a %{buildroot}%{_bindir}/numpydoc
%python_expand %fdupes %{buildroot}%{$python_sitelib}

%check
%pytest

%post
%python_install_alternative numpydoc

%postun
%python_uninstall_alternative numpydoc

%files %{python_files}
%license LICENSE.txt
%doc README.rst
%python_alternative %{_bindir}/numpydoc
%{python_sitelib}/numpydoc/
%{python_sitelib}/numpydoc-%{version}.dist-info

%changelog
