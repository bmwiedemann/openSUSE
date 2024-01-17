#
# spec file for package python-yaswfp
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


%{?!python_module:%define python_module() python-%{**} python3-%{**}}
Name:           python-yaswfp
Version:        0+git.1411687316.2a2cc6c
Release:        0
Summary:        Yet Another SWF Parser
License:        GPL-3.0
URL:            http://github.com/facundobatista/yaswfp
Source:         yaswfp-%{version}.tar.xz
BuildRequires:  python-rpm-macros
BuildRequires:  %{python_module setuptools}
BuildRequires:  %{python_module pytest}

BuildRequires:  fdupes
BuildArch:      noarch
Group:          Development/Libraries/Python

%python_subpackages

%description
Yet Another SWF Parser.

%prep
%setup -q -n yaswfp-%{version}

%build
%python_build

%install
%python_install
%python_clone -a %{buildroot}%{_bindir}/swfparser
%python_expand %fdupes %{buildroot}%{$python_sitelib}

%check
%pytest

%post
%python_install_alternative swfparser

%postun
%python_uninstall_alternative swfparser

%files %{python_files}
%doc README.rst
%license COPYING
%python_alternative %{_bindir}/swfparser
%{python_sitelib}/*

%changelog
