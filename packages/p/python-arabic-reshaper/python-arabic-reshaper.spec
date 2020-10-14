#
# spec file for package python-arabic-reshaper
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
Name:           python-arabic-reshaper
Version:        2.0.15
Release:        0
Summary:        Python module for formatting Arabic sentences
License:        MIT
Group:          Development/Languages/Python
URL:            https://github.com/mpcabd/python-arabic-reshaper/
Source:         https://github.com/mpcabd/python-arabic-reshaper/archive/v%{version}.tar.gz
BuildRequires:  %{python_module future}
BuildRequires:  %{python_module setuptools}
BuildRequires:  fdupes
BuildRequires:  python-rpm-macros
BuildRequires:  (python-configparser if python-base)
Requires:       python-future
BuildArch:      noarch
%ifpython2
Requires:       python-configparser
%endif
%python_subpackages

%description
A module for reconstructing Arabic sentences that are to be used in
applications that do not support Arabic.

%prep
%setup -q

%build
%python_build

%install
%python_install
%python_expand %fdupes %{buildroot}%{$python_sitelib}

%check
%python_exec setup.py test

%files %{python_files}
%license LICENSE
%doc README.md
%{python_sitelib}/*

%changelog
