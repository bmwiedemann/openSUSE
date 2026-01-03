#
# spec file for package paracon

# Copyright (c) 2025 SUSE LLC and contributors
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

%define pythons python3
Name:           paracon
Version:        1.3.0
Release:        0
Summary:        Packet radio terminal using the AGWPE protocol
License:        MIT
URL:            https://paracon.readthedocs.io/en/latest/
Source0:        https://github.com/mfncooper/paracon/archive/refs/tags/v%{version}.tar.gz#/paracon-%{version}.tar.gz
Source1:        pyproject.toml
Patch0:         use-home-dotfiles.patch
BuildRequires:  %{python_module Sphinx}
BuildRequires:  %{python_module base >= 3.9}
BuildRequires:  %{python_module flit-core}
BuildRequires:  %{python_module pip}
BuildRequires:  %{python_module pyham_ax25}
BuildRequires:  %{python_module pyham_pe}
BuildRequires:  %{python_module pytest}
BuildRequires:  %{python_module wheel}
BuildRequires:  fdupes
BuildRequires:  python-rpm-macros
Requires:       python3
Requires:       python3-pyham_ax25
Requires:       python3-pyham_pe
Requires:       python3-urwid
BuildArch:      noarch

%description
Paracon is a packet radio terminal. It is focused on simplicity and ease of
use, and incorporates the core functionality that most packet users need
without trying to include all of the bells and whistles that few would use.

It talks to the TNC using AGWPE and works well with the direwolf software TNC.
If you have a classic KISS or 6PACK TNC you can use the classic Linux native
AX.25 stack with ldsped on top to be able to speak AGWPE.

%prep
%autosetup -n paracon-%{version} -p1
# convert src files to a module
cp %{SOURCE1} ./
mv paracon/paracon.py paracon/__init__.py
sed -i 's/^import config$/import paracon.config as config/' paracon/__init__.py
sed -i 's/^import pserver$/import paracon.pserver as pserver/' paracon/__init__.py
sed -i 's/^import urwidx$/import paracon.urwidx as urwidx/' paracon/__init__.py
sed -i "s|'paracon', 'paracon_config'|'%{_prefix}%{_sysconfdir}/paracon'|" paracon/__init__.py
mv paracon/paracon.def ./
cat >bin <<EOF
#!$(realpath /usr/bin/python3)

import paracon
paracon.run()
EOF


%build
%pyproject_wheel
ln -s __init__.py paracon/paracon.py
cd docs
%make_build man
gzip _build/man/paracon.1

%install
%pyproject_install
%python_expand %fdupes %{buildroot}%{$python_sitelib}/paracon
install -Dm644 -v docs/_build/man/paracon.1.gz %{buildroot}%{_mandir}/man1/%{name}.1
install -Dm644 -v paracon.def %{buildroot}%{_prefix}%{_sysconfdir}/paracon.def
install -Dm755 -v bin %{buildroot}%{_bindir}/paracon

%files
%license LICENSE
%doc README.md
%{_mandir}/man1/paracon.1%{?ext_man}
%{python_sitelib}/paracon*
%{_prefix}%{_sysconfdir}/paracon.def
%{_bindir}/paracon

%changelog
