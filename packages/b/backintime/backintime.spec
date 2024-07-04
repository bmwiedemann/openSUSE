#
# spec file for package backintime
#
# Copyright (c) 2024 SUSE LLC
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


%if 0%{?suse_version} > 1500
%define pythons python3
%else
%{?sle15_python_module_pythons}
%endif

Name:           backintime
Version:        1.4.3
Release:        0
Summary:        Backup tool for Linux inspired by the "flyback project"
Group:          Productivity/Archiving/Backup
License:        GPL-2.0-or-later
URL:            https://github.com/bit-team/backintime
Source0:        https://github.com/bit-team/backintime/releases/download/v%{version}/%{name}-%{version}.tar.gz
# Public key mentioned in https://github.com/bit-team/backintime#archlinux
Source2:        %{name}.keyring
Source3:        %{name}.png
BuildRequires:  %{python_module devel >= 3.8}
# TEST REQUIREMENTS (only works on real hardware)
#BuildRequires:  %#{python_module packaging}
#BuildRequires:  %#{python_module dbus-python}
#BuildRequires:  %#{python_module keyring}
#BuildRequires:  %#{python_module pyfakefs}
#BuildRequires:  openssh
#BuildRequires:  rsync
#BuildRequires:  udev
# /TEST REQUIREMENTS
BuildConflicts: python3-devel < 3.8
BuildRequires:  fdupes
BuildRequires:  hicolor-icon-theme
BuildRequires:  python-rpm-macros
BuildRequires:  update-desktop-files
Requires:       %{python_flavor}-dbus-python
Requires:       %{python_flavor}-keyring
Requires:       %{python_flavor}-packaging
Requires:       cron
Requires:       openssh
Requires:       pkexec
Requires:       python3 >= 3.8
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
Requires:       %{python_flavor}-dbus-python
Requires:       %{python_flavor}-qt5
Requires:       libqt5-qttranslations
Requires:       polkit
# used as a fallback in case of missing icons
Recommends:     oxygen5-icon-theme
Obsoletes:      backintime-qt4 < %{version}
Provides:       backintime-qt4 = %{version}-%{release}

%description qt
This package has a Qt5 GUI for %{name}.

%lang_package

%prep
%setup -q

%build

# Fix documentation directories.
sed -i -e "s|'doc'|'doc/packages'|g" common/config.py
sed -i -e "s|'backintime-common'|'backintime'|g" common/config.py
sed -i -e "s|/share/doc/|/share/doc/packages/|g" common/configure qt/configure
sed -i -e "s|backintime-common|backintime|g" common/configure qt/configure

# Fix icon name.
sed -i 's/Icon=document-save/Icon=backintime/g' qt/backintime-qt.desktop qt/backintime-qt-root.desktop

# Fix shebangs
%python_expand sed -i "s|/usr/bin/env python|#!/usr/bin/$python|g" common/askpass.py

pushd common
%python_expand ./configure --python="%{_bindir}/$python"
make %{?_smp_mflags}
popd
pushd qt
%python_expand ./configure --python="%{_bindir}/$python"
make %{?_smp_mflags}
popd

%install
pushd common
%make_install
popd
pushd qt
%make_install
popd

install -D -m 644 %{SOURCE3} %{buildroot}/%{_datadir}/pixmaps/%{name}.png

# Fix duplicated files.
%fdupes %{buildroot}%{_datadir}/icons/hicolor/

%suse_update_desktop_file %{name}-qt System Backup
%suse_update_desktop_file %{name}-qt-root System Backup

%find_lang %{name} --without-kde --without-gnome

#%#check  # Only works on real hardware
#pushd common
#make test
#popd

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
%config %{_sysconfdir}/xdg/autostart/backintime.desktop
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
%dir %{_datadir}/dbus-1/system.d
%{_datadir}/dbus-1/system.d/net.launchpad.backintime.serviceHelper.conf

%changelog
