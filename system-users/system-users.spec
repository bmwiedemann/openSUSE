#
# spec file for package system-users
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


Name:           system-users
Version:        20170617
Release:        0
Summary:        Provide system accounts
License:        MIT
Group:          System/Fhs
Source1:        system-user-uucp.conf
Source2:        system-user-games.conf
Source3:        system-user-bin.conf
Source4:        system-user-daemon.conf
Source5:        system-user-man.conf
Source6:        system-user-news.conf
Source8:        system-group-obsolete.conf
Source9:        system-group-hardware.conf
Source10:       system-group-wheel.conf
Source11:       system-user-wwwrun.conf
Source12:       system-user-mail.conf
Source13:       system-user-ftp.conf
Source14:       system-user-lp.conf
Source15:       system-user-nobody.conf
Source16:       system-user-upsd.conf
Source17:       system-user-uuidd.conf
Source19:       system-user-tftp.conf
BuildRequires:  sysuser-shadow
BuildRequires:  sysuser-tools
BuildArch:      noarch

%description
This package provides various system users and their directories

%package -n system-user-bin
Summary:        System user and group 'bin'
#!BuildIgnore:  user(daemon)
Group:          System/Fhs
Requires(pre):  user(daemon)
%{sysusers_requires}

%description -n system-user-bin
This package provides the system account and group 'bin'
and their corresponding directories.

%package -n system-user-daemon
Summary:        System user and group 'daemon'
Group:          System/Fhs
%{sysusers_requires}

%description -n system-user-daemon
This package provides the system account and group 'daemon'
and their corresponding directories.

%package -n system-user-man
Summary:        System user and group 'man'
Group:          System/Fhs
%{sysusers_requires}

%description -n system-user-man
This package provides the system account and group 'man'
and their corresponding directories.

%package -n system-user-news
Summary:        System user and group 'news'
Group:          System/Fhs
%{sysusers_requires}

%description -n system-user-news
This package provides the system account and group 'news'
and their corresponding directories.

%package -n system-user-uucp
Summary:        System user and group uucp
#!BuildIgnore:  group(lock)
Group:          System/Fhs
Requires(pre):  group(lock)
%{sysusers_requires}

%description -n system-user-uucp
This package provides the system account and group 'uucp'
and their corresponding directories.

%package -n system-user-games
Summary:        System user and group games
Group:          System/Fhs
%{sysusers_requires}

%description -n system-user-games
This package provides the system account and group 'games'.

%package -n system-group-obsolete
Summary:        Obsolete system groups
Group:          System/Fhs
%{sysusers_requires}

%description -n system-group-obsolete
This package provides some obsolete system groups.

%package -n system-group-hardware
Summary:        Hardware related system groups
Group:          System/Fhs
%{sysusers_requires}

%description -n system-group-hardware
This package provides some hardware related system groups
required by udev.

%package -n system-group-wheel
Summary:        System group 'wheel'
Group:          System/Fhs
%{sysusers_requires}

%description -n system-group-wheel
This package provides the system group 'wheel'.

%package -n system-user-wwwrun
Summary:        System user wwwrun and group www
Group:          System/Fhs
%{sysusers_requires}

%description -n system-user-wwwrun
This package provides the system account 'wwwrun' and group 'www'.

%package -n system-user-mail
Summary:        System user and group mail
Group:          System/Fhs
%{sysusers_requires}

%description -n system-user-mail
This package provides the system account and group 'mail'.

%package -n system-user-ftp
Summary:        System user and group ftp
Group:          System/Fhs
%{sysusers_requires}

%description -n system-user-ftp
This package provides the system account and group 'ftp'.

%package -n system-user-lp
Summary:        System user lp
Group:          System/Fhs
Requires(pre):  group(lp)
#!BuildIgnore:  group(lp)
%{sysusers_requires}

%description -n system-user-lp
This package provides the system account and group 'lp'.

%package -n system-user-nobody
Summary:        System user and group nobody
Group:          System/Fhs
Requires(pre):  /usr/sbin/usermod
%{sysusers_requires}

