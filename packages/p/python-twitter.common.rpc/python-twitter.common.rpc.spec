#
# spec file for package python-twitter.common.rpc
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


Name:           python-twitter.common.rpc
Version:        0.3.11
Release:        0
Summary:        Thrift helpers including finagle and SSL transports
License:        Apache-2.0
Group:          Development/Languages/Python
Url:            https://github.com/twitter/commons
Source0:        https://files.pythonhosted.org/packages/source/t/twitter.common.rpc/twitter.common.rpc-%{version}.tar.gz
Source1:        https://raw.githubusercontent.com/twitter/commons/master/LICENSE
BuildRequires:  %{python_module devel}
BuildRequires:  %{python_module setuptools}
BuildRequires:  %{python_module twitter.common.finagle-thrift}
BuildRequires:  %{python_module twitter.common.lang}
BuildRequires:  python-rpm-macros
%python_subpackages

%description
twitter.common.rpc is a Python library with Thrift helpers including finagle
and SSL transport. It's a part of twitter.common set of libraries.

%prep
%setup -q -n twitter.common.rpc-%{version}
cp %{SOURCE1} .

%build
%python_build

%install
%python_install

%files %{python_files}
%license LICENSE
%{python_sitelib}/*

%changelog
