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
Version:        3.3.1
Release:        0
Summary:        The dynamic configurator for your Python Project
License:        MIT
URL:            https://github.com/dynaconf/dynaconf
Source:         https://github.com/dynaconf/dynaconf/archive/%{version}.tar.gz#/dynaconf-%{version}.tar.gz
BuildRequires:  %{python_module pip}
BuildRequires:  %{python_module setuptools >= 42}
BuildRequires:  %{python_module wheel}
BuildRequires:  fdupes
BuildRequires:  python-rpm-macros
Requires:       python-PyYAML
Requires:       python-click
Requires:       python-configobj >= 5.0.9
Requires:       python-hvac >= 1.1.0
Requires:       python-python-box
Requires:       python-python-dotenv >= 1.2.1
Requires:       python-redis >= 7.0.1
Requires:       python-setuptools
Requires:       python-toml >= 0.10.2
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
BuildRequires:  %{python_module Django >= 4.2.26}
BuildRequires:  %{python_module Flask >= 1.0}
BuildRequires:  %{python_module PyYAML}
BuildRequires:  %{python_module click}
BuildRequires:  %{python_module configobj >= 5.0.9}
BuildRequires:  %{python_module hvac >= 1.1.0}
BuildRequires:  %{python_module pytest >= 8.4.2}
BuildRequires:  %{python_module pytest-asyncio >= 0.21.0}
BuildRequires:  %{python_module pytest-mock >= 3.15.1}
BuildRequires:  %{python_module python-box}
BuildRequires:  %{python_module python-dotenv >= 1.2.1}
BuildRequires:  %{python_module redis >= 7.0.1}
BuildRequires:  %{python_module toml >= 0.10.2}
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
%python_expand rm -rf %{buildroot}%{$python_sitelib}/vendor_licenses
%python_expand %fdupes %{buildroot}%{$python_sitelib}

%check
export LANG=en_US.UTF-8
%{_sbindir}/redis-server --stop-writes-on-bgsave-error no &
export DYNACONF_TEST_REDIS_URL==http://127.0.0.1:6379
# test_help_dont_require_instance needs an installed binary in PATH
%pytest -k "not (test_help_dont_require_instance)" --ignore tests/test_release_utility.py tests/

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
