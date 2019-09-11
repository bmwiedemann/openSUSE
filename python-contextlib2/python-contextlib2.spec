#
# spec file for package python-contextlib2
#
# Copyright (c) 2018 SUSE LINUX GmbH, Nuernberg, Germany.
# Copyright (c) 2014 LISA GmbH, Bingen, Germany.
#
# All modifications and additions to the file contributed by third parties
# remain the property of their copyright owners, unless otherwise agreed
# upon. The license for this file, and modifications and additions to the
# file, is the same license as for the pristine package itself (unless the
# license for the pristine package is not an Open Source License, in which
# case the license is the MIT License). An "Open Source License" is a
# license that conforms to the Open Source Definition (Version 1.9)
# published by the Open Source Initiative.

# Please submit bugfixes or comments via http://bugs.opensuse.org/
#


%{?!python_module:%define python_module() python-%{**} python3-%{**}}
Name:           python-contextlib2
Version:        0.5.5
Release:        0
Summary:        Backports and enhancements for the contextlib module
License:        Python-2.0
Group:          Development/Languages/Python
URL:            http://contextlib2.readthedocs.org
Source:         https://files.pythonhosted.org/packages/source/c/contextlib2/contextlib2-%{version}.tar.gz
BuildRequires:  %{python_module setuptools}
BuildRequires:  %{python_module unittest2}
BuildRequires:  fdupes
BuildRequires:  python-rpm-macros
BuildArch:      noarch
%python_subpackages

%description
contextlib2 is a backport of the standard library's contextlib module to
earlier Python versions.

It also serves as a real world proving ground for possible future enhancements
to the standard library version.

%prep
%setup -q -n contextlib2-%{version}

%build
%python_build

%install
%python_install
%python_expand %fdupes %{buildroot}%{$python_sitelib}

%check
%python_expand PYTHONPATH=%{buildroot}%{$python_sitelib} $python test_contextlib2.py

%files %{python_files}
%license LICENSE.txt
%doc README.rst NEWS.rst
%{python_sitelib}/*

%changelog
