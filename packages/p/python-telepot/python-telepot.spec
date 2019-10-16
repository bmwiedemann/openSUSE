#
# spec file for package python-telepot
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
%define pyname telepot
Name:           python-telepot
Version:        12.7
Release:        0
Summary:        Python framework for Telegram Bot API
License:        MIT
URL:            https://github.com/nickoala/telepot
Source:         https://github.com/nickoala/telepot/archive/v%{version}.tar.gz
BuildRequires:  %{python_module setuptools}
BuildRequires:  %{python_module urllib3 >= 1.9.1}
BuildRequires:  fdupes
BuildRequires:  python-rpm-macros
BuildRequires:  python3-aiohttp >= 2.0.0
Requires:       python-urllib3 >= 1.9.1
BuildArch:      noarch
%ifpython3
Requires:       python3-aiohttp >= 2.0.0
%endif
%python_subpackages

%description
Telepot helps you build applications for Telegram Bot API. It works on Python 2.7 and Python 3. It also has an async version based on asyncio and Python 3.5+.

%prep
%setup -q -n telepot-%{version}

%build
%python_build

%install
%python_install
%python_expand %fdupes %{buildroot}%{$python_sitelib}/

%check
# online tests

%files %{python_files}
%doc CHANGELOG.md README.md
%license LICENSE.md
%{python_sitelib}/%{pyname}/
%{python_sitelib}/%{pyname}-%{version}-py%{py_ver}.egg-info

%changelog
