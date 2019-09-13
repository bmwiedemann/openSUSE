#
# spec file for package python-pyppeteer
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
Name:           python-pyppeteer
Version:        0.0.25
Release:        0
License:        MIT
Summary:        Headless chrome/chromium automation library
Url:            https://github.com/miyakogi/pyppeteer
Group:          Development/Languages/Python
Source:         https://files.pythonhosted.org/packages/source/p/pyppeteer/pyppeteer-%{version}.tar.gz
BuildRequires:  python-rpm-macros
BuildRequires:  %{python_module setuptools}
# SECTION test requirements
BuildRequires:  %{python_module appdirs}
BuildRequires:  %{python_module pyee}
BuildRequires:  %{python_module tqdm}
BuildRequires:  %{python_module urllib3}
BuildRequires:  %{python_module websockets}
# Tornado 5 is not available, but is only needed for tests
# BuildRequires:  %%{python_module tornado >= 5}
# /SECTION
BuildRequires:  fdupes
Requires:       python-appdirs
Requires:       python-pyee
Requires:       python-tqdm
Requires:       python-urllib3
Requires:       python-websockets
Recommends:     chromium
BuildArch:      noarch

%python_subpackages

%description
JavaScript (headless) chrome/chromium browser automation library.

%prep
%setup -q -n pyppeteer-%{version}

%build
%python_build

%install
%python_install
%python_expand %fdupes %{buildroot}%{$python_sitelib}

# This just installs chromium
rm -rf %{buildroot}%{_bindir}/pyppeteer-install

# Tests require tornada 5, which is not available
# %%check
# %%python_exec setup.py test

%files %{python_files}
%doc CHANGES.md README.md
%license LICENSE
%{python_sitelib}/*

%changelog
