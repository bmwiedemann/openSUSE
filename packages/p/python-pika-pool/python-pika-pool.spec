#
# spec file for package python-pika-pool
#
# Copyright (c) 2018 SUSE LINUX GmbH, Nuernberg, Germany.
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
Name:           python-pika-pool
Version:        0.1.3
Release:        0
Summary:        Pools for pikas
License:        BSD-3-Clause
Group:          Development/Languages/Python
Url:            https://github.com/bninja/pika-pool
Source:         https://pypi.python.org/packages/source/p/pika-pool/pika-pool-%{version}.tar.gz
BuildRequires:  %{python_module pika}
BuildRequires:  %{python_module setuptools}
BuildRequires:  python-rpm-macros
Requires:       python-pika >= 0.9
BuildArch:      noarch

%python_subpackages

%description
Pika connection pooling inspired by:

- `flask-pika <https://github.com/WeatherDecisionTechnologies/flask-pika>`_
- `sqlalchemy.pool.Pool <http://docs.sqlalchemy.org/en/latest/core/pooling.html#sqlalchemy.pool.Pool>`_

Typically you'll go with local `shovels <https://www.rabbitmq.com/shovel.html>`_, `krazee-eyez kombu <http://bit.ly/1txcnnO>`_, etc. but this works too.

%prep
%setup -q -n pika-pool-%{version}

%build
%python_build

%install
%python_install

%files %{python_files}
%defattr(-,root,root,-)
%doc README.rst
%{python_sitelib}/*

%changelog