%description -n system-user-nobody
This package provides the system account and group 'nobody'.

%package -n system-user-upsd
Summary:        System user upsd
#!BuildIgnore:  group(daemon)
Group:          System/Fhs
Requires(pre):  group(daemon)
%{sysusers_requires}

%description -n system-user-upsd
This package provides the system account 'upsd'.

%package -n system-user-uuidd
Summary:        System user and group uuidd
Group:          System/Fhs
%{sysusers_requires}

%description -n system-user-uuidd
This package provides the system account and group 'uuidd'.

%package -n system-user-tftp
Summary:        System user and group tftp
Group:          System/Fhs
%{sysusers_requires}

%description -n system-user-tftp
This package provides the system account and group 'tftp'.

%prep
%setup -q -c -T

%build
%sysusers_generate_pre %{SOURCE1} uucp
%sysusers_generate_pre %{SOURCE2} games
%sysusers_generate_pre %{SOURCE3} bin
%sysusers_generate_pre %{SOURCE4} daemon
%sysusers_generate_pre %{SOURCE5} man
%sysusers_generate_pre %{SOURCE6} news
%sysusers_generate_pre %{SOURCE8} obsolete
%sysusers_generate_pre %{SOURCE9} hardware
%sysusers_generate_pre %{SOURCE10} wheel
%sysusers_generate_pre %{SOURCE11} wwwrun
%sysusers_generate_pre %{SOURCE12} mail
%sysusers_generate_pre %{SOURCE13} ftp
%sysusers_generate_pre %{SOURCE14} lp
%sysusers_generate_pre %{SOURCE15} nobody
%sysusers_generate_pre %{SOURCE16} upsd
%sysusers_generate_pre %{SOURCE17} uuidd
%sysusers_generate_pre %{SOURCE19} tftp

%install
mkdir -p %{buildroot}%{_sysusersdir}
mkdir -p %{buildroot}%{_sysconfdir}/uucp
mkdir -p %{buildroot}%{_sysconfdir}/news
mkdir -p %{buildroot}%{_localstatedir}/games
mkdir -p %{buildroot}%{_localstatedir}/lib/wwwrun
mkdir -p %{buildroot}%{_localstatedir}/spool/clientmqueue
mkdir -p %{buildroot}%{_localstatedir}/spool/lpd
mkdir -p %{buildroot}%{_localstatedir}/run/uuidd
mkdir -p %{buildroot}/srv/ftp
mkdir -p %{buildroot}%{_localstatedir}/lib/nobody
mkdir -p %{buildroot}/srv/tftpboot
install -m 644 %{SOURCE1} %{buildroot}%{_sysusersdir}/system-user-uucp.conf
install -m 644 %{SOURCE2} %{buildroot}%{_sysusersdir}/system-user-games.conf
install -m 644 %{SOURCE3} %{buildroot}%{_sysusersdir}/system-user-bin.conf
install -m 644 %{SOURCE4} %{buildroot}%{_sysusersdir}/system-user-daemon.conf
install -m 644 %{SOURCE5} %{buildroot}%{_sysusersdir}/system-user-man.conf
install -m 644 %{SOURCE6} %{buildroot}%{_sysusersdir}/system-user-news.conf
install -m 644 %{SOURCE8} %{buildroot}%{_sysusersdir}/system-group-obsolete.conf
install -m 644 %{SOURCE9} %{buildroot}%{_sysusersdir}/system-group-hardware.conf
install -m 644 %{SOURCE10} %{buildroot}%{_sysusersdir}/system-group-wheel.conf
install -m 644 %{SOURCE11} %{buildroot}%{_sysusersdir}/system-user-wwwrun.conf
install -m 644 %{SOURCE12} %{buildroot}%{_sysusersdir}/system-user-mail.conf
install -m 644 %{SOURCE13} %{buildroot}%{_sysusersdir}/system-user-ftp.conf
install -m 644 %{SOURCE14} %{buildroot}%{_sysusersdir}/system-user-lp.conf
install -m 644 %{SOURCE15} %{buildroot}%{_sysusersdir}/system-user-nobody.conf
install -m 644 %{SOURCE16} %{buildroot}%{_sysusersdir}/system-user-upsd.conf
install -m 644 %{SOURCE17} %{buildroot}%{_sysusersdir}/system-user-uuidd.conf
install -m 644 %{SOURCE19} %{buildroot}%{_sysusersdir}/system-user-tftp.conf

