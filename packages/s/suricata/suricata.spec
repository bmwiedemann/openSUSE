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


%define soname 8_0_3

# Handling libxdp support
%if (0%{?suse_version} <= 1500) && (0%{?sle_version} <= 150500) && (0%{?is_opensuse})
    %bcond_with xdp_bpf
%else
    %bcond_without xdp_bpf
%endif

# Handling libmagic and libnet support
%if (0%{?suse_version} <= 1500) && (0%{?sle_version} <= 150600) && (0%{?is_opensuse})
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
%ifarch %{arm64} x86_64
    %bcond_without libhs
%else
    %bcond_with libhs
%endif

Name:           suricata
Version:        8.0.3
Release:        0
Summary:        Open Source Next Generation Intrusion Detection and Prevention Engine
License:        GPL-2.0-only
URL:            https://www.openinfosecfoundation.org/
Source0:        %{URL}/download/%{name}-%{version}.tar.gz
Source1:        %{URL}/download/%{name}-%{version}.tar.gz.sig
Source2:        https://www.openinfosecfoundation.org/downloads/OISF.pub#/%{name}.keyring
Source3:        suricata.service
Source4:        suricata.sysconfig
Source5:        suricata.logrotate
BuildRequires:  cargo
BuildRequires:  cargo-packaging
BuildRequires:  chrpath
BuildRequires:  dos2unix
BuildRequires:  pkgconfig
BuildRequires:  python3
BuildRequires:  python3-PyYAML
BuildRequires:  python3-setuptools
BuildRequires:  rust >= 1.63.0
BuildRequires:  systemd-rpm-macros
BuildRequires:  pkgconfig(hiredis)
BuildRequires:  pkgconfig(jansson)
BuildRequires:  pkgconfig(libcap-ng)
BuildRequires:  pkgconfig(libevent)
BuildRequires:  pkgconfig(liblz4)
BuildRequires:  pkgconfig(liblzma)
BuildRequires:  pkgconfig(libmaxminddb)
BuildRequires:  pkgconfig(libnetfilter_log)
BuildRequires:  pkgconfig(libnetfilter_queue)
BuildRequires:  pkgconfig(libnfnetlink)
BuildRequires:  pkgconfig(libpcap)
BuildRequires:  pkgconfig(libpcre2-8)
BuildRequires:  pkgconfig(nspr)
BuildRequires:  pkgconfig(nss)
BuildRequires:  pkgconfig(yaml-0.1)
BuildRequires:  pkgconfig(zlib)
Requires:       python3-PyYAML
Requires(pre):  %fillup_prereq
Recommends:     jq
Recommends:     logrotate
%{?systemd_requires}
%if %{with libmagic}
    %if 0%{?suse_version} >= 1600
BuildRequires:  pkgconfig(libmagic)
    %else
BuildRequires:  file-devel
    %endif
%endif
%if 0%{with libnet}
    %if 0%{?suse_version} >= 1600
BuildRequires:  pkgconfig(libnet)
    %else
BuildRequires:  libnet-devel
    %endif
%endif
%if 0%{with xdp_bpf}
BuildRequires:  pkgconfig(libbpf)
BuildRequires:  pkgconfig(libxdp)
%endif
%if 0%{with libhs}
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

%package -n libsuricata%{soname}
Summary:        Open Source Next Generation Intrusion Detection and Prevention Engine Library

%description -n libsuricata%{soname}
The Suricata Engine is an Open Source Next Generation Intrusion Detection and
Prevention Engine.

This package contains the shared library.

%package devel
Summary:        Development files for the Suricata engine library
Requires:       libsuricata%{soname} = %{version}
Requires:       pkgconfig(jansson)
Requires:       pkgconfig(libmagic)

%description devel
The Suricata Engine is an Open Source Next Generation Intrusion Detection and
Prevention Engine.

This package contains the development files for the Suricata engine library.

%prep
%autosetup
# Fix path in manpage
sed -i 's|%{_prefix}/local||g' doc/userguide/suricata.1

%build
%global _lto_cflags %{nil}
export HAVE_PYTHON=%{_bindir}/python3

%configure \
    --disable-dependency-tracking \
    --enable-gccmarch-native=no \
    --enable-ebpf \
    --enable-year2038 \
    --enable-python \
    --enable-hiredis \
    --enable-shared \
    --enable-nflog \
    --with-libnetfilter_log-includes=`pkg-config libnetfilter_log --variable=includedir` \
    --enable-nfqueue \
    --enable-gccprotect \
    --enable-geoip \
    %{nil}

# --output-sync=none is needed to avoid GNU Make
# buffering the entire cargo build output
%make_build --output-sync=none

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
install -Dpm 0644 %{SOURCE3} %{buildroot}%{_unitdir}/%{name}.service
install -Dpm 0644 %{SOURCE4} %{buildroot}%{_fillupdir}/sysconfig.%{name}
install -Dpm 0644 %{SOURCE5} %{buildroot}%{_sysconfdir}/logrotate.d/%{name}

mkdir -p %{buildroot}%{_sbindir}
ln -s %{_sbindir}/service %{buildroot}%{_sbindir}/rcsuricata
mkdir -p %{buildroot}%{_localstatedir}/log/suricata

# fix RPATH in the binary
chrpath --delete %{buildroot}%{_bindir}/suricata

# fix E: wrong-script-end-of-line-encoding
find %{buildroot}%{_prefix}/lib/suricata/python -type f -name "*.py" \
  -exec dos2unix {} \;

# fix E: script-without-shebang
find %{buildroot}%{_prefix}/lib/suricata/python -type f -name "*.py" \
  -exec chmod a-x {} \;

%pre
%service_add_pre %{name}.service

%post
%service_add_post %{name}.service
%fillup_only
suricata-update

%preun
%service_del_preun %{name}.service

%postun
%service_del_postun %{name}.service

%ldconfig_scriptlets -n libsuricata%{soname}

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
%dir %{_localstatedir}/log/suricata
%{_mandir}/man1/suricata.1%{?ext_man}
%{_mandir}/man1/suricatasc.1%{?ext_man}
%{_mandir}/man1/suricatactl.1%{?ext_man}
%{_mandir}/man1/suricatactl-filestore.1%{?ext_man}

%dir %{_localstatedir}/lib/suricata
%{_unitdir}/%{name}.service
%config(noreplace) %{_sysconfdir}/logrotate.d/%{name}
%{_fillupdir}/sysconfig.%{name}

%files -n libsuricata%{soname}
%{_libdir}/libsuricata.so.*

%files devel
%{_bindir}/libsuricata-config
%{_includedir}/suricata
%{_libdir}/libsuricata.so

%changelog
