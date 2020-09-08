#
# spec file for package python-fsspec
#
# Copyright (c) 2020 SUSE LLC
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
%define         skip_python2 1
Name:           python-fsspec
Version:        0.8.0
Release:        0
Summary:        Filesystem specification package
License:        BSD-3-Clause
URL:            https://github.com/intake/filesystem_spec
Source:         https://github.com/intake/filesystem_spec/archive/%{version}.tar.gz
BuildRequires:  %{python_module setuptools}
BuildRequires:  fdupes
BuildRequires:  python-rpm-macros
BuildArch:      noarch
# SECTION test requirements
BuildRequires:  %{python_module fusepy}
BuildRequires:  %{python_module numpy}
BuildRequires:  %{python_module pytest}
# /SECTION
%python_subpackages

%description
A specification for pythonic filesystems.

%prep
%setup -q -n filesystem_spec-%{version}

%build
%python_build

%install
%python_install
%python_expand %fdupes %{buildroot}%{$python_sitelib}

%check
# test_basic relies on speed of FS and timeouts in OBS
# test_not_cached needs sockets
%pytest -k 'not test_basic and not test_not_cached'

%files %{python_files}
%doc README.md
%license LICENSE
%{python_sitelib}/*

%changelog
