#
# spec file for package python-pydle
#
# Copyright (c) 2023 SUSE LLC
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
# pydle doesn't python 3.10 gh#Shizmob/pydle#162
# There's a WIP PR but looks like it's not good enough yet to be
# applied gh#Shizmob/pydle#180
%define skip_python310 1
%define skip_python311 1

%bcond_without test
Name:           python-pydle
Version:        1.0.1
Release:        0
Summary:        Modular, callback-based IRCv3 library for Python 3
License:        BSD-3-Clause
Group:          Development/Languages/Python
URL:            https://github.com/Shizmob/pydle
Source:         https://github.com/Shizmob/pydle/archive/v%{version}.tar.gz#/pydle-%{version}.tar.gz
BuildRequires:  %{python_module pip}
BuildRequires:  %{python_module poetry}
BuildRequires:  %{python_module pytest}
BuildRequires:  dos2unix
BuildRequires:  fdupes
BuildRequires:  python-rpm-macros
Requires:       python-pure-sasl
Requires(post): update-alternatives
Requires(postun):update-alternatives
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
%autosetup -p1 -n pydle-%{version}
dos2unix pydle/utils/irccat.py
sed -i 's,^#!%{_bindir}/env ,#!%{_bindir}/,' pydle/utils/irccat.py

%build
%pyproject_wheel

%install
%pyproject_install
%python_expand %fdupes %{buildroot}%{$python_sitelib}
%python_expand chmod +x %{buildroot}%{$python_sitelib}/pydle/utils/irccat.py
%python_clone -a %{buildroot}%{_bindir}/pydle
%python_clone -a %{buildroot}%{_bindir}/pydle-irccat

%post
%python_install_alternative pydle
%python_install_alternative pydle-irccat

%postun
%python_uninstall_alternative pydle
%python_uninstall_alternative pydle-irccat

%check
%pytest -m unit

%files %{python_files}
%license LICENSE.md
%{python_sitelib}/pydle
%{python_sitelib}/pydle-%{version}*-info
%python_alternative %{_bindir}/pydle
%python_alternative %{_bindir}/pydle-irccat

%changelog
