#
# spec file for package ptokax
#
# Copyright (c) 2019 SUSE LINUX GmbH, Nuernberg, Germany.
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
Version:        0.5.2.2
Release:        0
Summary:        Server application for the Neo-Modus DC++ sharing network
License:        GPL-3.0-only
Group:          Productivity/Networking/File-Sharing
URL:            http://www.ptokax.org/
BuildRequires:  gcc-c++
BuildRequires:  lua-devel
BuildRequires:  systemd-rpm-macros
BuildRequires:  tinyxml-devel
BuildRequires:  zlib-devel
Source:         http://www.ptokax.org/files/%version-nix-src.tgz
Source1:        ptokax.service
Patch1:         logs.patch
Patch2:         nodate.diff
Patch3:         gcc7.diff
BuildRoot:      %{_tmppath}/%{name}-%{version}-build
%{?systemd_requires}
Requires(pre):  shadow

%description
PtokaX Direct Connect Hub is a server application for Neo-Modus
Direct Connect Peer-To-Peer sharing network.

PtokaX has a comprehensive user interface, tuned built-in features,
scripting-based extendability.

%prep
%setup -q -n PtokaX
%autopatch -p1
sed -i 's/\r//' ReadMe.txt Changelog.txt scripting.docs/scripting-interface.txt
# remove tinyxml as we use system lib
rm -rf tinyxml

%build
sed -i 's|CXXFLAGS = -O -g -Wall -Wextra|CXXFLAGS = %optflags|' makefile
perl -i -pe 's{-llua5.3}{-llua}g' makefile*
make %{?_smp_mflags}

%install
install -D -m 755 PtokaX %buildroot/%_sbindir/%name
mkdir -p %buildroot/%_sysconfdir/%name
mkdir -p %buildroot/var/log/%name
cp -a cfg.example %buildroot/%_sysconfdir/%name/cfg
cp -a language %buildroot/%_sysconfdir/%name

find scripting.docs -type d -exec chmod a+x {} +
find scripting.docs -type f -exec chmod a-x {} +
chmod 644 Changelog.txt ReadMe.txt License.txt
install -D -m 644 %SOURCE1 %buildroot/%_unitdir/%name.service
ln -s service %buildroot/%_sbindir/rcptokax

%pre
getent group ptokax >/dev/null || %_sbindir/groupadd -r ptokax
getent passwd ptokax >/dev/null || %_sbindir/useradd -g ptokax \
	-s /bin/false -r -c "user for ptokax" -d %_sysconfdir/ptokax ptokax
%service_add_pre %name.service

%post
%service_add_post %name.service

%preun
%service_del_preun %name.service

%postun
%service_del_postun %name.service

%files
%defattr(-,root,root)
%doc Changelog.txt ReadMe.txt License.txt scripting.docs
%_sbindir/%name
%_sbindir/rcptokax
%_unitdir/%name.service
%attr(-,ptokax,ptokax) %dir %_sysconfdir/%name
%attr(-,ptokax,ptokax) %dir %_sysconfdir/%name/cfg
%attr(-,ptokax,ptokax) %dir %_sysconfdir/%name/language
%config %attr(644,ptokax,ptokax) %_sysconfdir/%name/cfg/*
%config %attr(644,ptokax,ptokax) %_sysconfdir/%name/language/*
%attr(-,ptokax,ptokax) %dir /var/log/%name

%changelog
