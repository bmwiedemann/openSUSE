#
# spec file for package python-dynaconf
#
# Copyright (c) 2023 SUSE LLC
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


Name:           python-dynaconf
Version:        3.1.11
Release:        0
Summary:        The dynamic configurator for your Python Project
License:        MIT
URL:            https://github.com/rochacbruno/dynaconf
Source:         https://github.com/rochacbruno/dynaconf/archive/%{version}.tar.gz#/dynaconf-%{version}.tar.gz
# PATCH-FIX-UPSTREAM gh#dynaconf/dynaconf#830
Patch0:         support-python-311.patch
BuildRequires:  %{python_module setuptools >= 38.6.0}
BuildRequires:  fdupes
BuildRequires:  python-rpm-macros
Requires:       python-PyYAML
Requires:       python-click
Requires:       python-configobj
Requires:       python-hvac
Requires:       python-python-box
Requires:       python-python-dotenv
Requires:       python-redis
Requires:       python-setuptools
Requires:       python-toml
Suggests:       python-Django
Requires(post): update-alternatives
Requires(postun):update-alternatives
BuildArch:      noarch
# SECTION test requirements
BuildRequires:  %{python_module Django}
BuildRequires:  %{python_module Flask >= 0.12}
BuildRequires:  %{python_module PyYAML}
BuildRequires:  %{python_module click}
BuildRequires:  %{python_module configobj}
BuildRequires:  %{python_module hvac}
BuildRequires:  %{python_module pytest-mock}
BuildRequires:  %{python_module pytest}
BuildRequires:  %{python_module python-box}
BuildRequires:  %{python_module python-dotenv}
BuildRequires:  %{python_module redis}
BuildRequires:  %{python_module toml}
BuildRequires:  redis
# /SECTION
%python_subpackages

%description
The dynamic configurator for your Python Project

%prep
%autosetup -p1 -n dynaconf-%{version}

# require running docker with the server
rm tests/test_vault.py

%build
%python_build

%install
%python_install
%python_clone -a %{buildroot}%{_bindir}/dynaconf
%python_expand %fdupes %{buildroot}%{$python_sitelib}

%check
export LANG=en_US.UTF-8
/usr/sbin/redis-server --stop-writes-on-bgsave-error no &
export DYNACONF_TEST_REDIS_URL==http://127.0.0.1:6379
%pytest tests/

%post
%python_install_alternative dynaconf

%postun
%python_uninstall_alternative dynaconf

%files %{python_files}
%doc CHANGELOG.md README.md
%license LICENSE
%python_alternative %{_bindir}/dynaconf
%{python_sitelib}/*

%changelog
