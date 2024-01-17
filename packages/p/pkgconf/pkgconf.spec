#
# spec file for package pkgconf
#
# Copyright (c) 2023 SUSE LLC
# Copyright (c) 2020 Neal Gompa <ngompa13@gmail.com>.
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


# Compatibility macros
%{!?make_build: %global make_build %{__make} %{?_smp_mflags}}
%{!?_rpmmacrodir: %global _rpmmacrodir %{_rpmconfigdir}/macros.d}

# pkgconf acts as pkgconfig for Tumbleweed (post SUSE Linux 15)
%if 0%{?suse_version} >= 1550
%bcond_without pkgconfig_compat
%else
%bcond_with pkgconfig_compat
%endif

%if %{with pkgconfig_compat}
%global pkgconfig_ver 0.29.2
# For obsoleting pkgconfig, bump the ver to a number higher than latest version
%global pkgconfig_obsver %{pkgconfig_ver}+1
%endif

# pkgconfig platform
%global pkgconf_target_platform %{_target_platform}%{?_gnu}

# Search path for pc files for pkgconf
%global pkgconf_libdirs %{_libdir}/pkgconfig:%{_datadir}/pkgconfig

%global somajor 3
%global libname lib%{name}%{somajor}
%global devname lib%{name}-devel

Name:           pkgconf
Version:        1.8.0
Release:        0
Summary:        Package compiler and linker metadata toolkit
License:        ISC
Group:          Development/Tools/Building
URL:            http://pkgconf.org/
Source0:        https://distfiles.dereferenced.org/%{name}/%{name}-%{version}.tar.xz
# Simple wrapper script to offer platform versions of pkgconfig from Fedora
Source1:        platform-pkg-config.in
# PATCH-FIX-UPSTREAM pkgconf-CVE-2023-24056.patch bsc#1207394 CVE-2023-24056 qzhao@suse.com -- Backport commit 628b2b2baf from upstream, test for, and stop string processing, on truncation.
Patch0:         pkgconf-CVE-2023-24056.patch
# For regenerating autotools scripts
BuildRequires:  autoconf
BuildRequires:  automake
BuildRequires:  gcc
BuildRequires:  libtool
BuildRequires:  make
# pkgconf uses libpkgconf internally
Requires:       %{libname}%{?_isa} = %{version}-%{release}
# This is defined within pkgconf code as a virtual pc (just like in pkgconfig)
Provides:       pkgconfig(pkgconf) = %{version}

%description
pkgconf is a program which helps to configure compiler and linker flags
for development frameworks. It is similar to pkg-config from freedesktop.org
and handles .pc files in a similar manner as pkg-config.

%package -n %{libname}
Summary:        Backend library for %{name}
License:        ISC
Group:          System/Libraries

%description -n %{libname}
This package provides libraries for applications to use the functionality
of %{name}.

%package -n %{devname}
Summary:        Development files for lib%{name}
License:        ISC
Group:          Development/Libraries/C and C++
Requires:       %{libname}%{?_isa} = %{version}-%{release}
# Avoid dependency loop on itself by specifying the Provides directly
Provides:       pkgconfig(libpkgconf) = %{version}

%description -n %{devname}
This package provides files necessary for developing applications
to use functionality provided by %{name}.

%if %{with pkgconfig_compat}
%package m4
Summary:        m4 macros for pkgconf
License:        GPL-2.0-or-later WITH Autoconf-exception-2.0
Group:          Development/Libraries/Other
BuildArch:      noarch
# Ensure that it Conflicts and Obsoletes pkgconfig since it contains content formerly from it
Conflicts:      pkgconfig < %{pkgconfig_obsver}
Obsoletes:      pkgconfig < %{pkgconfig_obsver}

%description m4
This package includes m4 macros used to support PKG_CHECK_MODULES
when using pkgconf with autotools.

%package pkg-config
Summary:        %{name} shim to provide /usr/bin/pkg-config
# Ensure that it Conflicts with pkg-config and is considered "better"
License:        ISC
Group:          Development/Tools/Building
Conflicts:      pkg-config < %{pkgconfig_obsver}
Obsoletes:      pkg-config < %{pkgconfig_obsver}
Provides:       pkg-config = %{pkgconfig_obsver}
Provides:       pkg-config%{?_isa} = %{pkgconfig_obsver}
# This is in the original pkgconfig package, set to match output from pkgconf
Provides:       pkgconfig(pkg-config) = %{version}
# Fedora/Mageia pkgconfig Provides for those who might use alternate package name
Provides:       pkgconfig = %{pkgconfig_obsver}
Provides:       pkgconfig%{?_isa} = %{pkgconfig_obsver}
Requires:       %{name}%{?_isa} = %{version}-%{release}
Requires:       %{name}-m4 = %{version}-%{release}

