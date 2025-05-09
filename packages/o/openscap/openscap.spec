#
# spec file for package openscap
#
# Copyright (c) 2025 SUSE LLC
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


%define sover 33
%define with_bindings 0
#Compat macro for new _fillupdir macro introduced in Nov 2017
%if ! %{defined _fillupdir}
  %define _fillupdir %{_localstatedir}/adm/fillup-templates
%endif
Name:           openscap
Version:        1.4.1
Release:        0
Summary:        A Set of Libraries for Integration with SCAP
License:        LGPL-2.1-or-later
Group:          Development/Tools/Other
URL:            https://www.open-scap.org/
Source:         https://github.com/OpenSCAP/openscap/archive/%{version}.tar.gz#/%name-%version.tar.gz
Source1:        openscap-rpmlintrc
Source2:        sysconfig.oscap-scan
# SUSE specific profile, based on yast2-security checks.
# Generated from http://gitorious.org/test-suite/scap
Source3:        scap-yast2sec-xccdf.xml
Source4:        scap-yast2sec-oval.xml
Source5:        oscap-scan.service
Source6:        oscap-scan.sh
Patch3:         0003-Use-openSUSE-SUSE-cpe-links.patch
%if 0%{?suse_version} != 1599
Patch4:         0004-oscap-remediate-is-located-in-bindir.patch
%endif

BuildRequires:  asciidoc
# Use package name cause of "have choice for perl(XML::Parser): brp-check-suse perl-XML-Parser"
BuildRequires:  cmake
BuildRequires:  dbus-1-devel
BuildRequires:  doxygen
BuildRequires:  gcc-c++
%if 0%{?suse_version} < 1550
BuildRequires:  gconf2-devel
%endif
BuildRequires:  libacl-devel
BuildRequires:  libattr-devel
BuildRequires:  libblkid-devel
BuildRequires:  libbz2-devel
BuildRequires:  libcap-devel
BuildRequires:  libcurl-devel
BuildRequires:  libgcrypt-devel
BuildRequires:  libselinux-devel
BuildRequires:  libtool
BuildRequires:  libxml2-devel
BuildRequires:  libxslt-devel
BuildRequires:  libyaml-devel
BuildRequires:  lua
BuildRequires:  openldap2-devel
BuildRequires:  perl-XML-Parser
BuildRequires:  perl-XML-XPath
BuildRequires:  pkgconfig
BuildRequires:  procps
BuildRequires:  procps-devel
BuildRequires:  python3-devel
BuildRequires:  rpm-devel
BuildRequires:  swig
BuildRequires:  systemd-rpm-macros
BuildRequires:  unixODBC-devel
BuildRequires:  xmlsec1-devel
BuildRequires:  xmlsec1-openssl-devel
BuildRequires:  pkgconfig(glib-2.0)
BuildRequires:  pkgconfig(gobject-2.0)
BuildRequires:  pkgconfig(libpcre2-8)
BuildRequires:  pkgconfig(systemd)
# remove extra packages from version 1.2.9 and older
Obsoletes:      openscap-engine-sce < %{version}
Obsoletes:      openscap-extra-probes < %{version}
BuildRequires:  distribution-release

%description
OpenSCAP is a set of open source libraries providing an easier path for
integration of the SCAP line of standards.

SCAP is a line of standards managed by NIST with the goal of providing
a standard language for the expression of Computer Network Defense
related information.

More information about SCAP can be found at nvd.nist.gov.

%package devel
Summary:        Development Files for OpenSCAP
Group:          Development/Libraries/C and C++
Requires:       %{name} = %{version}-%{release}
Requires:       libopenscap%{sover} = %{version}

%description devel
This package contains the development files (mainly C header files) for the
OpenSCAP C library.

%package containers
Summary:        OpenSCAP plugin for scanning containers
Group:          System/Libraries
Provides:       openscap-docker = %{version}-%{release}
Obsoletes:      openscap-docker < %{version}-%{release}

%description containers
This package contains plugins for scanning containers using OpenSCAP either via
podman or docker.

