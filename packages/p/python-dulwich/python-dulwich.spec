#
# spec file for package python-dulwich
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


%if 0%{?suse_version} >= 1550
%bcond_without test
%else
%bcond_with test
%endif

%define oldpython python
%{?!python_module:%define python_module() python-%{**} python3-%{**}}
%define skip_python2 1
Name:           python-dulwich
Version:        0.20.50
Release:        0
Summary:        Pure-Python Git Library
License:        Apache-2.0 OR GPL-2.0-or-later
Group:          Development/Languages/Python
URL:            https://www.dulwich.io
Source0:        https://files.pythonhosted.org/packages/source/d/dulwich/dulwich-%{version}.tar.gz
BuildRequires:  %{python_module devel}
BuildRequires:  %{python_module setuptools >= 17.1}
BuildRequires:  fdupes
BuildRequires:  python-rpm-macros
%if %{with test}
BuildRequires:  %{python_module Sphinx}
BuildRequires:  %{python_module fastimport}
BuildRequires:  %{python_module geventhttpclient}
BuildRequires:  %{python_module gevent}
BuildRequires:  %{python_module gpg}
BuildRequires:  %{python_module urllib3 >= 1.24.1}
%if 0%{?suse_version} <= 1500
BuildRequires:  python-mock
%endif
%endif
Requires:       python-urllib3 >= 1.24.1
Requires(post): update-alternatives
Requires(preun):update-alternatives
Recommends:     python-fastimport
Recommends:     python-gpg
Obsoletes:      %{oldpython}-dulwich-doc < 0.20.5
%python_subpackages

%description
Simple Pure-Python implementation of the Git file formats and protocols. Dulwich
is the place where Mr. and Mrs. Git live in one of the Monty Python sketches.

%prep
%autosetup -p1 -n dulwich-%{version}

%build
export CFLAGS="%{optflags}"
%python_build

%install
%python_install
# Do not remove tests as they are reused by other packages
#%%python_expand rm -r %{buildroot}%{$python_sitearch}/dulwich/tests
%python_expand %fdupes %{buildroot}%{$python_sitearch}
%python_clone -a %{buildroot}%{_bindir}/dulwich
%python_clone -a %{buildroot}%{_bindir}/dul-receive-pack
%python_clone -a %{buildroot}%{_bindir}/dul-upload-pack

%check
%if %{with test}
%python_expand PYTHONPATH=%{buildroot}%{$python_sitearch} $python -m unittest dulwich.tests.test_suite
%endif

%post
%python_install_alternative dulwich
%python_install_alternative dul-receive-pack
%python_install_alternative dul-upload-pack

%postun
%python_uninstall_alternative dulwich
%python_uninstall_alternative dul-receive-pack
%python_uninstall_alternative dul-upload-pack

%files %{python_files}
%license COPYING
%doc NEWS README.rst
%python_alternative dulwich
%python_alternative dul-receive-pack
%python_alternative dul-upload-pack
%{python_sitearch}/*

%changelog
