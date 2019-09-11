#
# spec file for package python-semantic_version
#
# Copyright (c) 2018 SUSE LINUX GmbH, Nuernberg, Germany.
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
Name:           python-semantic_version
Version:        2.6.0
Release:        0
Summary:        A library implementing the 'SemVer' scheme
License:        BSD-2-Clause
Group:          Development/Languages/Python
URL:            https://github.com/rbarrois/python-semanticversion
Source:         https://files.pythonhosted.org/packages/source/s/semantic_version/semantic_version-%{version}.tar.gz
BuildRequires:  %{python_module setuptools}
BuildRequires:  python-rpm-macros
BuildArch:      noarch
%python_subpackages

%description
This small python library provides a few tools to handle `SemVer`_ in Python.
It follows strictly the 2.0.0 version of the SemVer scheme.

%prep
%setup -q -n semantic_version-%{version}

%build
%python_build

%install
%python_install

%files %{python_files}
%license LICENSE
%doc README.rst ChangeLog
%{python_sitelib}/*

%changelog
