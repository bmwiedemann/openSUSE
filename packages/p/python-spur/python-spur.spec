#
# spec file for package python-spur
#
# Copyright (c) 2022 SUSE LLC
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


Name:           python-spur
Version:        0.3.22
Release:        0
Summary:        Run commands and manipulate files locally or over SSH
License:        BSD-2-Clause
URL:            http://github.com/mwilliamson/spur.py
Source:         https://github.com/mwilliamson/spur.py/archive/refs/tags/%{version}.tar.gz#/spur-%{version}-gh.tar.gz
BuildRequires:  python-rpm-macros
BuildRequires:  %{python_module setuptools}
BuildRequires:  %{python_module paramiko >= 1.13.1}
BuildRequires:  fdupes
Requires:       python-paramiko >= 1.13.1
BuildArch:      noarch
%python_subpackages

%description
Run commands and manipulate files locally or over SSH using the same interface

%prep
%autosetup -p1 -n spur.py-%{version}

%build
%python_build

%install
%python_install
%python_expand %fdupes %{buildroot}%{$python_sitelib}

%check
# TODO: denose
#
# This will be hard work, test suite heavily depends on nose.
#
# Upside: This package is used for testing python-locket from the same author,
# so the code is tested to be functional at least there.

%files %{python_files}
%doc README.rst
%{python_sitelib}/spur
%{python_sitelib}/spur-%{version}*-info

%changelog
