#
# spec file for package python-fakeredis
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


Name:           python-fakeredis
Version:        1.8.1
Release:        0
Summary:        Fake implementation of redis API for testing purposes
License:        BSD-3-Clause AND MIT
URL:            https://github.com//dsoftwareinc/fakeredis
Source:         https://github.com/dsoftwareinc/fakeredis-py/archive/refs/tags/v%{version}.tar.gz#/fakeredis-%{version}-gh.tar.gz
BuildRequires:  %{python_module base >= 3.7}
BuildRequires:  %{python_module pip}
BuildRequires:  %{python_module poetry-core}
BuildRequires:  fdupes
BuildRequires:  python-rpm-macros
Requires:       python-redis
Requires:       python-six >= 1.16
Requires:       python-sortedcontainers >= 2.4.0
Suggests:       (python-aioredis if python-redis < 4.2)
Suggests:       python-lupa
BuildArch:      noarch
# SECTION test requirements
BuildRequires:  %{python_module future}
BuildRequires:  %{python_module hypothesis}
BuildRequires:  %{python_module lupa}
BuildRequires:  %{python_module pytest >= 4.0}
BuildRequires:  %{python_module pytest-asyncio}
BuildRequires:  %{python_module pytest-mock}
BuildRequires:  %{python_module redis}
BuildRequires:  %{python_module six >= 1.16}
BuildRequires:  %{python_module sortedcontainers >= 2.4.0}
# /SECTION
%python_subpackages

%description
Fake implementation of redis API for testing purposes.

%prep
%setup -q -n fakeredis-py-%{version}

%build
%pyproject_wheel

%install
%pyproject_install
%python_expand %fdupes %{buildroot}%{$python_sitelib}

%check
export LANG="en_US.UTF8"
%pytest

%files %{python_files}
%doc README.md
%license LICENSE
%{python_sitelib}/fakeredis
%{python_sitelib}/fakeredis-%{version}*-info

%changelog
