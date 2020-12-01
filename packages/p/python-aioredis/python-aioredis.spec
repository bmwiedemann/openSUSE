#
# spec file for package python-aioredis
#
# Copyright (c) 2020 SUSE LLC
# Copyright (c) 2019 Matthias Fehring <buschmann23@opensuse.org>
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


%{?!python_module:%define python_module() python3-%{**}}
%define skip_python2 1
Name:           python-aioredis
Version:        1.3.1
Release:        0
Summary:        Python asyncio Redis support
License:        MIT
Group:          Development/Languages/Python
URL:            https://github.com/aio-libs/aioredis
Source0:        https://files.pythonhosted.org/packages/source/a/aioredis/aioredis-%{version}.tar.gz
# PATCH-FIX-UPSTREAM aioredis-1.3.1-fix-tests-on-python38.patch -- https://github.com/aio-libs/aioredis/pull/724
Patch0:         aioredis-1.3.1-fix-tests-on-python38.patch
# PATCH-FIX-UPSTREAM aioredis-1.3.1-fix-tests-on-python38-part2.patch -- https://github.com/aio-libs/aioredis/pull/727
Patch1:         aioredis-1.3.1-fix-tests-on-python38-part2.patch
BuildRequires:  %{python_module setuptools >= 38.6.0}
BuildRequires:  fdupes
BuildRequires:  python-rpm-macros
Requires:       python-async_timeout
Recommends:     redis
BuildArch:      noarch
# SECTION test requirements
BuildRequires:  %{python_module async_timeout}
BuildRequires:  %{python_module pytest}
BuildRequires:  redis
# /SECTION
%python_subpackages

%description
The library is intended to provide simple and clear interface to Redis based on asyncio.

%prep
%setup -q -n aioredis-%{version}
%if 0%{?suse_version} > 1500 || 0%{?sle_version} >= 150200
%patch0 -p1
%patch1 -p1
%endif
rm setup.cfg
# Remove dependency on hiredis, which is a redis server embedded in a Python package
sed -Ei '/(platform.python_implementation|hiredis)/d' setup.py

%build
%python_build

%install
%python_install
%python_expand %fdupes %{buildroot}%{$python_sitelib}

%check
export PATH=$PATH:%{_sbindir}

fail_pattern='(connection_commands_test and test_auth) or test_master__auth or test_failover_command or test_command_info or test_client_list'
# test_hincrbyfloat fail on armv7l with float rounding error
fail_pattern+=' or test_hincrbyfloat or test_auto_failover'

%pytest -k "not ($fail_pattern)"
# Show known errors
%pytest -k "$fail_pattern" ||:

%files %{python_files}
%license LICENSE
%doc CHANGES.txt
%{python_sitelib}/aioredis-%{version}-*.egg-info/
%{python_sitelib}/aioredis/

%changelog
