#
# spec file for package python-augeas
#
# Copyright (c) 2024 SUSE LLC
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


%{?sle15allpythons}
Name:           python-augeas
Version:        1.1.0
Release:        0
Summary:        Python bindings for Augeas
License:        LGPL-2.1-or-later
Group:          Development/Languages/Python
URL:            http://augeas.net/
Source:         https://github.com/hercules-team/python-augeas/archive/v%{version}/%{name}-%{version}.tar.gz
BuildRequires:  %{python_module cffi >= 1.0.0}
BuildRequires:  %{python_module setuptools}
BuildRequires:  augeas-lenses
BuildRequires:  python-rpm-macros
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

# do not pack tests
%python_expand rm -rf %{buildroot}%{$python_sitelib}/test

%check
cd test
%python_exec test_augeas.py

%files %{python_files}
%doc AUTHORS README.txt
%license COPYING
%{python_sitelib}/*

%changelog
