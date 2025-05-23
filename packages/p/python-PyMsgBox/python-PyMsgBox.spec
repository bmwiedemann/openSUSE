#
# spec file for package python-PyMsgBox
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


Name:           python-PyMsgBox
Version:        1.0.9
Release:        0
Summary:        A Python module for JavaScript-like message boxes
License:        BSD-3-Clause
Group:          Development/Languages/Python
URL:            https://github.com/asweigart/PyMsgBox
Source:         https://files.pythonhosted.org/packages/source/P/PyMsgBox/PyMsgBox-%{version}.tar.gz
Source99:       https://raw.githubusercontent.com/asweigart/PyMsgBox/master/LICENSE.txt
BuildRequires:  %{python_module pip}
BuildRequires:  %{python_module setuptools}
BuildRequires:  %{python_module wheel}
BuildRequires:  dos2unix
BuildRequires:  fdupes
BuildRequires:  python-rpm-macros
BuildRequires:  unzip
BuildArch:      noarch
%python_subpackages

%description
A pure Python module for JavaScript-like message boxes.

%prep
%setup -q -n PyMsgBox-%{version}
cp %{SOURCE99} .
dos2unix README.md

%build
%pyproject_wheel

%install
%pyproject_install
%python_expand %fdupes %{buildroot}%{$python_sitelib}

%files %{python_files}
%doc README.md
%license LICENSE.txt
%{python_sitelib}/pymsgbox
%{python_sitelib}/[Pp]y[Mm]sg[Bb]ox-%{version}*-info

%changelog
