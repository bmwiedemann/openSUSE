#
# spec file for package python-augeas
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
Name:           python-augeas
Version:        0.5.0
Release:        0
Summary:        Python bindings for Augeas
License:        LGPL-2.1-or-later
Group:          Development/Languages/Python
Url:            http://augeas.net/
Source:         https://fedorahosted.org/released/python-augeas/python-augeas-%{version}.tar.gz
BuildRequires:  augeas-lenses
BuildRequires:  python-rpm-macros
BuildRequires:  %{python_module setuptools}
Requires:       augeas
# We'd always want to have augeas-lenses installed
Requires:       augeas-lenses
BuildArch:      noarch
%python_subpackages

%description
Python bindings for Augeas, a library for programmatically editing
configuration files.

%prep
%setup -q

%build
%python_build

%install
%python_install

%check
cd test
%python_exec test_augeas.py

%files %{python_files}
%doc AUTHORS README.txt
%license COPYING
%{python_sitelib}/*

%changelog
