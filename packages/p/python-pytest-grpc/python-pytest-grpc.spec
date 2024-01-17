#
# spec file for package python-pytest-grpc
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


Name:           python-pytest-grpc
Version:        0.8.0
Release:        0
Summary:        pytest plugin for grpc
License:        MIT
URL:            https://github.com/open-telemetry/opentelemetry-python
Source:         https://files.pythonhosted.org/packages/source/p/pytest-grpc/pytest-grpc-%{version}.tar.gz
BuildRequires:  python-rpm-macros
BuildRequires:  %{python_module grpcio}
BuildRequires:  %{python_module pip}
BuildRequires:  %{python_module setuptools}
BuildRequires:  %{python_module wheel}
# SECTION test requirements
BuildRequires:  %{python_module pytest >= 3.6.0}
# /SECTION
BuildRequires:  fdupes
Requires:       python-pytest >= 3.6.0
BuildArch:      noarch
%python_subpackages

%description
pytest plugin for grpc

%prep
%autosetup -p1 -n pytest-grpc-%{version}

%build
%pyproject_wheel

%install
%pyproject_install
%python_expand %fdupes %{buildroot}%{$python_sitelib}

%files %{python_files}
%doc README.md
%{python_sitelib}/pytest_grpc
%{python_sitelib}/pytest_grpc-%{version}.dist-info

%changelog
