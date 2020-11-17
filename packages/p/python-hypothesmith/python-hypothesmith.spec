#
# spec file for package python-hypothesmith
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
# no release tags in repository, but we need LICENSE and tests not
# packaged in PyPI source https://github.com/Zac-HD/hypothesmith/issues/5
%define commithash 40947c2e590f06ea5f3b88c6e75d8a98e9443c63
%global flavor @BUILD_FLAVOR@%{nil}
%if "%{flavor}" == "test"
%define psuffix -test
%bcond_without test
%else
%define psuffix %{nil}
%bcond_with test
%endif
Name:           python-hypothesmith%{psuffix}
Version:        0.1.6
Release:        0
Summary:        Hypothesis strategies for generating Python programs, something like CSmith
License:        MPL-2.0
URL:            https://github.com/Zac-HD/hypothesmith
Source:         https://files.pythonhosted.org/packages/source/h/hypothesmith/hypothesmith-%{version}.tar.gz
Source1:        https://github.com/Zac-HD/hypothesmith/archive/%{commithash}.tar.gz#/hypothesmith-gh-%{version}.tar.gz
BuildRequires:  %{python_module base >= 3.6}
BuildRequires:  %{python_module setuptools}
BuildRequires:  fdupes
BuildRequires:  python-rpm-macros
Requires:       python-base >= 3.6
Requires:       python-hypothesis >= 5.23.7
Requires:       python-lark-parser >= 0.7.2
Requires:       python-libcst >= 0.3.8
%if %{with test}
BuildRequires:  %{python_module black}
BuildRequires:  %{python_module hypothesis >= 5.23.7}
BuildRequires:  %{python_module lark-parser >= 0.7.2}
BuildRequires:  %{python_module libcst >= 0.3.8}
BuildRequires:  %{python_module parso}
BuildRequires:  %{python_module pytest-xdist}
BuildRequires:  %{python_module pytest}
%endif
BuildArch:      noarch
%python_subpackages

%description
Hypothesis strategies for generating Python programs, something like CSmith.

%prep
%setup -q -n hypothesmith-%{version} -b 1
cp -r ../hypothesmith-%{commithash}/{LICENSE,CHANGELOG.md,tests} .

%build
%if !%{with test}
%python_build
%endif

%install
%if !%{with test}
%python_install
%python_expand %fdupes %{buildroot}%{$python_sitelib}
%endif

%check
%if %{with test}
# multibuild: test the source dir, nothing is installed
export PYTHONPATH=$(pwd)/src
%pytest -n auto
%endif

%if !%{with test}
%files %{python_files}
%doc README.md CHANGELOG.md
%license LICENSE
%{python_sitelib}/hypothesmith
%{python_sitelib}/hypothesmith-%{version}-py*.egg-info
%endif

%changelog
