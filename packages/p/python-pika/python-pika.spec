#
# spec file for package python-pika
#
# Copyright (c) 2019 SUSE LINUX GmbH, Nuernberg, Germany.
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


%define mod_name pika
%{?!python_module:%define python_module() python-%{**} python3-%{**}}
Name:           python-%{mod_name}
Version:        1.1.0
Release:        0
Summary:        Pika Python AMQP Client Library
License:        BSD-3-Clause
Group:          Development/Languages/Python
URL:            https://github.com/pika/pika
Source:         https://github.com/pika/pika/archive/%{version}.tar.gz
BuildRequires:  %{python_module Twisted}
BuildRequires:  %{python_module mock}
BuildRequires:  %{python_module nose}
BuildRequires:  %{python_module setuptools}
BuildRequires:  %{python_module tornado}
BuildRequires:  fdupes
BuildRequires:  python-rpm-macros
Requires:       python
Recommends:     python-Twisted
Recommends:     python-tornado
BuildArch:      noarch
%python_subpackages

%description
Pika is a pure-Python implementation of the AMQP 0-9-1 protocol that
tries to stay fairly independent of the underlying network support
library. Pika was developed primarily for use with RabbitMQ, but
should also work with other AMQP 0-9-1 brokers.

%prep
%setup -q -n %{mod_name}-%{version}
# acceptance needs running configured server
rm -rf tests/acceptance/
sed -i -e 's:,tests/acceptance::' setup.cfg

%build
%python_build

%install
%python_install
%python_expand %fdupes %{buildroot}%{$python_sitelib}/%{mod_name}
%python_expand %fdupes %{buildroot}%{$python_sitelib}/*.egg-info

%check
%python_expand PYTHONPATH="%{buildroot}%{$python_sitelib}" nosetests-%{$python_bin_suffix} tests/

%files %{python_files}
%doc README.rst CHANGELOG.rst
%license LICENSE
# You may have to add additional files here (documentation and binaries mostly)
%{python_sitelib}/%{mod_name}*

%changelog
