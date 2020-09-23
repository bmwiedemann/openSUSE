#
# spec file for package python-googleapis-common-protos
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
Name:           python-googleapis-common-protos
Version:        1.52.0
Release:        0
Summary:        Common protobufs used in Google APIs
License:        Apache-2.0
Group:          Development/Languages/Python
URL:            https://github.com/googleapis/googleapis
Source:         https://files.pythonhosted.org/packages/source/g/googleapis-common-protos/googleapis-common-protos-%{version}.tar.gz
# https://github.com/googleapis/python-api-common-protos/issues/21
Source1:        LICENSE
BuildRequires:  %{python_module setuptools}
BuildRequires:  fdupes
BuildRequires:  python-rpm-macros
Requires:       python-protobuf >= 3.6.0
Recommends:     python-grpcio >= 1.0.0
BuildArch:      noarch
BuildRequires:  %{python_module protobuf >= 3.6.0}
%python_subpackages

%description
googleapis-common-protos contains the python classes generated from the common
protos in the googleapis_ repository.

%prep
%setup -q -n googleapis-common-protos-%{version}

%build
cp %{SOURCE1} .
%python_build

%install
%python_install
%python_expand %fdupes %{buildroot}%{$python_sitelib}

# no tests

%files %{python_files}
%license LICENSE
%doc README.md
%{python_sitelib}/*

%changelog
