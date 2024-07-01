#
# spec file for package python-hunter
#
# Copyright (c) 2024 SUSE LLC
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


Name:           python-hunter
Version:        3.7.0
Release:        0
Summary:        Pytest plugin for coverage reporting
License:        BSD-2-Clause
URL:            https://github.com/ionelmc/python-hunter
Source:         https://files.pythonhosted.org/packages/source/h/hunter/hunter-%{version}.tar.gz
BuildRequires:  %{python_module Cython}
BuildRequires:  %{python_module setuptools_scm}
BuildRequires:  fdupes
BuildRequires:  python-rpm-macros
Requires(post): update-alternatives
Requires(postun): update-alternatives
%python_subpackages

%description
Hunter is a flexible code tracing toolkit, not for measuring coverage,
but for debugging, logging, inspection and other nefarious purposes.

%prep
%autosetup -p1 -n hunter-%{version}

%build
%python_build

%install
%python_install
%python_expand %fdupes %{buildroot}%{$python_sitearch}/
%python_clone -a %{buildroot}%{_bindir}/hunter-trace

%check

%post
%python_install_alternative hunter-trace

%postun
%python_uninstall_alternative hunter-trace

%files %{python_files}
%python_alternative %{_bindir}/hunter-trace
%license LICENSE
%doc AUTHORS.rst CHANGELOG.rst README.rst
%{python_sitearch}/*

%changelog
