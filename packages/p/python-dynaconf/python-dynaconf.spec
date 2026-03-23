#
# spec file for package python-dynaconf
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


%if 0%{?suse_version} > 1500
%bcond_without libalternatives
%else
%bcond_with libalternatives
%endif

Name:           python-dynaconf
Version:        3.2.13
Release:        0
Summary:        The dynamic configurator for your Python Project
License:        MIT
URL:            https://github.com/dynaconf/dynaconf
Source:         https://github.com/dynaconf/dynaconf/archive/%{version}.tar.gz#/dynaconf-%{version}.tar.gz
BuildRequires:  %{python_module pip}
BuildRequires:  %{python_module setuptools >= 38.6.0}
BuildRequires:  %{python_module wheel}
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
%if %{with libalternatives}
Requires:       alts
BuildRequires:  alts
%else
Requires(post): update-alternatives
Requires(postun): update-alternatives
%endif
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
%pyproject_wheel

%install
%pyproject_install
%python_clone -a %{buildroot}%{_bindir}/dynaconf
%python_expand %fdupes %{buildroot}%{$python_sitelib}

%check
export LANG=en_US.UTF-8
%{_sbindir}/redis-server --stop-writes-on-bgsave-error no &
export DYNACONF_TEST_REDIS_URL==http://127.0.0.1:6379
# test_help_dont_require_instance needs an installed binary in PATH
%pytest -k "not (test_help_dont_require_instance)" tests/

%pre
# If libalternatives is used: Removing old update-alternatives entries.
%python_libalternatives_reset_alternative dynaconf

%post
%python_install_alternative dynaconf

%postun
%python_uninstall_alternative dynaconf

%files %{python_files}
%doc CHANGELOG.md README.md
%license LICENSE
%python_alternative %{_bindir}/dynaconf
%{python_sitelib}/dynaconf
%{python_sitelib}/dynaconf-%{version}*-info

%changelog
