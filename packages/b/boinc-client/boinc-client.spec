#
# spec file for package boinc-client
#
# Copyright (c) 2026 SUSE LLC and contributors
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


# The devel package ships static libraries, keep them usable without LTO
%global _lto_cflags %{?_lto_cflags} -ffat-lto-objects
%define sonum 8
%define boinc_dir %{_localstatedir}/lib/boinc

# do not build boinc-manager on SLES
%if 0%{?is_opensuse}
%bcond_without  manager
%else
%bcond_with     manager
%endif

Name:           boinc-client
%define minor_version   8.2
Version:        %minor_version.15
Release:        0
Summary:        Client for Berkeley Open Infrastructure for Network Computing
License:        GPL-3.0-or-later OR LGPL-3.0-or-later
Group:          Productivity/Clustering/Computing
URL:            https://boinc.berkeley.edu/

#Git-Clone:     https://github.com/BOINC/boinc
Source0:        https://github.com/BOINC/boinc/archive/client_release/%{minor_version}/%{version}.tar.gz
Source3:        README.SUSE
Source4:        sysconfig.%{name}
Source6:        boinc-manager
Source20:       %{name}.service
Source100:      %{name}-rpmlintrc
Patch2:         boinc-docbook2x.patch
Patch4:         xlocale.patch
Patch6:         libboinc-shared.patch
BuildRequires:  Mesa-devel
BuildRequires:  docbook2x
BuildRequires:  docbook_4
BuildRequires:  fdupes
BuildRequires:  freeglut-devel
BuildRequires:  gcc-c++
BuildRequires:  gettext-runtime
BuildRequires:  libcurl-devel >= 7.17.1
BuildRequires:  libjpeg-devel
BuildRequires:  libnotify-devel
BuildRequires:  libtool
BuildRequires:  openssl-devel
BuildRequires:  pkg-config
BuildRequires:  sysuser-tools
BuildRequires:  xorg-x11-libXmu-devel
BuildRequires:  pkgconfig(systemd)
BuildRequires:  pkgconfig(xcb)
BuildRequires:  pkgconfig(xcb-util)
BuildRequires:  pkgconfig(xi)
%sysusers_requires
Requires:       ca-certificates-mozilla
Recommends:     boinc-client-lang = %{version}
%if %{with manager}
BuildRequires:  wxWidgets-3_2-devel >= 3.1.5
%lang_package -n boinc-manager
%endif
%lang_package

%description
The Berkeley Open Infrastructure for Network Computing (BOINC) is a
software platform which supports distributed computing, primarily in
the form of "volunteer" computing and "desktop grid" computing. It is
well suited for problems which are often described as "trivially
parallel". BOINC is the underlying software used by projects such as
Einstein@Home, ClimatePrediciton.net, the World Community
Grid, and many other distributed computing projects.

This package installs the BOINC client software, which will allow
your computer to participate in one or more BOINC projects, using
your spare computer time to search for cures for diseases, model
protein folding, study global warming, discover sources of
gravitational waves, and many other types of scientific and
mathematical research.

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
The Berkeley Open Infrastructure for Network Computing (BOINC) is a
software platform which supports distributed computing.

%package devel
Summary:        Development files for libboinc
Group:          Development/Libraries/C and C++
Requires:       libboinc%{sonum} = %{version}-%{release}
Requires:       openssl-devel
Obsoletes:      libboinc-devel < %{version}-%{release}
Provides:       libboinc-devel = %{version}-%{release}

%description devel
This package contains development files for libboinc.

%prep
%autosetup -p1 -n %{name}_release-%{minor_version}-%{version}

%build
# Install user hints
install -m0644 %{SOURCE3} README.SUSE

# Make the pt_PT translation available to all pt locales
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
rm -r android mac_build mac_installer win_build

autoreconf -fi
export CFLAGS="%optflags -W -pipe -fno-strict-aliasing -D_REENTRANT"
export CXXFLAGS="$CFLAGS"
export LDFLAGS="-Wl,-z,now"
%configure \
  --enable-shared \
  --disable-static \
  --enable-dynamic-client-linkage \
  --disable-server \
  --disable-fcgi \
