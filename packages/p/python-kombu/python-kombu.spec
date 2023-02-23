#
# spec file for package python-kombu
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


Name:           python-kombu
Version:        5.2.4
Release:        0
Summary:        AMQP Messaging Framework for Python
License:        BSD-3-Clause
URL:            https://github.com/celery/kombu
Source:         https://files.pythonhosted.org/packages/source/k/kombu/kombu-%{version}.tar.gz
# PATCH-FIX-OPENSUSE Use Pyro4 compatibility for now, upstream should switch
# for 5.3
Patch0:         support-pyro-5.patch
BuildRequires:  %{python_module Brotli >= 1.0.0}
BuildRequires:  %{python_module PyYAML >= 3.10}
BuildRequires:  %{python_module Pyro5}
BuildRequires:  %{python_module SQLAlchemy}
BuildRequires:  %{python_module amqp >= 5.0.9}
BuildRequires:  %{python_module boto3 >= 1.9.12}
BuildRequires:  %{python_module cached-property}
BuildRequires:  %{python_module case >= 1.5.2}
BuildRequires:  %{python_module importlib-metadata >= 0.18}
BuildRequires:  %{python_module msgpack}
BuildRequires:  %{python_module pycurl >= 7.43.0.2}
BuildRequires:  %{python_module pytest}
BuildRequires:  %{python_module pytz}
BuildRequires:  %{python_module redis >= 3.4.1}
BuildRequires:  %{python_module setuptools >= 20.6.7}
BuildRequires:  %{python_module vine}
BuildRequires:  fdupes
BuildRequires:  python-rpm-macros
Requires:       python-amqp >= 5.0.9
Requires:       python-cached-property
Requires:       python-importlib-metadata >= 0.18
Requires:       python-setuptools
Requires:       python-vine
Recommends:     python-Brotli >= 1.0.0
Recommends:     python-PyYAML >= 3.10
Obsoletes:      python-carrot
BuildArch:      noarch
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
%autosetup -p1 -n kombu-%{version}
# pinned dependencies are bad
sed -i -e 's:==:>=:g' requirements/*.txt requirements/extras/*.txt
# we don't want to pull in the whole azure stack because of few tests of a non-essential feature
rm t/unit/transport/test_azureservicebus.py

%build
%python_build

%install
%python_install
%python_expand %fdupes %{buildroot}%{$python_sitelib}

%check
%pytest

%files %{python_files}
%license LICENSE
%doc AUTHORS FAQ README.rst THANKS TODO
%{python_sitelib}/kombu
%{python_sitelib}/kombu-%{version}-py*.egg-info

%changelog
