#
# spec file for package python-fedora-messaging
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


%define         _modname fedora-messaging
Name:           python-fedora-messaging
Version:        3.8.0
Release:        0
Summary:        Python tools for Fedora's messaging infrastructure
License:        GPL-2.0-or-later
URL:            https://github.com/fedora-infra/fedora-messaging
Source:         https://github.com/fedora-infra/fedora-messaging/archive/refs/tags/v%{version}.tar.gz#/fedora-messaging-%{version}.tar.gz
BuildRequires:  %{python_module Sphinx}
BuildRequires:  %{python_module Twisted}
BuildRequires:  %{python_module base >= 3.9}
BuildRequires:  %{python_module blinker}
BuildRequires:  %{python_module click}
BuildRequires:  %{python_module coverage}
BuildRequires:  %{python_module crochet}
BuildRequires:  %{python_module jsonschema}
BuildRequires:  %{python_module pika >= 1.0.0}
BuildRequires:  %{python_module pip}
BuildRequires:  %{python_module poetry-core}
BuildRequires:  %{python_module pyOpenSSL}
BuildRequires:  %{python_module pytest-mock}
BuildRequires:  %{python_module pytest-twisted}
BuildRequires:  %{python_module pytest}
BuildRequires:  %{python_module service_identity}
BuildRequires:  %{python_module tomli}
BuildRequires:  %{python_module towncrier}
BuildRequires:  %{python_module treq}
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
Requires:       python-requests
Requires:       python-service_identity
Requires:       python-setuptools
Requires:       python-tomli
Requires(post): update-alternatives
Requires(postun): update-alternatives
BuildArch:      noarch
%python_subpackages

%description
A set of Python tools for using Fedora's messaging infrastructure.

%prep
%autosetup -p1 -n %{_modname}-%{version}

%build
%pyproject_wheel

%install
%pyproject_install
%python_clone -a %{buildroot}%{_bindir}/%{_modname}
%python_expand %fdupes %{buildroot}%{$python_sitelib}

%post
%python_install_alternative %{_modname}

%postun
%python_uninstall_alternative %{_modname}

%check
%pytest -k "not test_no_conf" tests/unit

%files %{python_files}
%license LICENSES/GPL-2.0-or-later.txt
%doc README.rst
%python_alternative %{_bindir}/%{_modname}
%{python_sitelib}/fedora_messaging
%{python_sitelib}/fedora_messaging-%{version}.dist-info

%changelog
