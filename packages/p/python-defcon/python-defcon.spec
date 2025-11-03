#
# spec file for package python-defcon
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


%{?sle15_python_module_pythons}
Name:           python-defcon
Version:        0.12.2
Release:        0
Summary:        A set of UFO based objects for use in font editing applications
License:        MIT
URL:            https://github.com/robotools/defcon
Source:         https://files.pythonhosted.org/packages/source/d/defcon/defcon-%{version}.tar.gz
BuildRequires:  %{python_module pip}
BuildRequires:  %{python_module setuptools_scm}
BuildRequires:  %{python_module setuptools}
BuildRequires:  %{python_module wheel}
BuildRequires:  fdupes
BuildRequires:  python-rpm-macros
Requires:       python-FontTools >= 4.59.0
# SECTION fonttools[ufo,unicode]
Requires:       python-fs >= 2.2
%if 0%{?python_version_nodots} < 39
Requires:       python-unicodedata2 >= 13.0.0
%endif
# /SECTION
Suggests:       python-fontPens >= 0.1.0
BuildArch:      noarch
# SECTION test requirements
BuildRequires:  %{python_module FontTools >= 4.59.0}
BuildRequires:  %{python_module fs >= 2.2}
BuildRequires:  %{python_module pytest >= 3.0.3}
BuildRequires:  %{python_module unicodedata2 >= 13.0.0 if %python-base < 3.9}
# /SECTION
%python_subpackages

%description
A set of UFO based objects optimized for use in font editing applications.

%prep
%setup -q -n defcon-%{version}
sed -i -e '1{\,^#!%{_bindir}/env python,d}' Lib/defcon/test/tools/test_unicodeTools.py

%build
%pyproject_wheel

%install
%pyproject_install
%python_expand %fdupes %{buildroot}%{$python_sitelib}

%check
%pytest

%files %{python_files}
%doc README.rst
%license License.txt
%{python_sitelib}/defcon
%{python_sitelib}/defcon-%{version}*-info

%changelog
