#
# spec file for package python-kafka-python
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


%if 0%{?suse_version} > 1500
%bcond_without libalternatives
%else
%bcond_with libalternatives
%endif

Name:           python-kafka-python
Version:        3.0.6
Release:        0
Summary:        Pure Python client for Apache Kafka
License:        Apache-2.0
URL:            https://github.com/dpkp/kafka-python
Source:         https://github.com/dpkp/kafka-python/archive/%version.tar.gz#/%{name}-%{version}.tar.gz
BuildRequires:  %{python_module pip}
BuildRequires:  %{python_module setuptools}
BuildRequires:  %{python_module wheel}
BuildRequires:  fdupes
BuildRequires:  python-rpm-macros
%if %{with libalternatives}
BuildRequires:  alts
Requires:       alts
%else
Requires(post): update-alternatives
Requires(postun): update-alternatives
%endif
# Recommends:   python-crc32c  # Not packaged
Recommends:     python-zstandard
Suggests:       python-lz4
Suggests:       python-xxhash
BuildArch:      noarch
# SECTION test requirements
BuildRequires:  %{python_module lz4}
BuildRequires:  %{python_module pytest-mock}
BuildRequires:  %{python_module pytest-timeout}
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
# Do not distribute tests
sed -i 's/exclude = ."test"./exclude = ["test*"]/' pyproject.toml
# remove all shebang from non-executable scripts
find . -name "*.py" -exec sed -i '/#!\/usr\/bin\/env python/d'  {} \;

%build
%pyproject_wheel

%install
%pyproject_install
%python_clone -a %{buildroot}%{_bindir}/kafka-python
%python_expand %fdupes %{buildroot}%{$python_sitelib}

%check
# python-crc32c not available
donttest="test_crc32c[None]"
%pytest test -k "not ($donttest)"

%pre
# removing old update-alternatives entries
%python_libalternatives_reset_alternative kafka-python

%post
%python_install_alternative kafka-python

%postun
%python_uninstall_alternative kafka-python

%files %{python_files}
%license LICENSE
%doc README.rst
%python_alternative %{_bindir}/kafka-python
%{python_sitelib}/kafka
%{python_sitelib}/kafka_python-%{version}.dist-info

%changelog
