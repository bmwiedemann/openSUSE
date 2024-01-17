#
# spec file for package RemoteBox
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


# We need to filter some dependencies that the RPM auto-dependency
# gatherer picks up as they reside within this RPM.
%global __requires_exclude ^perl\\(.*\\.pl\\)|^perl\\(vboxService\\)
# We don't want to be a provider of vboxService as it's private
# to remotebox so filter it
%global __provides_exclude ^perl\\(vboxService\\)
Name:           RemoteBox
Version:        3.2
Release:        0
Summary:        A VirtualBox client with remote management
License:        GPL-2.0-or-later
Group:          System/Emulators/PC
URL:            http://knobgoblin.org.uk
Source0:        http://knobgoblin.org.uk/downloads/%{name}-%{version}.tar.bz2
Source1:        http://knobgoblin.org.uk/docs/remotebox.pdf
Patch0:         RemoteBox-3.0_fix-env-script-interpreter.patch
BuildRequires:  desktop-file-utils
BuildRequires:  fdupes
Requires:       freerdp
Requires:       perl-Gtk3
Requires:       perl-SOAP-Lite
Requires:       typelib-1_0-GdkPixdata-2_0
Requires:       xdg-utils
BuildArch:      noarch

%description
VirtualBox is traditionally considered to be a virtualization solution aimed
at the desktop as opposed to other solutions such as KVM, Xen and VMWare ESX
which are considered more server orientated solutions. While it is certainly
possible to install VirtualBox on a server, it offers few remote management
features beyond using the vboxmanage command line. RemoteBox aims to fill
this gap by providing a graphical VirtualBox client which is able to
communicate with and manage a VirtualBox server installation.

%prep
%setup -q
%patch0
install -m 0644 %{SOURCE1} .
# Set the locations of Remotebox's files
sed -i 's|\$Bin/share/remotebox|%{_datadir}/%{name}|g' remotebox
sed -i 's|\$Bin/docs|%{_docdir}/%{name}|g' remotebox
# We need to update the reference to the .desktop file, as this package provides RemoteBox, instead of remotebox
sed -i 's|remotebox.desktop|RemoteBox.desktop|' packagers-readme/remotebox.appdata.xml

%build
# Create a desktop file
cat >%{name}.desktop <<EOF
[Desktop Entry]
Type=Application
Name=RemoteBox
GenericName=RemoteBox
Comment=Remote VirtualBox client
Exec=%{name} %c
Icon=%{name}
Terminal=false
StartupNotify=false
Categories=Emulator;System;
X-SuSE-translate=false
EOF

%install
mkdir -p -m0755 %{buildroot}%{_datadir}/{%{name},pixmaps,applications,appdata}
mkdir -m0755 %{buildroot}%{_bindir}
install -p -m0755 remotebox %{buildroot}%{_bindir}/%{name}
cp -a share/remotebox/* %{buildroot}%{_datadir}/%{name}

# Install the .desktop file
desktop-file-install --dir=%{buildroot}%{_datadir}/applications %{name}.desktop

# Install an icon for the desktop file
install -p -m0644 share/remotebox/icons/remotebox.png %{buildroot}%{_datadir}/pixmaps/%{name}.png
# link the icon back to the install directory. In preparation for app containerisation, as well
# as AppStream metadata generation, we need a real file in /usr/share/icons
# fdupes later on is likely to put the symlink there though
ln -sf %{_datadir}/pixmaps/%{name}.png %{buildroot}%{_datadir}/%{name}/icons/remotebox.png

# Install upstream provided appdata.xml
install -p -m0644 packagers-readme/remotebox.appdata.xml %{buildroot}%{_datadir}/appdata/RemoteBox.appdata.xml

%fdupes -s %{buildroot}

%check
desktop-file-validate %{buildroot}/%{_datadir}/applications/%{name}.desktop

%files
%license docs/COPYING
%doc docs/changelog.txt  remotebox.pdf
%dir %{_datadir}/appdata
%{_datadir}/appdata/%{name}.appdata.xml
%{_datadir}/applications/%{name}.desktop
%{_datadir}/pixmaps/%{name}.png
%{_datadir}/%{name}
%{_bindir}/%{name}

%changelog
