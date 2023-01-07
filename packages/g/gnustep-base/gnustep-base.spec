#
# spec file for package gnustep-base
#
# Copyright (c) 2022 SUSE LLC
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


%define lname   libgnustep-base1_28
%define         gnustep_sh       GNUstep.sh
%define         gs_config        %{_sysconfdir}/GNUstep/GNUstep.conf
%define         profile_dir      %{_sysconfdir}/profile.d
%define         gs_userstart     GNUstep-start.sh
%define         gs_makefiles     %{_datadir}/GNUstep/Makefiles
%define         gs_library       %{_libdir}/GNUstep
Name:           gnustep-base
Version:        1.28.1
Release:        0
Summary:        GNUstep Base library package
License:        GPL-3.0-or-later AND LGPL-2.1-or-later
Group:          System/GUI/Other
URL:            http://www.gnustep.org/
Source:         ftp://ftp.gnustep.org/pub/gnustep/core/%{name}-%{version}.tar.gz
Source1:        ftp://ftp.gnustep.org/pub/gnustep/core/%{name}-%{version}.tar.gz.sig
Source2:        %{name}-rpmlintrc
BuildRequires:  fdupes
BuildRequires:  gcc-objc
BuildRequires:  gmp-devel
BuildRequires:  gnustep-make
BuildRequires:  gnutls
BuildRequires:  libffi-devel >= 3.0.9
BuildRequires:  libicu-devel
BuildRequires:  libxml2-devel >= 2.3.0
BuildRequires:  libxslt-devel
BuildRequires:  openssl-devel
BuildRequires:  pkgconfig
BuildRequires:  zlib-devel
Requires:       gnustep-make
#Handle different package names on fedora and suse
%if 0%{?suse_version}
BuildRequires:  avahi-compat-mDNSResponder-devel
BuildRequires:  libgnutls-devel
%endif
%if 0%{?fedora}
BuildRequires:  avahi-compat-libdns_sd
BuildRequires:  avahi-compat-libdns_sd-devel
BuildRequires:  gnutls-devel
BuildRequires:  texi2html
BuildRequires:  texinfo-tex
%endif

%description
The GNUstep Base Library is a library of general-purpose,
non-graphical Objective C classes, inspired by the
OpenStep API but implementing Apple and GNU additions to the API
as well.

%package -n %{lname}
Summary:        GNUstep Base library package
Group:          System/Libraries

%description -n %{lname}
The GNUstep Base Library is a library of general-purpose,
non-graphical Objective C classes, inspired by the
OpenStep API but implementing Apple and GNU additions to the API
as well.  It includes, for example, classes for Unicode strings,
arrays, dictionaries, sets, byte streams, typed coders, invocations,
notifications, notification dispatchers, scanners, tasks, files,
networking, threading, remote object messaging support (distributed
objects), event loops, loadable bundles, attributed Unicode strings,
XML, MIME, user defaults.

%package devel
Summary:        Devel package for the GNUstep Base Library
Group:          Development/Libraries/C and C++
Requires:       %{lname} = %{version}
Requires:       %{name} = %{version}

%description devel
This package contains include files for developing applications
using the GNUstep Base Library.

%prep
%autosetup -p1
find . -type f -name "*.swp" -delete

%build
# Source GNUstep environment variables. This is done unconditionally
# to ensure that the values appropriate to this build get defined,
# irrespective of what happened to be in force for the build system.
. %{gs_config}
GNUSTEP_SH_EXPORT_ALL_VARIABLES="yes"
. ${GNUSTEP_MAKEFILES}/%{gnustep_sh}

# Configure and make.
%configure \
   --libdir=%{_libdir} --enable-ffi \
%ifarch aarch64 armv6hl
   --enable-fake-main \
%endif
%if 0%{?suse_version} == 1110
   --disable-icu \
%endif
   --with-installation-domain=SYSTEM
make %{?_smp_mflags}

%install
# Source GNUstep environment variables. This is done unconditionally
# to ensure that the values appropriate to this build get defined,
# irrespective of what happened to be in force for the build system.
. %{gs_config}
GNUSTEP_SH_EXPORT_ALL_VARIABLES="yes"
. ${GNUSTEP_MAKEFILES}/%{gnustep_sh}

