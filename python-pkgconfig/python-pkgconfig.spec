#
# spec file for package python-pkgconfig
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

# Please submit bugfixes or comments via https://bugs.opensuse.org/
#


%{?!python_module:%define python_module() python-%{**} python3-%{**}}
Name:           python-pkgconfig
Version:        1.3.1
Release:        0
Summary:        Interface Python with pkg-config
License:        MIT
Group:          Development/Languages/Python
URL:            http://github.com/matze/pkgconfig
Source:         https://files.pythonhosted.org/packages/source/p/pkgconfig/pkgconfig-%{version}.tar.gz
BuildRequires:  %{python_module nose}
BuildRequires:  %{python_module setuptools}
BuildRequires:  fdupes
BuildRequires:  pkgconfig
BuildRequires:  python-rpm-macros
Requires:       pkgconfig
BuildArch:      noarch
%python_subpackages

%description
A Python module to interface with the pkg-config
command line tool and supports Python 2.6+.

%prep
%setup -q -n pkgconfig-%{version}

%build
%python_build

%install
%python_install
%python_expand %fdupes %{buildroot}%{$python_sitelib}

%check
%python_exec -m nose test.py

%files %{python_files}
%license LICENSE
%doc README.rst
%{python_sitelib}/*

%changelog
