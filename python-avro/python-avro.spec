#
# spec file for package python-avro
#
# Copyright (c) 2019 SUSE LINUX GmbH, Nuernberg, Germany.
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
Name:           python-avro
Version:        1.9.0
Release:        0
Summary:        A serialization and RPC framework for Python
License:        Apache-2.0
Group:          Development/Languages/Python
Url:            http://avro.apache.org/
Source:         https://files.pythonhosted.org/packages/source/a/avro/avro-%{version}.tar.gz
BuildRequires:  %{python_module setuptools}
BuildRequires:  fdupes
BuildRequires:  python-rpm-macros
Suggests:       python-python-snappy
BuildArch:      noarch

%python_subpackages

%description
Avro is a serialization and RPC framework.

%prep
%setup -q -n avro-%{version}

%build
%python_build

%install
%python_install
%python_expand %fdupes %{buildroot}%{$python_sitelib}

%check
%python_exec setup.py test

%files %{python_files}
%python3_only %{_bindir}/avro
%{python_sitelib}/*

%changelog
