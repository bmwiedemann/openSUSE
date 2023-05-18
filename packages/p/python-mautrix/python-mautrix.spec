#
# spec file for package python-mautrix
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


%if 0%{?suse_version} >= 1550
%bcond_without test
%else
# Leap 15.x: Ignore that upstream doesn't support Python < 3.8 and does not have the test requirements
%define skip_python2 1
%bcond_with test
%endif

Name:           python-mautrix
Version:        0.19.14
Release:        0
Summary:        A Python 3 asyncio Matrix framework
License:        MPL-2.0
URL:            https://github.com/mautrix/python
# The GitHub Archive has json data required for the test suite
Source:         https://github.com/mautrix/python/archive/refs/tags/v%{version}.tar.gz#/mautrix-python-%{version}-gh.tar.gz
# PATCH-FIX-UPSTREAM no-immutable.patch gh#mautrix/python#147 mcepl@suse.com
# SQLAlchemy 2.0 renamed sql.base.ImmutableColumnCollection to ReadOnlyColumnCollection
Patch0:         no-immutable.patch
BuildRequires:  %{python_module base}
BuildRequires:  %{python_module setuptools}
BuildRequires:  fdupes
BuildRequires:  python-rpm-macros
Requires:       python-aiohttp >= 3
Requires:       python-attrs >= 18.1.0
Requires:       python-yarl >= 1
Suggests:       python-python-magic >= 0.4.15
BuildArch:      noarch
BuildRequires:  %{python_module aiohttp >= 3.0.1}
BuildRequires:  %{python_module attrs >= 18.1.0}
BuildRequires:  %{python_module yarl >= 1}
# SECTION optional requirements
BuildRequires:  %{python_module python-magic >= 0.4.15}
# /SECTION optional requirements
%if %{with test}
BuildRequires:  %{python_module typing_extensions}
BuildRequires:  %{python_module commonmark}
BuildRequires:  %{python_module lxml}
BuildRequires:  %{python_module uvloop}
BuildRequires:  %{python_module pytest-asyncio}
BuildRequires:  %{python_module asyncpg}
BuildRequires:  %{python_module pytest}
BuildRequires:  %{python_module aiosqlite}
BuildRequires:  %{python_module sqlalchemy}
BuildRequires:  %{python_module olm}
BuildRequires:  %{python_module unpaddedbase64}
BuildRequires:  %{python_module pycryptodomex}
BuildRequires:  %{python_module ruamel.yaml}
BuildRequires:  %{python_module prometheus_client}
%endif
%python_subpackages

%description
A Python 3 asyncio Matrix framework.

%prep
%autosetup -p1 -n python-%{version}

%build
%python_build

%install
%python_install
%python_expand %fdupes %{buildroot}%{$python_sitelib}

%if %{with test}
%check
%pytest
%endif

%files %{python_files}
%doc README.rst CHANGELOG.md
%license LICENSE
%{python_sitelib}/mautrix
%{python_sitelib}/mautrix-%{version}*-info

%changelog
