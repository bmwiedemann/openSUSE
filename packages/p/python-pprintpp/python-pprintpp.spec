#
# spec file for package python-pprintpp
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


Name:           python-pprintpp
Version:        0.4.0
Release:        0
Summary:        A variant of pprint that is arguably "prettier"
License:        BSD-2-Clause
Group:          Development/Languages/Python
URL:            https://github.com/wolever/pprintpp
Source:         https://files.pythonhosted.org/packages/source/p/pprintpp/pprintpp-%{version}.tar.gz
# https://github.com/wolever/pprintpp/commit/3a35e815.patch
Patch0:         3a35e815.patch
# gh#wolever/pprintpp#28
Patch1:         python-pprintpp-remove-nose.patch
# PATCH-FIX-OPENSUSE python-311.patch small fix to support python 3.11
Patch2:         python-311.patch
BuildRequires:  %{python_module parameterized}
BuildRequires:  %{python_module pytest}
BuildRequires:  %{python_module setuptools}
BuildRequires:  fdupes
BuildRequires:  python-rpm-macros
Requires(post): update-alternatives
Requires(postun):update-alternatives
BuildArch:      noarch
%python_subpackages

%description
A drop-in replacement for pprint that is arguably prettier.

%prep
%autosetup -p1 -n pprintpp-%{version}

%build
export LANG=en_US.utf-8
%python_build

%install
export LANG=en_US.utf-8
%python_install
%python_clone -a %{buildroot}%{_bindir}/pypprint
%python_expand %fdupes %{buildroot}%{$python_sitelib}

%check
export LANG=en_US.utf-8
%pytest -v test.py

%post
%python_install_alternative pypprint

%postun
%python_uninstall_alternative pypprint

%files %{python_files}
%doc CHANGELOG.txt README.rst
%license LICENSE.txt
%python_alternative %{_bindir}/pypprint
%{python_sitelib}/pprintpp
%{python_sitelib}/pprintpp-%{version}*-info

%changelog
