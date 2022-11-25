#
# spec file for package python-meson-python
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


Name:           python-meson-python
Version:        0.11.0
Release:        0
Summary:        Meson Python build backend (PEP 517)
License:        MIT
URL:            https://github.com/mesonbuild/meson-python
Source0:        https://files.pythonhosted.org/packages/source/m/meson_python/meson_python-%{version}.tar.gz
# for the test suite
Source1:        https://files.pythonhosted.org/packages/py3/t/tomli/tomli-2.0.1-py3-none-any.whl
Source2:        https://files.pythonhosted.org/packages/py3/p/pyproject_metadata/pyproject_metadata-0.6.1-py3-none-any.whl
Source3:        https://files.pythonhosted.org/packages/py3/p/packaging/packaging-21.3-py3-none-any.whl
Source4:        https://files.pythonhosted.org/packages/py3/p/pyparsing/pyparsing-3.0.9-py3-none-any.whl
# PATCH-FEATURE-OPENSUSE mesonpy-trim-deps.patch code@bnavigator.de
Patch11:        mesonpy-trim-deps.patch
# PATCH-FEATURE-OPENSUSE mesonpy-no-wheel-rebuild.patch code@bnavigator.de
Patch12:        mesonpy-no-wheel-rebuild.patch
BuildRequires:  %{python_module base >= 3.7}
BuildRequires:  %{python_module pip}
BuildRequires:  %{python_module pyproject-metadata >= 0.5.0}
BuildRequires:  %{python_module tomli >= 1.0.0 if %python-base < 3.11}
BuildRequires:  %{python_module typing-extensions >= 3.7.4 if %python-base < 3.8}
BuildRequires:  fdupes
BuildRequires:  meson >= 0.63.3
BuildRequires:  ninja
BuildRequires:  python-rpm-macros
Requires:       meson >= 0.63.3
Requires:       python-pyproject-metadata >= 0.5.0
%if 0%{python_version_nodots} < 311
Requires:       python-tomli >= 1.0.0
%endif
%if 0%{python_version_nodots} < 38
Requires:       python-typing-extensions >= 3.7.4
%endif
# SECTION test
BuildRequires:  %{python_module GitPython}
BuildRequires:  %{python_module Cython}
BuildRequires:  %{python_module build}
BuildRequires:  %{python_module devel}
BuildRequires:  %{python_module pyproject-metadata >= 0.6.1}
BuildRequires:  %{python_module pytest-mock}
BuildRequires:  %{python_module pytest}
BuildRequires:  %{python_module wheel}
BuildRequires:  patchelf
# /SECTION
BuildArch:      noarch
%python_subpackages

%description
Python build backend (PEP 517) for Meson projects.

%prep
%autosetup -p1 -n meson_python-%{version}

%build
%pyproject_wheel

%install
%pyproject_install
%python_expand %fdupes %{buildroot}%{$python_sitelib}

%check
export MESONPY_FORCE_LOCAL_LIB=1
%python_expand cp %{SOURCE1} %{SOURCE2} %{SOURCE3} %{SOURCE4} build/
# can test test_spam only once gh#mesonbuild/meson-python#169
# this has benn fixed shortly after the release of 0.11
%python_expand $python_ignore="--ignore tests/docs/examples/test_spam.py"
unset python310_ignore
%pytest ${$python_ignore}

%files %{python_files}
%license LICENSE
%doc README.md
%{python_sitelib}/mesonpy
%{python_sitelib}/meson_python-%{version}*-info

%changelog
