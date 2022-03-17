#
# spec file for package python-aiodataloader
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


%{?!python_module:%define python_module() python-%{**} python3-%{**}}
Name:           python-aiodataloader
Version:        0.2.1
Release:        0
Summary:        Asyncio DataLoader implementation for Python
License:        MIT
URL:            https://github.com/syrusakbary/aiodataloader
Source:         https://github.com/syrusakbary/aiodataloader/archive/v%{version}.tar.gz#/%{name}-%{version}.tar.gz
# pypi tarball has no tests
#Source:         https://files.pythonhosted.org/packages/source/a/aiodataloader/aiodataloader-%%{version}.tar.gz
BuildRequires:  %{python_module setuptools}
BuildRequires:  fdupes
BuildRequires:  python-rpm-macros
# SECTION tests
BuildRequires:  %{python_module pytest >= 3.6}
BuildRequires:  %{python_module pytest-asyncio}
BuildArch:      noarch
%python_subpackages

%description
A generic utility to be used as part of your application's
data fetching layer to provide a simplified and consistent API over
various remote data sources such as databases or web services via
batching and caching.

%prep
%setup -q -n aiodataloader-%{version}

%build
%python_build

%install
%python_install
%python_expand %fdupes %{buildroot}%{$python_sitelib}

%check
%pytest

%files %{python_files}
%doc README.md
%license LICENSE
%{python_sitelib}/*

%changelog
