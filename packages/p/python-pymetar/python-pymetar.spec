#
# spec file for package python-pymetar
#
# Copyright (c) 2019 SUSE LINUX GmbH, Nuernberg, Germany.
# Copyright (c) 2012 Malcolm J Lewis <malcolmlewis@opensuse.org>
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


%define         modname pymetar
%define         oldpython python
%{?!python_module:%define python_module() python-%{**} python3-%{**}}
%define skip_python2 1
Name:           python-%{modname}
Version:        1.1
Release:        0
Summary:        METAR weather report parser
License:        GPL-2.0-or-later
Group:          Development/Languages/Python
URL:            https://www.schwarzvogel.de/software-pymetar.shtml
Source0:        http://www.schwarzvogel.de/pkgs/pymetar-%{version}.tar.gz
BuildRequires:  %{python_module setuptools}
BuildRequires:  fdupes
BuildRequires:  python-rpm-macros
Obsoletes:      %{oldpython}-%{modname}
BuildArch:      noarch
%python_subpackages

%description
This library downloads the weather report for a given station ID, decodes
it and provides easy access to all the data found in the report.

%prep
%setup -q -n %{modname}-%{version}

%build
%python_build

%install
%python_install
# we install docs on our own
rm -r %{buildroot}%{_datadir}/doc/
%python_expand %fdupes %{buildroot}%{$python_sitelib}

%check
cd testing/smoketest/
tar -xf reports.tgz
mkdir logs
./runtests.sh
cd -

%files %{python_files}
%doc README.md
%license COPYING
%python3_only %{_bindir}/%{modname}
%{python_sitelib}/*
%python3_only %{_mandir}/man1/%{modname}.1%{?ext_man}

%changelog
