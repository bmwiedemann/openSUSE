#
# spec file for package boinc-client
#
# Copyright (c) 2018 SUSE LINUX GmbH, Nuernberg, Germany.
# Copyright (c) 2016 by Aaron Puchert <aaronpuchert@alice-dsl.net>
# Copyright (c) 2011 by Sascha Manns <saigkill@opensuse.org>
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
  %define _fillupdir /var/adm/fillup-templates
%endif

%define sonum 7
%define boinc_dir %{_localstatedir}/lib/boinc

# do not build boinc-manager on SLES 11/12
%if 0%{?is_opensuse}
%bcond_without  manager
%else
%bcond_with     manager
%endif

Name:           boinc-client
%define rel_name        %{name}_release
%define minor_version   7.14
Version:        %{minor_version}.2
Release:        0
Summary:        The BOINC client
License:        GPL-3.0-or-later OR LGPL-3.0-or-later
Group:          Productivity/Clustering/Computing
Url:            http://boinc.berkeley.edu/

#Git-Clone:	git://github.com/BOINC/boinc
Source0:        https://github.com/BOINC/boinc/archive/client_release/%{minor_version}/%{version}.tar.gz
Source1:        boinc-icons.tar.bz2
Source2:        boinc-gui.desktop
Source3:        README.SUSE
Source4:        sysconfig.%{name}
Source5:        boinc-logrotate
Source6:        boinc-manager
Source10:       %{name}.init
Source20:       %{name}.service
Source100:      %{name}-rpmlintrc
Patch1:         boinc-guirpcauth.patch
Patch2:         boinc-docbook2x.patch
Patch4:         xlocale.patch
Patch5:         build-client-scripts.patch
Patch6:         libboinc-shared.patch
BuildRoot:      %{_tmppath}/%{name}-%{version}-build
#
BuildRequires:  Mesa-devel
BuildRequires:  docbook2x
BuildRequires:  docbook_4
BuildRequires:  fdupes
BuildRequires:  freeglut-devel
BuildRequires:  gcc-c++
BuildRequires:  gcc-fortran
BuildRequires:  gettext-runtime
BuildRequires:  libcurl-devel >= 7.17.1
BuildRequires:  libjpeg-devel
BuildRequires:  libnotify-devel
BuildRequires:  libtool
BuildRequires:  openssl-devel
BuildRequires:  pkg-config
BuildRequires:  pwdutils
BuildRequires:  sqlite3-devel
BuildRequires:  xorg-x11-libXmu-devel
Requires(pre):  pwdutils
Requires:       ca-certificates-mozilla
Recommends:     boinc-client-lang = %{version}
Recommends:     logrotate
#
%if 0%{?suse_version} >= 1310
BuildRequires:  libXi-devel
BuildRequires:  libxcb-devel
BuildRequires:  xcb-util-devel
%else
BuildRequires:  xorg-x11-libxcb-devel
%endif
#
%if 0%{?suse_version} >= 1210
BuildRequires:  pkgconfig(systemd)
%define has_systemd 1
%else
Requires(pre):  %fillup_prereq
Requires(pre):  %insserv_prereq
%endif
#
%if %{with manager}
BuildRequires:  update-desktop-files
BuildRequires:  wxWidgets-3_0-devel >= 3.0.2
%lang_package -n boinc-manager
%endif
#
%lang_package

%description
The Berkeley Open Infrastructure for Network Computing (BOINC) is an open-
source software platform which supports distributed computing, primarily in
the form of "volunteer" computing and "desktop Grid" computing.  It is well
suited for problems which are often described as "trivially parallel".  BOINC
is the underlying software used by projects such as SETI@home, Einstein@Home,
ClimatePrediciton.net, the World Community Grid, and many other distributed
computing projects.

This package installs the BOINC client software, which will allow your
computer to participate in one or more BOINC projects, using your spare
computer time to search for cures for diseases, model protein folding, study
global warming, discover sources of gravitational waves, and many other types
of scientific and mathematical research.

