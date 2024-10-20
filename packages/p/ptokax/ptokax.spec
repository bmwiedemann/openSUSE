#
# spec file for package ptokax
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


Name:           ptokax
Version:        0.5.3
Release:        0
Summary:        Server application for the Neo-Modus DC++ sharing network
License:        GPL-3.0-only
Group:          Productivity/Networking/File-Sharing
URL:            http://www.ptokax.org/
BuildRequires:  gcc-c++
BuildRequires:  systemd-rpm-macros
BuildRequires:  sysuser-tools
BuildRequires:  tinyxml-devel
BuildRequires:  zlib-devel
BuildRequires:  pkgconfig(lua) >= 5.1
Source:         http://www.ptokax.org/files/0.5.3.0-nix-src.tgz
Source1:        ptokax.service
Patch1:         logs.patch
Patch2:         nodate.diff
%sysusers_requires

%description
PtokaX Direct Connect Hub is a server application for Neo-Modus
Direct Connect Peer-To-Peer sharing network.

PtokaX has a comprehensive user interface, tuned built-in features,
scripting-based extendability.

%prep
%autosetup -p1 -n PtokaX
sed -i 's/\r//' ReadMe.txt Changelog.txt scripting.docs/scripting-interface.txt
# remove tinyxml as we use system lib
rm -rf tinyxml

%build
perl -i -pe '
	s{^CXXFLAGS = .*}{CXXFLAGS = %optflags}g;
	s{-llua5.\d+\b}{'"$(pkg-config lua --libs)"'}g;
	s{-I/usr/include/lua5.\d+\b}{'"$(pkg-config lua --cflags)"'}g;
' makefile
%make_build

%install
b="%buildroot"
install -Dpm 755 PtokaX "$b/%_sbindir/%name"
mkdir -p "$b/%_sysconfdir/%name"
mkdir -p "$b/var/log/%name"
cp -a cfg.example "$b/%_sysconfdir/%name/cfg"
cp -a language "$b/%_sysconfdir/%name/"

find scripting.docs -type d -exec chmod a+x {} +
find scripting.docs -type f -exec chmod a-x {} +
chmod 644 Changelog.txt ReadMe.txt License.txt
install -Dpm 644 %SOURCE1 "$b/%_unitdir/%name.service"

mkdir -p "$b/%_sysusersdir"
echo 'u ptokax - "user for ptokax"' >system-user-ptokax.conf
cp -a system-user-ptokax.conf "$b/%_sysusersdir/"
%sysusers_generate_pre system-user-ptokax.conf random system-user-ptokax.conf

%pre -f random.pre
%service_add_pre %name.service

%post
%service_add_post %name.service

%preun
%service_del_preun %name.service

%postun
%service_del_postun %name.service

%files
%doc Changelog.txt ReadMe.txt scripting.docs
%license License.txt
%_sbindir/%name
%_unitdir/%name.service
%_sysusersdir/*
%attr(-,ptokax,ptokax) %dir %_sysconfdir/%name
%attr(-,ptokax,ptokax) %dir %_sysconfdir/%name/cfg
%attr(-,ptokax,ptokax) %dir %_sysconfdir/%name/language
%config(noreplace) %attr(644,ptokax,ptokax) %_sysconfdir/%name/cfg/*
%config %attr(644,ptokax,ptokax) %_sysconfdir/%name/language/*
%attr(-,ptokax,ptokax) %dir /var/log/%name

%changelog
