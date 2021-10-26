#
# spec file for package python-sox
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
Name:           python-sox
Version:        1.4.1
Release:        0
License:        BSD-3-Clause
Summary:        Python wrapper around SoX
URL:            https://github.com/rabitt/pysox
Group:          Development/Languages/Python
Source0:        https://files.pythonhosted.org/packages/py2.py3/s/sox/sox-%{version}-py2.py3-none-any.whl
BuildRequires:  %{python_module pip}
BuildRequires:  fdupes
BuildRequires:  python-rpm-macros
Requires:       sox
BuildArch:      noarch

%python_subpackages

%description
SOX is intended to be the Swiss Army knife of sound processing tools.
It does many things, it just does not do them all well. Sooner or later
it will come in very handy. SOX is really only usable day-to-day if you
hide the wacky options with one-line shell scripts.

This is a Python wrapper for SOX.

%prep
%setup -q -c -T

%build
# not needed

%install
cp -a %{SOURCE0} .
%pyproject_install
%python_expand sed -i -e '/^#!\//, 1d' %{buildroot}%{$python_sitelib}/sox/*.py
%python_expand %fdupes %{buildroot}%{$python_sitelib}

%files %{python_files}
%license %{python_sitelib}/sox-%{version}.dist-info/LICENSE
%{python_sitelib}/sox-%{version}.dist-info/
%{python_sitelib}/sox

%changelog
