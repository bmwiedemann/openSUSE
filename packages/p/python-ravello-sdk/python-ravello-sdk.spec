#
# spec file for package python-ravello-sdk
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
Name:           python-ravello-sdk
Version:        2.17
Release:        0
Summary:        Python SDK for the Ravello API
License:        Apache-2.0
Group:          Development/Languages/Python
URL:            https://github.com/ravello/python-sdk
Source:         https://files.pythonhosted.org/packages/source/r/ravello-sdk/ravello-sdk-%{version}.tar.gz
BuildRequires:  %{python_module docopt}
BuildRequires:  %{python_module requests >= 2.6.0}
BuildRequires:  %{python_module setuptools}
BuildRequires:  %{python_module six}
BuildRequires:  python-rpm-macros
Requires:       python-docopt
Requires:       python-requests >= 2.6.0
Requires:       python-six
BuildArch:      noarch
%python_subpackages

%description
This is a micro-SDK for accessing the Ravello API in Python. It also contains
a few useful utility scripts.

%prep
%setup -q -n ravello-sdk-%{version}

%build
%python_build

%install
%python_install

%check
%python_exec tests/unit.py

%files %{python_files}
%license LICENSE
%doc README.rst
%{python_sitelib}/*

%changelog
