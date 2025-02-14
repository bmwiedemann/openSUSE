#
# spec file for package python-quart-trio
#
# Copyright (c) 2025 SUSE LLC
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
Name:           python-quart-trio
Version:        0.12.0
Release:        0
Summary:        A Quart extension to provide trio support
License:        MIT
URL:            https://github.com/pgjones/quart-trio/
Source:         https://github.com/pgjones/quart-trio/archive/refs/tags/%{version}.tar.gz#/quart_trio-%{version}.tar.gz
BuildRequires:  %{python_module Quart >= 0.19}
BuildRequires:  %{python_module exceptiongroup}
BuildRequires:  %{python_module pdm-backend}
BuildRequires:  %{python_module pip}
BuildRequires:  %{python_module pytest-cov}
BuildRequires:  %{python_module pytest-trio}
BuildRequires:  %{python_module pytest}
BuildRequires:  %{python_module trio >= 0.19}
BuildRequires:  fdupes
BuildRequires:  python-rpm-macros
Requires:       python-Quart >= 0.19
Requires:       python-exceptiongroup
Requires:       python-hypercorn >= 0.12
Requires:       python-trio >= 0.19
Recommends:     python-python-dotenv
BuildArch:      noarch
%python_subpackages

%description
Quart-Trio is an extension for Quart to support the Trio event loop. This is
an alternative to using the asyncio event loop present in the Python standard
library and supported by default in Quart.

%prep
%autosetup -p1 -n quart-trio-%{version}

%build
%pyproject_wheel

%install
%pyproject_install
%python_expand %fdupes %{buildroot}%{$python_sitelib}

%check
# Trio breakage with exceptiongroup handling
%pytest -k 'not (test_websocket_exception_group or test_websocket_abort)'

%files %{python_files}
%doc README.rst
%license LICENSE
%{python_sitelib}/quart_trio
%{python_sitelib}/quart_trio-%{version}.dist-info

%changelog
