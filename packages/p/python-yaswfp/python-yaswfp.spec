#
# spec file for package python-yaswfp
#
# Copyright (c) 2025 SUSE LLC
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


%define pkg_version 0.9.3
%bcond_without libalternatives
Name:           python-yaswfp
Version:        0+git.1411687316.2a2cc6c
Release:        0
Summary:        Yet Another SWF Parser
License:        GPL-3.0-only
Group:          Development/Libraries/Python
URL:            https://github.com/facundobatista/yaswfp
Source:         yaswfp-%{version}.tar.xz
BuildRequires:  %{python_module pip}
BuildRequires:  %{python_module pytest}
BuildRequires:  %{python_module setuptools}
BuildRequires:  %{python_module wheel}
BuildRequires:  alts
BuildRequires:  fdupes
BuildRequires:  python-rpm-macros
Requires:       alts
BuildArch:      noarch
%python_subpackages

%description
Yet Another SWF Parser.

%prep
%setup -q -n yaswfp-%{version}

%build
%pyproject_wheel

%install
%pyproject_install
%python_clone -a %{buildroot}%{_bindir}/swfparser
%python_expand %fdupes %{buildroot}%{$python_sitelib}

%check
%pytest

%pre
%python_libalternatives_reset_alternative swfparser

%files %{python_files}
%doc README.rst
%license COPYING
%python_alternative %{_bindir}/swfparser
%{python_sitelib}/yaswfp
%{python_sitelib}/yaswfp-%{pkg_version}*-info

%changelog
