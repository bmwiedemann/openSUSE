#
# spec file for package python-confluent-kafka
#
# Copyright (c) 2026 SUSE LLC and contributors
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
Version:        2.14.0
Release:        0
Summary:        Confluent's Apache Kafka client for Python
License:        Apache-2.0
Group:          Development/Languages/Python
URL:            https://github.com/confluentinc/confluent-kafka-python
Source:         https://files.pythonhosted.org/packages/source/c/confluent-kafka/confluent_kafka-%{version}.tar.gz
BuildRequires:  %{python_module devel}
BuildRequires:  %{python_module pip}
BuildRequires:  %{python_module setuptools >= 62}
BuildRequires:  %{python_module wheel}
BuildRequires:  fdupes
BuildRequires:  librdkafka-devel >= %{version}
BuildRequires:  python-rpm-macros
# SECTION Runtime dependencies
%if 0%{?python_version_nodots} < 311
Requires:       python-typing-extensions
%endif
Requires:       python-Authlib >= 1.0.0
Requires:       python-attrs >= 21.2.0
Requires:       python-cachetools >= 5.5.0
Requires:       python-certifi
Requires:       python-httpx >= 0.26
# /SECTION
%python_subpackages

%description
Confluent's Apache Kafka client for Python

%prep
%setup -q -n confluent_kafka-%{version}

%build
export CFLAGS="%{optflags}"
%pyproject_wheel

%install
%pyproject_install
%python_expand %fdupes %{buildroot}%{$python_sitearch}

%files %{python_files}
%license LICENSE
%doc README.md
%{python_sitearch}/confluent[_-]kafka
%{python_sitearch}/confluent[_-]kafka-%{version}*-info

%changelog
