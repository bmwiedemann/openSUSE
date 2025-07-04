#
# spec file for package torrentinfo
#
# Copyright (c) 2025 SUSE LLC
# Copyright (c) 2009 Pascal Bleser <guru@unixtech.be>
# Copyright (c) 2024 Andreas Stieger <Andreas.Stieger@gmx.de>
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
Name:           torrentinfo
Version:        1.8.7
Release:        0
Summary:        Displays information contained in .torrent Files
License:        GPL-2.0-only
Group:          Productivity/Networking/Other
URL:            https://github.com/Fuuzetsu/torrentinfo
Source0:        https://github.com/Fuuzetsu/torrentinfo/archive/v%{version}.tar.gz#/%{name}-%{version}.tar.gz
Source1:        %{name}.changes
# PATCH-FIX-UPSTREAM torrentinfo-fix_man.patch -- removes deprecated dependency
Patch0:         torrentinfo-fix_man.patch
# PATCH-FIX-UPSTREAM torrentinfo-fix_tests_py3.patch
Patch1:         torrentinfo-fix_tests_py3.patch
BuildRequires:  %{python_module Sphinx}
BuildRequires:  %{python_module devel}
BuildRequires:  %{python_module pip}
BuildRequires:  %{python_module pytest}
BuildRequires:  %{python_module setuptools}
BuildRequires:  %{python_module wheel}
BuildRequires:  python-rpm-macros
BuildArch:      noarch

%description
TorrentInfo is a command line script that parses .torrent files and displays
the information contained within them. Currently, it can display a summary
of the whole torrent, information on each file within the torrent, and a
full hierarchical dump of the torrent file's contents.

%prep
%autosetup -p1

%build
%pyproject_wheel
make -C doc man

%install
%pyproject_install
install -Dm0644 doc/_build/man/%{name}.1 %{buildroot}%{_mandir}/man1/%{name}.1

%check
# https://github.com/Fuuzetsu/torrentinfo/issues/17
sed -i '/import nose/d' test/tests.py
PYTHONPATH=src:%{buildroot}%{python3_sitelib} PYTHONDONTWRITEBYTECODE=1 \
 pytest -v test/tests.py

%files
%doc README.md
%license LICENSE
%{_bindir}/%{name}
%{_mandir}/man1/%{name}.1%{ext_man}
%{python3_sitelib}/torrentinfo-%{version}.dist-info
%if 0%{?suse_version} && 0%{?suse_version} >= 1600
%{python3_sitelib}/torrentinfo.py
%pycache_only %{python3_sitelib}/__pycache__/torrentinfo.*
%endif

%changelog
