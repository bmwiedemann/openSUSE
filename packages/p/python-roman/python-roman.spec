#
# spec file for package python-roman
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
Name:           python-roman
Version:        3.2
Release:        0
Summary:        Integer to Roman numerals converter
License:        Python-2.0
Group:          Development/Languages/Python
URL:            https://github.com/zopefoundation/roman
Source:         https://files.pythonhosted.org/packages/source/r/roman/roman-%{version}.tar.gz
BuildRequires:  %{python_module setuptools}
BuildRequires:  fdupes
BuildRequires:  python-rpm-macros
BuildArch:      noarch
%python_subpackages

%description
This module converts from and to Roman numerals. It can convert numbers from
1 to 4999 and understands the common shortcuts (IX == 9), but not illegal ones (MIM == 1999).

%prep
%setup -q -n roman-%{version}

%build
%python_build

%install
%python_install
%python_expand %fdupes %{buildroot}%{$python_sitelib}

%check
%python_exec setup.py test

%files %{python_files}
%doc CHANGES.txt
%{python_sitelib}/*

%changelog
