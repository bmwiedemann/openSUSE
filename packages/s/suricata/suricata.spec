#
# spec file for package suricata
#
# Copyright (c) 2025 SUSE LLC
# Copyright (c) 2026 Eyad Issa <eyadlorenzo@gmail.com>
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


%global flavor @BUILD_FLAVOR@%{nil}
%define soname 8_0_8
%if "%{?flavor}" == "dpdk"
%define dpdk_flavor 1
%define package_name suricata-dpdk
%define library_name libsuricata%{soname}-dpdk
%else
%define dpdk_flavor 0
%define package_name suricata
%define library_name libsuricata%{soname}
%endif

# Handling libxdp support
%if (0%{?suse_version} <= 1500 && 0%{?sle_version} <= 150500 && 0%{?is_opensuse}) || (0%{?sle_version} == 150700 && !0%{?is_opensuse})
    %bcond_with xdp_bpf
%else
    %bcond_without xdp_bpf
%endif

# libnetfilter_log is unavailable in Leap 16.0/16.1 and SLE 15 SP7.
%if (0%{?is_opensuse} && (0%{?suse_version} == 1600 || 0%{?suse_version} == 1610)) || (0%{?sle_version} == 150700 && !0%{?is_opensuse})
    %bcond_with nflog
%else
    %bcond_without nflog
%endif

# SLE 15 SP7's configured repository does not provide hiredis.
%if 0%{?sle_version} == 150700 && !0%{?is_opensuse}
    %bcond_with hiredis
%else
    %bcond_without hiredis
%endif
# Handling libmagic and libnet support
%if 0%{?suse_version} <= 1500 && 0%{?sle_version} <= 150600 && 0%{?is_opensuse}
    %ifarch aarch64
        %bcond_with libmagic
        %bcond_with libnet
    %else
        %bcond_without libmagic
        %bcond_without libnet
    %endif
%else
    %bcond_without libmagic
    %bcond_without libnet
%endif

# vectorscan (libhs) only supports 64-bit ARM and x86_64
%if 0%{?sle_version} == 150700 && !0%{?is_opensuse}
    %bcond_with libhs
%else
%ifarch %{arm64} x86_64
    %bcond_without libhs
%else
    %bcond_with libhs
%endif
%endif

Name:           %{package_name}
Version:        8.0.8
Release:        0
Summary:        Open Source Next Generation Intrusion Detection and Prevention Engine
License:        GPL-2.0-only
URL:            https://www.openinfosecfoundation.org/
Source0:        %{URL}/download/suricata-%{version}.tar.gz
Source1:        %{URL}/download/suricata-%{version}.tar.gz.sig
Source2:        https://www.openinfosecfoundation.org/downloads/OISF.pub#/suricata.keyring
Source3:        suricata.service
Source4:        suricata.sysconfig
Source5:        suricata.logrotate
Source6:        suricata-user.conf
Source99:       suricata-rpmlintrc
BuildRequires:  cargo
BuildRequires:  cargo-packaging
BuildRequires:  chrpath
BuildRequires:  dos2unix
BuildRequires:  pkgconfig
BuildRequires:  python3
BuildRequires:  python3-PyYAML
BuildRequires:  python3-setuptools
BuildRequires:  rust >= 1.75.0
BuildRequires:  systemd-rpm-macros
BuildRequires:  sysuser-tools
%if %{with hiredis}
BuildRequires:  pkgconfig(hiredis)
%endif
BuildRequires:  pkgconfig(hwloc) >= 2.0.0
BuildRequires:  pkgconfig(jansson)
BuildRequires:  pkgconfig(libcap-ng)
BuildRequires:  pkgconfig(libevent)
BuildRequires:  pkgconfig(liblz4)
BuildRequires:  pkgconfig(liblzma)
BuildRequires:  pkgconfig(libmaxminddb)
%if %{with nflog}
BuildRequires:  pkgconfig(libnetfilter_log)
%endif
BuildRequires:  pkgconfig(libnetfilter_queue)
BuildRequires:  pkgconfig(libnfnetlink)
BuildRequires:  pkgconfig(libpcap)
BuildRequires:  pkgconfig(libpcre2-8)
BuildRequires:  pkgconfig(nspr)
BuildRequires:  pkgconfig(nss)
BuildRequires:  pkgconfig(yaml-0.1)
BuildRequires:  pkgconfig(zlib)
%if %{dpdk_flavor}
ExclusiveArch:  x86_64 aarch64 ppc64le
%if 0%{?sle_version} == 150700 && !0%{?is_opensuse}
BuildRequires:  dpdk-devel
%endif
BuildRequires:  pkgconfig(libdpdk) >= 19.11
BuildRequires:  libnuma-devel
Provides:       suricata = %{version}-%{release}
Conflicts:      suricata
%else
Conflicts:      suricata-dpdk
%endif
Requires:       %{library_name} = %{version}-%{release}
Requires:       python3-PyYAML
Requires(pre):  %fillup_prereq
Recommends:     jq
Recommends:     logrotate
%sysusers_requires
%{?systemd_requires}
%if %{with libmagic}
    %if 0%{?suse_version} >= 1600
