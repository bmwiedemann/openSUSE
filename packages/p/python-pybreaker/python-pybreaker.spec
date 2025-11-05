#
# spec file for package python-pybreaker
#
# Copyright (c) 2025 SUSE LLC and contributors
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


Name:           python-pybreaker
Version:        1.4.1
Release:        0
Summary:        Python implementation of the Circuit Breaker pattern
License:        BSD-3-Clause
URL:            http://github.com/danielfm/pybreaker
Source:         https://github.com/danielfm/pybreaker/archive/refs/tags/v%{version}.tar.gz#/pybreaker-%{version}.tar.gz
BuildRequires:  %{python_module flit-core >= 3.9}
BuildRequires:  %{python_module pip}
BuildRequires:  python-rpm-macros
# SECTION test requirements
BuildRequires:  %{python_module fakeredis}
BuildRequires:  %{python_module pytest}
BuildRequires:  %{python_module redis}
BuildRequires:  %{python_module tornado}
# /SECTION
BuildRequires:  fdupes
BuildArch:      noarch
%python_subpackages

%description
PyBreaker is a Python implementation of the Circuit Breaker pattern, described
in Michael T. Nygard's book `Release It!`_.

In Nygard's words, *"circuit breakers exists to allow one subsystem to fail
without destroying the entire system. This is done by wrapping dangerous
operations (typically integration points) with a component that can circumvent
calls when the system is not healthy"*.

%prep
%autosetup -p1 -n pybreaker-%{version}

%build
%pyproject_wheel

%install
%pyproject_install
%python_expand %fdupes %{buildroot}%{$python_sitelib}

%check
# Fails on 32 bit arches
%pytest -k 'not test_fail_max_thread_safety'

%files %{python_files}
%doc README.rst
%license LICENSE
%{python_sitelib}/pybreaker
%{python_sitelib}/pybreaker-%{version}.dist-info

%changelog