%description pkg-config
This package provides the shim links for pkgconf to be automatically
used in place of pkgconfig. This ensures that pkgconf is used as
the system provider of pkg-config.

%endif

%prep
%autosetup -p1

%build
autoreconf -fiv
%configure --disable-static \
           --with-pkg-config-dir=%{pkgconf_libdirs} \
           --with-system-includedir=%{_includedir} \
           --with-system-libdir=%{_libdir}

%make_build

%install
%make_install

find %{buildroot} -type f -name "*.la" -delete -print

mkdir -p %{buildroot}%{_sysconfdir}/pkgconfig/personality.d
mkdir -p %{buildroot}%{_datadir}/pkgconfig/personality.d

# pkgconf rpm macros
mkdir -p %{buildroot}%{_rpmmacrodir}/

cat > %{buildroot}%{_rpmmacrodir}/macros.pkgconf <<EOM
%%pkgconfig_personalitydir %{_datadir}/pkgconfig/personality.d
EOM

# Purge autotools-created docdir, as we'll docify with the SUSE-specific documentation paths later
rm -rf %{buildroot}%{_datadir}/doc/%{name}

%if %{with pkgconfig_compat}
install -pm 0755 %{SOURCE1} %{buildroot}%{_bindir}/%{pkgconf_target_platform}-pkg-config

sed -e "s|@TARGET_PLATFORM@|%{pkgconf_target_platform}|" \
    -e "s|@PKGCONF_LIBDIRS_LOCAL@|/usr/local/%{_lib}/pkgconfig:/usr/local/share/pkgconfig:%{pkgconf_libdirs}|" \
    -e "s|@PKGCONF_SYSLIBDIR_LOCAL@|/usr/local/%{_lib}:%{_libdir}|" \
    -e "s|@PKGCONF_SYSINCDIR_LOCAL@|/usr/local/include:%{_includedir}|" \
    -e "s|@PKGCONF_LIBDIRS@|%{pkgconf_libdirs}|" \
    -e "s|@PKGCONF_SYSLIBDIR@|%{_libdir}|" \
    -e "s|@PKGCONF_SYSINCDIR@|%{_includedir}|" \
    -i %{buildroot}%{_bindir}/%{pkgconf_target_platform}-pkg-config

ln -sr %{buildroot}%{_bindir}/%{pkgconf_target_platform}-pkg-config %{buildroot}%{_bindir}/pkg-config

# Link pkg-config(1) to pkgconf(1)
echo ".so man1/pkgconf.1" > %{buildroot}%{_mandir}/man1/pkg-config.1

mkdir -p %{buildroot}%{_libdir}/pkgconfig
mkdir -p %{buildroot}%{_datadir}/pkgconfig
%endif

# If we're not providing pkgconfig override & compat
# we should not provide the pkgconfig m4 macros
%if ! %{with pkgconfig_compat}
rm -rf %{buildroot}%{_datadir}/aclocal
rm -rf %{buildroot}%{_mandir}/man7
%endif

%post -n %{libname} -p /sbin/ldconfig
%postun -n %{libname} -p /sbin/ldconfig

%files
%license COPYING
%doc README.md AUTHORS NEWS
%{_bindir}/%{name}
%{_mandir}/man1/%{name}.1*
%{_mandir}/man5/pc.5*
%{_mandir}/man5/%{name}-personality.5*
%{_rpmmacrodir}/macros.pkgconf
%dir %{_sysconfdir}/pkgconfig
%dir %{_sysconfdir}/pkgconfig/personality.d
%dir %{_datadir}/pkgconfig/personality.d

%files -n %{libname}
%license COPYING
%{_libdir}/lib%{name}*.so.%{somajor}
%{_libdir}/lib%{name}*.so.%{somajor}.*

%files -n %{devname}
%{_libdir}/lib%{name}*.so
%{_includedir}/%{name}/
%{_libdir}/pkgconfig/lib%{name}.pc

%if %{with pkgconfig_compat}
%files m4
%dir %{_datadir}/aclocal
%{_datadir}/aclocal/pkg.m4
%{_mandir}/man7/pkg.m4.7%{?ext_man}

%files pkg-config
%{_bindir}/pkg-config
%{_bindir}/%{pkgconf_target_platform}-pkg-config
%{_mandir}/man1/pkg-config.1%{?ext_man}
%endif

%changelog
