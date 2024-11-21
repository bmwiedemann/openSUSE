#
# spec file for package python-weblate-language-data
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


%{?sle15_python_module_pythons}
%define modname weblate_language_data
Name:           python-weblate-language-data
Version:        2024.14
Release:        0
Summary:        Language Data for Weblate
License:        MIT
URL:            https://github.com/WeblateOrg/language-data
Source0:        https://files.pythonhosted.org/packages/source/w/%{modname}/%{modname}-%{version}.tar.gz
BuildRequires:  %{python_module pip}
BuildRequires:  %{python_module setuptools}
BuildRequires:  %{python_module translate-toolkit >= 3.1}
BuildRequires:  %{python_module wheel}
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
%pyproject_wheel

%install
%pyproject_install
%python_expand %fdupes %{buildroot}%{$python_sitelib}/weblate_language_data

%files %{python_files}
%license LICENSE
%doc README.rst
%{python_sitelib}/weblate_language_data
%{python_sitelib}/weblate_language_data-%{version}.dist-info

%changelog
