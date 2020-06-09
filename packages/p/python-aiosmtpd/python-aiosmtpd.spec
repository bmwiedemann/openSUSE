#
# spec file for package python-aiosmtpd
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
%define skip_python2 1
Name:           python-aiosmtpd
Version:        1.2.1
Release:        0
Summary:        SMTP server based on asyncio
License:        Apache-2.0
Group:          Development/Languages/Python
URL:            https://aiosmtpd.readthedocs.io/
Source:         https://github.com/aio-libs/aiosmtpd/archive/%{version}.tar.gz#/aiosmtpd-%{version}.tar.gz
Source1:        http://www.apache.org/licenses/LICENSE-2.0.txt
Patch0:         https://github.com/aio-libs/aiosmtpd/commit/f414dcdc.patch
BuildRequires:  %{python_module setuptools}
BuildRequires:  fdupes
BuildRequires:  python-rpm-macros
Requires:       python-atpublic
Requires:       user(nobody)
Requires(post): update-alternatives
Requires(postun): update-alternatives
BuildArch:      noarch
# SECTION test requirements
BuildRequires:  %{python_module atpublic}
BuildRequires:  %{python_module pytest}
BuildRequires:  user(nobody)
# /SECTION
%python_subpackages

%description
SMTP server based on asyncio.

%prep
%setup -q -n aiosmtpd-%{version}
%patch0 -p1
cp %{SOURCE1} .

%build
%python_build

%install
%python_install
%python_clone -a %{buildroot}%{_bindir}/aiosmtpd
%python_expand rm -r %{buildroot}%{$python_sitelib}/examples
%python_expand %fdupes %{buildroot}%{$python_sitelib}

%check
%pytest

%post
%python_install_alternative aiosmtpd

%postun
%python_uninstall_alternative aiosmtpd

%files %{python_files}
%doc README.rst
%license LICENSE-2.0.txt
%python_alternative %{_bindir}/aiosmtpd
%{python_sitelib}/*

%changelog
