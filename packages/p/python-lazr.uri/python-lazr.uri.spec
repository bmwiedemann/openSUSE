#
# spec file for package python-lazr.uri
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


Name:           python-lazr.uri
Version:        1.0.3
Release:        0
Summary:        Code for parsing and dealing with URI
License:        LGPL-3.0-or-later
Group:          Development/Languages/Python
URL:            https://launchpad.net/lazr.uri
Source:         https://files.pythonhosted.org/packages/source/l/lazr.uri/lazr.uri-%{version}.tar.gz
BuildRequires:  %{python_module setuptools}
BuildRequires:  fdupes
BuildRequires:  python-rpm-macros
BuildArch:      noarch
%python_subpackages

%description
The lazr.uri package includes code for parsing and dealing with URIs.

%prep
%setup -q -n lazr.uri-%{version}

%build
%python_build

%install
%python_install
%python_expand %fdupes %{buildroot}%{$python_sitelib}

%check
%python_exec setup.py test

%files %{python_files}
%license COPYING.txt
%doc README.txt
%{python_sitelib}/*

%changelog
