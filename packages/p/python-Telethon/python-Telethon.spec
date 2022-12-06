#
# spec file for package python-Telethon
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
# Python2 is not supported
%define skip_python2 1
%define modname Telethon
Name:           python-Telethon
Version:        1.26.0
Release:        0
Summary:        Full-featured Telegram client library for Python 3
License:        MIT
URL:            https://github.com/LonamiWebs/Telethon
Source:         https://github.com/LonamiWebs/%{modname}/archive/refs/tags/v%{version}.tar.gz#/%{modname}-%{version}.tar.gz
BuildRequires:  %{python_module pyaes}
BuildRequires:  %{python_module pytest-asyncio}
BuildRequires:  %{python_module pytest-tornasync}
BuildRequires:  %{python_module pytest-trio}
BuildRequires:  %{python_module pytest}
BuildRequires:  %{python_module rsa}
BuildRequires:  %{python_module setuptools}
BuildRequires:  fdupes
BuildRequires:  python-rpm-macros
Requires:       python-pyaes
Requires:       python-rsa
BuildArch:      noarch
%python_subpackages

%description
Telethon is an asyncio Python 3 MTProto library to interact with Telegram's API as a user or through a bot account (bot API alternative).

%prep
%setup -q -n Telethon-%{version}
chmod 644 *.rst LICENSE

%build
%python_build

%install
%python_install
%python_expand %fdupes %{buildroot}%{$python_sitelib}

%check
# test_all_methods_present needs readthedocs available
%pytest -k 'not test_all_methods_present'

%files %{python_files}
%doc README.rst
%license LICENSE
%{python_sitelib}/telethon
%{python_sitelib}/Telethon-%{version}-py*.egg-info

%changelog
