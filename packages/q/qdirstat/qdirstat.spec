#
# spec file for package qdirstat
#
# Copyright (c) 2016-2019 SUSE LINUX GmbH, Nuernberg, Germany.
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


Name:           qdirstat
Version:        1.6
Release:        0
Summary:        Directory Statistics
License:        GPL-2.0-only
Group:          Productivity/File utilities
Url:            https://github.com/shundhammer/qdirstat
Source0:        %{name}-%{version}.tar.bz2
BuildRequires:  libQt5Core-devel
BuildRequires:  libQt5Widgets-devel
BuildRequires:  libqt5-qtbase-common-devel
BuildRequires:  zlib-devel
BuildRoot:      %{_tmppath}/%{name}-%{version}-build

%description
QDirStat is a graphical application to show where your disk space has gone and
to help you to clean it up.

This is a Qt-only port of the old Qt3/KDE3-based KDirStat, now based on the
latest Qt 5. It does not need any KDE libs or infrastructure. It runs on every
X11-based desktop on Linux, BSD and other Unix-like systems.

QDirStat has a number of new features compared to KDirStat. To name a few:

- Multi-selection in both the tree and the treemap.
- Unlimited number of user-defined cleanup actions.
- Properly show errors of cleanup actions (and their output, if desired).
- File categories (MIME types) and their treemap color are now configurable.
- Exclude rules for directories are easily configurable.
- Desktop-agnostic; no longer relies on KDE or any other specific desktop.

For more details and screenshots, see

    https://github.com/shundhammer/qdirstat

and the local documentation in

    /usr/share/doc/packages/qdirstat/README.md

%prep
%setup -q

%build
qmake-qt5
make

%install
make install INSTALL_ROOT=%{buildroot} %{?_smp_mflags}

# %suse_update_desktop_file -N "QDirStat" -G "Directory Statistics" %name Filesystem

%files
%defattr(-,root,root)
%{_bindir}/qdirstat
%{_bindir}/qdirstat-cache-writer
%{_datadir}/applications/qdirstat.desktop
%dir %{_datadir}/icons/hicolor
%dir %{_datadir}/icons/hicolor/scalable
%dir %{_datadir}/icons/hicolor/scalable/apps
%{_datadir}/icons/hicolor/scalable/apps/qdirstat.svg
%doc README.md LICENSE doc/cache-file-format.txt doc/*.md
%dir %{_docdir}/%{name}/stats
%{_docdir}/%{name}/stats/*.md
# %{_mandir}/man1/qdirstat.1.gz
# %{_mandir}/man1/qdirstat-cache-writer.1.gz

%changelog
