#
# spec file for package python-fedora-messaging
#
# Copyright (c) 2024 SUSE LLC
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


Name:           python-fedora-messaging
Version:        3.4.1
Release:        0
Summary:        Python tools for Fedora's messaging infrastructure
License:        GPL-2.0-or-later
URL:            https://github.com/fedora-infra/fedora-messaging
Source:         https://github.com/fedora-infra/fedora-messaging/archive/refs/tags/v%{version}.tar.gz#/fedora-messaging-%{version}.tar.gz
BuildRequires:  %{python_module pip}
BuildRequires:  %{python_module setuptools}
BuildRequires:  %{python_module wheel}
BuildRequires:  fdupes
BuildRequires:  python-rpm-macros
Requires:       python-Twisted
Requires:       python-blinker
Requires:       python-click
Requires:       python-crochet
Requires:       python-jsonschema
Requires:       python-pika >= 1.0.1
Requires:       python-pyOpenSSL
Requires:       python-pytz
Requires:       python-service_identity
Requires:       python-setuptools
Requires:       python-tomli
BuildArch:      noarch
# SECTION test requirements
BuildRequires:  %{python_module Sphinx}
BuildRequires:  %{python_module Twisted}
BuildRequires:  %{python_module blinker}
BuildRequires:  %{python_module click}
BuildRequires:  %{python_module coverage}
BuildRequires:  %{python_module crochet}
BuildRequires:  %{python_module jsonschema}
BuildRequires:  %{python_module pika >= 1.0.1}
BuildRequires:  %{python_module pyOpenSSL}
BuildRequires:  %{python_module pytest-mock}
BuildRequires:  %{python_module pytest-twisted}
BuildRequires:  %{python_module pytest}
BuildRequires:  %{python_module pytz}
BuildRequires:  %{python_module service_identity}
BuildRequires:  %{python_module setuptools}
BuildRequires:  %{python_module tomli}
BuildRequires:  %{python_module towncrier}
BuildRequires:  %{python_module treq}
# /SECTION
Requires(post): update-alternatives
Requires(postun): update-alternatives
%python_subpackages

%description
A set of Python tools for using Fedora's messaging infrastructure.

%prep
%autosetup -p1 -n fedora-messaging-%{version}

%build
%pyproject_wheel

%install
%pyproject_install
%python_clone -a %{buildroot}%{_bindir}/fedora-messaging
%{python_expand rm -r %{buildroot}%{$python_sitelib}/fedora_messaging/tests/
%fdupes %{buildroot}%{$python_sitelib}
}

%post
%python_install_alternative fedora-messaging

%postun
%python_uninstall_alternative fedora-messaging

%check
export PATH=$PATH:%{buildroot}%{_bindir}
export PYTHONDONTWRITEBYTECODE=1
export LANG=en_US.UTF-8
# to avoid import collision
pushd fedora_messaging
# Tests that fails on python 3.12 because unittest.mock
donttest="test_bindings_dict"
donttest+=" or test_bindings_list_of_dict"
donttest+=" or test_defaults"
donttest+=" or test_with_queues"
donttest+=" or test_wrap_bindings"
donttest+=" or test_app_name"
donttest+=" or test_callable_getattr_failure"
donttest+=" or test_cli_callable_import_failure_cli_opt"
donttest+=" or test_cli_callable_wrong_format"
donttest+=" or test_missing_cli_and_conf_callable"
%pytest -k "not ($donttest)" tests/unit
popd

%files %{python_files}
%doc README.rst
%license LICENSE
%python_alternative %{_bindir}/fedora-messaging
%{python_sitelib}/fedora_messaging
%{python_sitelib}/fedora_messaging-%{version}*-info

%changelog
