#
# spec file for package python-mhash
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


%define skip_python3 1
%{?!python_module:%define python_module() python-%{**} python3-%{**}}
Name:           python-mhash
Version:        1.4
Release:        0
Summary:        Python interface to the mhash library
License:        LGPL-2.1+
Group:          Development/Libraries/Python
URL:            http://labix.org/python-mhash
Source:         http://labix.org/download/python-mhash/%{name}-%{version}.tar.gz
BuildRequires:  %{python_module devel}
BuildRequires:  %{python_module setuptools}
BuildRequires:  mhash-devel
BuildRequires:  python-rpm-macros
%python_subpackages

%description
python-mhash is a comprehensive Python interface to the mhash library,
which provides a uniform interface to access several hashing algorithms
such as MD4, MD5, SHA1, SHA160, and many others.

%prep
%setup -q

%build
%python_build

%install
%python_install

%files %{python_files}
%doc AUTHORS LICENSE NEWS README
%{python_sitearch}/*

%changelog
