#
# spec file for package python-itsdangerous
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
Name:           python-itsdangerous
Version:        1.1.0
Release:        0
Summary:        Various helpers to pass trusted data to untrusted environments and back
License:        BSD-3-Clause
Group:          Development/Languages/Python
URL:            http://github.com/mitsuhiko/itsdangerous
Source:         https://files.pythonhosted.org/packages/source/i/itsdangerous/itsdangerous-%{version}.tar.gz
BuildRequires:  %{python_module freezegun}
BuildRequires:  %{python_module pytest}
BuildRequires:  %{python_module setuptools}
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
%python_build

%install
%python_install
%python_expand %fdupes %{buildroot}%{$python_sitelib}

%check
%pytest tests

%files %{python_files}
%license LICENSE.rst
%doc CHANGES.rst README.rst
%{python_sitelib}/*

%changelog
