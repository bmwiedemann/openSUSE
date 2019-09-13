#
# spec file for package python-PasteScript
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
%define oldpython python
Name:           python-PasteScript
Version:        3.1.0
Release:        0
Summary:        A pluggable command-line frontend to setup package file layouts
License:        MIT
Group:          Development/Languages/Python
URL:            https://github.com/cdent/pastescript
Source:         https://files.pythonhosted.org/packages/source/P/PasteScript/PasteScript-%{version}.tar.gz
BuildRequires:  %{python_module Paste >= 2.0}
BuildRequires:  %{python_module PasteDeploy}
BuildRequires:  %{python_module nose >= 0.11}
BuildRequires:  %{python_module setuptools}
BuildRequires:  %{python_module six}
BuildRequires:  fdupes
BuildRequires:  python-rpm-macros
Requires:       python-Paste >= 2.0
Requires:       python-PasteDeploy
Requires:       python-setuptools
Requires:       python-six
Requires(post): update-alternatives
Requires(preun): update-alternatives
BuildArch:      noarch
%ifpython2
Provides:       %{oldpython}-pastescript = %{version}
Obsoletes:      %{oldpython}-pastescript < %{version}
%endif
%python_subpackages

%description
This is a pluggable command-line tool. It includes some built-in features:

  * Create file layouts for packages.
  * Serving up web applications, with configuration based on paste.deploy

%prep
%setup -q -n PasteScript-%{version}
# remove with next release
echo "[nosetests]" >> setup.cfg
echo "tests=tests" >> setup.cfg

%build
%python_build

%install
%python_install
%python_expand %fdupes %{buildroot}%{$python_sitelib}

# Prepare for update-alternatives usage
%python_clone -a %{buildroot}%{_bindir}/paster

%check
%python_exec setup.py test

%post
%python_install_alternative paster

%preun
%python_uninstall_alternative paster

%files %{python_files}
%license docs/license.txt
%doc README.rst docs/news.txt
%python_alternative %{_bindir}/paster
%{python_sitelib}/PasteScript-%{version}-py*.egg-info
%{python_sitelib}/PasteScript-%{version}-py*-nspkg.pth
%{python_sitelib}/paste/script/

%changelog
