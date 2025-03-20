#
# spec file for package python-filelock
#
# Copyright (c) 2025 SUSE LLC
# Copyright (c) 2018 Matthias Fehring <buschmann23@opensuse.org>
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


%global flavor @BUILD_FLAVOR@%{nil}
%if "%{flavor}" == "test"
%define pkg_suffix -test
%bcond_without test
%else
%define pkg_suffix %{nil}
%bcond_with test
%endif
%{?sle15_python_module_pythons}
Name:           python-filelock%{?pkg_suffix}
Version:        3.18.0
Release:        0
Summary:        Platform Independent File Lock in Python
License:        Unlicense
URL:            https://github.com/tox-dev/py-filelock
Source:         https://files.pythonhosted.org/packages/source/f/filelock/filelock-%{version}.tar.gz
BuildRequires:  %{python_module asyncio}
BuildRequires:  %{python_module hatch_vcs}
BuildRequires:  %{python_module hatchling}
BuildRequires:  %{python_module pip}
BuildRequires:  %{python_module wheel}
%if %{with test}
BuildRequires:  %{python_module pytest-asyncio}
BuildRequires:  %{python_module pytest-mock}
BuildRequires:  %{python_module pytest}
BuildRequires:  %{python_module virtualenv}
%endif
BuildRequires:  fdupes
BuildRequires:  python-rpm-macros
%if 0%{?python_version_nodots} < 311
Requires:       python-typing_extensions >= 4.7.1
%endif
Requires:       python-asyncio
BuildArch:      noarch
%python_subpackages

%description
This package contains a single module, which implements a platform
independent file lock in Python, which provides a simple way of
inter-process communication.

%prep
%setup -q -n filelock-%{version}

%build
%pyproject_wheel

%if !%{with test}
%install
%pyproject_install
%python_expand %fdupes %{buildroot}/%{$python_sitelib}

%files %{python_files}
%doc README.md
%license LICENSE
%{python_sitelib}/filelock
%{python_sitelib}/filelock-%{version}*-info
%else

%check
%pytest -rs
%endif

%changelog
