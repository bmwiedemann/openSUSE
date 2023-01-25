#
# spec file for package python-avro
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


%define skip_python2 1
Name:           python-avro
Version:        1.11.1
Release:        0
Summary:        A serialization and RPC framework for Python
License:        Apache-2.0
Group:          Development/Languages/Python
URL:            https://avro.apache.org/
Source:         https://files.pythonhosted.org/packages/source/a/avro/avro-%{version}.tar.gz
# PATCH-FIX-UPSTREAM: py311.patch gh#apache/avro#1961
Patch:          py311.patch
BuildRequires:  %{python_module pytest}
BuildRequires:  %{python_module setuptools}
BuildRequires:  fdupes
BuildRequires:  python-rpm-macros
Requires(post): update-alternatives
Requires(postun):update-alternatives
Requires:       python-Twisted
Requires:       python-zope.interface
Suggests:       python-python-snappy
BuildArch:      noarch
%python_subpackages

%description
Apache Avro is a serialization and RPC framework.
This package contains the python implementation of Avro.

%prep
%autosetup -p1 -n avro-%{version}
sed -i '1{\@^#!/usr/bin/env python@d}' avro/*.py avro/tether/*.py avro/test/*.py

%build
%python_build

%install
%python_install
%python_clone -a %{buildroot}%{_bindir}/avro
%python_expand %fdupes %{buildroot}%{$python_sitelib}

%check
# test_server_with_path: tries to connect to apache.org
# test_minimum_speed is not stable in OBS
%pytest -k "not test_server_with_path and not test_minimum_speed"

%post
%python_install_alternative avro

%postun
%python_uninstall_alternative avro

%files %{python_files}
%python_alternative %{_bindir}/avro
%{python_sitelib}/avro
%{python_sitelib}/avro-%{version}-py*.egg-info

%changelog