%package -n boinc-manager
Summary:        GUI to control and monitor boinc-client
Group:          Productivity/Scientific/Astronomy
Recommends:     boinc-manager-lang = %{version}
Requires:       hicolor-icon-theme

%description -n boinc-manager
The BOINC Manager is a graphical monitor and control utility for the BOINC
core client. It gives a detailed overview of the state of the client it is
monitoring. The BOINC Manager has two modes of operation, the "Simple View" in
which it only displays the most important information and the "Advanced View"
in which all information and all control elements are available.

%package -n libboinc%{sonum}
Summary:        Berkeley Open Infrastructure For Network Computing library
Group:          System/Libraries

%description -n libboinc%{sonum}
The BOINC Manager is a graphical monitor and control utility for the BOINC
core client. It gives a detailed overview of the state of the client it is
monitoring. The BOINC Manager has two modes of operation, the "Simple View" in
which it only displays the most important information and the "Advanced View"
in which all information and all control elements are available.

%package -n libboinc-devel
Summary:        Development files for libboinc
Group:          Development/Libraries/C and C++
Requires:       libboinc%{sonum} = %{version}-%{release}
Conflicts:      %{name}-devel
Requires:       openssl-devel

%description -n libboinc-devel
This package contains development files for libboinc.

%prep
%setup -q -n %{name}_release-%{minor_version}-%{version} -D -a 1
%patch -P 1 -P 2 -P 4 -P 5 -P 6 -p1

%build
# Fix default path for boincscr
sed -i -e "s,/var/lib/boinc-client,%{boinc_dir},g" \
  clientscr/screensaver_x11.cpp

# Install user hints
install -m0644 %{SOURCE3} README.SUSE

# Fix lang directories (refer patch2)
mv locale/pt_PT locale/pt

# fix utf8
for i in 2005 2009 2010 2011; do
  iconv -f ISO88591 -t UTF8 < checkin_notes_$i > checkin_notes_$i.utf8
  touch -r checkin_notes_$i checkin_notes_$i.utf8
  mv checkin_notes_$i.utf8 checkin_notes_$i
done

## remove files with questionable licenses
# removing NVIDIA owned file that does not clearly allow redistribution or
# modification
rm -r coprocs/NVIDIA

# Remove unnecessary components and files for other platforms.
rm -r android drupal mac_build mac_installer win_build xcompile

autoreconf -fi
%configure \
  --enable-optimize \
  --enable-shared \
  --disable-static \
  --enable-dynamic-client-linkage \
  --enable-unicode \
  --disable-server \
  --disable-fcgi \
%if ! %{with manager}
  --disable-manager \
%endif
  --with-ssl

# Disable rpaths
sed -i 's|^hardcode_libdir_flag_spec=.*|hardcode_libdir_flag_spec=""|g' libtool
sed -i 's|^runpath_var=LD_RUN_PATH|runpath_var=DIE_RPATH_DIE|g' libtool

# Export Path and make
make clean %{?_smp_mflags}
make libboinc_la_LIBADD="-L%{_libdir} -lssl -ldl" \
   CFLAGS="%{optflags} -g -W -pipe -fno-strict-aliasing -D_REENTRANT" \
   CXXFLAGS="%{optflags} -g -W -pipe -fno-strict-aliasing -D_REENTRANT" \
   DESTDIR=%{_prefix} %{?_smp_mflags}

%install
make DESTDIR=%{buildroot} install %{?_smp_mflags}
%if %{with manager}
for i in clientgui locale; do
%else
for i in locale; do
%endif
  pushd $i
  make DESTDIR=%{buildroot} install %{?_smp_mflags}
  popd
done

# Creates default folders
install -dm0755 %{buildroot}%{boinc_dir}
install -dm0755 %{buildroot}%{_mandir}/man1

# Remove old boinc & rename boinc_client to boinc-client
rm -f %{buildroot}%{_bindir}/boinc
mv -f %{buildroot}%{_bindir}/boinc_client %{buildroot}%{_bindir}/%{name}

