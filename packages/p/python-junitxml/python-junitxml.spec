#
# spec file for package python-junitxml
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


Name:           python-junitxml
Version:        0.7
Release:        0
Summary:        A pyunit extension to output JUnit compatible XML
License:        LGPL-3.0-or-later
URL:            https://launchpad.net/pyjunitxml
Source:         https://files.pythonhosted.org/packages/source/j/junitxml/junitxml-%{version}.tar.gz
# tests are failing
Patch0:         junitxml-tests.patch
BuildRequires:  %{python_module pip}
BuildRequires:  %{python_module setuptools}
BuildRequires:  %{python_module wheel}
BuildRequires:  %{python_module xml}
BuildRequires:  fdupes
BuildRequires:  python-rpm-macros
Requires(post): update-alternatives
Requires(postun): update-alternatives
BuildArch:      noarch
%python_subpackages

%description
A Python unittest TestResult that outputs JUnit compatible XML.

%prep
%autosetup -p1 -n junitxml-%{version}

%build
%pyproject_wheel

%install
%pyproject_install
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
%{python_sitelib}/junitxml
%{python_sitelib}/junitxml-%{version}.dist-info

%changelog
