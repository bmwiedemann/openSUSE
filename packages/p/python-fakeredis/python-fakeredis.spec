#
# spec file for package python-fakeredis
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


%{?sle15_python_module_pythons}
Name:           python-fakeredis
Version:        2.32.0
Release:        0
Summary:        Fake implementation of redis API for testing purposes
License:        BSD-3-Clause AND MIT
URL:            https://github.com/cunla/fakeredis-py
Source:         https://github.com/cunla/fakeredis-py/archive/refs/tags/v%{version}.tar.gz#/fakeredis-%{version}-gh.tar.gz
BuildRequires:  %{python_module base >= 3.7}
BuildRequires:  %{python_module hatchling}
BuildRequires:  %{python_module pip}
BuildRequires:  %{python_module wheel}
BuildRequires:  fdupes
BuildRequires:  python-rpm-macros
Requires:       python-redis >= 4
Requires:       python-sortedcontainers >= 2.4.0
Suggests:       python-lupa >= 1.14
BuildArch:      noarch
# SECTION test requirements
BuildRequires:  %{python_module hypothesis >= 6.56}
BuildRequires:  %{python_module pytest >= 7.1.2}
BuildRequires:  %{python_module pytest-asyncio >= 0.19.0}
BuildRequires:  %{python_module pytest-mock >= 3.7.0}
BuildRequires:  %{python_module redis >= 4}
BuildRequires:  %{python_module sortedcontainers >= 2.4.0}
BuildRequires:  %{python_module valkey >= 6}
BuildRequires:  redis
# /SECTION
%python_subpackages

%description
Fake implementation of redis API for testing purposes.

%prep
%autosetup -p1 -n fakeredis-py-%{version}

%build
%pyproject_wheel

%install
%pyproject_install
%python_expand %fdupes %{buildroot}%{$python_sitelib}

%check
export LANG="en_US.UTF8"
%{_sbindir}/redis-server --port 6390 --save &
# Lag is not -1
donttest="test_zrank_redis7_2 or test_zrevrank_redis7_2"
donttest+=" or test_xgroup_setid_redis7"
# Raises unknown command errors
donttest+=" or (test_save and (StrictRedis2 or StrictRedis3))"
donttest+=" or (test_raises_valkey_response_error and FakeStrictRedis)"
%pytest -m "not slow" -k "not ($donttest)"

%files %{python_files}
%doc README.md
%license LICENSE
%{python_sitelib}/fakeredis
%{python_sitelib}/fakeredis-%{version}.dist-info

%changelog