%if %{with manager}
# Rename boincmgr and wrap it
mv %{buildroot}%{_bindir}/boincmgr %{buildroot}%{_bindir}/boinc-gui

# Install boinc-manager wrapper script
install -Dm0755 %{SOURCE6} %{buildroot}%{_bindir}/boinc-manager
%endif

# Use symlink instead of hardlink
pushd %{buildroot}%{_bindir}
ln -s -f %{name} boinc
%if %{with manager}
ln -s -f boinc-manager boincmgr
ln -s -f boinc-manager boincmanager
%endif
popd

%if %{with manager}
# replace @boinc_dir@, @bindir@
sed -i \
  -e "s,@boinc_dir@,%{boinc_dir},g" \
  -e "s,@bindir@,%{_bindir},g" \
  %{buildroot}%{_bindir}/boinc-manager
%endif

# Remove {buildroot}/etc/sysconfig/boinc-client, it is added by %%fillup_and_insserv
rm -f %{buildroot}%{_sysconfdir}/sysconfig/%{name}

# Install init and create symlink for rcboinc
install -dm0755 %{buildroot}%{_sbindir}
%if 0%{?has_systemd}
install -D -m0644 %{SOURCE20} %{buildroot}%{_unitdir}/%{name}.service
# And remove sysvinit script installed by boinc
rm -r %{buildroot}/%{_initddir}
ln -s %{_sbindir}/service %{buildroot}%{_sbindir}/rc%{name}
%else
install -Dm0755 %{SOURCE10} %{buildroot}%{_initddir}/%{name}
/bin/ln -sf %{_sysconfdir}/init.d/%{name} %{buildroot}%{_sbindir}/rc%{name}
%endif
# Install template for sysconfig
install -Dm0644 %{SOURCE4} %{buildroot}%{_fillupdir}/sysconfig.%{name}

# Install logrotate
install -Dm0644 %{SOURCE5} %{buildroot}%{_sysconfdir}/logrotate.d/%{name}

# Install bash completion
install -Dpm0644 client/scripts/boinc.bash %{buildroot}%{_datadir}/bash-completion/completions/boinc

%if %{with manager}
# Install desktop-file and icons
install -Dm0644 boinc-gui-128.png %{buildroot}%{_datadir}/icons/hicolor/128x128/apps/boinc-gui.png
install -Dm0644 boinc-gui-64.png %{buildroot}%{_datadir}/icons/hicolor/64x64/apps/boinc-gui.png
install -Dm0644 boinc-gui-48.png %{buildroot}%{_datadir}/icons/hicolor/48x48/apps/boinc-gui.png
install -Dm0644 boinc-gui-32.png %{buildroot}%{_datadir}/icons/hicolor/32x32/apps/boinc-gui.png
install -Dm0644 boinc-gui-22.png %{buildroot}%{_datadir}/icons/hicolor/22x22/apps/boinc-gui.png
install -Dm0644 boinc-gui-16.png %{buildroot}%{_datadir}/icons/hicolor/16x16/apps/boinc-gui.png

# Install *.desktop File
%suse_update_desktop_file -i boinc-gui Utility
%endif

