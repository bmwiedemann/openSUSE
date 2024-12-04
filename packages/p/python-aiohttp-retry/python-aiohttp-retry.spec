#
# spec file for package python-aiohttp-retry
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


%define modname aiohttp_retry
Name:           python-aiohttp-retry
Version:        2.9.1
Release:        0
Summary:        Simple retry client for aiohttp
License:        MIT
URL:            https://github.com/inyutin/aiohttp_retry
# Source0:         https://files.pythonhosted.org/packages/source/a/%%{modname}/%%{modname}-%%{version}.tar.gz
Source0:        https://github.com/inyutin/%{modname}/archive/refs/tags/v%{version}.tar.gz#/%{modname}-%{version}.tar.gz
# PATCH-FIX-UPSTREAM fix_version.patch gh#inyutin/aiohttp_retry@1a3bc19e15de mcepl@suse.com
# add missing version bump
Patch0:         fix_version.patch
BuildRequires:  %{python_module pip}
BuildRequires:  %{python_module setuptools}
BuildRequires:  %{python_module wheel}
BuildRequires:  fdupes
BuildRequires:  python-rpm-macros
Requires:       python-aiohttp
Recommends:     python-yarl
BuildArch:      noarch
# SECTION test requirements
BuildRequires:  %{python_module aiohttp}
BuildRequires:  %{python_module pytest-aiohttp}
BuildRequires:  %{python_module pytest}
# /SECTION
%python_subpackages

%description
Simple retry client for aiohttp.

%prep
%autosetup -p1 -n %{modname}-%{version}

%build
%pyproject_wheel

%install
%pyproject_install
%python_expand %fdupes %{buildroot}%{$python_sitelib}

%check
export PYTHONPATH=.
%pytest

%files %{python_files}
%{python_sitelib}/%{modname}
%{python_sitelib}/%{modname}-%{version}*-info

%changelog
