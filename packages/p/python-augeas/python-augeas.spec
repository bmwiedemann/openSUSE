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
Version:        1.2.0
Release:        0
Summary:        Python bindings for Augeas
License:        LGPL-2.1-or-later
URL:            http://augeas.net/
Source:         https://github.com/hercules-team/python-augeas/archive/v%{version}/%{name}-%{version}.tar.gz
BuildRequires:  %{python_module cffi >= 1.0.0}
BuildRequires:  %{python_module devel}
BuildRequires:  %{python_module pip}
BuildRequires:  %{python_module pytest}
BuildRequires:  %{python_module setuptools}
BuildRequires:  %{python_module wheel}
BuildRequires:  augeas-devel
BuildRequires:  augeas-lenses
BuildRequires:  fdupes
BuildRequires:  python-rpm-macros
Requires:       augeas
Requires:       python-cffi >= 1.0.0
# We'd always want to have augeas-lenses installed
Requires:       augeas-lenses
%python_subpackages

%description
Python bindings for Augeas, a library for programmatically editing
configuration files.

%prep
%setup -q

%build
%pyproject_wheel

%install
%pyproject_install
%python_expand %fdupes %{buildroot}%{$python_sitearch}

%check
%pytest_arch

%files %{python_files}
%doc AUTHORS README.md
%license COPYING
%{python_sitearch}/augeas
%{python_sitearch}/_augeas.abi3.so
%{python_sitearch}/python_augeas-%{version}.dist-info

%changelog
