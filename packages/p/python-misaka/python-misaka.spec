#
# spec file for package python-misaka
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
Name:           python-misaka
Version:        2.1.1
Release:        0
Summary:        A CFFI binding for Hoedown, a markdown parsing library
License:        MIT
Group:          Development/Languages/Python
URL:            https://github.com/FSX/misaka
Source:         https://files.pythonhosted.org/packages/source/m/misaka/misaka-%{version}.tar.gz
BuildRequires:  %{python_module cffi >= 1.12.0}
BuildRequires:  %{python_module devel}
BuildRequires:  %{python_module setuptools}
BuildRequires:  fdupes
BuildRequires:  python-rpm-macros
BuildRequires:  tidy
Requires:       python-cffi >= 1.12.0
Requires(post): update-alternatives
Requires(postun): update-alternatives
%python_subpackages

%description
A CFFI binding for Hoedown_ (version 3), a markdown parsing library.

%prep
%setup -q -n misaka-%{version}

%build
%python_build

%install
%python_install
%python_clone -a %{buildroot}%{_bindir}/misaka
%python_expand %fdupes %{buildroot}%{$python_sitearch}

%check
%{python_expand $python setup.py build_ext --inplace
$python tests/run_tests.py
}

%post
%python_install_alternative misaka

%postun
%python_uninstall_alternative misaka

%files %{python_files}
%license LICENSE.txt
%doc README.rst
%python_alternative %{_bindir}/misaka
%{python_sitearch}/*

%changelog
