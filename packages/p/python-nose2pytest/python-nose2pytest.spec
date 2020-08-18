#
# spec file for package python-nose2pytest
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
%define skip_python2 1
Name:           python-nose2pytest
Version:        1.0.8
Release:        0
Summary:        Convert nose tests to pytest
License:        BSD-3-Clause
Group:          Development/Languages/Python
URL:            https://github.com/schollii/nose2pytest
Source:         https://files.pythonhosted.org/packages/source/n/nose2pytest/nose2pytest-%{version}.tar.gz
Patch0:         merged_pr_9.patch
Patch1:         merged_pr_10.patch
Patch2:         pr_11.patch
BuildRequires:  %{python_module nose}
BuildRequires:  %{python_module pytest}
BuildRequires:  %{python_module setuptools}
BuildRequires:  dos2unix
BuildRequires:  fdupes
BuildRequires:  python-rpm-macros
Requires(post): update-alternatives
Requires(postun): update-alternatives
BuildArch:      noarch
%python_subpackages

%description
Convert nose.tools.assert_ calls found in your Nose test modules into raw asserts for pytest.

%prep
%setup -q -n nose2pytest-%{version}
dos2unix nose2pytest/*.py tests/*.py README.rst
%autopatch -p1

%build
%python_build

%install
%python_install
%python_clone -a %{buildroot}%{_bindir}/nose2pytest
%python_expand %fdupes %{buildroot}%{$python_sitelib}

%post
%python_install_alternative nose2pytest

%postun
%python_uninstall_alternative nose2pytest

%check
%python_exec -m pytest -k 'not test_add_parens'

%files %{python_files}
%doc README.rst
%license LICENSE.txt
%python_alternative %{_bindir}/nose2pytest
%{python_sitelib}/*

%changelog
