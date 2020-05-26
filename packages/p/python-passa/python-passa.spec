#
# spec file for package python-passa
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
Name:           python-passa
Version:        0.3.0
Release:        0
Summary:        A resolver implementation for Pipenv-compatible Lockfiles
License:        ISC
Group:          Development/Languages/Python
URL:            https://github.com/sarugaku/passa
Source:         https://github.com/sarugaku/passa/archive/%{version}.tar.gz#/passa-%{version}.tar.gz
BuildRequires:  %{python_module setuptools >= 36.2.2}
BuildRequires:  fdupes
BuildRequires:  python-rpm-macros
Requires:       python-appdirs
Requires:       python-distlib
Requires:       python-packaging
Requires:       python-pip-shims >= 0.1.2
Requires:       python-plette >= 0.1.1
Requires:       python-requests
Requires:       python-requirementslib >= 1.1.1
Requires:       python-resolvelib >= 0.2.1
Requires:       python-six
Requires:       python-vistir >= 0.1.4
Requires(post): update-alternatives
Requires(postun): update-alternatives
BuildArch:      noarch
# SECTION test requirements
BuildRequires:  %{python_module appdirs}
BuildRequires:  %{python_module distlib}
BuildRequires:  %{python_module packaging}
BuildRequires:  %{python_module pip-shims >= 0.1.2}
BuildRequires:  %{python_module plette >= 0.1.1}
BuildRequires:  %{python_module pytest}
BuildRequires:  %{python_module requests}
BuildRequires:  %{python_module requirementslib >= 1.1.1}
BuildRequires:  %{python_module resolvelib >= 0.2.1}
BuildRequires:  %{python_module six}
BuildRequires:  %{python_module vistir >= 0.1.4}
# /SECTION
%python_subpackages

%description
A resolver implementation for generating and interacting with Pipenv-compatible Lockfiles.

%prep
%setup -q -n passa-%{version}

%build
%python_build

%install
%python_install
%python_clone -a %{buildroot}%{_bindir}/passa
%python_expand %fdupes %{buildroot}%{$python_sitelib}

%check
%pytest

%post
%python_install_alternative passa

%postun
%python_uninstall_alternative passa

%files %{python_files}
%doc CHANGELOG.rst README.rst
%license LICENSE
%python_alternative %{_bindir}/passa
%{python_sitelib}/*

%changelog
