#
# spec file for package python-pydle
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


%define skip_python2 1
%{?!python_module:%define python_module() python-%{**} python3-%{**}}
%bcond_without test
Name:           python-pydle
Version:        0.9.2
Release:        0
Summary:        Modular, callback-based IRCv3 library for Python 3
License:        BSD-3-Clause
Group:          Development/Languages/Python
URL:            https://github.com/Shizmob/pydle
Source:         https://files.pythonhosted.org/packages/source/p/pydle/pydle-%{version}.tar.gz
Source1:        LICENSE.md
BuildRequires:  %{python_module setuptools}
BuildRequires:  dos2unix
BuildRequires:  fdupes
BuildRequires:  python-rpm-macros
Requires:       python-pure-sasl
BuildArch:      noarch
%python_subpackages

%description
Pydle is a modular, callback-based IRCv3 library for Python 3.
Features include:

* TLS
* CTCP
* ISUPPORT/PROTOCTL
* WHOX
* IRCv3.1 (full)
* IRCv3.2 (base only, work in progress)

%prep
%setup -q -n pydle-%{version}
dos2unix pydle/utils/irccat.py
sed -i 's,^#!%{_bindir}/env ,#!%{_bindir}/,' pydle/utils/irccat.py
cp %{SOURCE1} .

%build
%python_build

%install
%python_install
%python_expand %fdupes %{buildroot}%{$python_sitelib}
%python_expand chmod +x %{buildroot}%{$python_sitelib}/pydle/utils/irccat.py

%files %{python_files}
%license LICENSE.md
%{python_sitelib}/*
%{_bindir}/pydle
%{_bindir}/pydle-irccat

%changelog
