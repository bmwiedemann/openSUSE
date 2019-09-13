#
# spec file for package python-atpublic
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

# Please submit bugfixes or comments via http://bugs.opensuse.org/


%{?!python_module:%define python_module() python-%{**} python3-%{**}}
%define skip_python2 1
Name:           python-atpublic
Version:        1.0
Release:        0
License:        Apache-2.0
Summary:        @public decorator for populating __all__
Url:            http://public.readthedocs.io/
Group:          Development/Languages/Python
Source:         https://files.pythonhosted.org/packages/source/a/atpublic/atpublic-%{version}.tar.gz
BuildRequires:  python-rpm-macros
BuildRequires:  %{python_module devel}
BuildRequires:  %{python_module setuptools}
BuildRequires:  fdupes

%python_subpackages

%description
public -- @public for populating __all__.

%prep
%setup -q -n atpublic-%{version}

%build
export CFLAGS="%{optflags}"
export ATPUBLIC_BUILD_EXTENSION=1
%python_build

%install
export ATPUBLIC_BUILD_EXTENSION=1
%python_install

%{python_expand rm -r %{buildroot}%{$python_sitearch}/public/tests
%fdupes %{buildroot}%{$python_sitearch}
}

%check
%python_exec setup.py test --test-suite=public.tests

%files %{python_files}
%doc NEWS.rst README.rst
%license LICENSE.txt
%{python_sitearch}/*

%changelog
