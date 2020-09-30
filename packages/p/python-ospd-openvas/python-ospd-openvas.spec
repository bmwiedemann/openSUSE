#
# spec file for package python-ospd-openvas
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
Name:           python-ospd-openvas
Version:        20.8.0
Release:        0
Summary:        An OSP server implementation
License:        AGPL-3.0-or-later
URL:            https://github.com/greenbone/ospd-openvas
Source:         https://github.com/greenbone/ospd-openvas/archive/v%{version}.tar.gz#/ospd-openvas-%{version}.tar.gz
Source98:       https://github.com/greenbone/ospd-openvas/releases/download/v%{version}/ospd-openvas-%{version}.tar.gz.sig
Source99:       https://www.greenbone.net/GBCommunitySigningKey.asc#/ospd-openvas.keyring
BuildRequires:  %{python_module setuptools}
BuildRequires:  fdupes
BuildRequires:  python-rpm-macros
Requires:       python-ospd >= 2.0.0
Requires:       python-packaging
Requires:       python-psutil
Requires:       python-redis >= 3.0.1
Provides:       ospd-openvas
BuildArch:      noarch
# SECTION test requirements
BuildRequires:  %{python_module Deprecated}
BuildRequires:  %{python_module ospd >= 2.0.0}
BuildRequires:  %{python_module packaging}
BuildRequires:  %{python_module psutil}
BuildRequires:  %{python_module pytest}
BuildRequires:  %{python_module redis >= 3.0.1}
# /SECTION
%python_subpackages

%description
An OSP server implementation to allow GVM to remotely control OpenVAS.

%prep
%setup -q -n ospd-openvas-%{version}

%build
%python_build

%install
%python_install
%python_clone -a %{buildroot}%{_bindir}/ospd-openvas
%python_expand %fdupes %{buildroot}%{$python_sitelib}

%post
%python_install_alternative ospd-openvas

%postun
%python_uninstall_alternative ospd-openvas

%check
%pytest

%files %{python_files}
%license COPYING
%doc CHANGELOG.md README.md
%python_alternative %{_bindir}/ospd-openvas
%{python_sitelib}/ospd_openvas*

%changelog
