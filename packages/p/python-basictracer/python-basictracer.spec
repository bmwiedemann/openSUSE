#
# spec file for package python-basictracer
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


%{?!python_module:%define python_module() python-%{**} python3-%{**}}
%define skip_python2 1
Name:           python-basictracer
Version:        3.2.0
Release:        0
Summary:        BasicTracer reference implementation for OpenTracing
License:        MIT
URL:            https://github.com/opentracing/basictracer-python
Source:         https://files.pythonhosted.org/packages/source/b/basictracer/basictracer-%{version}.tar.gz
BuildRequires:  %{python_module setuptools}
BuildRequires:  fdupes
BuildRequires:  python-rpm-macros
Requires:       python-opentracing >= 2.0
Requires:       python-protobuf >= 3.0.0
Requires:       python-six >= 1.10.0
BuildArch:      noarch
# SECTION test requirements
BuildRequires:  %{python_module opentracing >= 2.0}
BuildRequires:  %{python_module protobuf >= 3.0.0}
BuildRequires:  %{python_module pytest-mock}
BuildRequires:  %{python_module pytest}
BuildRequires:  %{python_module six >= 1.10.0}
# /SECTION
%python_subpackages

%description
Python "BasicTracer" reference implementation for OpenTracing.

%prep
%setup -q -n basictracer-%{version}

%build
%python_build

%install
%python_install
%python_expand %fdupes %{buildroot}%{$python_sitelib}

%check
# opentracing.harness.api_check requires mock
# (tracked in https://trello.com/c/S6eADbii/64-remove-python-mock, too)
rm tests/test_api.py
%pytest

%files %{python_files}
%doc CHANGELOG.rst README.md
%license LICENSE
%{python_sitelib}/*

%changelog
