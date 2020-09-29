#
# spec file for package python-ospd
#
# Copyright (c) 2020 SUSE LLC
# Copyright (c) 2020, Martin Hauke <mardnh@gmx.de>
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
Name:           python-ospd
Version:        20.8.0
Release:        0
Summary:        A base class for the OSP (Open Scanner Protocol)
License:        GPL-2.0-or-later
Group:          Development/Languages/Python
URL:            https://www.openvas.org
Source:         https://github.com/greenbone/ospd/archive/v%{version}.tar.gz#/ospd-%{version}.tar.gz
Source98:       https://github.com/greenbone/ospd/releases/download/v%{version}/ospd-%{version}.tar.gz.sig
Source99:       https://www.greenbone.net/GBCommunitySigningKey.asc#/%{name}.keyring
BuildRequires:  %{python_module setuptools}
BuildRequires:  fdupes
BuildRequires:  python-rpm-macros
# SECTION test requirements
BuildRequires:  %{python_module Deprecated}
BuildRequires:  %{python_module defusedxml}
BuildRequires:  %{python_module lxml}
BuildRequires:  %{python_module paramiko}
BuildRequires:  %{python_module psutil}
BuildRequires:  %{python_module pytest}
# /SECTION
Requires:       python-defusedxml
Requires:       python-lxml
Requires:       python-paramiko
BuildArch:      noarch
%python_subpackages

%description
OSPD is a base class for scanner wrappers which share the same
communication protocol: OSP (Open Scanner Protocol). OSP creates
a unified interface for different security scanners and makes
their control flow and scan results consistently available under
the central Greenbone Vulnerability Manager service.

%prep
%setup -q -n ospd-%{version}

%build
%python_build

%install
%python_install
# Remove tests from sitelib
%python_expand rm -rf %{buildroot}%{$python_sitelib}/tests
%python_expand %fdupes %{buildroot}%{$python_sitelib}

%check
%pytest

%files %{python_files}
%license COPYING
%doc README.md
%{python_sitelib}/ospd*

%changelog