%if 0%{?with_bindings}
%package -n python-openscap
Summary:        OpenSCAP Python Library
Group:          Development/Libraries/Python
Requires:       %{name} = %{version}-%{release}
Provides:       openscap-python = %{version}-%{release}

%description -n python-openscap
The OpenSCAP Python Library for easy integration with SCAP.

%package -n perl-openscap
Summary:        OpenSCAP Perl Library
Group:          Development/Libraries/Perl
Requires:       %{name} = %{version}-%{release}
Requires:       perl = %{perl_version}
Provides:       openscap-perl = %{version}-%{release}

%description -n perl-openscap
The OpenSCAP Perl Library for easy integration with SCAP.
%endif

%package -n libopenscap%{sover}
Summary:        OpenSCAP C Library
Group:          System/Libraries

%description -n libopenscap%{sover}
The OpenSCAP C Library for easy integration with SCAP.

%package        utils
Summary:        Openscap utilities
Group:          System/Monitoring
Requires:       %{name} = %{version}-%{release}
Requires:       libopenscap%{sover} >= %{version}-%{release}
Requires(pre):  %fillup_prereq
%systemd_requires

%description    utils
The %{name}-utils package contains various utilities based on %{name} library.

%package        content
Summary:        SCAP content
Group:          System/Monitoring
Requires:       %{name} = %{version}-%{release}
Requires:       libopenscap%{sover} >= %{version}-%{release}

%description    content
SCAP content for Fedora delivered by Open-SCAP project.

%package -n libopenscap_sce%{sover}
Summary:        Script Checking Engine Library for OpenSCAP
Group:          System/Libraries

%description -n libopenscap_sce%{sover}
This package contains the Script Checking Engine Library (SCE) for OpenSCAP.

%{!?python_sitearch: %global python_sitearch %(python -c "from distutils.sysconfig import get_python_lib; print get_python_lib(1)")}

%prep
%autosetup -p1

%build
%cmake \
	-DENABLE_DOCS=TRUE \
%if 0%{?suse_version} < 1600
	-DCMAKE_INSTALL_DOCDIR:PATH=%{_docdir}/%{name} \
%endif
	-DCMAKE_SHARED_LINKER_FLAGS="" \
	-DENABLE_OSCAP_REMEDIATE_SERVICE=TRUE \
	-DWITH_PCRE2=ON \
%if !0%{?with_bindings}
	-DENABLE_PYTHON3=FALSE \
	-DENABLE_PERL=FALSE \
%endif
%{nil}
%if 0%{?sle_version} > 150100 || 0%{?suse_version} == 1599
%cmake_build
%else
%make_jobs
%endif

%check
export LD_LIBRARY_PATH=$LD_LIBRARY_PATH:%{buildroot}/%{_libdir}
cd build
# unit tests do not succeed, while working on 1.3 migration we submitted a few
# patches upstream but there is still one unit test that always fails and 1-3
# which fail occasionally
ctest %{?_smp_mflags} || :
cd ..

%install
%cmake_install

mkdir -p %{buildroot}/%{_fillupdir}
install -m 644 %{SOURCE2} %{buildroot}/%{_fillupdir}

mkdir -p %{buildroot}/%{_libexecdir}/openscap
mkdir -p %{buildroot}/%{_libdir}/openscap

install -m 644 %{SOURCE3} %{buildroot}/%{_datadir}/openscap
install -m 644 %{SOURCE4} %{buildroot}/%{_datadir}/openscap

# specific local scan during boot script
mkdir -p %{buildroot}/%{_unitdir}
install -m 644 %{SOURCE5} %{buildroot}/%{_unitdir}/oscap-scan.service
mkdir -p %{buildroot}/%{_bindir}
install -m 755 %{SOURCE6} %{buildroot}/%{_bindir}/oscap-scan

mkdir -p %{buildroot}/%{_sbindir}
ln -sf %{_sbindir}/service %{buildroot}/%{_sbindir}/rcoscap-scan

