#
# spec file for package distcc
#
# Copyright (c) 2020 SUSE LLC
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


#Compat macro for new _fillupdir macro introduced in Nov 2017
%if ! %{defined _fillupdir}
  %define _fillupdir %{_localstatedir}/adm/fillup-templates
%endif
Name:           distcc
Version:        3.3.3
Release:        0
Summary:        A distributed C/C++ compiler
License:        GPL-2.0-or-later
Group:          Development/Tools/Building
URL:            https://github.com/distcc/distcc
Source0:        https://github.com/distcc/distcc/archive/v%{version}.tar.gz#/%{name}-%{version}.tar.gz
Source1:        distccd.sysconfig
Source2:        distccd.service
Patch1:         distcc-3.2_rc1-freedesktop.patch
Patch2:         distcc-3.2_rc1-gssapi.patch
Patch3:         distcc-3.2_rc1-python.patch
Patch4:         gcc-10-no-common.patch
BuildRequires:  autoconf
BuildRequires:  automake
BuildRequires:  binutils-devel
BuildRequires:  fdupes
BuildRequires:  gcc
BuildRequires:  libtool
BuildRequires:  make
BuildRequires:  pkgconfig
BuildRequires:  python
BuildRequires:  update-desktop-files
BuildRequires:  pkgconfig(avahi-client)
BuildRequires:  pkgconfig(gtk+-2.0)
BuildRequires:  pkgconfig(libgssglue)
BuildRequires:  pkgconfig(pango)
BuildRequires:  pkgconfig(python3)
BuildRequires:  pkgconfig(systemd)
Recommends:     %{name}-server = %{version}
Suggests:       %{name}-gui = %{version}

%description
distcc is a program to distribute builds of C, C++, Objective C or
Objective C++ code across several machines on a network, thereby
completing the task in less time. distcc should always generate the
same results as a local build.

%package gui
Summary:        GUI monitor for distcc server/client
Group:          Development/Tools/Building

%description gui
distcc is a program to distribute builds of C, C++, Objective C or
Objective C++ code across several machines on a network, thereby
completing the task in less time. distcc should always generate the
same results as a local build.

%package server
Summary:        Server for distributed C/C++ compilation
Group:          Development/Tools/Building
Requires:       %{name} = %{version}
%{?systemd_requires}

%description server
This package contains the compilation server needed to use %{name}.

%prep
%autosetup -p1

# do not use date/time in the c files
modified="$(sed -n '/^----/n;s/ - .*$//;p;q' "%{_sourcedir}/%{name}.changes")"
DATE="\"$(date -d "${modified}" "+%%b %%e %%Y")\""
TIME="\"$(date -d "${modified}" "+%%R")\""
sed -i \
    -e "s/__DATE__/${DATE}/g;s/__TIME__/${TIME}/g" \
    src/daemon.c src/help.c lzo/minilzo.c

autoreconf -fvi

%build
export CFLAGS="%{optflags} -fno-strict-aliasing"
export CXXFLAGS="%{optflags} -fno-strict-aliasing"
%configure \
    --disable-Werror \
    --enable-rfc2553 \
    --with-gtk \
    --with-avahi \
    --with-auth
# For some reason CC is not propagated to makefile and we get empty string
sed -i \
    -e 's:CC = :CC = cc:' \
    Makefile
make %{?_smp_mflags}

%install
%make_install docdir=%{_docdir}/%{name}
# service
mkdir -p %{buildroot}/%{_sbindir}
ln -sf service %{buildroot}/%{_sbindir}/rc%{name}d
install -D -m 0644 %{SOURCE2} %{buildroot}/%{_unitdir}/%{name}d.service
# sysconfig
install -Dm 644 %{SOURCE1} %{buildroot}%{_fillupdir}/sysconfig.%{name}d
# compat links for env override
install -d %{buildroot}%{_libexecdir}/%{name}/bin
ln -sf %{_bindir}/%{name} %{buildroot}%{_libexecdir}/%{name}/bin/cc
ln -sf %{_bindir}/%{name} %{buildroot}%{_libexecdir}/%{name}/bin/gcc
ln -sf %{_bindir}/%{name} %{buildroot}%{_libexecdir}/%{name}/bin/g++
ln -sf %{_bindir}/%{name} %{buildroot}%{_libexecdir}/%{name}/bin/c++
ln -sf %{_bindir}/%{name} %{buildroot}%{_libexecdir}/%{name}/bin/cpp
ln -sf %{_bindir}/%{name} %{buildroot}%{_libexecdir}/%{name}/bin/clang
ln -sf %{_bindir}/%{name} %{buildroot}%{_libexecdir}/%{name}/bin/clang++

# pointless files
rm -rf %{buildroot}%{_docdir}/%{name}/{INSTALL,COPYING}
# cleanups
%suse_update_desktop_file -r distccmon-gnome Development Building
%fdupes ${buildroot}

%pre server
%service_add_pre distccd.service

%post server
%fillup_only -n distccd
%service_add_post distccd.service

%preun server
%service_del_preun distccd.service

%postun server
%service_del_postun distccd.service

%files
%license COPYING
%doc AUTHORS doc/* NEWS README.pump TODO README survey.txt
%dir %{_libexecdir}/distcc
%dir %{_libexecdir}/distcc/bin
%dir %{_docdir}/distcc
%{_libexecdir}/distcc/bin/c++
%{_libexecdir}/distcc/bin/cc
%{_libexecdir}/distcc/bin/cpp
%{_libexecdir}/distcc/bin/g++
%{_libexecdir}/distcc/bin/gcc
%{_libexecdir}/distcc/bin/clang
%{_libexecdir}/distcc/bin/clang++
%{_sbindir}/update-distcc-symlinks
%{_bindir}/distcc
%{_bindir}/distccmon-text
%{_bindir}/lsdistcc
%{_bindir}/pump
%{_mandir}/man1/distcc.1%{?ext_man}
%{_mandir}/man1/lsdistcc.1%{?ext_man}
%{_mandir}/man1/pump*
%{_mandir}/man1/distccmon-text.1%{?ext_man}
%dir %{_sysconfdir}/distcc
%config(noreplace) %{_sysconfdir}/%{name}/hosts

%files server
%license COPYING
%doc README
%{_bindir}/distccd
%{_unitdir}/distccd.service
%{_sbindir}/rcdistccd
%config(noreplace) %{_sysconfdir}/default/distcc
%config(noreplace) %{_sysconfdir}/distcc/*allow*
%{_mandir}/man1/distccd*
%{_mandir}/man1/include_server*
%{_fillupdir}/*
%{python3_sitearch}/include_server*

%files gui
%{_bindir}/distccmon-gnome
%{_datadir}/applications/distccmon-gnome.desktop
%{_datadir}/pixmaps/distccmon-gnome-icon.png

%changelog
