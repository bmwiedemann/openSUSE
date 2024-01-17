#
# spec file for package python-wadllib
#
# Copyright (c) 2021 SUSE LLC
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
Name:           python-wadllib
Version:        1.3.6
Release:        0
Summary:        Navigate HTTP resources using WADL files as guides
License:        LGPL-3.0-or-later
Group:          Development/Languages/Python
URL:            https://launchpad.net/wadllib
Source:         https://files.pythonhosted.org/packages/source/w/wadllib/wadllib-%{version}.tar.gz
BuildRequires:  %{python_module importlib-metadata}
BuildRequires:  %{python_module lazr.uri}
BuildRequires:  %{python_module setuptools}
BuildRequires:  fdupes
BuildRequires:  python-rpm-macros
Requires:       python-lazr.uri
BuildArch:      noarch
%python_subpackages

%description
An Application object represents a web service described by a WADL
file.

%prep
%setup -q -n wadllib-%{version}

%build
%python_build

%install
%python_install
%python_expand %fdupes %{buildroot}%{$python_sitelib}

%check
cd src
%pyunittest discover -v

%files %{python_files}
%license COPYING.txt
%doc README.rst NEWS.rst HACKING.rst
%{python_sitelib}/*

%changelog
