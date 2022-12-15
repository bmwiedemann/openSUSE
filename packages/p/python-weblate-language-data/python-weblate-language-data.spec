#
# spec file for package python-weblate-language-data
#
# Copyright (c) 2022 SUSE LLC
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
%define modname weblate-language-data
%define skip_python2 1
Name:           python-weblate-language-data
Version:        2022.9
Release:        0
Summary:        Language Data for Weblate
License:        MIT
URL:            https://github.com/WeblateOrg/language-data
Source0:        https://files.pythonhosted.org/packages/source/w/%{modname}/%{modname}-%{version}.tar.gz
BuildRequires:  %{python_module setuptools}
BuildRequires:  %{python_module translate-toolkit >= 3.1}
BuildRequires:  fdupes
BuildRequires:  python-rpm-macros
BuildArch:      noarch
%python_subpackages

%description
Contains several modules containing language definitions and Gettext
translations for them (in a way that they would be discovered by Django
when used as an Django application).

%prep
%setup -q -n %{modname}-%{version}

%build
%python_build

%install
%python_install
%python_expand %fdupes %{buildroot}%{$python_sitelib}/weblate_language_data

%files %{python_files}
%license LICENSE
%doc README.rst
%{python_sitelib}/*

%changelog
