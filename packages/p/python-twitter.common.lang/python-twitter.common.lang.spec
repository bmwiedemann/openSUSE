#
# spec file for package python-twitter.common.lang
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


Name:           python-twitter.common.lang
Version:        0.3.11
Release:        0
Summary:        Python language and compatibility facilities
License:        Apache-2.0
Group:          Development/Languages/Python
URL:            https://github.com/twitter/commons
Source0:        https://files.pythonhosted.org/packages/source/t/twitter.common.lang/twitter.common.lang-%{version}.tar.gz
Source1:        https://raw.githubusercontent.com/twitter/commons/master/LICENSE
BuildRequires:  %{python_module setuptools}
BuildRequires:  python-rpm-macros
%python_subpackages

%description
twitter.commonn.lang is a Python library for language and compatibility
facilities. It's a part of twitter.common set of libraries.

%prep
%setup -q -n twitter.common.lang-%{version}
cp %{SOURCE1} .

%build
%python_build

%install
%python_install

%files %{python_files}
%license LICENSE
%{python_sitelib}/*

%changelog
