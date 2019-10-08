#
# spec file for package xplatproviders
#
# Copyright (c) 2019 SUSE LINUX GmbH, Nuernberg, Germany.
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


Name:           xplatproviders
Version:        1.0.0
Release:        0
Summary:        Operations Manager Cross Platform Providers
License:        MS-PL
Group:          System/Management
Url:            http://scx.codeplex.com/
Source:         %{name}-%{version}.tar.gz
Patch1:         0001-Recognize-openSUSE.patch
Patch2:         0002-Fix-preprocessor-if-aix-if-defined-aix.patch
Patch3:         0003-dos2unix.patch
Patch4:         0004-Include-cstdio-for-EOF.patch
Patch5:         0005-Recognize-OBS-Open-Build-Service.patch
Patch6:         0006-Support-OBS-in-build-Makefile.pf.Linux.patch
Patch7:         0007-Compute-major.minor-os-version-inside-OBS.patch
Patch8:         0008-untab-indentation-for.patch
Patch9:         0009-Honor-DESTDIR-in-install.patch
Patch10:        0001-Get-release-string-and-version-right.patch
Patch11:        Consider-gcc-in-SUSE-and-REDHAT-can-handle-dynamic_c.patch
Patch12:        0003-Include-unistd.h.patch
Patch13:        0004-Remove-const-qualifier-from-functions-returning-inte.patch
Patch14:        0001-config.guess-SuSEconfig-is-gone-post-openSUSE-12.2.patch
Patch15:        xplatproviders-gcc48.patch
Patch16:        fix-gcc6.patch
Patch17:        reproducible.patch
Patch18:        configure-assume-host-SUSE-if-SUSE_VERSION-set.patch
Patch19:        drop-stropts.h-include.patch
BuildRequires:  gcc-c++
BuildRequires:  sblim-cmpi-devel
Requires(pre):  /bin/hostname
Requires(pre):  coreutils
Requires(pre):  grep
Requires(pre):  sed
BuildRoot:      %{_tmppath}/%{name}-%{version}-build
ExclusiveArch:  %{ix86} x86_64
%if 0%{?rhel_version} > 0
BuildRequires:  -vim
%endif
%if 0%{?suse_version} > 1010
BuildRequires:  fdupes
%endif

%description
System Center Cross Platform Solutions are open source add-ons for
System Center products to enable management of heterogeneous
enterprise infrastructures. Current solutions include support for UNIX
and Linux management through Operations Manager 2007 R2.

%prep
%setup -q
%patch1 -p1
%patch2 -p1
%patch3 -p1
%patch4 -p1
%patch5 -p1
%patch6 -p1
%patch7 -p1
%patch8 -p1
%patch9 -p1

%patch10 -p1
%patch11 -p1
%patch12 -p1
%patch13 -p1

%patch14 -p1
%patch15
%patch16 -p1
%patch17 -p1
%patch18 -p1
%patch19 -p1

%build
export CFLAGS="%{optflags}"
export CXXFLAGS="%{optflags}"
%if 0%{?suse_version}
  export SUSE_VERSION=0%{?suse_version}
%else
  %if 0%{?fedora_version}
    export FEDORA_VERSION=0%{?fedora_version}
  %endif
%endif
sh -x configure \
  --prefix=%{_libdir}/cmpi \
  --libdir=%{_libdir}/cmpi \
  --confdir=%{_sysconfdir} \
  --logdir=%{_localstatedir}/log \
  --rundir=%{_localstatedir}/run \
  --mofdir=%{_datadir}/mof \
  --with-cmpi-headers=%{_includedir}/cmpi
make %{?_smp_mflags}

%install
make %{?_smp_mflags} DESTDIR=%{buildroot} install
rm -f %{buildroot}%{_sysconfdir}/installinfo.txt

%files
%defattr(-,root,root)
%doc license.txt readme.txt xplatproviders.pdf
%{_libdir}/cmpi
%{_datadir}/mof
%config(noreplace) %{_sysconfdir}/*.conf

%changelog
