#
# spec file for package python-cu2qu
#
# Copyright (c) 2022 SUSE LLC
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
%global skip_python36 1
Name:           python-cu2qu
Version:        1.6.7.post2
Release:        0
Summary:        Cubic-to-quadratic bezier curve conversion
License:        Apache-2.0
URL:            https://github.com/googlefonts/cu2qu
Source:         https://files.pythonhosted.org/packages/source/c/cu2qu/cu2qu-%{version}.zip
BuildRequires:  %{python_module devel}
BuildRequires:  %{python_module fs}
BuildRequires:  %{python_module setuptools_scm}
BuildRequires:  %{python_module setuptools}
BuildRequires:  fdupes
BuildRequires:  python-rpm-macros
BuildRequires:  unzip
Requires:       python-FontTools >= 3.32.0
Recommends:     python-defcon >= 0.6.0
# SECTION test requirements
BuildRequires:  %{python_module FontTools >= 3.32.0}
BuildRequires:  %{python_module defcon >= 0.6.0}
BuildRequires:  %{python_module pytest >= 2.8}
# /SECTION
%python_subpackages

%description
Cubic-to-quadratic bezier curve conversion

%prep
%setup -q -n cu2qu-%{version}
sed -i -e '/pytest-runner/d' setup.py

%build
export CFLAGS="%{optflags}"
%python_build

%install
%python_install
%python_expand %fdupes %{buildroot}%{$python_sitearch}
%python_clone -a %{buildroot}%{_bindir}/cu2qu

%check
%pytest_arch

%post
%python_install_alternative cu2qu

%postun
%python_uninstall_alternative cu2qu

%files %{python_files}
%doc README.rst
%license LICENSE
%python_alternative %{_bindir}/cu2qu
%{python_sitearch}/*

%changelog
