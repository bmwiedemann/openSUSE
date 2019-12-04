#
# spec file for package python-authheaders
#
# Copyright (c) 2019 SUSE LINUX GmbH, Nuernberg, Germany.
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
Name:           python-authheaders
Version:        0.12.0
Release:        0
Summary:        A library wrapping email authentication header verification and generation
License:        MIT
URL:            https://github.com/ValiMail/authentication-headers
Source:         https://files.pythonhosted.org/packages/source/a/authheaders/authheaders-%{version}.tar.gz
BuildRequires:  %{python_module setuptools}
BuildRequires:  fdupes
BuildRequires:  python-rpm-macros
Requires:       python-authres >= 1.0.1
Requires:       python-dkimpy >= 0.7.1
Requires:       python-dnspython
Requires:       python-publicsuffix
BuildArch:      noarch
# SECTION test requirements
BuildRequires:  %{python_module authres >= 1.2.0}
BuildRequires:  %{python_module dkimpy >= 0.7.1}
BuildRequires:  %{python_module dnspython}
BuildRequires:  %{python_module publicsuffix}
BuildRequires:  %{python_module pytest}
# /SECTION
%python_subpackages

%description
A library wrapping email authentication header verification and generation.

%prep
%setup -q -n authheaders-%{version}

%build
%python_build

%install
%python_install
%python_expand %fdupes %{buildroot}%{$python_sitelib}

%check
%pytest

%files %{python_files}
%doc CHANGES README.md
%license COPYING
%{python_sitelib}/*

%changelog
