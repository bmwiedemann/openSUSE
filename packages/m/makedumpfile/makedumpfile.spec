#
# spec file for package makedumpfile
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


%if 0%{!?have_snappy:1}
%if 0%{?suse_version} >= 1310
%define have_snappy 1
%else
%define have_snappy 0
%endif
%endif

# Compatibility cruft
# there is no separate -ltinfo until openSUSE 13.1
%if 0%{?suse_version} < 1310 && 0%{?sles_version} < 12
%define ncurses_make_opts TINFOLIB=-lncurses
%endif
# End of compatibility cruft

Name:           makedumpfile
Version:        1.6.7
Release:        0
Summary:        Partial kernel dump
License:        GPL-2.0-only
Group:          System/Kernel
URL:            https://sourceforge.net/projects/makedumpfile/
Source:         https://sourceforge.net/projects/makedumpfile/files/makedumpfile/%{version}/%{name}-%{version}.tar.gz
Source99:       %{name}-rpmlintrc
Patch1:         %{name}-override-libtinfo.patch
Patch2:         %{name}-ppc64-VA-range-SUSE.patch
Patch3:         %{name}-PN_XNUM.patch
Patch4:         %{name}-arm64-Align-PMD_SECTION_MASK-with-PHYS_MASK.patch
Patch5:         %{name}-Fix-cd_header-offset-overflow-with-large-pfn.patch
Patch6:         %{name}-sadump-Fix-failure-of-reading.patch
BuildRequires:  libdw-devel
BuildRequires:  libelf-devel
BuildRequires:  libeppic-devel
BuildRequires:  lzo-devel
BuildRequires:  ncurses-devel
BuildRequires:  xz-devel
BuildRequires:  zlib-devel
BuildRoot:      %{_tmppath}/%{name}-%{version}-build
ExclusiveArch:  %{ix86} x86_64 ia64 ppc ppc64 ppc64le s390x %{arm} aarch64
%if 0%{?suse_version} >= 1140 || 0%{?sles_version} >= 11
BuildRequires:  libbz2-devel
%else
BuildRequires:  bzip2
%endif
%if %{have_snappy}
BuildRequires:  snappy-devel
%endif

%description
makedumpfile is a dump program to shorten the size of dump file. It
copies only the necessary pages for analysis with various dump levels,
and can compress the page data. The obtained dump file can by analyzed
via gdb or crash utility.

%prep
%setup -q
%autopatch -p1

%build
export CFLAGS="%{optflags} -fcommon"
%if %{have_snappy}
export USESNAPPY=on
%endif
export USELZO=on
export LINKTYPE=dynamic
make %{?_smp_mflags} LDFLAGS="-Wl,-rpath,%{_libdir}/%{name}-%{version}"
make %{?_smp_mflags} eppic_makedumpfile.so %{?ncurses_make_opts}

%install
install -D -m 0755 makedumpfile %{buildroot}%{_bindir}/makedumpfile
install -D -m 0755 makedumpfile-R.pl %{buildroot}%{_bindir}/makedumpfile-R.pl
install -D -m 0644 makedumpfile.8 %{buildroot}%{_mandir}/man8/makedumpfile.8
install -D -m 0644 makedumpfile.conf.5 %{buildroot}%{_mandir}/man5/makedumpfile.conf.5
install -D -m 0755 eppic_makedumpfile.so %{buildroot}%{_libdir}/%{name}-%{version}/eppic_makedumpfile.so
install -d -m 0755 %{buildroot}%{_datadir}/%{name}-%{version}/eppic_scripts
install -m 0644 -t %{buildroot}%{_datadir}/%{name}-%{version}/eppic_scripts/ eppic_scripts/*

# Compatibility cruft
# there is no %license prior to SLE12
%if %{undefined _defaultlicensedir}
%define license %doc
%else
# filesystem before SLE12 SP3 lacks /usr/share/licenses
%if 0%(test ! -d %{_defaultlicensedir} && echo 1)
%define _defaultlicensedir %_defaultdocdir
%endif
%endif
# End of compatibility cruft

%files
%defattr(-,root,root)
%license COPYING
%doc README IMPLEMENTATION
%{_mandir}/man?/*
%{_bindir}/*
%dir %{_libdir}/%{name}-%{version}
%{_libdir}/%{name}-%{version}/eppic_makedumpfile.so
%dir %{_datadir}/%{name}-%{version}
%{_datadir}/%{name}-%{version}/eppic_scripts/

%changelog
