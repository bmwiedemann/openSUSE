#
# spec file for package python-requests-aws
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

# Please submit bugfixes or comments via http://bugs.opensuse.org/
#


%{?!python_module:%define python_module() python-%{**} python3-%{**}}
Name:           python-requests-aws
Version:        0.1.8
Release:        0
Summary:        AWS authentication for Amazon S3 for the python requests module
License:        BSD-3-Clause
Group:          Development/Languages/Python
URL:            https://github.com/tax/python-requests-aws
Source:         https://files.pythonhosted.org/packages/source/r/requests-aws/requests-aws-%{version}.tar.gz
BuildRequires:  %{python_module devel}
BuildRequires:  %{python_module requests}
BuildRequires:  %{python_module setuptools}
BuildRequires:  python-rpm-macros
Requires:       python-requests >= 2.4.1
BuildArch:      noarch
%python_subpackages

%description
AWS authentication for Amazon S3 for the Python "requests" library.
It is made to work with Python 2.7 and 3.
At the moment, only S3 is supported.

%prep
%setup -q -n requests-aws-%{version}

%build
%python_build

%install
%python_install

%files %{python_files}
%license LICENSE.txt
%doc README.md
%{python_sitelib}/*

%changelog
