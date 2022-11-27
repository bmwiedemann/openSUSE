#
# spec file for package backintime
#
# Copyright (c) 2022 SUSE LLC
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


Name:           backintime
Version:        1.3.2
Release:        0
Summary:        Backup tool for Linux inspired by the "flyback project"
License:        GPL-2.0-or-later
URL:            https://github.com/bit-team/backintime
Source0:        https://github.com/bit-team/backintime/releases/download/v%{version}/%{name}-%{version}.tar.gz
Source1:        https://github.com/bit-team/backintime/releases/download/v%{version}/%{name}-%{version}.tar.gz.asc
# Public key mentioned in https://github.com/bit-team/backintime#archlinux
Source2:        %{name}.keyring
Source3:        %{name}.png
# PATCH-FEATURE-OPENSUSE %%{name}-polkit_priv_downgrade.patch boo#1007723
Patch0:         %{name}-polkit_priv_downgrade.patch
# PATCH-FIX-UPSTREAM %%{name}-rsync324_args.patch rsync-3.2.4 on TW changes argument syntax; workaround until new release of backintime
Patch1:         %{name}-rsync324_args.patch
BuildRequires:  fdupes
BuildRequires:  hicolor-icon-theme
BuildRequires:  python3-devel
BuildRequires:  update-desktop-files
Requires:       cron
Requires:       dbus-1-python3
Requires:       openssh
%if 0%{?suse_version} > 1500
Requires:       pkexec
%endif
Requires:       python3
Requires:       python3-keyring
Requires:       rsync
Recommends:     encfs
Recommends:     sshfs
Requires:       libnotify-tools
Conflicts:      backintime-gnome
Conflicts:      backintime-kde
Obsoletes:      backintime-doc < %{version}
Provides:       backintime-doc = %{version}-%{release}
BuildArch:      noarch

%description
Back In Time is a backup tool for Linux inspired by the "flyback project".

It provides a command line client 'backintime' and a Qt5 GUI 'backintime-qt'
both written in Python3.

You only need to specify 3 things:
    * where to save snapshots;
    * what folders to backup; and
    * backup frequency (manual, every hour, every day, every month).

%package qt
Summary:        Back In Time Qt5 GUI
Requires:       %{name} = %{version}
Requires:       dbus-1-python3
Requires:       polkit
Requires:       python3-qt5
Obsoletes:      backintime-qt4

%description qt
This package has a Qt5 GUI for %{name}.

%lang_package

%prep
%setup -q
%patch0
# rsync-3.2.4 on TW changes argument syntax; workaround until new release of backintime
%if 0%{?suse_version} > 1500
%patch1
%endif

%build

# Fix documentation directories.
sed -i -e "s|'doc'|'doc/packages'|g" common/config.py
sed -i -e "s|'backintime-common'|'backintime'|g" common/config.py
sed -i -e "s|/share/doc/|/share/doc/packages/|g" common/configure qt/configure
sed -i -e "s|backintime-common|backintime|g" common/configure qt/configure

# Fix icon name.
sed -i 's/Icon=document-save/Icon=backintime/g' qt/backintime-qt.desktop qt/backintime-qt-root.desktop

# Fix shebangs
sed -i 's|/usr/bin/env python|#!/usr/bin/python|g' common/askpass.py

pushd common
./configure --python3
make %{?_smp_mflags}
popd
pushd  qt
./configure --python3
make %{?_smp_mflags}
popd

%install
pushd common
%make_install
popd
pushd qt
%make_install
popd

# Remove unmaintained documentation.
rm -r %{buildroot}%{_docdir}/qt

install -D -m 644 %{SOURCE3} %{buildroot}/%{_datadir}/pixmaps/%{name}.png

# Fix duplicated files.
%fdupes %{buildroot}%{_datadir}/icons/hicolor/

%suse_update_desktop_file %{name}-qt System Backup
%suse_update_desktop_file %{name}-qt-root System Backup

%find_lang %{name} --without-kde --without-gnome

%postun
rm -f %{_sysconfdir}/udev/rules.d/99-backintime-*.rules

%files
%defattr(-,root,root)
%{_bindir}/%{name}
%{_bindir}/%{name}-askpass
%{_datadir}/%{name}/
%{_datadir}/icons/hicolor/*/actions/show-hidden.svg
%{_datadir}/pixmaps/%{name}.png
%{_datadir}/bash-completion
%{_docdir}/%{name}/
%{_mandir}/man1/%{name}-askpass.1%{ext_man}
%{_mandir}/man1/%{name}-config.1%{ext_man}
%{_mandir}/man1/%{name}.1%{ext_man}
%{_sysconfdir}/xdg/autostart/backintime.desktop
%exclude %{_docdir}/%{name}-*/
%exclude %{_datadir}/%{name}/qt
%exclude %{_datadir}/%{name}/plugins

%files lang -f %{name}.lang

%files qt
%defattr(-,root,root)
%{_bindir}/%{name}-qt
%{_bindir}/%{name}-qt_polkit
%{_datadir}/applications/%{name}-qt.desktop
%{_datadir}/applications/%{name}-qt-root.desktop
%{_datadir}/%{name}/qt
%{_datadir}/%{name}/plugins
%dir %{_datadir}/dbus-1
%dir %{_datadir}/dbus-1/system-services
%{_datadir}/dbus-1/system-services/net.launchpad.backintime.serviceHelper.service
%dir %{_datadir}/polkit-1
%dir %{_datadir}/polkit-1/actions
%{_datadir}/polkit-1/actions/net.launchpad.backintime.policy
%{_docdir}/%{name}-qt/
%{_mandir}/man1/%{name}-qt.1%{ext_man}
%dir %{_sysconfdir}/dbus-1
%dir %{_sysconfdir}/dbus-1/system.d
%config %{_sysconfdir}/dbus-1/system.d/net.launchpad.backintime.serviceHelper.conf

%changelog
