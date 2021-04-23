#
# spec file for package python-xdoctest
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
Name:           python-xdoctest
Version:        0.15.4
Release:        0
Summary:        Enhanced Python builtin doctest module
License:        Apache-2.0
URL:            https://github.com/Erotemic/xdoctest
Source:         https://github.com/Erotemic/xdoctest/archive/%{version}.tar.gz#/xdoctest-%{version}.tar.gz
Patch0:         https://github.com/Erotemic/xdoctest/pull/97.patch
BuildRequires:  %{python_module pygments}
BuildRequires:  %{python_module pytest}
BuildRequires:  %{python_module setuptools}
BuildRequires:  fdupes
BuildRequires:  python-rpm-macros
Requires(post): update-alternatives
Requires(postun): update-alternatives
Recommends:     python-pygments
BuildArch:      noarch
%python_subpackages

%description
A rewrite of the builtin doctest module with a pytest plugin.

%prep
%setup -q -n xdoctest-%{version}
%autopatch -p1
sed -i '1{/^#!/d}' xdoctest/__main__.py
sed -i 's/--ignore-glob=setup.py//' pytest.ini

%build
%python_build

%install
%python_install
%python_clone -a %{buildroot}%{_bindir}/xdoctest
%python_expand %fdupes %{buildroot}%{$python_sitelib}

%post
%python_install_alternative xdoctest

%postun
%python_uninstall_alternative xdoctest

%check
mkdir -p ~/bin
export PATH=$PATH:~/bin
export PYTHONDONTWRITEBYTECODE=1
# Python 2 on openSUSE 15.x gets confused if buildroot installed copy is in PYTHONPATH
%{python_expand cp -p %{buildroot}%{_bindir}/xdoctest-%{$python_bin_suffix} ~/bin/xdoctest
PYTHONPATH=. $python -m pytest -rs
}

%files %{python_files}
%doc README.rst
%license LICENSE
%python_alternative %{_bindir}/xdoctest
%{python_sitelib}/*

%changelog
