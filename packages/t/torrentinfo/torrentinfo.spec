#
# spec file for package torrentinfo
#
# Copyright (c) 2017 SUSE LINUX GmbH, Nuernberg, Germany.
# Copyright (c) 2009 Pascal Bleser <guru@unixtech.be>
#
# All modifications and additions to the file contributed by third parties
# remain the property of their copyright owners, unless otherwise agreed
# upon. The license for this file, and modifications and additions to the
# file, is the same license as for the pristine package itself (unless the
# license for the pristine package is not an Open Source License, in which
# case the license is the MIT License). An "Open Source License" is a
# license that conforms to the Open Source Definition (Version 1.9)
# published by the Open Source Initiative.

# Please submit bugfixes or comments via http://bugs.opensuse.org/
#


Name:           torrentinfo
Version:        1.8.6
Release:        0
Summary:        Displays information contained in .torrent Files
License:        GPL-2.0
Group:          Productivity/Networking/Other
# formerly at http://vrai.net/project.php?project=torrentinfo
URL:            http://fuuzetsu.co.uk/torrentinfo
Source0:        https://github.com/Fuuzetsu/torrentinfo/archive/v%{version}.tar.gz#/%{name}-%{version}.tar.gz
Source1:        %{name}.changes
# PATCH-FIX-UPSTREAM torrentinfo-fix_man.patch -- removes deprecated dependency
Patch0:         torrentinfo-fix_man.patch
# PATCH-FIX-UPSTREAM torrentinfo-fix_tests_py3.patch
Patch1:         torrentinfo-fix_tests_py3.patch
BuildRequires:  python3
BuildRequires:  python3-devel
BuildRequires:  python3-nose
BuildRequires:  python3-Sphinx
BuildArch:      noarch

%description
TorrentInfo is a command line script that parses .torrent files and displays
the information contained within them. Currently, it can display a summary
of the whole torrent, information on each file within the torrent, and a
full hierarchical dump of the torrent file's contents.

%prep
%setup -q
%patch0 -p1
%patch1 -p1
FAKE_BUILDDATE=$(LC_ALL=C date -u -r %{SOURCE1} '+%%Y-%%m-%%d')
sed -e "s/__DATE__/$FAKE_BUILDDATE/" -i doc/conf.py

%build
python3 setup.py build
make -C doc man

%install
python3 setup.py install --prefix="%{_prefix}" --root=%{buildroot}
install -Dm0644 doc/_build/man/%{name}.1 %{buildroot}%{_mandir}/man1/%{name}.1

%check
nosetests test/tests.py

%files
%doc README.md
%license LICENSE
%{_bindir}/%{name}
%{_mandir}/man1/%{name}.1%{ext_man}
%{python3_sitelib}/*

%changelog
