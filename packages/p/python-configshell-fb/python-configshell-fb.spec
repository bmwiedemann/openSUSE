#
# spec file for package python-configshell-fb
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


%define modname configshell-fb
%{?!python_module:%define python_module() python-%{**} python3-%{**}}
Name:           python-%{modname}
Version:        1.1.25
Release:        0%{?dist}
Summary:        A Python library for building configuration shells
License:        Apache-2.0
Group:          Development/Libraries/Python
Url:            http://github.com/open-iscsi/configshell-fb
Source:         https://pypi.python.org/packages/source/c/%{modname}/%{modname}-%{version}.tar.gz
BuildRequires:  %{python_module pyparsing}
BuildRequires:  %{python_module setuptools}
BuildRequires:  %{python_module six}
BuildRequires:  fdupes
BuildRequires:  python-rpm-macros
Requires:       %{_bindir}/env
Requires:       python-pyparsing
Requires:       python-six
Requires:       python-urwid
Provides:       python-configshell = %{version}-%{release}
Obsoletes:      python-configshell < %{version}
BuildArch:      noarch
%python_subpackages

%description
configshell-fb is a Python library that provides a framework for building simple
but nice CLI-based applications.

configshell-fb is a fork of the "configshell" code written by RisingTide
Systems. The "-fb" differentiates between the original and this version. Please
ensure to use either all "fb" versions of the targetcli components -- targetcli,
rtslib, and configshell, or stick with all non-fb versions, since they are
no longer strictly compatible.

%package doc
Summary:        Documentation for Python configshell-fb
Group:          Documentation/HTML

%description doc
configshell-fb is a Python library that provides a framework for building simple
but nice CLI-based applications.

configshell-fb is a fork of the "configshell" code written by RisingTide
Systems. The "-fb" differentiates between the original and this version. Please
ensure to use either all "fb" versions of the targetcli components -- targetcli,
rtslib, and configshell, or stick with all non-fb versions, since they are
no longer strictly compatible.

%prep
%setup -q -n %{modname}-%{version}

%build
%python_build

%install
%python_install --skip-build
%fdupes %{buildroot}

%files %{python_files}
%{python_sitelib}/*
%doc README.md

%changelog
