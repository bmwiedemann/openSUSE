#
# spec file for package python-confluent-kafka
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


%{?sle15_python_module_pythons}
Name:           python-confluent-kafka
Version:        2.2.0
Release:        0
Summary:        Confluent's Apache Kafka client for Python
License:        Apache-2.0
Group:          Development/Languages/Python
URL:            https://github.com/confluentinc/confluent-kafka-python
Source:         https://files.pythonhosted.org/packages/source/c/confluent-kafka/confluent-kafka-%{version}.tar.gz
BuildRequires:  %{python_module devel}
BuildRequires:  %{python_module setuptools}
BuildRequires:  fdupes
BuildRequires:  librdkafka-devel >= 2.2.0
BuildRequires:  python-rpm-macros

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
