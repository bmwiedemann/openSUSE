#
# spec file for package python-compileall2
#
# Copyright (c) 2023 SUSE LLC
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
%define skip_python2 1
Name:           python-compileall2
Version:        0.7.2
Release:        0
Summary:        Enhanced Python `compileall` module
License:        Python-2.0
URL:            https://github.com/fedora-python/compileall2
Source:         https://files.pythonhosted.org/packages/source/c/compileall2/compileall2-%{version}.tar.gz
Source1:        https://raw.githubusercontent.com/fedora-python/compileall2/master/LICENSE
Source2:        https://raw.githubusercontent.com/fedora-python/compileall2/master/test_compileall2.py
BuildRequires:  %{python_module pip}
BuildRequires:  %{python_module pytest}
BuildRequires:  %{python_module testsuite}
BuildRequires:  %{python_module wheel}
BuildRequires:  fdupes
BuildRequires:  python-rpm-macros
BuildArch:      noarch
%python_subpackages

%description
Enhanced Python `compileall` module.

%prep
%setup -q -n compileall2-%{version}
cp %{SOURCE1} %{SOURCE2} .

%build
export LANG=en_US.UTF-8
%pyproject_wheel

%install
export LANG=en_US.UTF-8
%pyproject_install
%python_clone -a %{buildroot}%{_bindir}/compileall2
%python_expand %fdupes %{buildroot}%{$python_sitelib}

%check
export LANG=en_US.UTF-8
%pytest -rs test_compileall2.py -k 'not test_hardlink_deduplication_import'

%post
%python_install_alternative compileall2

%postun
%python_uninstall_alternative compileall2

%files %{python_files}
%doc README.md
%license LICENSE
%python_alternative %{_bindir}/compileall2
%{python_sitelib}/*

%changelog
