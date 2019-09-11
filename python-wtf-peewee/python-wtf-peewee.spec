#
# spec file for package python-wtf-peewee
#
# Copyright (c) 2018 SUSE LINUX GmbH, Nuernberg, Germany.
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
Version:        3.0.0
Release:        0
Summary:        WTForms integration for peewee models
License:        MIT
Group:          Development/Languages/Python
Url:            https://github.com/coleifer/wtf-peewee/
Source:         https://files.pythonhosted.org/packages/source/w/wtf-peewee/wtf-peewee-%{version}.tar.gz
BuildRequires:  python-rpm-macros
%if %{suse_version} < 1500
BuildRequires:  python2
%endif
BuildRequires:  %{python_module setuptools}
# SECTION test requirements
BuildRequires:  %{python_module WTForms}
BuildRequires:  %{python_module peewee >= 3.0.0}
# /SECTION
BuildRequires:  fdupes
Requires:       python-WTForms
Requires:       python-peewee >= 3.0.0
BuildArch:      noarch

%python_subpackages

%description
wtf-peewee provides a bridge between peewee models and wtforms, mapping
model fields to form fields.

%prep
%setup -q -n wtf-peewee-%{version}

%build
%python_build

%install
%python_install
%python_expand %fdupes %{buildroot}%{$python_sitelib}

%check
%python_exec setup.py test

%files %{python_files}
%doc README.md
%license LICENSE
%{python_sitelib}/wtfpeewee/
%{python_sitelib}/wtf_peewee-%{version}-py%{py_ver}.egg-info

%changelog
