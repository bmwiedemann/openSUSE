#
# spec file for package python-parfive
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


%{?!python_module:%define python_module() python-%{**} python3-%{**}}
%define         skip_python2 1
Name:           python-parfive
Version:        1.0.0
Release:        0
License:        MIT
Summary:        A HTTP and FTP parallel file downloader
Url:            https://parfive.readthedocs.io/
Group:          Development/Languages/Python
Source:         https://files.pythonhosted.org/packages/source/p/parfive/parfive-%{version}.tar.gz
BuildRequires:  %{python_module devel}
BuildRequires:  %{python_module setuptools}
BuildRequires:  %{python_module setuptools_scm}
BuildRequires:  fdupes
BuildRequires:  python-rpm-macros
# SECTION test requirements
BuildRequires:  %{python_module aioftp}
BuildRequires:  %{python_module aiohttp}
BuildRequires:  %{python_module pytest-asyncio}
BuildRequires:  %{python_module pytest-cov}
BuildRequires:  %{python_module pytest-localserver}
BuildRequires:  %{python_module pytest-socket}
BuildRequires:  %{python_module pytest}
BuildRequires:  %{python_module tqdm}
# /SECTION
Requires:       python-aiohttp
Requires:       python-tqdm
Recommends:     python-aioftp
BuildArch:      noarch

%python_subpackages

%description
A parallel file downloader using asyncio.

%prep
%setup -q -n parfive-%{version}

%build
%python_build

%install
%python_install
%python_expand %fdupes %{buildroot}%{$python_sitelib}

%check
# Disable tests that require a network connection
%pytest -k 'not test_ftp and not test_ftp_http'

%files %{python_files}
%doc README.rst
%license LICENSE
%{python_sitelib}/*

%changelog