# Remove static libraries, libtool archives
rm %{buildroot}%{_libdir}/*.la

# Relinking Manpages
%if %{with manager}
ln -s -f boincmgr.1.gz %{buildroot}%{_mandir}/man1/boinc-manager.1.gz
%endif
ln -s -f boinccmd.1.gz %{buildroot}%{_mandir}/man1/boinccmd.1.gz
ln -s -f boinc.1.gz %{buildroot}%{_mandir}/man1/boinc.1.gz

# Install fake /var/lib/boinc
install -dm0755 %{buildroot}%{_var}/lib/boinc

# Prepare $LANG Packages
%find_lang BOINC-Client
%if %{with manager}
%find_lang BOINC-Manager
%else
find %{buildroot}/%{_datadir}/locale/ -name "BOINC-Manager.mo" -exec rm -f \{\} \;
%endif

%fdupes -s %{buildroot}

%pre
# add group
%{_sbindir}/groupadd -r boinc 2>/dev/null || :
# add user
%{_sbindir}/useradd -c "BOINC Client" -d "%{_localstatedir}/lib/boinc" \
  -g boinc -r -s /sbin/nologin boinc 2>/dev/null || :
# fix replacing old sysconfig file (r21)
if [ -f %{_sysconfdir}/sysconfig/%{name} ]; then
  if ! grep -q "BOINC_BOINC_USR" %{_sysconfdir}/sysconfig/boinc-client; then
    mv -f %{_sysconfdir}/sysconfig/%{name} %{_sysconfdir}/sysconfig/%{name}.save
  fi
fi
%if 0%{?has_systemd}
%service_add_pre %{name}.service
%endif

%preun
%if 0%{?has_systemd}
%service_del_preun %{name}.service
%else
%stop_on_removal %{name}
%endif

%post
%if 0%{?has_systemd}
%{fillup_only}
%service_add_post %{name}.service
%else
%fillup_and_insserv %{name}
%endif
%{_sbindir}/usermod -c "BOINC Client" -s /sbin/nologin boinc 2>/dev/null || :

%postun
%if 0%{?has_systemd}
%service_del_postun %{name}.service
%else
%restart_on_update %{name}
%insserv_cleanup
%endif

%post -n boinc-manager
%{_bindir}/touch --no-create %{_datadir}/icons/hicolor || :
if [ -x %{_bindir}/gtk-update-icon-cache ]; then
  %{_bindir}/gtk-update-icon-cache --quiet %{_datadir}/icons/hicolor || :
fi

%postun -n boinc-manager
%{_bindir}/touch --no-create %{_datadir}/icons/hicolor || :
if [ -x %{_bindir}/gtk-update-icon-cache ]; then
  %{_bindir}/gtk-update-icon-cache --quiet %{_datadir}/icons/hicolor || :
fi

%post -n libboinc%{sonum} -p /sbin/ldconfig

%postun -n libboinc%{sonum} -p /sbin/ldconfig

%files
%defattr(-,root,root,-)
%license COPYING* COPYRIGHT
%doc README.SUSE
%config(noreplace) %{_sysconfdir}/logrotate.d/%{name}
%{_datadir}/bash-completion/completions/*
%{_bindir}/boinc
%{_bindir}/%{name}
%{_bindir}/boinccmd
%{_bindir}/switcher
%{_mandir}/man1/boinccmd.1.gz
%{_mandir}/man1/boinc.1.gz
%if 0%{?has_systemd}
%{_unitdir}/%{name}.service
%else
%{_initddir}/%{name}
%endif
%{_sbindir}/rc%{name}
%{_fillupdir}/sysconfig.%{name}
%defattr(-,boinc,boinc,-)
%{boinc_dir}/

%files -n %{name}-lang -f BOINC-Client.lang
%defattr(-,root,root)
%if 0%{?sles_version} == 11
%dir %{_datadir}/locale/fa_IR
%dir %{_datadir}/locale/fa_IR/LC_MESSAGES
%endif

%if %{with manager}
%files -n boinc-manager
%defattr(-,root,root,-)
%{_bindir}/boinc-gui
%{_bindir}/boinc-manager
%{_bindir}/boincmgr
%{_bindir}/boincmanager
%{_bindir}/boincscr
%{_datadir}/applications/boinc-gui.desktop
%{_datadir}/icons/hicolor/*/apps/*
%{_mandir}/man1/boincmgr.1.gz
%{_mandir}/man1/boinc-manager.1.gz

%files -n boinc-manager-lang -f BOINC-Manager.lang
%defattr(-,root,root)
%endif

%files -n libboinc%{sonum}
%defattr(-,root,root,-)
%{_libdir}/*.so.*

%files -n libboinc-devel
%defattr(-,root,root,-)
%{_libdir}/*.a
%{_libdir}/*.so
%{_includedir}/boinc

%changelog
