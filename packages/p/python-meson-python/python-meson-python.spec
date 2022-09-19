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
Version:        0.8.1
Release:        0
Summary:        Meson Python build backend (PEP 517)
License:        MIT
URL:            https://github.com/FFY00/meson-python
Source:         https://files.pythonhosted.org/packages/source/m/meson_python/meson_python-%{version}.tar.gz
# PATCH-FIX-UPSTREAM mesonpy-force-flavor.patch gh#FY00/meson-python#51, gh#FY00/meson-python#127
Patch0:         mesonpy-force-flavor.patch
# PATCH-FEATURE-OPENSUSE mesonpy-trim-deps.patch code@bnavigator.de
Patch1:         mesonpy-trim-deps.patch
# PATCH-FIX-OPENSUSE mesonpy-no-rpath.patch code@bnavigator.de -- https://github.com/FFY00/meson-python/issues/125#issuecomment-1243388061
Patch2:         mesonpy-no-rpath.patch
BuildRequires:  %{python_module base >= 3.7}
BuildRequires:  %{python_module pip}
BuildRequires:  %{python_module pyproject-metadata >= 0.5}
BuildRequires:  %{python_module tomli >= 1.0.0}
BuildRequires:  %{python_module typing-extensions >= 3.7.4 if %python-base < 3.8}
BuildRequires:  %{python_module wheel}
BuildRequires:  fdupes
BuildRequires:  meson
BuildRequires:  ninja
BuildRequires:  python-rpm-macros
Requires:       meson
Requires:       ninja
Requires:       python-pyproject-metadata >= 0.5.0
Requires:       python-tomli >= 1.0.0
BuildArch:      noarch
%if 0%{python_version_nodots} < 38
Requires:       python-typing-extensions >= 3.7.4
%endif
# SECTION test
BuildRequires:  %{python_module GitPython}
BuildRequires:  %{python_module devel}
BuildRequires:  %{python_module pytest-mock}
BuildRequires:  %{python_module pytest}
BuildRequires:  patchelf
# /SECTION
%python_subpackages

%description
Python build backend (PEP 517) for Meson projects.

%prep
%autosetup -p1 -n meson_python-%{version}

%build
# until we have https://github.com/openSUSE/python-rpm-macros/pull/139, this will build
# a pure wheel three times.
%pyproject_wheel

%install
%pyproject_install
%python_expand %fdupes %{buildroot}%{$python_sitelib}

%check
export MESONPY_FORCE_LOCAL_LIB=1
%pytest

%files %{python_files}
%license LICENSE
%doc README.md
%{python_sitelib}/mesonpy
%{python_sitelib}/meson_python-%{version}*-info

%changelog
