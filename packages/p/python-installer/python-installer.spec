#
# spec file
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


%{?!python_module:%define python_module() python3-%{**}}
%global flavor @BUILD_FLAVOR@%{nil}
%if "%{flavor}" == "test"
%define pkg_suffix -test
%bcond_without test
%else
%define pkg_suffix %{nil}
%bcond_with test
%endif
Name:           python-installer%{pkg_suffix}
Version:        0.6.0
Release:        0
Summary:        A library for installing Python wheels
License:        MIT
URL:            https://github.com/pypa/installer
Source:         https://files.pythonhosted.org/packages/source/i/installer/installer-%{version}.tar.gz
BuildRequires:  %{python_module flit-core}
BuildRequires:  fdupes
BuildRequires:  python-rpm-macros
%if %{with test}
BuildRequires:  %{python_module installer}
BuildRequires:  %{python_module pytest}
%endif
BuildArch:      noarch
%python_subpackages

%description
A library for installing Python wheels.

%prep
%autosetup -p1 -n installer-%{version}

%if !%{with test}
%build
%python_expand $python -m flit_core.wheel
%endif

%if !%{with test}
%install
export PYTHONPATH=src
%python_expand $python -m installer -d %{buildroot} dist/*.whl
%python_expand %fdupes %{buildroot}%{$python_sitelib}
%endif

%if %{with test}
%check
%pytest
%endif

%if !%{with test}
%files %{python_files}
%doc README.md
%license LICENSE
%{python_sitelib}/installer
%{python_sitelib}/installer*dist-info
%endif

%changelog
