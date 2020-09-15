#
# spec file for package multitail
#
# Copyright (c) 2018 SUSE LINUX GmbH, Nuernberg, Germany.
# Copyright (c) 2010-2012 Pascal Bleser <pascal.bleser@opensuse.org>
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


Name:           multitail
Version:        6.5.0
Release:        0
Summary:        Tail Multiple Files
License:        GPL-2.0+
Group:          System/X11/Terminals
Url:            https://www.vanheusden.com/multitail/
Source:         https://www.vanheusden.com/multitail/%{name}-%{version}.tgz
Patch3:         multitail-fix_missing_proto_do_check_for_mail.patch
BuildRequires:  ncurses-devel
BuildRequires:  pkgconfig

%description
MultiTail lets you view one or multiple files like the original
tail program.

The difference is that it creates multiple windows on your console
(with ncurses). Merging of 2 or even more logfiles is possible.

It can also use colors while displaying the logfiles (through
regular expressions), for faster recognition of what is important
and what not. It can also filter lines (again with regular
expressions). It has interactive menus for editing given regular
expressions and deleting and adding windows. One can also have
windows with the output of shell scripts and other software. When
viewing the output of external software, MultiTail can mimic the
functionality of tools like 'watch' and such.

%prep
%setup -q
%patch3

sed -i 's/\.new//g' Makefile
sed -i 's|%{_sysconfdir}/%{name}|%{_datadir}/%{name}|g' "%{name}.conf"

%build
export CFLAGS="%{optflags} -I%{_includedir}/ncurses"
#as there is no .pc for ncurses in some older releases, specify manually
export LDFLAGS="-lpanelw -lncursesw "
make %{?_smp_mflags} \
    PKG_CONFIG="pkg-config" \
    UTF8_SUPPORT=yes \
    PREFIX=%_prefix \
    CONFIG_FILE="%{_sysconfdir}/%{name}.conf"

%install
%make_install PREFIX=%_prefix
mv %{buildroot}/%_prefix/%_sysconfdir %{buildroot}/%_sysconfdir

# docs are shipped already
rm -fr %{buildroot}%{_datadir}/doc/%{name}-%{version}

%files
%doc *.txt manual*.html
%config(noreplace) %{_sysconfdir}/%{name}.conf
%{_bindir}/%{name}
%{_mandir}/man1/%{name}.1%{ext_man}
%dir %{_sysconfdir}/%{name}
%{_sysconfdir}/%{name}/colors-example.pl
%{_sysconfdir}/%{name}/colors-example.sh
%{_sysconfdir}/%{name}/convert-geoip.pl
%{_sysconfdir}/%{name}/convert-simple.pl

%changelog
