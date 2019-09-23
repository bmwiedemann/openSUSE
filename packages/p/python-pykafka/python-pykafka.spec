#
# spec file for package python-pykafka
#
# Copyright (c) 2017 SUSE LINUX GmbH, Nuernberg, Germany.
#
# All modifications and additions to the file contributed by third parties
# remain the property of their copyright owners, unless otherwise agreed
# upon. The license for this file, and modifications and additions to the
# file, is the same license as for the pristine package itself (unless the
# license for the pristine package is not an Open Source License, in which
# case the license is the MIT License). An "Open Source License" is a
# license that conforms to the Open Source Definition (Version 1.9)
# published by the Open Source Initiative.

# Please submit bugfixes or comments via http://bugs.opensuse.org/
#


%{?!python_module:%define python_module() python-%{**} python3-%{**}}
Name:           python-pykafka
Version:        2.8.0
Release:        0
Summary:        Full-Featured Pure-Python Kafka Client
License:        Apache-2.0
Group:          Development/Languages/Python
Url:            https://github.com/Parsely/pykafka
Source:         https://pypi.io/packages/source/p/pykafka/pykafka-%{version}.tar.gz
BuildRequires:  %{python_module devel}
BuildRequires:  %{python_module setuptools}
BuildRequires:  python-rpm-macros
BuildRequires:  fdupes
Requires:       python-six
Requires:       python-kazoo
Requires:       python-tabulate
Requires:       python-gevent
Requires:       python-setuptools

%python_subpackages

%description
PyKafka is a cluster-aware Kafka>=0.8.2 client for Python. It includes Python
implementations of Kafka producers and consumers, which are optionally backed
by a C extension built on `librdkafka`_, and runs under Python 2.7+, Python 3.4+,
and PyPy.

.. _librdkafka: https://github.com/edenhill/librdkafka

PyKafka's primary goal is to provide a similar level of abstraction to the
`JVM Kafka client`_ using idioms familiar to Python programmers and exposing
the most Pythonic API possible.

%prep
%setup -q -n pykafka-%{version}

%build
%python_build

%install
%python_install

# Don't package tests in generic directory
%python_expand rm -rf %{buildroot}%{$python_sitearch}/tests/

%python_clone -a %{buildroot}%{_bindir}/kafka-tools
%python_expand %fdupes %{buildroot}%{$python_sitearch}

%post
%{python_install_alternative kafka-tools}

%postun
%python_uninstall_alternative kafka-tools

%files %{python_files}
%license LICENSE
%python_alternative %{_bindir}/kafka-tools
%{python_sitearch}/*

%changelog
