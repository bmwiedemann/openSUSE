#
# spec file for package python-twitter.common.finagle-thrift
#
# Copyright (c) 2024 SUSE LLC
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


Name:           python-twitter.common.finagle-thrift
Version:        0.3.9
Release:        0
Summary:        Thrift stubs for zipkin RPC tracing support in finagle
License:        Apache-2.0
URL:            https://github.com/twitter/commons
Source0:        https://files.pythonhosted.org/packages/source/t/twitter.common.finagle-thrift/twitter.common.finagle-thrift-0.3.9.tar.gz
Source1:        https://raw.githubusercontent.com/twitter/commons/master/LICENSE
Patch0:         setup-ns-fix.patch
BuildRequires:  %{python_module pip}
BuildRequires:  %{python_module setuptools}
BuildRequires:  %{python_module wheel}
BuildRequires:  fdupes
BuildRequires:  python-rpm-macros
%python_subpackages

%description
twitter.common.finagle-thrift is a Python library with Thrift stubs for zipkin
RPC tracing support in finagle. It's a part of twitter.common set of libraries.

%prep
%autosetup -p1 -n twitter.common.finagle-thrift-%{version}
cp %{SOURCE1} .
rm src/__init__.py

%build
%pyproject_wheel

%install
%pyproject_install
%python_expand %fdupes %{buildroot}%{$python_sitelib}

%files %{python_files}
%license LICENSE
%{python_sitelib}/gen
%{python_sitelib}/twitter.common.finagle_thrift-%{version}.dist-info
%{python_sitelib}/twitter.common.finagle_thrift-%{version}-py3.*-nspkg.pth

%changelog
