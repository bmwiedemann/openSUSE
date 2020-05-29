#
# spec file for package gammu
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


%define so_ver 8
%define gammu_docdir %{_docdir}/%{name}
Name:           gammu
Version:        1.41.0
Release:        0
Summary:        Mobile phone management utility
License:        GPL-2.0-only
Group:          Productivity/Telephony/Utilities
URL:            https://wammu.eu/gammu/
Source0:        https://dl.cihar.com/gammu/releases/%{name}-%{version}.tar.xz
# PATCH-FIX-OPENSUSE gammu-remove-gplv3-files.patch idoenmez@suse.de -- Remove GPLv3 files bnc#775397
Patch1:         gammu-remove-gplv3-files.patch
Patch2:         0001-Enable-fPIE-pie.patch
BuildRequires:  cmake >= 2.8
BuildRequires:  doxygen
BuildRequires:  gettext
BuildRequires:  gnu-free-fonts
BuildRequires:  graphviz
BuildRequires:  graphviz-gd
BuildRequires:  mysql-devel
BuildRequires:  pkgconfig
BuildRequires:  postgresql-devel
BuildRequires:  python3-Sphinx
BuildRequires:  python3-breathe
BuildRequires:  pkgconfig(bluez) >= 2.0
BuildRequires:  pkgconfig(glib-2.0) >= 2.16
BuildRequires:  pkgconfig(gobject-2.0)
BuildRequires:  pkgconfig(gudev-1.0)
BuildRequires:  pkgconfig(libcurl)
BuildRequires:  pkgconfig(libusb-1.0)
BuildRequires:  pkgconfig(odbc)
BuildRequires:  pkgconfig(systemd)
Recommends:     bluez
Requires:       dialog
Recommends:     gammu-doc

%description
Gammu is command line utility and library to work with mobile phones
from many vendors. Support for different models differs, but basic
functions should work with majority of them. Program can work with
contacts, messages (SMS, EMS and MMS), calendar, todos, filesystem,
integrated radio, camera, etc. It also supports daemon mode to send and
receive SMSes.

Currently supported phones include:

* Many Nokia models.
* Alcatel BE5 (501/701), BF5 (715), BH4 (535/735).
* AT capable phones (Siemens, Nokia, Alcatel, IPAQ).
* OBEX and IrMC capable phones (Sony-Ericsson, Motorola).
* Symbian phones through gnapplet.

This package contains Gammu binary as well as some examples.

%package devel
Summary:        Development files for Gammu
Group:          Development/Libraries/C and C++
Requires:       libGammu%{so_ver} = %{version}
Requires:       libgsmsd%{so_ver} = %{version}
Requires:       pkgconfig

%description devel
Gammu is command line utility and library to work with mobile phones
from many vendors. Support for different models differs, but basic
functions should work with majority of them. Program can work with
contacts, messages (SMS, EMS and MMS), calendar, todos, filesystem,
integrated radio, camera, etc. It also supports daemon mode to send and
receive SMSes.

Currently supported phones include:

* Many Nokia models.
* Alcatel BE5 (501/701), BF5 (715), BH4 (535/735).
* AT capable phones (Siemens, Nokia, Alcatel, IPAQ).
* OBEX and IrMC capable phones (Sony-Ericsson, Motorola).
* Symbian phones through gnapplet.

This package contain files needed for development.

%package doc
Summary:        Documentation of Gammu
Group:          Documentation/HTML
BuildArch:      noarch

%package bash-completion
Summary:        Bash completion for gammu
Group:          System/Shells
BuildRequires:  bash-completion
Requires:       bash-completion
Requires:       gammu
Supplements:    packageand(%{name}:bash-completion)

%description bash-completion
This package contains the bash completion command for gammu.

%description doc
This package contains the manual for gammu.

%package smsd
Summary:        SMS message daemon
Group:          Hardware/Mobile

%description smsd
Gammu is command line utility and library to work with mobile phones
from many vendors. Support for different models differs, but basic
functions should work with majority of them. Program can work with
contacts, messages (SMS, EMS and MMS), calendar, todos, filesystem,
integrated radio, camera, etc. It also supports daemon mode to send and
receive SMSes.

Currently supported phones include:

* Many Nokia models.
* Alcatel BE5 (501/701), BF5 (715), BH4 (535/735).
* AT capable phones (Siemens, Nokia, Alcatel, IPAQ).
* OBEX and IrMC capable phones (Sony-Ericsson, Motorola).
* Symbian phones through gnapplet.

This package contains the Gammu SMS Daemon and tool to inject messages
into the queue.

%package -n libGammu%{so_ver}
Summary:        Mobile phone management library
Group:          System/Libraries

%description -n libGammu%{so_ver}
Gammu is command line utility and library to work with mobile phones
from many vendors. Support for different models differs, but basic
functions should work with majority of them. Program can work with
contacts, messages (SMS, EMS and MMS), calendar, todos, filesystem,
integrated radio, camera, etc. It also supports daemon mode to send and
receive SMSes.

Currently supported phones include:

* Many Nokia models.
* Alcatel BE5 (501/701), BF5 (715), BH4 (535/735).
* AT capable phones (Siemens, Nokia, Alcatel, IPAQ).
* OBEX and IrMC capable phones (Sony-Ericsson, Motorola).
* Symbian phones through gnapplet.

This package contains the Gammu shared library.

%package -n libgsmsd%{so_ver}
Summary:        SMS daemon helper library
Group:          System/Libraries

