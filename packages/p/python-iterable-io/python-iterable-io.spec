#
# spec file for package python-iterableio
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

Name:           python-iterable-io
Version:        1.0.0
Release:        0
Summary:        Adapt generators and other iterables to a file-like interface
License:        LGPL-3.0
URL:            https://github.com/pR0Ps/iterable-io
Source:         https://files.pythonhosted.org/packages/source/i/iterable-io/iterable-io-%{version}.tar.gz
BuildRequires:  python-rpm-macros
BuildRequires:  %{python_module pip}
BuildRequires:  %{python_module setuptools}
BuildRequires:  %{python_module wheel}
BuildRequires:  %{python_module pytest}
BuildRequires:  fdupes
BuildArch:      noarch
%python_subpackages

%description
Adapt generators and other iterables to a file-like interface

%prep
%autosetup -p1 -n iterable-io-%{version}

%build
%pyproject_wheel

%install
%pyproject_install
%python_expand %fdupes %{buildroot}%{$python_sitelib}

%check
%pytest

%files %{python_files}
%doc README.md
%pycache_only %{python_sitelib}/__pycache__/*
%{python_sitelib}/iterableio.py
%{python_sitelib}/iterable_io-%{version}.dist-info

%changelog