BuildRequires:  pkgconfig(libmagic)
    %else
BuildRequires:  file-devel
    %endif
%endif
%if %{with libnet}
    %if 0%{?suse_version} >= 1600
BuildRequires:  pkgconfig(libnet)
    %else
BuildRequires:  libnet-devel
    %endif
%endif
%if %{with xdp_bpf}
BuildRequires:  pkgconfig(libbpf)
BuildRequires:  pkgconfig(libxdp)
%endif
%if %{with libhs}
BuildRequires:  pkgconfig(libhs)
%endif

%description
The Suricata Engine is an Open Source Next Generation Intrusion Detection and
Prevention Engine. This engine is not intended to just replace or emulate the
existing tools in the industry, but will bring new ideas and technologies to
the field.

OISF is part of and funded by the Department of Homeland Security's Directorate
for Science and Technology HOST program (Homeland Open Security Technology), by
the the Navy's Space and Naval Warfare Systems Command (SPAWAR), as well as
through the very generous support of the members of the OISF Consortium. More
information about the Consortium is available, as well as a list of our current
Consortium Members.

%package -n %{library_name}
Summary:        Open Source Next Generation Intrusion Detection and Prevention Engine Library
%if %{dpdk_flavor}
Conflicts:      libsuricata%{soname}
%else
Conflicts:      libsuricata%{soname}-dpdk
%endif

%description -n %{library_name}
The Suricata Engine is an Open Source Next Generation Intrusion Detection and
Prevention Engine.

This package contains the shared library.

%package devel
Summary:        Development files for the Suricata engine library
Requires:       %{library_name} = %{version}-%{release}
%if %{dpdk_flavor}
Conflicts:      suricata-devel
%else
Conflicts:      suricata-dpdk-devel
%endif
Requires:       pkgconfig(jansson)
%if %{with libmagic}
    %if 0%{?suse_version} >= 1600
Requires:       pkgconfig(libmagic)
    %else
Requires:       file-devel
    %endif
%endif

%description devel
The Suricata Engine is an Open Source Next Generation Intrusion Detection and
Prevention Engine.

This package contains the development files for the Suricata engine library.

%prep
%autosetup -n suricata-%{version}
# Fix path in manpage
sed -i 's|%{_prefix}/local||g' doc/userguide/suricata.1

%build
%global _lto_cflags %{nil}
export HAVE_PYTHON=%{_bindir}/python3

%configure \
    --disable-dependency-tracking \
    --enable-gccmarch-native=no \
    --enable-year2038 \
    --enable-python \
%if %{with hiredis}
    --enable-hiredis \
%else
    --disable-hiredis \
%endif
    --enable-shared \
%if %{dpdk_flavor}
    --enable-dpdk \
%endif
%if %{with xdp_bpf}
    --enable-ebpf \
%else
    --disable-af-xdp \
%endif
%if %{with nflog}
    --enable-nflog \
    --with-libnetfilter_log-includes=`pkg-config libnetfilter_log --variable=includedir` \
%endif
    --enable-nfqueue \
    --enable-gccprotect \
    --enable-geoip \
%if %{with libmagic}
    --enable-libmagic \
%else
    --disable-libmagic \
%endif
    --enable-hwloc \
    %{nil}

# --output-sync=none is needed to avoid GNU Make
# buffering the entire cargo build output
%make_build --output-sync=none
%sysusers_generate_pre %{SOURCE6} %{name} suricata-user.conf

%install
%make_install install-library install-headers

mkdir -p %{buildroot}%{_localstatedir}/log/suricata
mkdir -p %{buildroot}%{_localstatedir}/lib/suricata

