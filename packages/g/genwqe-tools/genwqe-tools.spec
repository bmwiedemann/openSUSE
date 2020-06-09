#
# spec file for package genwqe-tools
#
# Copyright (c) 2020 SUSE LLC
# Copyright 2015, International Business Machines
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


Summary:        GenWQE userspace tools
License:        Apache-2.0
Group:          Development/Tools
Name:           genwqe-tools
Version:        4.0.20
Release:        1%{?dist}
URL:            https://github.com/ibm-genwqe/genwqe-user/
Requires:       zlib >= 1.2.7
BuildRequires:  help2man
BuildRequires:  zlib-devel >= 1.2.7
%ifarch ppc64le ppc64
BuildRequires:  kernel-devel >= 4.4.21-69
BuildRequires:  libcxl-devel
%endif
BuildRequires:  fdupes
BuildRoot:      %{_tmppath}/%{name}-%{version}-build
ExclusiveArch:  s390x ppc64le ppc64
#Source0: https://github.com/ibm-genwqe/genwqe-user/archive/v%%{version}.tar.gz
#for building from local git (fetched from _service)
Source0:        genwqe-user-%{version}.tar.xz
Source1:        %{name}-rpmlintrc
Patch0:         genwqe-user-4.0.18-install-gzFile_test.patch
Patch1:         genwqe-user-4.0.18-config.patch
Patch2:         genwqe-user-4.0.20-glibc-2.30-gettid-naming-conflict.patch

%description
Provide a suite of utilities to manage and configure the IBM GenWQE card.

%package -n genwqe-zlib
Summary:        GenWQE hardware accelerated libz
Group:          System/Libraries

%description -n genwqe-zlib
GenWQE hardware accelerated libz and test-utilities.

%package -n genwqe-vpd
Summary:        GenWQE adapter VPD tools
Group:          System/Libraries

%description -n genwqe-vpd
The genwqe-vpd package contains GenWQE adapter VPD tools.

%package        devel
Summary:        Development files for %{name}
Group:          Development/Libraries/C and C++
Requires:       %{name} = %{version}

%description devel
The %{name}-devel package contains libraries and header files for
developing applications that use %{name}.

%prep
%autosetup -p1 -n genwqe-user-%{version}

%build
%global _lto_cflags %{_lto_cflags} -ffat-lto-objects
make %{?_smp_mflags} tools lib VERSION=%{version} \
       CONFIG_ZLIB_PATH=/%{_lib}/libz.so.1

%install
make %{?_smp_mflags} install DESTDIR=%{buildroot}/%{_prefix} \
        VERSION=%{version} SYSTEMD_UNIT_DIR=%{buildroot}/%{_unitdir} \
	LIB_INSTALL_PATH=%{buildroot}/%{_libdir}/genwqe \
	INCLUDE_INSTALL_PATH=%{buildroot}/%{_includedir}/genwqe

# FIXME Instead of trying to fixup things in the spec fike, let us consider
#       changing the associated install rule, such that the spec file
#       can get smaller and simpler.
#

# Move genwqe_vpd.csv to expected location.
mkdir -p %{buildroot}/%{_sysconfdir}/
install -m 0644 tools/genwqe_vpd.csv %{buildroot}/etc/

%fdupes %{buildroot}%{_bindir}

ln -sf %{_bindir}/genwqe_gunzip %{buildroot}/%{_libdir}/genwqe/gunzip
ln -sf %{_bindir}/genwqe_gzip   %{buildroot}/%{_libdir}/genwqe/gzip

%ifarch ppc64le ppc64
%pre
%service_add_pre genwqe_maint.service

%post
%service_add_post genwqe_maint.service

%preun
%service_del_preun genwqe_maint.service

%postun
%service_del_postun genwqe_maint.service
%endif

%files -n genwqe-tools
%defattr(0755,root,root)
%{_bindir}/genwqe_echo
%{_bindir}/genwqe_ffdc
%{_bindir}/genwqe_cksum
%{_bindir}/genwqe_memcopy
%{_bindir}/genwqe_peek
%{_bindir}/genwqe_poke
%{_bindir}/genwqe_update

%{_bindir}/genwqe_gunzip
%{_bindir}/genwqe_gzip
%{_bindir}/genwqe_test_gz
%{_bindir}/genwqe_mt_perf
%{_bindir}/zlib_mt_perf
%{_bindir}/gzFile_test

%{_libdir}/genwqe/gunzip
%{_libdir}/genwqe/gzip

%defattr(-,root,root)
%doc LICENSE
%{_mandir}/man1/genwqe_echo.1.gz
%{_mandir}/man1/genwqe_ffdc.1.gz
%{_mandir}/man1/genwqe_gunzip.1.gz
%{_mandir}/man1/genwqe_gzip.1.gz
%{_mandir}/man1/genwqe_cksum.1.gz
%{_mandir}/man1/genwqe_memcopy.1.gz
%{_mandir}/man1/genwqe_peek.1.gz
%{_mandir}/man1/genwqe_poke.1.gz
%{_mandir}/man1/genwqe_update.1.gz
%{_mandir}/man1/zlib_mt_perf.1.gz
%{_mandir}/man1/gzFile_test.1.gz

%ifarch ppc64le ppc64
%{_bindir}/genwqe_maint
%{_bindir}/genwqe_loadtree
%{_unitdir}/genwqe_maint.service
%{_mandir}/man1/genwqe_maint.1.gz
%{_mandir}/man1/genwqe_loadtree.1.gz
%endif

%files -n genwqe-zlib
%defattr(-,root,root)
%doc LICENSE
%defattr(0755,root,root)
%dir %{_libdir}/genwqe
%{_libdir}/genwqe/*.so*

%files -n genwqe-vpd
%defattr(-,root,root,-)
%{_bindir}/genwqe_csv2vpd
%{_bindir}/genwqe_vpdconv
%{_bindir}/genwqe_vpdupdate
%defattr(-,root,root)
%doc LICENSE
%{_sysconfdir}/genwqe_vpd.csv
%{_mandir}/man1/genwqe_csv2vpd.1.gz
%{_mandir}/man1/genwqe_vpdconv.1.gz
%{_mandir}/man1/genwqe_vpdupdate.1.gz
%{_mandir}/man1/genwqe_mt_perf.1.gz
%{_mandir}/man1/genwqe_test_gz.1.gz

%files devel
%defattr(-,root,root,-)
%dir %{_includedir}/genwqe
%{_includedir}/genwqe/*
%{_libdir}/genwqe/*.a

%changelog
