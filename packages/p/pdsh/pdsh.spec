#
# spec file
#
# Copyright (c) 2023 SUSE LLC
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


#
%define slurm_version @BUILD_FLAVOR@%{nil}

%if "%slurm_version" != ""
%define _slurm_version _%{slurm_version}
%endif

%if 0%{!?sle_version:1} || 0%{?sle_version} >= 120200
%define have_munge 1
%define have_slurm 1
%define have_genders 1
%endif
%if 0%{?suse_version} >= 1550 || "%{?slurm_version}" != "18_08"
 %ifarch %ix86 %arm ppc s390
   %define have_slurm 0
 %endif
%endif

%if !0%{?have_slurm} && 0%{?_slurm_version:1}
ExclusiveArch:  do_not_build
%endif

%define pname pdsh
Name:           %{pname}%{?_slurm_version:_slurm%{?_slurm_version}}
BuildRequires:  dejagnu
BuildRequires:  openssh
BuildRequires:  readline-devel
%if 0%{?have_slurm}
BuildRequires:  slurm%{?_slurm_version}-devel
%endif
%if 0%{?have_munge}
BuildRequires:  munge-devel
%endif
BuildRequires:  pam-devel
Recommends:     mrsh
%if 0%{?have_genders}
BuildRequires:  genders-devel > 1.0
%endif
URL:            http://pdsh.googlecode.com/
Version:        2.34
Release:        0
Summary:        Parallel remote shell program
# git clone of https://code.google.com/p/pdsh/
License:        GPL-2.0-or-later
Group:          Productivity/Clustering/Computing
Source:         https://github.com/chaos/%{pname}/releases/download/%{pname}-%{version}/%{pname}-%{version}.tar.gz
Patch1:         slurm-add-C-features-constraint.patch
Patch2:         slurm-add-documentation-for-C.patch
Patch3:         hostlist-fix-use-of-strchr.patch
Patch4:         dshbak-fix-uninitialized-use-of-tag-on-empty-input.patch
Patch5:         Release-a-lock-that-is-no-longer-used-in-dsh.patch
Patch6:         fail-fast-on-ssh-errors-or-non-zero-return-code.patch
Patch7:         doc-fast-fail-update.patch

%description
Pdsh is a multithreaded remote shell client which executes commands on
multiple remote hosts in parallel.  Pdsh can use several different
remote shell services, including Kerberos IV and ssh.

%package -n     %{pname}-slurm%{?_slurm_version}
Summary:        SLURM plugin for pdsh
Group:          Productivity/Clustering/Computing
%{?_slurm_version:BuildRequires:  %pname}
Requires:       %pname = %{version}
Enhances:       slurm%{?_slurm_version}
%if 0%{?_slurm_version:1}
Provides:       %{pname}-slurm = %{version}
Conflicts:      %{pname}-slurm
%endif

%description -n %{pname}-slurm%{?_slurm_version}
Plugin for pdsh to determine nodes to run on by SLURM jobs or partitions.

%package genders
Summary:        Genders plugin for pdsh
Group:          Productivity/Clustering/Computing
Requires:       pdsh = %{version}
Conflicts:      pdsh-dshgroup
Conflicts:      pdsh-machines
Conflicts:      pdsh-netgroup

%description genders
Plugin for pdsh to determine nodes to run on by genders attributes.

%package machines
Summary:        Machines plugin for pdsh
Group:          Productivity/Clustering/Computing
Requires:       pdsh = %{version}
Conflicts:      pdsh-genders

%description machines
Plugin for pdsh to determine nodes to run on from machines file.

%package dshgroup
Summary:        Dsh plugin for pdsh
Group:          Productivity/Clustering/Computing
Requires:       pdsh = %{version}
Conflicts:      pdsh-genders
Conflicts:      pdsh-netgroup

%description dshgroup
Plugin for pdsh to determine nodes from dsh-style "group" files

%package netgroup
Summary:        Netgroup plugin for pdsh
Group:          Productivity/Clustering/Computing
Requires:       pdsh = %{version}
Conflicts:      pdsh-dshgroup
Conflicts:      pdsh-genders

%description netgroup
Plugin for pdsh to determine nodes to run on from netgroups.

%prep
%setup -q -n %{pname}-%{version}
%patch1 -p1
%patch2 -p1
%patch3 -p1
%patch4 -p1
%patch5 -p1
%patch6 -p1
%patch7 -p1

%build
export CFLAGS="%{optflags} -fno-strict-aliasing"
%configure \
%if 0%{?_slurm_version:1}
        --without-exec \
%else
	--with-readline \
	--with-machines=%{_sysconfdir}/pdsh/machines \
	--with-ssh \
	--with-dshgroups \
	--with-netgroup \
        --with-rcmd-rank-list="ssh %{?have_munge:mrsh} krb4 qsh mqsh exec xcpu" \
        --with-pam \
        %{?have_genders:--with-genders} \
        %{?have_munge:--with-mrsh} \
%endif
        %{?have_slurm:--with-slurm} \
	--without-rsh \
	--disable-static
%if 0%{!?make_build:1}
# accomodate < SLE-15
 %define make_build make %{?_smp_mflags}
%endif
%make_build

%install
%{?_slurm_version:cd src/modules}
%make_install
rm -f %buildroot/%{_libdir}/pdsh/*.la

%if !0%{?_slurm_version:1}
%check
make check

%files
%doc README DISCLAIMER.* README.* NEWS TODO
%license COPYING
%attr(755, root, root) %{_bindir}/pdsh
%attr(755, root, root) %{_bindir}/pdcp
%{_bindir}/dshbak
%{_bindir}/rpdcp
%{_mandir}/man1/pdsh.1.gz
%{_mandir}/man1/pdcp.1.gz
%{_mandir}/man1/dshbak.1.gz
%{_mandir}/man1/rpdcp.1.gz
%{_libdir}/pdsh
%{?have_genders:%exclude %{_libdir}/pdsh/genders.so}
%{?have_slurm:%exclude %{_libdir}/pdsh/slurm.so}
%exclude %{_libdir}/pdsh/machines.so
%exclude %{_libdir}/pdsh/dshgroup.so
%exclude %{_libdir}/pdsh/netgroup.so

%if 0%{?have_genders}
%files genders
%{_libdir}/pdsh/genders.so
%endif

%files machines
%{_libdir}/pdsh/machines.so

%files dshgroup
%{_libdir}/pdsh/dshgroup.so

%files netgroup
%{_libdir}/pdsh/netgroup.so
%endif # if _slurm_version

%if 0%{?have_slurm}
%files -n %{pname}-slurm%{?_slurm_version}
%{_libdir}/pdsh/slurm.so
%endif

%changelog
