#
# spec file for package python-junitxml
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
Name:           python-junitxml
Version:        0.7
Release:        0
Summary:        A pyunit extension to output JUnit compatible XML
License:        LGPL-3.0-or-later
Group:          Development/Languages/Python
URL:            https://launchpad.net/pyjunitxml
Source:         https://files.pythonhosted.org/packages/source/j/junitxml/junitxml-%{version}.tar.gz
# tests are failing
Patch0:         junitxml-tests.patch
BuildRequires:  %{python_module setuptools}
BuildRequires:  fdupes
BuildArch:      noarch
%python_subpackages

%description
A Python unittest TestResult that outputs JUnit compatible XML.

%prep
%setup -q -n junitxml-%{version}
%patch0 -p1

%build
%python_build

%install
%python_install
%python_expand %fdupes %{buildroot}%{$python_sitelib}

%python_clone -a %{buildroot}%{_bindir}/pyjunitxml

%post
%python_install_alternative pyjunitxml

%postun
%python_uninstall_alternative pyjunitxml

%check
%python_exec -m unittest discover

%files %{python_files}
%license COPYING
%doc README
%python_alternative %{_bindir}/pyjunitxml
%{python_sitelib}/*

%changelog