%description -n libgsmsd%{so_ver}
Gammu is command line utility and library to work with mobile phones
from many vendors. Support for different models differs, but basic
functions should work with majority of them. Program can work with
contacts, messages (SMS, EMS and MMS), calendar, todos, filesystem,
integrated radio, camera, etc. It also supports daemon mode to send and
receive SMSes.

Currently supported phones include:

* Many Nokia models.
* Alcatel BE5 (501/701), BF5 (715), BH4 (535/735).
* AT capable phones (Siemens, Nokia, Alcatel, IPAQ).
* OBEX and IrMC capable phones (Sony-Ericsson, Motorola).
* Symbian phones through gnapplet.

This package contains the Gammu SMS daemon shared library.

%prep
%setup -q
%patch1 -p1
%patch2 -p1

# GPL-3.0 licensed files, bnc#775397
rm -rf contrib/sms-gammu2android
rm -rf contrib/smscgi
rm -rf helper/win32-*

%build
%cmake \
    -DBUILD_SHARED_LIBS=ON \
    -DINSTALL_DOC_DIR=%{gammu_docdir} \
    -DBASH_COMPLETION_COMPLETIONSDIR=%{_datadir}/bash-completion/completions/ \
    -DINSTALL_LSB_INIT=OFF \
    -DINSTALL_UDEV_RULES=OFF
%make_jobs
make %{?_smp_mflags} manual-html

%check
# cannot use %%ctest since running the tests in parallel is broken
export LD_LIBRARY_PATH=$LD_LIBRARY_PATH:%{buildroot}/%{_libdir}
cd build
ctest -V

%install
%cmake_install

# Install config file
install -D -pm 0644 docs/config/smsdrc %{buildroot}%{_sysconfdir}/gammu-smsdrc

# Install additional doc files
install -pm 0644 README.rst %{buildroot}%{gammu_docdir}/
cp -a contrib/udev/ %{buildroot}%{gammu_docdir}/

# Install the html manual
rm -rf %{buildroot}%{gammu_docdir}/manual/
rm -rf build/docs/manual/html/{.doctrees/,.buildinfo,_sources/}
cp -a build/docs/manual/html/ %{buildroot}%{gammu_docdir}/manual

install -d "%{buildroot}/%{_sbindir}"
ln -s service "%{buildroot}/%{_sbindir}/rcgammu-smsd"

%find_lang %{name}
%find_lang libgammu

%post -n libGammu%{so_ver} -p /sbin/ldconfig
%postun -n libGammu%{so_ver} -p /sbin/ldconfig
%post -n libgsmsd%{so_ver} -p /sbin/ldconfig
%postun -n libgsmsd%{so_ver} -p /sbin/ldconfig

%if 0%{?suse_version} >= 1330
%pre smsd
%service_add_pre gammu-smsd.service

%preun smsd
%service_del_preun gammu-smsd.service

%post smsd
%service_add_post gammu-smsd.service

%postun smsd
%service_del_postun gammu-smsd.service
%endif

%files -f %{name}.lang
%{_bindir}/gammu
%{_bindir}/gammu-config
%{_bindir}/gammu-detect
%{_bindir}/jadmaker
%doc %{gammu_docdir}
%exclude %{gammu_docdir}/manual/
%{_datadir}/gammu/
%{_mandir}/man1/gammu-config.1%{?ext_man}
%{_mandir}/man1/gammu-detect.1%{?ext_man}
%{_mandir}/man1/gammu.1%{?ext_man}
%{_mandir}/man1/jadmaker.1%{?ext_man}
%{_mandir}/man5/gammu-backup.5%{?ext_man}
%{_mandir}/man5/gammu-smsbackup.5%{?ext_man}
%{_mandir}/man5/gammurc.5%{?ext_man}

%files bash-completion
%{_datadir}/bash-completion/completions/gammu

%files devel
%{_includedir}/gammu/
%{_libdir}/libGammu.so
%{_libdir}/libgsmsd.so
%{_libdir}/pkgconfig/gammu-smsd.pc
%{_libdir}/pkgconfig/gammu.pc

%files doc
%doc %{gammu_docdir}/manual/

%files smsd
%config %{_sysconfdir}/gammu-smsdrc
%{_bindir}/gammu-smsd
%{_bindir}/gammu-smsd-inject
%{_bindir}/gammu-smsd-monitor
%{_sbindir}/rcgammu-smsd
%{_unitdir}/gammu-smsd.service
%{_mandir}/man1/gammu-smsd-inject.1%{?ext_man}
%{_mandir}/man1/gammu-smsd-monitor.1%{?ext_man}
%{_mandir}/man1/gammu-smsd.1%{?ext_man}
%{_mandir}/man5/gammu-smsdrc.5%{?ext_man}
%{_mandir}/man7/gammu-smsd-dbi.7%{?ext_man}
%{_mandir}/man7/gammu-smsd-files.7%{?ext_man}
%{_mandir}/man7/gammu-smsd-mysql.7%{?ext_man}
%{_mandir}/man7/gammu-smsd-null.7%{?ext_man}
%{_mandir}/man7/gammu-smsd-odbc.7%{?ext_man}
%{_mandir}/man7/gammu-smsd-pgsql.7%{?ext_man}
%{_mandir}/man7/gammu-smsd-run.7%{?ext_man}
%{_mandir}/man7/gammu-smsd-sql.7%{?ext_man}
%{_mandir}/man7/gammu-smsd-tables.7%{?ext_man}

%files -n libGammu%{so_ver} -f libgammu.lang
%{_libdir}/libGammu.so.%{so_ver}*

%files -n libgsmsd%{so_ver}
%{_libdir}/libgsmsd.so.%{so_ver}*

%changelog
