#
# spec file for package python-antlr4-python3-runtime
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
%define         skip_python2 1
Name:           python-antlr4-python3-runtime
Version:        4.9.3
Release:        0
Summary:        ANTLR runtime for Python 3
License:        BSD-3-Clause
URL:            https://www.antlr.org
Source:         https://github.com/antlr/antlr4/archive/%{version}.tar.gz#/%{name}-%{version}.tar.gz
Source1:        LICENSE.txt
BuildRequires:  %{python_module setuptools}
BuildRequires:  fdupes
BuildRequires:  python-rpm-macros
Requires(post): update-alternatives
Requires(postun):update-alternatives
BuildArch:      noarch
%if %{python3_version_nodots} < 35
Requires:       python-typing
%endif
%python_subpackages

%description
ANTLR (ANother Tool for Language Recognition) is a powerful parser generator for
reading, processing, executing, or translating structured text or binary files.

This package contains the runtime for Python 3.

%prep
%setup -q -n antlr4-%{version}/runtime/Python3
cp %{SOURCE1} LICENSE.txt

%build
%python_build

%install
%python_install
%python_clone -a %{buildroot}%{_bindir}/pygrun
%python_expand %fdupes %{buildroot}%{$python_sitelib}
%prepare_alternative pygrun

%post
%python_install_alternative pygrun

%postun
%python_uninstall_alternative pygrun

%check
cd %{_builddir}/antlr4-%{version}/runtime/Python3
%pyunittest discover -v --pattern "*.py" --start-directory tests

%files %{python_files}
%doc README.txt
%license LICENSE.txt
%python_alternative %{_bindir}/pygrun
%{python_sitelib}/antlr4_python3_runtime-*.egg-info
%{python_sitelib}/antlr4

%changelog
