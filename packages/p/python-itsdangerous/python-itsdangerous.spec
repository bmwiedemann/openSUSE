#
# spec file for package python-itsdangerous
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


%{?sle15_python_module_pythons}
Name:           python-itsdangerous
Version:        2.2.0
Release:        0
Summary:        Various helpers to pass trusted data to untrusted environments and back
License:        BSD-3-Clause
URL:            https://itsdangerous.palletsprojects.com
Source:         https://files.pythonhosted.org/packages/source/i/itsdangerous/itsdangerous-%{version}.tar.gz
BuildRequires:  %{python_module flit-core}
BuildRequires:  %{python_module freezegun}
BuildRequires:  %{python_module pip}
BuildRequires:  %{python_module pytest}
BuildRequires:  %{python_module wheel}
BuildRequires:  fdupes
BuildRequires:  python-rpm-macros
BuildArch:      noarch
%python_subpackages

%description
It's Dangerous
   ... so better sign this

Various helpers to pass data to untrusted environments and to get it back
safe and sound.

This repository provides a module that is a port of the django signing
module.  It's not directly copied but some changes were applied to
make it work better on its own.

Also I plan to add some extra things.  Work in progress.

%prep
%setup -q -n itsdangerous-%{version}

%build
%pyproject_wheel

%install
%pyproject_install
%python_expand %fdupes %{buildroot}%{$python_sitelib}

%check
%pytest tests

%files %{python_files}
%license LICENSE.txt
%doc CHANGES.rst README.md
%{python_sitelib}/itsdangerous
%{python_sitelib}/itsdangerous-%{version}.dist-info

%changelog
