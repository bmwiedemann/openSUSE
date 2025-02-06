#
# spec file for package fswatch
#
# Copyright (c) 2025 SUSE LLC
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


Name:           fswatch
Version:        1.18.2
Release:        0
Summary:        Multi platform file change monitor
License:        GPL-3.0-or-later
URL:            https://github.com/emcrisostomo/fswatch
Source:         https://github.com/emcrisostomo/fswatch/releases/download/%{version}/fswatch-%{version}.tar.gz
BuildRequires:  autoconf
BuildRequires:  automake
BuildRequires:  gcc-c++ > 7
BuildRequires:  libtool

%package -n lib%{name}13
Summary:        Shared library for %{name}

%description -n lib%{name}13
Shared library for %{name} a file change monitor.

%package -n lib%{name}-devel
Summary:        Development files for %{name}
Requires:       lib%{name}13 = %{version}-%{release}

%description -n lib%{name}-devel
Development files for %{name} a file change monitor.

%package doc
Summary:        Documentation for %{name}
Requires:       %{name} = %{version}-%{release}
BuildArch:      noarch

%description doc
Documentation for %{name} a file change monitor.

%description
fswatch is a file change monitor that receives notifications when the contents
of the specified files or directories are modified. fswatch implements several
monitors based on:

 * the File System Events API of Apple macOS.
 * kqueue, a notification interface introduced in FreeBSD 4.1 (and supported on
   most *BSD systems, including macOS).
 * the File Events Notification API of the Solaris kernel and its derivatives.
 * inotify, a Linux kernel subsystem that reports file system changes to applications.
 * ReadDirectoryChangesW, a Microsoft Windows API that reports changes to a directory.
 * A monitor which periodically stats the file system, saves file modification times
   in memory, and manually calculates file system changes (which works anywhere stat(2)
   can be used).

%lang_package

%prep
%autosetup

%build
%configure
%make_build

%check
%{__make} check

%install
%make_install

# remove static library
rm %{buildroot}%{_libdir}/lib%{name}.a
rm %{buildroot}%{_libdir}/lib%{name}.la

# remove copying - will get installed via license
rm %{buildroot}%{_datadir}/doc/%{name}/COPYING

# remove non Linux READMEs
rm %{buildroot}%{_datadir}/doc/%{name}/README.bsd \
   %{buildroot}%{_datadir}/doc/%{name}/README.freebsd \
   %{buildroot}%{_datadir}/doc/%{name}/README.illumos \
   %{buildroot}%{_datadir}/doc/%{name}/README.macos \
   %{buildroot}%{_datadir}/doc/%{name}/README.smartos \
   %{buildroot}%{_datadir}/doc/%{name}/README.solaris \
   %{buildroot}%{_datadir}/doc/%{name}/README.windows

install -d -m0755 %{buildroot}%{_defaultdocdir}
mv %{buildroot}%{_datadir}/doc/%{name} %{buildroot}%{_defaultdocdir}

%find_lang %{name} %{?no_lang_C}

%post -n lib%{name}13 -p /sbin/ldconfig
%postun -n lib%{name}13 -p /sbin/ldconfig

%files
%license COPYING
%attr(0755,root,root) %{_bindir}/%{name}
%{_mandir}/man7/%{name}*

%files -n lib%{name}13
%license COPYING
%{_libdir}/lib%{name}.so.*

%files -n lib%{name}-devel
%{_includedir}/lib%{name}
%{_libdir}/lib%{name}.so
%{_libdir}/pkgconfig/lib%{name}.pc

%files doc
%dir %{_defaultdocdir}/%{name}
%doc %{_defaultdocdir}/%{name}/*

%files lang -f %{name}.lang

%changelog
