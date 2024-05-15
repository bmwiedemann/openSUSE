#
# spec file for package python-sox
#
# Copyright (c) 2024 SUSE LLC
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


Name:           python-sox
Version:        1.5.0
Release:        0
License:        BSD-3-Clause
Summary:        Python wrapper around SoX
URL:            https://github.com/rabitt/pysox
Group:          Development/Languages/Python
Source:         https://github.com/marl/pysox/archive/v%{version}/sox-%{version}.tar.gz
BuildRequires:  %{python_module numpy}
BuildRequires:  %{python_module pytest}
BuildRequires:  %{python_module setuptools}
BuildRequires:  %{python_module soundfile}
BuildRequires:  %{python_module typing-extensions}
BuildRequires:  fdupes
BuildRequires:  python-rpm-macros
BuildRequires:  sox
Requires:       python-numpy
Requires:       python-typing-extensions
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
%autosetup -p1 -n pysox-%{version}
sed -i -e '/^#!\//, 1d' sox/*.py

%build
%python_build

%install
%python_install
%python_expand %fdupes %{buildroot}%{$python_sitelib}

%check
# Fails in i586
donttest="test_multichannel or test_valid"
%pytest -k "not ($donttest)"

%files %{python_files}
%license LICENSE
%{python_sitelib}/sox-%{version}*-info/
%{python_sitelib}/sox

%changelog
