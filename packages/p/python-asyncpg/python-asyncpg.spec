#
# spec file for package python-asyncpg
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
Name:           python-asyncpg
Version:        0.30.0
Release:        0
Summary:        Python asyncio PosgtreSQL driver
License:        Apache-2.0
URL:            https://github.com/MagicStack/asyncpg
Source:         https://files.pythonhosted.org/packages/source/a/asyncpg/asyncpg-%{version}.tar.gz
# PATCH-FIX-OPENSUSE Skip a broken test
Patch0:         skip-dsn_ipv6_multi_host-parse-test.patch
BuildRequires:  %{python_module Cython}
BuildRequires:  %{python_module async_timeout if %python-base < 3.11}
BuildRequires:  %{python_module devel >= 3.6}
BuildRequires:  %{python_module distro}
BuildRequires:  %{python_module pip}
BuildRequires:  %{python_module setuptools}
BuildRequires:  %{python_module typing-extensions >= 3.7.4.3 if %python-base < 3.8}
BuildRequires:  fdupes
BuildRequires:  python-rpm-macros
Requires:       libpq5 >= 9.4
%if 0%{?python_version_nodots} < 311
Requires:       python-async_timeout
%endif
%if 0%{?python_version_nodots} < 38
Requires:       python-typing-extensions >= 3.7.4.3
%endif
# SECTION test requirements
BuildRequires:  %{python_module pytest >= 6}
BuildRequires:  postgresql-contrib
BuildRequires:  postgresql-server
%if 0%{?suse_version} > 1500
# uvloop >= 0.15.3 does not exist in Leap nor in python36 flavor
BuildRequires:  %{python_module uvloop >= 0.15.3 if (%python-base without python36-base)}
%endif
# /SECTION
%python_subpackages

%description
A fast PostgreSQL Database Client Library for Python/asyncio.

**asyncpg** is a database interface library designed specifically for
PostgreSQL and Python/asyncio with clean implementation

%prep
%autosetup -p1 -n asyncpg-%{version}
# no uvloop in python36 but in newer flavors
sed -i asyncpg/_testbase/__init__.py \
  -e "/import re/ a import sys" \
  -e "s/if os.environ.get('USE_UVLOOP')/& and sys.version_info[:2] > (3, 6)/"

%build
%pyproject_wheel

%install
%pyproject_install
%{python_expand find %{buildroot}%{$python_sitearch} -name '*.[ch]' -delete
%fdupes %{buildroot}%{$python_sitearch}
}

%check
# Needed to avoid asyncpg.cluster.ClusterError:
#                 could not find pg_config executable
export PGINSTALLATION=%{_bindir}
%if 0%{?suse_version} > 1500
export USE_UVLOOP=1
%endif
# fails inside obs chroot
donttest="test_timetz_encoding"
# fails because ssl_user doesn't have permission to create tables
# permission denied for schema public
donttest+=" or test_executemany_uvloop_ssl_issue_700"

mv asyncpg .asyncpg
%pytest_arch -rs -k "not ($donttest)"
mv .asyncpg asyncpg

%files %{python_files}
%license LICENSE
%doc README.rst
%{python_sitearch}/asyncpg
%{python_sitearch}/asyncpg-%{version}.dist-info

%changelog
