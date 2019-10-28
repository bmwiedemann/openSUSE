#
# spec file for package python-urlgrabber
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
%define modname urlgrabber
Name:           python-urlgrabber
Version:        4.1.0
Release:        0
Summary:        A high-level cross-protocol url-grabber
License:        LGPL-2.1-only
URL:            https://github.com/rpm-software-management/urlgrabber
Source:         https://github.com/rpm-software-management/%{modname}/releases/download/%{modname}-4-1-0/%{modname}-%{version}.tar.gz
BuildRequires:  %{python_module pycurl}
BuildRequires:  %{python_module setuptools}
BuildRequires:  %{python_module six}
BuildRequires:  fdupes
BuildRequires:  python-rpm-macros
Requires:       python-pycurl
Requires:       python-six
BuildArch:      noarch
%python_subpackages

%description
A high-level cross-protocol url-grabber for python supporting HTTP, FTP
and file locations.  Features include keepalive, byte ranges,
throttling, authentication, proxies and more.

%prep
%setup -q -n urlgrabber-%{version}
# Remove with next release
sed -i "13d" urlgrabber/__init__.py # Remove wrong license header, fixes bnc#781323

%build
%python_build

%install
%python_install
rm -rf %{buildroot}%{_datadir}/doc/urlgrabber-%{version} # Remove wrongly installed docs
mv -v %{buildroot}%{_prefix}/libexec/urlgrabber-ext-down %{buildroot}%{_prefix}/lib/urlgrabber-ext-down
%python_expand %fdupes %{buildroot}%{$python_sitelib}

%files %{python_files}
%license LICENSE
%doc ChangeLog README TODO
%python3_only %{_bindir}/urlgrabber
%{python_sitelib}/*
%python3_only %{_prefix}/lib/urlgrabber*

%changelog
