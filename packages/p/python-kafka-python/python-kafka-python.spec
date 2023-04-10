#
# spec file for package python-kafka-python
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


Name:           python-kafka-python
Version:        2.0.2
Release:        0
Summary:        Pure Python client for Apache Kafka
License:        Apache-2.0
Group:          Development/Languages/Python
URL:            https://github.com/mumrah/kafka-python
Source:         https://files.pythonhosted.org/packages/source/k/kafka-python/kafka-python-%{version}.tar.gz
Source1:        https://raw.githubusercontent.com/dpkp/kafka-python/master/servers/0.11.0.3/resources/zookeeper.properties
Source2:        https://raw.githubusercontent.com/dpkp/kafka-python/master/test/conftest.py
Source3:        https://raw.githubusercontent.com/dpkp/kafka-python/master/test/fixtures.py
Source4:        https://raw.githubusercontent.com/dpkp/kafka-python/master/test/service.py
# PATCH-FIX-OPENSUSE Remove use of mock module
Patch0:         remove-mock.patch
# PATCH-FIX-UPSTREAM fix tests for py3.11 gh#dpkp/kafka-python#2358
Patch1:         python-311.patch
BuildRequires:  %{python_module setuptools}
BuildRequires:  fdupes
BuildRequires:  python-rpm-macros
# Recommends:   python-crc32c  # Not packaged
Recommends:     python-zstandard
Suggests:       python-lz4
Suggests:       python-xxhash
BuildArch:      noarch
# SECTION test requirements
BuildRequires:  %{python_module lz4}
BuildRequires:  %{python_module pytest-mock}
BuildRequires:  %{python_module pytest}
BuildRequires:  %{python_module python-snappy}
BuildRequires:  %{python_module xxhash}
BuildRequires:  %{python_module zstandard}
# /SECTION
%python_subpackages

%description
This module provides low-level protocol support for Apache Kafka as well as
high-level consumer and producer classes. Request batching is supported by the
protocol as well as broker-aware request routing. Gzip and Snappy compression
is also supported for message sets.

%prep
%autosetup -p1 -n kafka-python-%{version}
mkdir -p servers/0.11.0.2/resources/
cp %{SOURCE1} servers/0.11.0.2/resources/

cp %{SOURCE2} %{SOURCE3} %{SOURCE4} test/

touch test/__init__.py

%build
%python_build

%install
%python_install
%python_expand %fdupes %{buildroot}%{$python_sitelib}

%check
# test_kafka_producer_gc_cleanup is sometimes off by 1
%pytest -rs -k 'not (test_kafka_consumer_offsets_for_time_old or test_kafka_producer_gc_cleanup)'

%files %{python_files}
%license LICENSE
%doc README.rst
%{python_sitelib}/kafka*/

%changelog