%if ! %{with manager}
  --disable-manager \
%endif
  --with-ssl

# Disable rpaths
sed -i 's|^hardcode_libdir_flag_spec=.*|hardcode_libdir_flag_spec=""|g' libtool
sed -i 's|^runpath_var=LD_RUN_PATH|runpath_var=DIE_RPATH_DIE|g' libtool

%make_build libboinc_la_LIBADD="-L%{_libdir} -lssl -ldl" V=1

%install
%make_install
mkdir -p "%buildroot/%_sysusersdir"
cat >system-user-boinc.conf <<-EOF
	g boinc -
	u boinc -:boinc "BOINC Client" /var/lib/boinc
	# Several BOINC applications want to use the GPU for computations.
	m boinc render
	m boinc video
EOF
cp -a system-user-boinc.conf "%buildroot/%_sysusersdir/"
%sysusers_generate_pre system-user-boinc.conf random system-user-boinc.conf

%if %{with manager}
for i in clientgui locale; do
%else
for i in locale; do
%endif
  pushd $i
  %make_install
  popd
done

rm -f "%{buildroot}/etc/init.d/boinc-client"

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
install -D -m0644 %{SOURCE20} %{buildroot}%{_unitdir}/%{name}.service
ln -s %{_sbindir}/service %{buildroot}%{_sbindir}/rc%{name}
# Install template for sysconfig
install -Dm0644 %{SOURCE4} %{buildroot}%{_fillupdir}/sysconfig.%{name}

# Install bash completion
install -Dpm0644 client/scripts/boinc.bash %{buildroot}%{_datadir}/bash-completion/completions/boinc

# Remove static libraries, libtool archives
rm %{buildroot}%{_libdir}/*.la

# Relinking Manpages
%if %{with manager}
ln -s -f boincmgr.1.gz %{buildroot}%{_mandir}/man1/boinc-manager.1.gz
%endif
ln -s -f boinccmd.1.gz %{buildroot}%{_mandir}/man1/boinccmd.1.gz
ln -s -f boinc.1.gz %{buildroot}%{_mandir}/man1/boinc.1.gz

# Prepare $LANG Packages
%find_lang BOINC-Client
%if %{with manager}
%find_lang BOINC-Manager
%else
find %{buildroot}/%{_datadir}/locale/ -name "BOINC-Manager.mo" -delete
%endif

%fdupes -s %{buildroot}

%pre -f random.pre
%service_add_pre %{name}.service

%preun
%service_del_preun %{name}.service

%post
%{fillup_only}
%service_add_post %{name}.service

%postun
%service_del_postun %{name}.service

%post -n libboinc%{sonum} -p /sbin/ldconfig
%postun -n libboinc%{sonum} -p /sbin/ldconfig

%files
%license COPYING* COPYRIGHT
%doc README.SUSE
%{_datadir}/bash-completion/completions/*
%{_bindir}/boinc
%{_bindir}/%{name}
%{_bindir}/boinccmd
%{_mandir}/man1/boinccmd.1.gz
%{_mandir}/man1/boinc.1.gz
%{_unitdir}/%{name}.service
%{_sbindir}/rc%{name}
%{_fillupdir}/sysconfig.%{name}
%_sysusersdir/*
%attr(-,boinc,boinc) %{boinc_dir}/

%files -n %{name}-lang -f BOINC-Client.lang

%if %{with manager}
%files -n boinc-manager
%{_bindir}/boinc-gui
%{_bindir}/boinc-manager
%{_bindir}/boincmgr
%{_bindir}/boincmanager
%{_bindir}/boincscr
%{_datadir}/applications/boinc.desktop
%{_datadir}/icons/hicolor/*/apps/*
%{_datadir}/boinc-manager/
%{_mandir}/man1/boincmgr.1.gz
%{_mandir}/man1/boinc-manager.1.gz

%files -n boinc-manager-lang -f BOINC-Manager.lang
%endif

%files -n libboinc%{sonum}
%{_libdir}/*.so.*

%files devel
%{_libdir}/*.a
%{_libdir}/*.so
%{_libdir}/pkgconfig/*.pc
%{_includedir}/boinc

%changelog
