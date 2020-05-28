#
# spec file for package python-nox
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
Name:           python-nox
Version:        2019.11.9
Release:        0
Summary:        Flexible test automation
License:        Apache-2.0
Group:          Development/Languages/Python
URL:            https://nox.thea.codes
Source:         https://github.com/theacodes/nox/archive/%{version}.tar.gz#/nox-%{version}.tar.gz
BuildRequires:  %{python_module base >= 3.5}
BuildRequires:  %{python_module setuptools}
BuildRequires:  fdupes
BuildRequires:  python-rpm-macros
Requires:       python-argcomplete >= 1.9.4
Requires:       python-colorlog >= 2.6.1
Requires:       python-py >= 1.4.0
Requires:       python-setuptools
Requires:       python-virtualenv >= 14.0.0
Requires(post): update-alternatives
Requires(postun): update-alternatives
Suggests:       python-Jinja2
Suggests:       python-tox
BuildArch:      noarch
# SECTION test requirements
BuildRequires:  %{python_module Flask}
BuildRequires:  %{python_module argcomplete >= 1.9.4}
BuildRequires:  %{python_module colorlog >= 2.6.1}
BuildRequires:  %{python_module contexter}
BuildRequires:  %{python_module py >= 1.4.0}
BuildRequires:  %{python_module pytest}
BuildRequires:  %{python_module tox}
BuildRequires:  %{python_module virtualenv >= 14.0.0}
# Missing deps conda
# /SECTION
%python_subpackages

%description
Flexible test automation.

%prep
%setup -q -n nox-%{version}
# Remove upper pins on dependencies
sed -Ei 's/,? ?<=?[0-9][0-9.]*//' setup.py

%build
%python_build

%install
%python_install
%python_clone -a %{buildroot}%{_bindir}/tox-to-nox
%python_clone -a %{buildroot}%{_bindir}/nox
%python_expand %fdupes %{buildroot}%{$python_sitelib}

%check
%pytest

%post
%python_install_alternative tox-to-nox
%python_install_alternative nox

%postun
%python_uninstall_alternative tox-to-nox
%python_uninstall_alternative nox

%files %{python_files}
%doc README.rst
%license LICENSE
%python_alternative %{_bindir}/nox
%python_alternative %{_bindir}/tox-to-nox
%{python_sitelib}/*

%changelog
