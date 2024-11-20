#
# spec file for package python-slimit
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


%{?sle15_python_module_pythons}
%define oldpython python
Name:           python-slimit
Version:        0.8.1
Release:        0
Summary:        JavaScript minifier written in Python
License:        MIT
URL:            https://slimit.readthedocs.io/
Source:         https://files.pythonhosted.org/packages/source/s/slimit/slimit-%{version}.zip
# PATCH-FIX-OPENSUSE python-slimit-add-licence.patch -- Include the licence file that is present in git since 4111f2d.
Patch0:         python-slimit-add-licence.patch
# https://github.com/rspivak/slimit/commit/40956e7fc6e954b3e6d7b629faeb3303f5efb7ea
Patch1:         python-slimit-fix-python3.patch
Patch2:         py313-makesuite.patch
BuildRequires:  %{python_module pip}
BuildRequires:  %{python_module ply >= 3.4}
BuildRequires:  %{python_module setuptools}
BuildRequires:  %{python_module wheel}
BuildRequires:  fdupes
BuildRequires:  python-rpm-macros
BuildRequires:  unzip
# SECTION test requirements
BuildRequires:  %{python_module pytest}
# /SECTION
Requires:       python-ply >= 3.4
Requires(post): update-alternatives
Requires(postun): update-alternatives
BuildArch:      noarch
%ifpython2
# python-slimit was last used in openSUSE Leap 15.0.
Provides:       %{oldpython}-slimit = %{version}
Obsoletes:      %{oldpython}-slimit < %{version}
%endif

%description
SlimIt is a JavaScript minifier written in Python. It compiles
JavaScript into more compact code so that it downloads and runs
faster.

SlimIt also provides a library that includes a JavaScript parser,
lexer, pretty printer and a tree visitor.

%python_subpackages

%prep
%autosetup -p1 -n slimit-%{version}

%build
%pyproject_wheel

%install
%pyproject_install
%python_expand %fdupes %{buildroot}%{$python_sitelib}/
%python_clone -a %{buildroot}%{_bindir}/slimit

%post
%python_install_alternative slimit

%postun
%python_uninstall_alternative slimit

%check
%pytest

%files %{python_files}
%license LICENSE
%doc CHANGES README.rst
%python_alternative %{_bindir}/slimit
%{python_sitelib}/slimit
%{python_sitelib}/slimit-%{version}.dist-info

%changelog
