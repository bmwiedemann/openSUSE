#
# spec file for package opa-fm
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


%define git_ver .0.35.0.317bb9f13773

%define pseudo_opt %{_prefix}/lib/opa-fm
%define opasysconfdir %{_sysconfdir}/opa-fm/
%define opavarlibdir %{_localstatedir}/usr/lib/opa-fm/
Name:           opa-fm
Version:        10.10.1
Release:        0
Summary:        Intel Omni-Path Fabric Management Software
License:        BSD-3-Clause
Group:          Development/Libraries/C and C++
URL:            http://www.intel.com/
Source0:        %{name}-%{version}%{git_ver}.tar.gz
Source1:        %{name}-rpmlintrc
Patch1:         opa-fm-Fallback-to-custom-vendor-if-os_vendor-fails.patch
Patch2:         opa-fm-use-RPM_OPT_FLAGS.patch
Patch3:         opa-fm-force-code-symbols-to-be-loaded.patch
Patch4:         opa-fm-fix-multiple-definitions.patch
BuildRequires:  gcc-c++
BuildRequires:  infiniband-diags-devel
BuildRequires:  libexpat-devel
BuildRequires:  libopenssl-devel
BuildRequires:  ncurses-devel
BuildRequires:  rdma-core-devel
BuildRequires:  tcl-devel
BuildRequires:  zlib-devel
Requires:       infiniband-diags
Requires:       rdma >= 12
BuildRoot:      %{_tmppath}/%{name}-%{version}-build
#Currently ONLY builds on x86_64
ExclusiveArch:  x86_64

%description
The %{name} contains Intel Omni-Path fabric management applications. This
 includes: the Subnet Manager, Baseboard Manager, Performance Manager,
Fabric Executive, and some fabric management tools.

%prep
%setup -q -n  %{name}-%{version}%{git_ver}
%patch1
%patch2
%patch3
%patch4

%build
export RPM_OPT_FLAGS
if [ -d Esm ]; then
	cd Esm
fi
./fmbuild -r -C

%install
# directories
install -d -m0755 %{buildroot}%{opasysconfdir}

install -D -m 644 stage.rpm/opafm.service %{buildroot}%{_prefix}/lib/systemd/system/opafm.service
install -D -m 755 stage.rpm/opafmctrl %{buildroot}/%{pseudo_opt}/bin/opafmctrl
install -D -m 755 stage.rpm/opafmd %{buildroot}/%{pseudo_opt}/bin/opafmd

%if 0%{?rhel} && 0%{?rhel} < 7
install -D -m 755 stage.rpm/opafm %{buildroot}%{_sysconfdir}/init.d/opafm
%endif

install -D -m 644 stage.rpm/opafm.xml  %{buildroot}%{opasysconfdir}/opafm.xml
install -D stage.rpm/fm_capture %{buildroot}/%{pseudo_opt}/bin/fm_capture
install -D stage.rpm/fm_cmd %{buildroot}/%{pseudo_opt}/bin/fm_cmd
install -D stage.rpm/fm_cmdall %{buildroot}/%{pseudo_opt}/bin/fm_cmdall
install -D stage.rpm/smpoolsize %{buildroot}/%{pseudo_opt}/bin/smpoolsize

install -D stage.rpm/sm %{buildroot}/%{pseudo_opt}/runtime/sm
install -D stage.rpm/fe %{buildroot}/%{pseudo_opt}/runtime/fe

install -D stage.rpm/config_check %{buildroot}/%{pseudo_opt}/%{_sysconfdir}/config_check
install -D stage.rpm/config_convert %{buildroot}/%{pseudo_opt}/%{_sysconfdir}/config_convert
install -D stage.rpm/config_diff %{buildroot}/%{pseudo_opt}/%{_sysconfdir}/config_diff
install -D stage.rpm/config_generate %{buildroot}/%{pseudo_opt}/%{_sysconfdir}/config_generate
install -D stage.rpm/opafm %{buildroot}/%{pseudo_opt}/%{_sysconfdir}/opafm
if [ -d Esm ]; then
	sub_dir=Esm/
else
	sub_dir=
fi
install -D -m 644 ${sub_dir}ib/src/linux/startup/opafm_src.xml %{buildroot}/%{pseudo_opt}/%{_sysconfdir}/opafm_src.xml

install -D -m 644 stage.rpm/opafm.xml %{buildroot}/%{pseudo_opt}/%{_sysconfdir}/opafm.xml
install -D stage.rpm/opaxmlextract %{buildroot}/%{pseudo_opt}/%{_sysconfdir}/opaxmlextract
install -D stage.rpm/opaxmlfilter %{buildroot}/%{pseudo_opt}/%{_sysconfdir}/opaxmlfilter

mkdir -p %{buildroot}%{_sbindir}
mkdir -p %{buildroot}/opt
mkdir -p %{buildroot}%{opavarlibdir}
ln -s /%{pseudo_opt}/bin/fm_cmd %{buildroot}%{_sbindir}/opafmcmd
ln -s /%{pseudo_opt}/bin/fm_cmdall %{buildroot}%{_sbindir}/opafmcmdall
ln -s %{pseudo_opt} %{buildroot}/opt/
ln -s %{_sbindir}/service %{buildroot}%{_sbindir}/rcopafm

%pre
%service_add_pre opafm.service

%post
%service_add_post opafm.service

%preun
%service_del_preun opafm.service

%postun
%service_del_postun opafm.service

%files
%defattr(-,root,root,-)
%dir %{opasysconfdir}
%dir %{pseudo_opt}/
%dir %{pseudo_opt}/bin
%dir %{pseudo_opt}/etc
%dir %{pseudo_opt}/runtime
/opt/opa-fm
%config(noreplace) %{opasysconfdir}/opafm.xml

%doc README
%license LICENSE

%{_prefix}/lib/systemd/system/opafm.service
%{pseudo_opt}/bin/*
%{pseudo_opt}%{_sysconfdir}/*
%{pseudo_opt}/runtime/*
%{_sbindir}/opafmcmd
%{_sbindir}/opafmcmdall
%{_sbindir}/rcopafm

%changelog
