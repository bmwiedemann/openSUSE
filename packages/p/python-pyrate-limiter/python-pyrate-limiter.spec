#
# spec file for package python-pyrate-limiter
#
# Copyright (c) 2026 SUSE LLC and contributors
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


Name:           python-pyrate-limiter
Version:        4.1.0
Release:        0
Summary:        Python Rate-Limiter using Leaky-Bucket Algorithm Family
License:        MIT
URL:            https://github.com/vutran1710/PyrateLimiter
Source:         https://files.pythonhosted.org/packages/source/p/pyrate_limiter/pyrate_limiter-%{version}.tar.gz
BuildArch:      noarch
BuildRequires:  %{python_module base >= 3.10}
BuildRequires:  %{python_module pip}
BuildRequires:  %{python_module hatchling}
BuildRequires:  %{python_module sqlite3}
BuildRequires:  %{python_module pytest >= 8.4.1}
BuildRequires:  %{python_module pytest-asyncio >= 1.1.0}
BuildRequires:  %{python_module filelock >= 3.0}
BuildRequires:  %{python_module redis >= 6.2.0}
BuildRequires:  %{python_module psycopg >= 3.2.9}
BuildRequires:  fdupes
BuildRequires:  redis
Requires:       python-filelock >= 3.0
Requires:       python-redis >= 6.2.0
Requires:       python-psycopg >= 3.2.9
%python_subpackages

%description
The request rate limiter using Leaky-bucket Algorithm.

%prep
%autosetup -p1 -n pyrate_limiter-%{version}

%build
%pyproject_wheel

%install
%pyproject_install
%python_expand %fdupes %{buildroot}/%{$python_sitelib}

%check
# Run the redis server on background since it is required for the tests
%{_sbindir}/redis-server &

%pytest

%files %{python_files}
%license LICENSE
%doc CHANGELOG.md README.md
%{python_sitelib}/pyrate_limiter
%{python_sitelib}/pyrate_limiter-%{version}.dist-info

%changelog

