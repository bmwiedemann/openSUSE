#
# spec file for package python-wtf-peewee
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


%{?!python_module:%define python_module() python-%{**} python3-%{**}}
Name:           python-wtf-peewee
Version:        3.0.6
Release:        0
Summary:        WTForms integration for peewee models
License:        MIT
URL:            https://github.com/coleifer/wtf-peewee/
Source:         https://files.pythonhosted.org/packages/source/w/wtf-peewee/wtf-peewee-%{version}.tar.gz
BuildRequires:  %{python_module WTForms}
BuildRequires:  %{python_module peewee >= 3.0.0}
BuildRequires:  %{python_module pip}
BuildRequires:  %{python_module setuptools}
BuildRequires:  %{python_module wheel}
BuildRequires:  %{pythons}
BuildRequires:  fdupes
BuildRequires:  python-rpm-macros
Requires:       python-WTForms
Requires:       python-peewee >= 3.0.0
BuildArch:      noarch
%python_subpackages

%description
wtf-peewee provides a bridge between peewee models and wtforms, mapping
model fields to form fields.

%prep
%autosetup -p1 -n wtf-peewee-%{version}

%build
%pyproject_wheel

%install
%pyproject_install
%python_expand %fdupes %{buildroot}%{$python_sitelib}

%check
%pyunittest -v

%files %{python_files}
%doc README.md
%license LICENSE
%{python_sitelib}/wtfpeewee/
%{python_sitelib}/wtf_peewee-%{version}*-info

%changelog