%pre -n system-user-uucp -f uucp.pre
%pre -n system-user-games -f games.pre
%pre -n system-user-bin -f bin.pre
%pre -n system-user-daemon -f daemon.pre
%pre -n system-user-man -f man.pre
%pre -n system-user-news -f news.pre
%pre -n system-group-obsolete -f obsolete.pre
%pre -n system-group-hardware -f hardware.pre
%pre -n system-group-wheel -f wheel.pre
%pre -n system-user-wwwrun -f wwwrun.pre
%pre -n system-user-mail -f mail.pre
%pre -n system-user-ftp -f ftp.pre
%pre -n system-user-lp -f lp.pre
%pre -n system-user-nobody -f nobody.pre
%post -n system-user-nobody
/usr/sbin/usermod -s /bin/bash nobody

%pre -n system-user-upsd -f upsd.pre
%pre -n system-user-uuidd -f uuidd.pre
%pre -n system-user-tftp -f tftp.pre

%files -n system-user-uucp
%defattr(-,root,root)
%dir %attr(0750,uucp,uucp) %{_sysconfdir}/uucp
%{_sysusersdir}/system-user-uucp.conf

%files -n system-user-games
%defattr(-,root,root)
%dir %attr(0755,root,root) %{_localstatedir}/games
%{_sysusersdir}/system-user-games.conf

%files -n system-user-bin
%defattr(-,root,root)
%{_sysusersdir}/system-user-bin.conf

%files -n system-user-daemon
%defattr(-,root,root)
%{_sysusersdir}/system-user-daemon.conf

%files -n system-user-man
%defattr(-,root,root)
%{_sysusersdir}/system-user-man.conf

%files -n system-user-news
%defattr(-,root,root)
%dir %attr(0750,news,news) %{_sysconfdir}/news
%{_sysusersdir}/system-user-news.conf

%files -n system-group-obsolete
%defattr(-,root,root)
%{_sysusersdir}/system-group-obsolete.conf

%files -n system-group-hardware
%defattr(-,root,root)
%{_sysusersdir}/system-group-hardware.conf

%files -n system-group-wheel
%defattr(-,root,root)
%{_sysusersdir}/system-group-wheel.conf

%files -n system-user-wwwrun
%defattr(-,root,root)
%dir %attr(0755,wwwrun,root) %{_localstatedir}/lib/wwwrun
%{_sysusersdir}/system-user-wwwrun.conf

%files -n system-user-mail
%defattr(-,root,root)
%dir %attr(0770,mail,mail) %{_localstatedir}/spool/clientmqueue
%{_sysusersdir}/system-user-mail.conf

%files -n system-user-ftp
%defattr(-,root,root)
%dir %attr(0755,root,root) /srv/ftp
%{_sysusersdir}/system-user-ftp.conf

%files -n system-user-lp
%defattr(-,root,root)
%dir %attr(0755,lp,lp) %{_localstatedir}/spool/lpd
%{_sysusersdir}/system-user-lp.conf

%files -n system-user-nobody
%defattr(-,root,root)
%dir %attr(0755,nobody,root) %{_localstatedir}/lib/nobody
%{_sysusersdir}/system-user-nobody.conf

%files -n system-user-upsd
%defattr(-,root,root)
%{_sysusersdir}/system-user-upsd.conf

%files -n system-user-uuidd
%defattr(-,root,root)
%{_sysusersdir}/system-user-uuidd.conf

%files -n system-user-tftp
%defattr(-,root,root)
%dir %attr(0755,tftp,tftp) /srv/tftpboot
%{_sysusersdir}/system-user-tftp.conf

%changelog
