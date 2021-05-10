#
# spec file for package python-mailman-web
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


%{?!python_module:%define python_module() python3-%{**}}
# mailman is built only for primary python3 flavor
%define pythons python3
Name:           python-mailman-web
Version:        0.0.1
Release:        0
Summary:        Mailman 3 Web interface
License:        GPL-3.0-only
URL:            https://gitlab.com/mailman/mailman-web
Source:         https://files.pythonhosted.org/packages/source/m/mailman-web/mailman-web-%{version}.tar.gz
BuildRequires:  %{python_module devel}
BuildRequires:  %{python_module setuptools_scm}
BuildRequires:  %{python_module setuptools}
BuildRequires:  fdupes
BuildRequires:  python-rpm-macros
Requires:       python-Django
Requires:       python-HyperKitty
Requires:       python-Whoosh
Requires:       python-django-settings-toml >= 0.0.3
Requires:       python-postorius
BuildArch:      noarch
# SECTION test requirements
BuildRequires:  %{python_module Django}
BuildRequires:  %{python_module HyperKitty}
BuildRequires:  %{python_module Whoosh}
BuildRequires:  %{python_module django-settings-toml >= 0.0.3}
BuildRequires:  %{python_module postorius}
# /SECTION
%if 0%{python3_version_nodots} == 38
# help in replacing any previously installed multiflavor package back to the primary python3 package
Provides:       python38-mailman-web = %{version}-%{release}
Obsoletes:      python38-mailman-web < %{version}-%{release}
%endif
%python_subpackages

%description
Mailman 3 Web interface.

%prep
%setup -q -n mailman-web-%{version}

%build
%python_build

%install
%python_install
%python_expand %fdupes %{buildroot}%{$python_sitelib}

%check
# no upstream testsuite

%files %{python_files}
%doc README.rst docs/*.rst docs/*.toml
%license LICENSE.txt
%{python_sitelib}/*

%changelog
