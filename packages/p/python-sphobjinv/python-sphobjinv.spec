#
# spec file for package python-sphobjinv
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
%define skip_python2 1
Name:           python-sphobjinv
Version:        2.0.1
Release:        0
Summary:        Sphinx objectsinv Inspection/Manipulation Tool
License:        MIT
Group:          Development/Languages/Python
URL:            https://github.com/bskinn/sphobjinv
Source:         https://files.pythonhosted.org/packages/source/s/sphobjinv/sphobjinv-%{version}.tar.gz
BuildRequires:  %{python_module pathlib}
BuildRequires:  %{python_module setuptools}
BuildRequires:  fdupes
BuildRequires:  python-rpm-macros
Requires:       python-attrs >= 17.4
Requires:       python-certifi
Requires:       python-fuzzywuzzy >= 0.3
Requires:       python-jsonschema >= 2.0
Requires:       python-setuptools
Requires(post): update-alternatives
Requires(postun): update-alternatives
BuildArch:      noarch
# SECTION test requirements
BuildRequires:  %{python_module attrs >= 17.4}
BuildRequires:  %{python_module certifi}
BuildRequires:  %{python_module fuzzywuzzy >= 0.3}
BuildRequires:  %{python_module jsonschema >= 2.0}
# /SECTION
%python_subpackages

%description
Sphinx objects.inv Inspection/Manipulation Tool

%prep
%setup -q -n sphobjinv-%{version}

%build
%python_build

%install
%python_install
%python_clone -a %{buildroot}%{_bindir}/sphobjinv
%python_expand %fdupes %{buildroot}%{$python_sitelib}

%post
%python_install_alternative sphobjinv

%postun
%python_uninstall_alternative sphobjinv

%files %{python_files}
%doc CHANGELOG.md README.rst
%license LICENSE.txt
%python_alternative %{_bindir}/sphobjinv
%{python_sitelib}/*

%changelog
