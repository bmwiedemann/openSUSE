#
# spec file for package python-avro
#
# Copyright (c) 2025 SUSE LLC and contributors
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
%{?sle15_python_module_pythons}
Name:           python-avro
Version:        1.12.1
Release:        0
Summary:        A serialization and RPC framework for Python
License:        Apache-2.0
URL:            https://avro.apache.org/
Source:         https://files.pythonhosted.org/packages/source/a/avro/avro-%{version}.tar.gz
BuildRequires:  %{python_module base >= 3.7}
BuildRequires:  %{python_module pip}
BuildRequires:  %{python_module setuptools}
BuildRequires:  %{python_module wheel}
BuildRequires:  fdupes
BuildRequires:  python-rpm-macros
BuildArch:      noarch
%if %{with libalternatives}
BuildRequires:  alts
Requires:       alts
%else
Requires(post): update-alternatives
Requires(postun): update-alternatives
%endif
%python_subpackages

%description
Apache Avro is a serialization and RPC framework.
This package contains the python implementation of Avro.

%prep
%autosetup -p1 -n avro-%{version}
sed -i '1{\@^#!/usr/bin/env python@d}' avro/*.py avro/tether/*.py avro/test/*.py

%build
%pyproject_wheel

%install
%pyproject_install
%python_clone -a %{buildroot}%{_bindir}/avro
%python_expand %fdupes %{buildroot}%{$python_sitelib}

%check
# Only contains test_server_with_path; tries to connect to apache.org
rm avro/test/test_ipc.py
%pyunittest discover -v

%post
%python_install_alternative avro

%postun
%python_uninstall_alternative avro

%pre
%python_libalternatives_reset_alternative avro

%files %{python_files}
%python_alternative %{_bindir}/avro
%{python_sitelib}/avro
%{python_sitelib}/avro-%{version}.dist-info

%changelog
