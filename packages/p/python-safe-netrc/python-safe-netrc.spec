#
# spec file for package python-safe-netrc
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


%global srcname safe-netrc
%define modname %(echo %{srcname} | tr '-' '_')
Name:           python-safe-netrc
Version:        1.0.1
Release:        0
Summary:        Safe netrc file parser
License:        GPL-2.0-or-later
URL:            https://git.ligo.org/emfollow/safe-netrc
Source:         https://files.pythonhosted.org/packages/source/s/safe-netrc/%{srcname}-%{version}.tar.gz
BuildRequires:  %{python_module base >= 3.9}
BuildRequires:  %{python_module pip}
BuildRequires:  %{python_module pytest}
BuildRequires:  %{python_module setuptools_scm}
BuildRequires:  %{python_module wheel}
BuildRequires:  fdupes
BuildRequires:  python-rpm-macros
BuildArch:      noarch
%python_subpackages

%description
This package provides a subclass of the Python standard library netrc.netrc
class to add some custom behaviors.

%prep
%setup -q -n %{srcname}-%{version}

%build
%pyproject_wheel

%install
%pyproject_install
%python_expand %fdupes %{buildroot}%{$python_sitelib}

%check
%pytest

%files %{python_files}
%doc README.md
%license LICENSE.md
%{python_sitelib}/%{modname}/
%{python_sitelib}/%{modname}-%{version}*.*-info/

%changelog