# Install into RPM "build root" directory.
make -e DESTDIR=%{buildroot} \
  GNUSTEP_INSTALLATION_DOMAIN=SYSTEM \
  install

# Rename pl to pllist to fix naming conflict
mv %{buildroot}%{_bindir}/pl %{buildroot}%{_bindir}/pllist

%if 0%{?fedora}
rm -f Examples/.cvsignore
rm -f Examples/.gdbinit

# We need a modified GNUstep.conf, because the DTDs are install not
# on their real destination

sed -e "s|GNUSTEP_SYSTEM_LIBRARY=|GNUSTEP_SYSTEM_LIBRARY=%{buildroot}|" \
    -e "s|GNUSTEP_SYSTEM_HEADERS=|GNUSTEP_SYSTEM_HEADERS=%{buildroot}|" \
    %{_sysconfdir}/GNUstep/GNUstep.conf >GNUstep.conf

export LD_LIBRARY_PATH=%{buildroot}%{_libdir}
export GNUSTEP_CONFIG_FILE=$(pwd)/GNUstep.conf

%else

# Create scripts to source GNUstep environment variables,
# and update cache of services and applications, on user login.
mkdir -p %{buildroot}%{profile_dir}
cat > %{buildroot}%{profile_dir}/%{gs_userstart} << "EOF"
#!/bin/sh
. %{gs_config}

if [ -d ${HOME}/${GNUSTEP_USER_DIR} ]
then

    # Run 'make_services' in background if possible. We run it in a subshell;
    # otherwise, shells with job control (like bash) output an annoying
    # message when make_services is done, while we want it to happen silently.

    [ -x "${GNUSTEP_SYSTEM_TOOLS}/make_services" ] \
      && ("${GNUSTEP_SYSTEM_TOOLS}/make_services" &)

fi
EOF
chmod 755 %{buildroot}%{profile_dir}/%{gs_userstart}
%endif

# save disk space: symlink duplicates
%fdupes -s %{buildroot}

# Comment out checks because they break building on some systems. The NSOperation test seems to loop infinite.
#%check
#make check

%post   -n %{lname} -p /sbin/ldconfig
%postun -n %{lname} -p /sbin/ldconfig

%files
%license COPYING COPYING.LIB
%doc ANNOUNCE ChangeLog NEWS README.md
%{_bindir}/HTMLLinker
%{_bindir}/autogsdoc
%{_bindir}/cvtenc
%{_bindir}/defaults
%{_bindir}/gdnc
%{_bindir}/gdomap
%{_bindir}/gspath
%{_bindir}/make_strings
%{_bindir}/pl2link
%{_bindir}/pldes
%{_bindir}/plget
%{_bindir}/pllist
%{_bindir}/plmerge
%{_bindir}/plparse
%{_bindir}/plser
%{_bindir}/plutil
%{_bindir}/sfparse
%{_bindir}/xmlparse
%{gs_library}
%{gs_makefiles}
%{_mandir}/man1/HTMLLinker.1%{?ext_man}
%{_mandir}/man1/autogsdoc.1%{?ext_man}
%{_mandir}/man1/cvtenc.1%{?ext_man}
%{_mandir}/man1/defaults.1%{?ext_man}
%{_mandir}/man1/gdnc.1%{?ext_man}
%{_mandir}/man1/gspath.1%{?ext_man}
%{_mandir}/man1/make_strings.1%{?ext_man}
%{_mandir}/man1/pldes.1%{?ext_man}
%{_mandir}/man1/sfparse.1%{?ext_man}
%{_mandir}/man1/xmlparse.1%{?ext_man}
%{_mandir}/man1/plutil.1%{?ext_man}
%{_mandir}/man8/gdomap.8%{?ext_man}
%if 0%{?suse_version}
%config(noreplace) %{profile_dir}/%{gs_userstart}
%endif

%files -n %{lname}
%{_libdir}/libgnustep-base.so.*

%files devel
%{_includedir}/*
%{_libdir}/libgnustep-base.so

%changelog
