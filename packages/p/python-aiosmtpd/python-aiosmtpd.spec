#
# spec file for package python-aiosmtpd
#
# Copyright (c) 2021 SUSE LLC
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


%{?!python_module:%define python_module() python3-%{**}}
%define skip_python2 1
Name:           python-aiosmtpd
Version:        1.4.2
Release:        0
Summary:        SMTP server based on asyncio
License:        Apache-2.0
Group:          Development/Languages/Python
URL:            https://aiosmtpd.readthedocs.io/
Source:         https://github.com/aio-libs/aiosmtpd/archive/%{version}.tar.gz#/aiosmtpd-%{version}.tar.gz
Source1:        http://www.apache.org/licenses/LICENSE-2.0.txt
BuildRequires:  %{python_module setuptools}
BuildRequires:  fdupes
BuildRequires:  git-core
BuildRequires:  python-rpm-macros
Requires:       python-atpublic
Requires:       python-attrs
%if 0%{python_version_nodots} < 38
Requires:       python-typing_extensions
%endif
Requires:       user(nobody)
Requires(post): update-alternatives
Requires(postun):update-alternatives
BuildArch:      noarch
# SECTION test requirements
BuildRequires:  %{python_module atpublic}
BuildRequires:  %{python_module attrs}
BuildRequires:  %{python_module pytest-mock}
BuildRequires:  %{python_module pytest}
# this package is used in projects which do not support boolean python_module BuildRequires yet :(
%if 0%{?suse_version} >= 1550
BuildRequires:  python36-typing_extensions
%else
BuildRequires:  python3-typing_extensions
%endif
BuildRequires:  user(nobody)
# /SECTION
%python_subpackages

%description
SMTP server based on asyncio.

%prep
%setup -q -n aiosmtpd-%{version}
cp %{SOURCE1} .

%build
%python_build

%install
%python_install
%python_clone -a %{buildroot}%{_bindir}/aiosmtpd
%python_expand %fdupes %{buildroot}%{$python_sitelib}

%check
# https://github.com/aio-libs/aiosmtpd/issues/268
donttest="(test_byclient and login and False)"
%pytest -k "not ($donttest)"

%post
%python_install_alternative aiosmtpd

%postun
%python_uninstall_alternative aiosmtpd

%files %{python_files}
%doc README.rst
%license LICENSE-2.0.txt
%python_alternative %{_bindir}/aiosmtpd
%{python_sitelib}/aiosmtpd
%{python_sitelib}/aiosmtpd-%{version}*-info
%exclude %{python_sitelib}/aiosmtpd/docs

%changelog
