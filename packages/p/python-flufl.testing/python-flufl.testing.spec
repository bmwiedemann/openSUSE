#
# spec file for package python-flufl.testing
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
%define skip_python2 1
Name:           python-flufl.testing
Version:        0.8
Release:        0
Summary:        A small collection of test tool plugins
License:        Apache-2.0
URL:            https://gitlab.com/warsaw/flufl.testing
Source:         https://files.pythonhosted.org/packages/source/f/flufl.testing/flufl.testing-%{version}.tar.gz
BuildRequires:  %{python_module setuptools}
BuildRequires:  fdupes
BuildRequires:  python-rpm-macros
BuildArch:      noarch
%python_subpackages

%description
A small collection of test tool plugins

%prep
%setup -q -n flufl.testing-%{version}

%build
%python_build

%install
%python_install
%python_expand %fdupes %{buildroot}%{$python_sitelib}

%check
# no upstream tests found

%files %{python_files}
%doc NEWS.rst README.rst
%license LICENSE.txt
%{python_sitelib}/*

%changelog