mkdir -p            %{buildroot}%{_sysconfdir}/suricata
cp *.config         %{buildroot}%{_sysconfdir}/suricata/
cp etc/*.config     %{buildroot}%{_sysconfdir}/suricata/
cp suricata.yaml    %{buildroot}%{_sysconfdir}/suricata/
cp -R rules         %{buildroot}%{_sysconfdir}/suricata/

rm -rf %{buildroot}/%{_datadir}/doc/suricata
rm -rf %{buildroot}%{python3_sitelib}/suricata/__pycache__

# we don't ship static libraries
rm -rf %{buildroot}%{_libdir}/libsuricata*.a

# install misc files
install -Dpm 0644 %{SOURCE3} %{buildroot}%{_unitdir}/suricata.service
install -Dpm 0644 %{SOURCE4} %{buildroot}%{_fillupdir}/sysconfig.suricata
install -Dpm 0644 %{SOURCE5} %{buildroot}%{_sysconfdir}/logrotate.d/suricata
install -Dpm 0644 %{SOURCE6} %{buildroot}%{_sysusersdir}/suricata-user.conf

mkdir -p %{buildroot}%{_sbindir}
ln -s %{_sbindir}/service %{buildroot}%{_sbindir}/rcsuricata

# fix RPATH in the binary
chrpath --delete %{buildroot}%{_bindir}/suricata

# fix E: wrong-script-end-of-line-encoding
find %{buildroot}%{_prefix}/lib/suricata/python -type f -name "*.py" \
  -exec dos2unix {} \;

# fix E: script-without-shebang
find %{buildroot}%{_prefix}/lib/suricata/python -type f -name "*.py" \
  -exec chmod a-x {} \;

%pre -f %{name}.pre
%service_add_pre suricata.service

%post
%service_add_post suricata.service
%fillup_only -n suricata
# Migrate existing logs and libs to the new user if they exist
if [ $1 -ge 1 ]; then
    # Notify the user about the security hardening only once and migrate files
    if [ ! -f %{_localstatedir}/lib/suricata.migrated-to-nonroot ]; then
        chown -R suricata:suricata %{_localstatedir}/log/suricata || :
        chown -R suricata:suricata %{_localstatedir}/lib/suricata || :

        mkdir -p %{_localstatedir}/adm/update-messages
        cat > %{_localstatedir}/adm/update-messages/%{name}-%{version}-%{release} << EOF
Suricata has been hardened and now runs as a non-privileged 'suricata' user.
Existing logs in %{_localstatedir}/log/suricata and data in %{_localstatedir}/lib/suricata
have been migrated to the new user ownership.

If you have custom rule files or configurations outside these directories,
please ensure they are readable by the 'suricata' user.
EOF
        touch %{_localstatedir}/lib/suricata.migrated-to-nonroot
    fi
fi
suricata-update || :

%preun
%service_del_preun suricata.service

%postun
%service_del_postun suricata.service

%ldconfig_scriptlets -n %{library_name}

%files
%license COPYING
%doc doc/AUTHORS doc/Basic_Setup.txt doc/Setting_up_IPSinline_for_Linux.txt doc/Third_Party_Installation_Guides.txt doc/TODO
%config(noreplace)%{_sysconfdir}/suricata
%{_bindir}/suricata
%{_bindir}/suricatasc
%{_bindir}/suricatactl
%{_bindir}/suricata-update
%{_sbindir}/rcsuricata
%dir %{_prefix}/lib/suricata
%dir %{_prefix}/lib/suricata/python
%{_prefix}/lib/suricata/python/suricata/
%{_datadir}/suricata*
%dir %attr(0750,suricata,suricata) %{_localstatedir}/log/suricata
%{_mandir}/man1/suricata.1%{?ext_man}
%{_mandir}/man1/suricatasc.1%{?ext_man}
%{_mandir}/man1/suricatactl.1%{?ext_man}
%{_mandir}/man1/suricatactl-filestore.1%{?ext_man}

%dir %attr(0750,suricata,suricata) %{_localstatedir}/lib/suricata
%{_unitdir}/suricata.service
%{_sysusersdir}/suricata-user.conf
%config(noreplace) %{_sysconfdir}/logrotate.d/suricata
%{_fillupdir}/sysconfig.suricata
%ghost %attr(0644,root,root) %{_localstatedir}/lib/suricata.migrated-to-nonroot
%ghost %attr(0644,root,root) %{_localstatedir}/adm/update-messages/%{name}-%{version}-%{release}

%files -n %{library_name}
%{_libdir}/libsuricata.so.*

%files devel
%{_bindir}/libsuricata-config
%{_includedir}/suricata
%{_libdir}/libsuricata.so

%changelog
