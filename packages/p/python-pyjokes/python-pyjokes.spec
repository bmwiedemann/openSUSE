#
# spec file for package python-pyjokes
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
Name:           python-pyjokes
Version:        0.6.0
Release:        0
Summary:        One line jokes for programmers (jokes as a service)
License:        BSD-3-Clause
Group:          Development/Languages/Python
URL:            https://github.com/pyjokes/pyjokes
Source:         https://files.pythonhosted.org/packages/source/p/pyjokes/pyjokes-%{version}.tar.gz
Source99:       https://raw.githubusercontent.com/pyjokes/pyjokes/master/LICENCE.txt
BuildRequires:  %{python_module setuptools}
BuildRequires:  fdupes
BuildRequires:  python-rpm-macros
Requires(post): update-alternatives
Requires(postun): update-alternatives
BuildArch:      noarch
%python_subpackages

%description
This package provides one line jokes for programmers (jokes as a service)
Simply call `pyjoke` from the command line and use the -c argumnet to get jokes
from a specific category (neutral/adult/chuck/all). The default is neutral.

%prep
%setup -q -n pyjokes-%{version}
cp %{SOURCE99} .

%build
%python_build

%install
%python_install
%python_clone -a %{buildroot}%{_bindir}/pyjokes
%python_clone -a %{buildroot}%{_bindir}/pyjoke
%python_expand %fdupes %{buildroot}%{$python_sitelib}

%post
%python_install_alternative pyjokes
%python_install_alternative pyjoke

%postun
%python_uninstall_alternative pyjokes
%python_uninstall_alternative pyjoke

%files %{python_files}
%doc README.rst
%license LICENCE.txt
%python_alternative %{_bindir}/pyjoke
%python_alternative %{_bindir}/pyjokes
%{python_sitelib}/*

%changelog
