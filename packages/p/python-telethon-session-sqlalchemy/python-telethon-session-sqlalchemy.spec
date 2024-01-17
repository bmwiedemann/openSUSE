#
# spec file for package python-telethon-session-sqlalchemy
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
%define skip_python2 1
Name:           python-telethon-session-sqlalchemy
Version:        0.2.16
Release:        0
Summary:        SQLAlchemy backend for Telethon session storage
License:        MIT
URL:            https://github.com/tulir/telethon-session-sqlalchemy
Source:         https://files.pythonhosted.org/packages/source/t/telethon-session-sqlalchemy/telethon-session-sqlalchemy-%{version}.tar.gz
Source99:       https://raw.githubusercontent.com/tulir/telethon-session-sqlalchemy/master/LICENSE
BuildRequires:  %{python_module setuptools}
BuildRequires:  fdupes
BuildRequires:  python-rpm-macros
Requires:       python-SQLAlchemy >= 1.2
BuildArch:      noarch
# SECTION test requirements
BuildRequires:  %{python_module SQLAlchemy >= 1.2}
# /SECTION
%python_subpackages

%description
SQLAlchemy backend for Telethon session storage

%prep
%setup -q -n telethon-session-sqlalchemy-%{version}
cp %{SOURCE99} .

%build
%python_build

%install
%python_install
%python_expand %fdupes %{buildroot}%{$python_sitelib}

%files %{python_files}
%doc README.rst
%license LICENSE
%{python_sitelib}/*

%changelog
