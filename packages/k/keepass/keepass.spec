#
# spec file for package keepass
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


%define _name KeePass
Name:           keepass
Version:        2.57
Release:        0
Summary:        Password Manager
License:        GPL-2.0-or-later
Group:          Productivity/Other
URL:            https://keepass.info/
Source0:        https://netcologne.dl.sourceforge.net/project/keepass/KeePass%202.x/%{version}/KeePass-%{version}-Source.zip
Source1:        https://keepass.info/integrity/v2/KeePass-%{version}-Source.zip.asc
# http://keepass.info/integrity/Dominik_Reichl.asc
Source2:        keepass.keyring
BuildRequires:  dos2unix
BuildRequires:  mono-devel
BuildRequires:  unzip
BuildRequires:  xdotool-devel
BuildRequires:  xorg-x11-fonts-core
BuildRequires:  xsel
Recommends:     libargon2-1
Recommends:     libgcrypt20
Recommends:     xdotool
BuildArch:      noarch

%description
KeePass is a password manager, which helps you to manage your
passwords. You can put all your passwords in one database, which is
locked with one master key or a key file, so that you only have to
remember one single master password or select the key file to unlock
the whole database. The databases are encrypted using AES and
Twofish.

%prep
%setup -q -c %{name}-%{version}
dos2unix Docs/License.txt Docs/History.txt

sed -i '1s/ 10.00/ 11.00/' KeePass.sln
find . -name "*.csproj" -exec sed -i '1s/"3.5"/"4.0"/' {} +

pushd Build &>/dev/null
bash PrepMonoDev.sh
sh PrepMonoDev.sh
popd &>/dev/null

%build
xbuild /target:KeePass /property:Configuration=Release

%install
install -d %{buildroot}%{_prefix}/lib/%{name}
install -d %{buildroot}%{_prefix}/lib/%{name}/XSL
install -m 644 Build/%{_name}Lib_Distrib/%{_name}Lib.dll %{buildroot}%{_prefix}/lib/%{name}/
install -m 644 Build/%{_name}/Release/%{_name}.exe* %{buildroot}%{_prefix}/lib/%{name}/
install -m 644 Ext/%{_name}.config.xml %{buildroot}%{_prefix}/lib/%{name}/
install -m 644 Ext/%{_name}.exe.config %{buildroot}%{_prefix}/lib/%{name}/
install -m 644 Ext/XSL/* %{buildroot}%{_prefix}/lib/%{name}/XSL

# Bin wrapper
install -d %{buildroot}%{_bindir}
cat << EOF > %{buildroot}%{_bindir}/%{name}
#!/bin/sh
exec mono %{_prefix}/lib/%{name}/%{_name}.exe "\$@"
EOF

# Desktop file
install -d %{buildroot}%{_datadir}/applications
cat << EOF > %{buildroot}%{_datadir}/applications/%{name}.desktop
[Desktop Entry]
Type=Application
Name=%{_name}
GenericName=Password Manager
Comment=Secure Password Management System
Icon=keepass
TryExec=%{_bindir}/keepass
Exec=keepass
Terminal=false
Categories=Utility;Security;
X-SuSE-translate=false
EOF

# Icon
install -d %{buildroot}%{_datadir}/pixmaps
install -m 644 Ext/Icons_04_CB/Finals/plock-blu.png %{buildroot}%{_datadir}/pixmaps/%{name}.png

%files
%license Docs/License.txt
%doc Docs/History.txt
%attr(755,root,root) %{_bindir}/%{name}
%{_datadir}/applications/%{name}.desktop
%{_datadir}/pixmaps/%{name}.png
%{_prefix}/lib/keepass

%changelog
