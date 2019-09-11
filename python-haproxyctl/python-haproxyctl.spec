#
# spec file for package python-haproxyctl
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

# Please submit bugfixes or comments via http://bugs.opensuse.org/

%define skip_python2 1

%{?!python_module:%define python_module() python-%{**} python3-%{**}}
Name:           python-haproxyctl
Version:        0.5
Release:        0
License:        GPL-3.0
Summary:        HAProxy control tool
Url:            http://github.com/neurogeek/haproxyctl
Group:          Development/Languages/Python
Source:         https://github.com/neurogeek/haproxyctl/archive/v%{version}.tar.gz#/haproxyctl-%{version}.tar.gz
Source1:        gpl-3.0.txt
BuildRequires:  python-rpm-macros
BuildRequires:  %{python_module setuptools}
BuildRequires:  unzip
BuildRequires:  fdupes
Requires:       haproxy
BuildArch:      noarch

%python_subpackages

%description
This is a utility to control HAProxy features through its admin
socket. haproxyctl has the ability to disable/enable servers, fetch
info from the running instance and list available servers, together
with their status.

%prep
%setup -q -n haproxyctl-%{version}
# The package is under GPL-3.0, as expressed in setup.py, but the
# license file is not included in the source code.
cp %{SOURCE1} .

%build
%python_build

%install
%python_install
%python_expand %fdupes %{buildroot}%{$python_sitelib}

mkdir -p %{buildroot}%{_datadir}/%{name}/
cp -a conf %{buildroot}%{_datadir}/%{name}/

%check
%{python_expand $python -m unittest discover -s haproxy/tests}

%files %{python_files}
%doc README.md
%license gpl-3.0.txt
%dir %{_datadir}/%{name}
%{python_sitelib}/*
%{_bindir}/haproxyctl
%{_datadir}/%{name}/*

%changelog
