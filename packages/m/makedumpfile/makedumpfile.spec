#
# spec file for package makedumpfile
#
# Copyright (c) 2024 SUSE LLC
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


%define build_eppic 1
%define eppic_commit 21808c78596d6d80c67eeaa08a618570ae0d886d

%if 0%{!?have_zstd:1}
%if 0%{?sle_version} >= 150200 || 0%{?suse_version} > 1500
%define have_zstd 1
%else
%define have_zstd 0
%endif
%endif

Name:           makedumpfile
Version:        1.7.5
Release:        0
Summary:        Partial kernel dump
License:        GPL-2.0-only
Group:          System/Kernel
URL:            https://github.com/makedumpfile/makedumpfile
Source:         https://github.com/makedumpfile/makedumpfile/releases/download/%{version}/%{name}-%{version}.tar.gz
Source1:        https://github.com/lucchouina/eppic/archive/%{eppic_commit}.tar.gz#/eppic-%{eppic_commit}.tar.gz
Source99:       %{name}-rpmlintrc
Patch0:         %{name}-override-libtinfo.patch
Patch1:         %{name}-ppc64-VA-range-SUSE.patch
Patch2:         %{name}-PN_XNUM.patch
Patch3:         0001-PATCH-Fix-failure-of-hugetlb-pages-exclusion-on-Linu.patch
Patch4:         0002-PATCH-Fix-wrong-exclusion-of-Slab-pages-on-Linux-6.1.patch
BuildRequires:  libbz2-devel
BuildRequires:  libdw-devel
BuildRequires:  libelf-devel
BuildRequires:  lzo-devel
BuildRequires:  ncurses-devel
BuildRequires:  snappy-devel
BuildRequires:  xz-devel
BuildRequires:  zlib-devel
BuildRoot:      %{_tmppath}/%{name}-%{version}-build
ExclusiveArch:  %{ix86} x86_64 ia64 ppc ppc64 ppc64le riscv64 s390x %{arm} aarch64
%if %{have_zstd}
BuildRequires:  libzstd-devel
%endif
%if %{build_eppic}
BuildRequires:  bison
BuildRequires:  flex
%endif

%description
makedumpfile is a dump program to shorten the size of dump file. It
copies only the necessary pages for analysis with various dump levels,
and can compress the page data. The obtained dump file can by analyzed
via gdb or crash utility.

%prep
%if %{build_eppic}
%autosetup -p1 -b1
%else
%autosetup -p1
%endif

%check

%build
export CFLAGS="%{optflags} -fcommon"
export USESNAPPY=on
%if %{have_zstd}
export USEZSTD=on
%endif
export USELZO=on
export LINKTYPE=dynamic
make %{?_smp_mflags} LDFLAGS="-Wl,-rpath,%{_libdir}/%{name}-%{version}"

%if %{build_eppic}
pushd ../eppic-%{eppic_commit}/libeppic
make
popd
export CFLAGS="-I../eppic-%{eppic_commit}/libeppic $CFLAGS"
export LDFLAGS="-L../eppic-%{eppic_commit}/libeppic $LDFLAGS"
make %{?_smp_mflags} eppic_makedumpfile.so %{?ncurses_make_opts}
%endif

%install
install -D -m 0755 makedumpfile %{buildroot}%{_bindir}/makedumpfile
install -D -m 0755 makedumpfile-R.pl %{buildroot}%{_bindir}/makedumpfile-R.pl
install -D -m 0644 makedumpfile.8 %{buildroot}%{_mandir}/man8/makedumpfile.8
install -D -m 0644 makedumpfile.conf.5 %{buildroot}%{_mandir}/man5/makedumpfile.conf.5
%if %{build_eppic}
install -D -m 0755 eppic_makedumpfile.so %{buildroot}%{_libdir}/%{name}-%{version}/eppic_makedumpfile.so
install -d -m 0755 %{buildroot}%{_datadir}/%{name}-%{version}/eppic_scripts
install -m 0644 -t %{buildroot}%{_datadir}/%{name}-%{version}/eppic_scripts/ eppic_scripts/*
%endif

# Compatibility cruft
# there is no %%license prior to SLE12
%if %{undefined _defaultlicensedir}
%define license %doc
%else
# filesystem before SLE12 SP3 lacks /usr/share/licenses
%if 0%(test ! -d %{_defaultlicensedir} && echo 1)
%define _defaultlicensedir %{_defaultdocdir}
%endif
%endif # End of compatibility cruft

%files
%defattr(-,root,root)
%license COPYING
%doc README IMPLEMENTATION
%{_mandir}/man?/*
%{_bindir}/*
%if %{build_eppic}
%dir %{_libdir}/%{name}-%{version}
%{_libdir}/%{name}-%{version}/eppic_makedumpfile.so
%dir %{_datadir}/%{name}-%{version}
%{_datadir}/%{name}-%{version}/eppic_scripts/
%endif

%changelog
