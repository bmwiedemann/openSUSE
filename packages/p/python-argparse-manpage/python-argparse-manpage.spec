#
# spec file for package python-argparse-manpage
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


%define mod_name argparse-manpage
%{?!python_module:%define python_module() python-%{**} python3-%{**}}
Name:           python-argparse-manpage
Version:        1.1
Release:        0
Summary:        Tool for automatic manual page building from a Python ArgumentParser object
License:        Apache-2.0
Group:          Development/Languages/Python
URL:            https://github.com/praiskup/argparse-manpage
Source:         https://github.com/praiskup/argparse-manpage/archive/v%{version}.tar.gz
BuildRequires:  %{python_module pytest}
BuildRequires:  %{python_module setuptools}
BuildRequires:  %{python_module six}
BuildRequires:  fdupes
BuildRequires:  python-rpm-macros
%python_subpackages

%description
This utility generates a manual page in an automatic way from an
ArgumentParser object, so the manpage 1:1 corresponds to the
automatically generated --help output. The manpage generator needs to
known the location of the object, user can specify that by (a) the
module name or corresponding python filename and (b) the object name
or the function name which returns the object. There's a limited
support for (deprecated) optparse objects, too.

%prep
%setup -q -n %{mod_name}-%{version}

%build
%python_build

%install
%python_install
%python_expand %fdupes %{buildroot}%{$python_sitelib}

%check
%pytest

%files %{python_files}
%doc README*
%license LICENSE
%{python_sitelib}/*
%python3_only %{_bindir}/argparse-manpage
%python3_only %{_mandir}/man1/argparse-manpage.1%{?ext_man}

%changelog
