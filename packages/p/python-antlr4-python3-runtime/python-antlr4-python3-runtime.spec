#
# spec file for package python-antlr4-python3-runtime
#
# Copyright (c) 2025 SUSE LLC and contributors
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


%if 0%{?suse_version} > 1500
%bcond_without libalternatives
%else
%bcond_with libalternatives
%endif
%{?sle15_python_module_pythons}
Name:           python-antlr4-python3-runtime
Version:        4.13.2
Release:        0
Summary:        ANTLR runtime for Python 3
License:        BSD-3-Clause
URL:            https://www.antlr.org
Source:         https://github.com/antlr/antlr4/archive/%{version}.tar.gz#/%{name}-%{version}.tar.gz
Source1:        LICENSE.txt
BuildRequires:  %{python_module pip}
BuildRequires:  %{python_module setuptools}
BuildRequires:  %{python_module wheel}
BuildRequires:  fdupes
BuildRequires:  python-rpm-macros
BuildArch:      noarch
%if %{with libalternatives}
BuildRequires:  alts
Requires:       alts
%else
Requires(post): update-alternatives
Requires(postun): update-alternatives
%endif
%python_subpackages

%description
ANTLR (ANother Tool for Language Recognition) is a powerful parser generator for
reading, processing, executing, or translating structured text or binary files.

This package contains the runtime for Python 3.

%prep
%setup -q -n antlr4-%{version}/runtime/Python3
cp %{SOURCE1} LICENSE.txt
# fixing for python 3.12
sed -i 's,self.assertEquals,self.assertEqual,' tests/Test*

%build
%pyproject_wheel

%install
%pyproject_install
%python_clone -a %{buildroot}%{_bindir}/pygrun
%python_expand %fdupes %{buildroot}%{$python_sitelib}
%prepare_alternative pygrun

%post
%python_install_alternative pygrun

%postun
%python_uninstall_alternative pygrun

%pre
%python_libalternatives_reset_alternative pygrun

%check
cd %{_builddir}/antlr4-%{version}/runtime/Python3
%{python_expand #
PYTHONPATH=%{buildroot}%{$python_sitelib} $python tests/run.py
}

%files %{python_files}
%doc README.txt
%license LICENSE.txt
%python_alternative %{_bindir}/pygrun
%{python_sitelib}/antlr4_python3_runtime-*.dist-info
%{python_sitelib}/antlr4

%changelog
