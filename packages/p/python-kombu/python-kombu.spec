#
# spec file for package python-kombu
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


%{?!python_module:%define python_module() python-%{**} python3-%{**}}
Name:           python-kombu
Version:        4.6.3
Release:        0
Summary:        AMQP Messaging Framework for Python
License:        BSD-3-Clause
Group:          Development/Languages/Python
URL:            https://github.com/celery/kombu
Source:         https://files.pythonhosted.org/packages/source/k/kombu/kombu-%{version}.tar.gz
# Test requirements:
BuildRequires:  %{python_module PyYAML}
BuildRequires:  %{python_module Pyro4}
BuildRequires:  %{python_module amqp >= 2.5.0}
BuildRequires:  %{python_module boto3}
BuildRequires:  %{python_module case >= 1.5.2}
BuildRequires:  %{python_module msgpack > 0.5.2}
BuildRequires:  %{python_module pytest}
BuildRequires:  %{python_module pytz}
BuildRequires:  %{python_module redis >= 3.2.0}
BuildRequires:  %{python_module setuptools >= 20.6.7}
BuildRequires:  fdupes
BuildRequires:  python-rpm-macros
Requires:       python-amqp >= 2.5.0
Requires:       python-setuptools
Obsoletes:      python-carrot
BuildArch:      noarch
%if 0%{?suse_version}
Suggests:       couchdb
Suggests:       mongodb
Suggests:       python-Pyro4
Suggests:       rabbitmq-server
%endif
%python_subpackages

%description
An AMQP messaging framework for Python.

AMQP is the Advanced Message Queuing Protocol, an open standard protocol
for message orientation, queuing, routing, reliability and security.

One of the most popular implementations of AMQP is RabbitMQ.

The aim of Kombu is to make messaging in Python as easy as possible by
providing an idiomatic high-level interface for the AMQP protocol, and also
provide proven and tested solutions to common messaging problems.

%prep
%setup -q -n kombu-%{version}

%build
%python_build

%install
%python_install
%python_expand %fdupes %{buildroot}%{$python_sitelib}

%check
%pytest

%files %{python_files}
%license LICENSE
%doc AUTHORS Changelog FAQ README.rst THANKS TODO
%{python_sitelib}/kombu
%{python_sitelib}/kombu-%{version}-py%{py_ver}.egg-info

%changelog