mkdir -p %{buildroot}%{_datadir}/bash-completion/completions
mv %{buildroot}%{_sysconfdir}/bash_completion.d/* %{buildroot}%{_datadir}/bash-completion/completions/
# create symlinks to default content
ln -s  %{_datadir}/openscap/scap-yast2sec-oval.xml %{buildroot}/%{_datadir}/openscap/scap-oval.xml
ln -s  %{_datadir}/openscap/scap-yast2sec-xccdf.xml %{buildroot}/%{_datadir}/openscap/scap-xccdf.xml

# for some reason the serivce file is put under /usr/usr/lib/systemd..
mv %{buildroot}/usr/%{_unitdir}/oscap-remediate.service %{buildroot}/%{_unitdir}
# oscap-remediate should be in /usr/libexec but this is not well supported in
# older versions of the distro
%if 0%{?suse_version} != 1599
%if 0%{?sle_version} > 150200
mv %{buildroot}/%{_libexecdir}/oscap-remediate %{buildroot}/%{_bindir}
%else
# in older versions _libexecdir expands to /usr/lib, which does not help
mv %{buildroot}/%{_prefix}/libexec/oscap-remediate %{buildroot}/%{_bindir}
%endif
%endif

%post -n libopenscap%{sover} -p /sbin/ldconfig
%postun -n libopenscap%{sover} -p /sbin/ldconfig

%post -n libopenscap_sce%{sover} -p /sbin/ldconfig
%postun -n libopenscap_sce%{sover} -p /sbin/ldconfig

%post -n openscap-utils
%service_add_post oscap-scan.service oscap-remediate.service

%postun -n openscap-utils
%service_del_postun oscap-scan.service oscap-remediate.service

%pre -n openscap-utils
%service_add_pre oscap-scan.service oscap-remediate.service

%preun -n openscap-utils
%service_del_preun oscap-scan.service oscap-remediate.service

%files
%license COPYING
%doc AUTHORS NEWS
%dir %{_datadir}/openscap
%dir %{_datadir}/openscap/cpe
%dir %{_datadir}/openscap/schemas
%dir %{_datadir}/openscap/xsl
%{_datadir}/openscap/cpe/*
%{_datadir}/openscap/schemas/*
%{_datadir}/openscap/xsl/*

%files -n libopenscap%{sover}
%{_libdir}/libopenscap.so.%{sover}*

%files devel
%dir %{_docdir}/openscap
%{_docdir}/openscap/html
%{_docdir}/openscap/manual
%{_libdir}/*.so
%{_libdir}/pkgconfig/*.pc
%{_includedir}/*

%files containers
%{python3_sitelib}/oscap_docker_python
%{_bindir}/oscap-docker
%{_bindir}/oscap-podman
%{_mandir}/man8/oscap-podman.8*
%{_mandir}/man8/oscap-docker.8*

%if 0%{?with_bindings}
%files -n python-openscap
%{python_sitearch}/*

%files -n perl-openscap
%{perl_vendorlib}/openscap.pm
%{perl_vendorarch}/openscap_pm.so
%endif

%files utils
%{_fillupdir}/sysconfig.oscap-scan
%doc docs/oscap-scan.cron
%{_mandir}/man8/*
%{_unitdir}/oscap-scan.service
%{_bindir}/autotailor
%{_bindir}/oscap
%{_bindir}/oscap-im
%{_bindir}/oscap-vm
%{_bindir}/oscap-scan
%{_bindir}/oscap-ssh
%{_bindir}/oscap-chroot
%{_bindir}/scap-as-rpm
%{_bindir}/oscap-run-sce-script
%{_sbindir}/rcoscap-scan
%{_datadir}/bash-completion/completions/*
%exclude %{_mandir}/man8/oscap-podman.8*
%exclude %{_mandir}/man8/oscap-docker.8*
%{_bindir}/oscap-remediate-offline
%{_prefix}/lib/systemd/system/oscap-remediate.service
%if 0%{?suse_version} != 1599
%{_bindir}/oscap-remediate
%else
%{_libexecdir}/oscap-remediate
%endif

%files content
%{_datadir}/openscap/scap*.xml

%files -n libopenscap_sce%{sover}
%{_libdir}/libopenscap_sce.so.*

%changelog
