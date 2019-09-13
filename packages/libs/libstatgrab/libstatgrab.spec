#
# spec file for package libstatgrab
#
# Copyright (c) 2018 SUSE LINUX GmbH, Nuernberg, Germany.
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


%define soname  10

Name:           libstatgrab
Version:        0.91
Release:        0
Summary:        Interface to System Statistics
License:        LGPL-2.1+
Group:          Development/Libraries/C and C++
Url:            http://www.i-scream.org/libstatgrab/
Source:         ftp://ftp.i-scream.org/pub/i-scream/libstatgrab/libstatgrab-%{version}.tar.gz
Source1:        statgrab.desktop
Source2:        saidar.desktop
Source3:        baselibs.conf
Source4:        %{name}-rpmlintrc
BuildRequires:  autoconf >= 2.69
BuildRequires:  automake
BuildRequires:  gcc
BuildRequires:  glibc-devel
BuildRequires:  libtool
BuildRequires:  make
BuildRequires:  ncurses-devel
BuildRequires:  pkgconfig
%if 0%{?suse_version}
BuildRequires:  fdupes
BuildRequires:  update-desktop-files
%endif
BuildRoot:      %{_tmppath}/%{name}-%{version}-build

%description
The libstatgrab library provides an easy-to-use interface for accessing system
statistics and information.
Available statistics include CPU, Load, Memory, Swap, Disk I/O, and Network
I/O. It was developed to work on Linux, FreeBSD, and Solaris.

The package also includes two tools: saidar provides a curses-based interface
for viewing live system statistics, and statgrab is a sysctl-like interface to
the statistics.

%package -n %{name}%{soname}
Summary:        Library for %{name}
License:        LGPL-2.1+
Group:          Development/Libraries/C and C++

%description -n %{name}%{soname}
Library for package libstatgrab.

%package devel
Summary:        Development Environment for %{name}
License:        LGPL-2.1+
Group:          Development/Libraries/C and C++
Requires:       %{name}%{soname} = %{version}

%description devel
Development environment for libstatgrab (headers, library links, static library).

%package -n statgrab
Summary:        Portable System Statistics Tools
License:        GPL-2.0+
Group:          System/Monitoring
Requires:       %{name}%{soname} = %{version}

%description -n statgrab
This package includes a couple of useful tools that use the %{name} library.
- statgrab: gives a sysctl-style interface to the statistics gathered by libstatgrab
This extends the use of libstatgrab to people writing scripts or anything else
that can't easily make C function calls.
Included with this package is a script to generate an MRTG configuration file
to use statgrab.

%package -n saidar
Summary:        Portable System Statistics Tools
License:        GPL-2.0+
Group:          System/Monitoring
Requires:       %{name}%{soname} = %{version}

%description -n saidar
This package includes a couple of useful tools that use the %{name} library.
- saidar: provides a curses-based interface to viewing the current state of the system
This extends the use of libstatgrab to people writing scripts or anything else
that can't easily make C function calls.

%prep
%setup -q

%build
autoreconf -fi

%configure \
	--docdir=/usr/share/doc/packages/%{name} \
	--enable-statgrab \
	--enable-saidar \
	--disable-examples \
	--disable-setuid-binaries \
	--disable-setgid-binaries \
	--disable-static \
	--with-curses-prefix=/usr/include/

make %{?_smp_mflags}

%install
%make_install

# Remove not needed static libraries
rm -f %{buildroot}%{_libdir}/%{name}.la

# install Desktop file
mkdir -p  %{buildroot}%{_datadir}/applications
install -Dm 0644 %{S:1} %{buildroot}%{_datadir}/applications/
install -Dm 0644 %{S:2} %{buildroot}%{_datadir}/applications/

%if 0%{?suse_version}
    %suse_update_desktop_file -r saidar System Monitor
    %suse_update_desktop_file -r statgrab System Monitor
    %fdupes -s %{buildroot}%{_prefix}
%endif

# install Examples
rm -fr examples/Makefile*
cp -a examples %{buildroot}%{_docdir}/%{name}/examples/

%post -n %{name}%{soname} -p /sbin/ldconfig

%postun -n %{name}%{soname} -p /sbin/ldconfig

%files -n %{name}%{soname}
%defattr(-,root,root)
%{_libdir}/%{name}.so.*

%files devel
%defattr(-,root,root)
%doc %{_docdir}/%{name}
%{_includedir}/statgrab.h
%{_libdir}/pkgconfig/%{name}.pc
%{_libdir}/%{name}.so
%{_mandir}/man3/sg_*.3%{ext_man}
%{_mandir}/man3/statgrab.3%{ext_man}
%{_mandir}/man3/%{name}.3%{ext_man}

%files -n statgrab
%defattr(-,root,root)
%doc COPYING
%{_bindir}/statgrab
%{_bindir}/statgrab-make-mrtg-config
%{_bindir}/statgrab-make-mrtg-index
%{_mandir}/man1/statgrab.1%{ext_man}
%{_mandir}/man1/statgrab-make-mrtg-config.1%{ext_man}
%{_mandir}/man1/statgrab-make-mrtg-index.1%{ext_man}
%{_datadir}/applications/statgrab.desktop

%files -n saidar
%defattr(-,root,root)
%doc COPYING
%{_bindir}/saidar
%{_mandir}/man1/saidar.1%{ext_man}
%{_datadir}/applications/saidar.desktop

%changelog
