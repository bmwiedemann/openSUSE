#
# spec file for package python-confluent-kafka
#
# Copyright (c) 2020 SUSE LLC
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
Name:           python-confluent-kafka
Version:        1.5.0
Release:        0
Summary:        Confluent's Apache Kafka client for Python
License:        Apache-2.0
Group:          Development/Languages/Python
URL:            https://github.com/confluentinc/confluent-kafka-python
Source:         https://files.pythonhosted.org/packages/source/c/confluent-kafka/confluent-kafka-%{version}.tar.gz
BuildRequires:  %{python_module devel}
BuildRequires:  %{python_module setuptools}
BuildRequires:  fdupes
BuildRequires:  librdkafka-devel
BuildRequires:  python-rpm-macros
%ifpython2
Requires:       python2-avro
Requires:       python2-enum34
Requires:       python2-futures
%endif
Suggests:       python-fastavro
Suggests:       python-requests
Suggests:       python-avro-python3
Suggests:       python-pytest
Suggests:       python-flake8

%python_subpackages

%description
Confluent's Apache Kafka client for Python

%prep
%setup -q -n confluent-kafka-%{version}

%build
export CFLAGS="%{optflags}"
%python_build

%install
%python_install
rm -v %{buildroot}/%{_prefix}/LICENSE.txt
%python_expand %fdupes %{buildroot}%{$python_sitearch}

%files %{python_files}
%license LICENSE.txt
%doc README.md
%{python_sitearch}/*

%changelog
