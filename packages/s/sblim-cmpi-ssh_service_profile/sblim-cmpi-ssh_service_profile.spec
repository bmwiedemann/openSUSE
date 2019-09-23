#
# spec file for package sblim-cmpi-ssh_service_profile
#
# Copyright (c) 2013 SUSE LINUX Products GmbH, Nuernberg, Germany.
#
# All modifications and additions to the file contributed by third parties
# remain the property of their copyright owners, unless otherwise agreed
# upon. The license for this file, and modifications and additions to the
# file, is the same license as for the pristine package itself (unless the
# license for the pristine package is not an Open Source License, in which
# case the license is the MIT License). An "Open Source License" is a
# license that conforms to the Open Source Definition (Version 1.9)
# published by the Open Source Initiative.

# Please submit bugfixes or comments via http://bugs.opensuse.org/
#


Name:           sblim-cmpi-ssh_service_profile
BuildRequires:  gcc
BuildRequires:  gcc-c++
BuildRequires:  konkretcmpi-devel
BuildRequires:  libtool
BuildRequires:  sblim-cmpi-devel
BuildRequires:  sblim-cmpiutil-devel
BuildRequires:  sblim-sfcb
Url:            http://www.omc-project.org
# Increment the version every time the source code changes.
Version:        1.0.0
Release:        0
Summary:        Instrumentation for DMTF SSH Service Profile.
License:        EPL-1.0
Group:          System/Management
# This is necessary to build the RPM as a non-root user.
BuildRoot:      %{_tmppath}/%{name}-%{version}-build
# "yes" is the default, but we put it here explicitly to avoid someone
# setting it to "no"
Requires:       cim-schema >= 2.17
Requires:       sblim-cmpi-base
Requires:       sblim-sfcb
Source0:        sblim-cmpi-ssh_service_profile-%{version}.tar.gz
Patch1:         bnc530329-pclose.patch
%if 0%{?suse_version} >= 1210
BuildRequires:  systemd
%{?systemd_requires}
%endif

%description
Linux providers for instrumentation of DMTF SSH Service Profile (DSP
1017)



Authors:
--------
    Bart Whiteley
    Norm Paxton
    Mike Brasher

%prep
# Untar the sources.
%setup -n sblim-cmpi-ssh_service_profile-%{version}
%patch1 -p1

%build
# If the LD_RUN_PATH environment variable is set at link time,
# it's value is embedded in the resulting binary.  At run time,
# The binary will look here first for shared libraries.  This way
# we link against the libraries we want at run-time even if libs
# by the same name are in /usr/lib or some other path in /etc/ld.so.conf
autoreconf --force --install
CFLAGS="$RPM_OPT_FLAGS -fstack-protector" \
CXXFLAGS="$RPM_OPT_FLAGS -fstack-protector" \
%configure --disable-static --with-pic
%{__make}

%install
# Tell 'make install' to install into the BuildRoot
%makeinstall
find %{buildroot} -type f -name "*.la" -exec %{__rm} -fv {} +

%clean
rm -rf %{buildroot}

%pre
# If upgrading/not new install/not removing, deregister old version
if [ $1 -gt 1 ]
then
  sfcbunstage -n root/cimv2 -r linux-ssh-service-profile.reg linux-ssh-service-profile.mof
  sfcbunstage -n root/cimv2 linux-ssh-service-profile-interop.mof
  sfcbunstage -n root/interop linux-ssh-service-profile-interop.mof
  sfcbrepos -f
%if 0%{?suse_version} >= 1210
  systemctl condrestart sfcbd.service >/dev/null 2>&1 || :
%else
  /etc/init.d/sfcb condrestart
%endif
fi

%post
/sbin/ldconfig
sfcbstage -n root/cimv2 -r %{_datadir}/mof/%{name}/linux-ssh-service-profile.reg %{_datadir}/mof/%{name}/linux-ssh-service-profile.mof
sfcbstage -n root/cimv2 %{_datadir}/mof/%{name}/linux-ssh-service-profile-interop.mof
sfcbstage -n root/interop %{_datadir}/mof/%{name}/linux-ssh-service-profile-interop.mof
sfcbrepos -f
%if 0%{?suse_version} >= 1210
  systemctl condrestart sfcbd.service >/dev/null 2>&1 || :
%else
  /etc/init.d/sfcb condrestart
%endif

%preun
# If removing (not upgrading) then de-register, before the files are gone
if [ "x$1" = "x0" ]; then
  sfcbunstage -n root/cimv2 -r linux-ssh-service-profile.reg linux-ssh-service-profile.mof
  sfcbunstage -n root/cimv2 linux-ssh-service-profile-interop.mof
  sfcbunstage -n root/interop linux-ssh-service-profile-interop.mof
  sfcbrepos -f
%if 0%{?suse_version} >= 1210
  systemctl condrestart sfcbd.service >/dev/null 2>&1 || :
%else
  /etc/init.d/sfcb condrestart
%endif
fi

%postun -p /sbin/ldconfig

%files
%defattr(-,root,root)
%{_libdir}/cmpi/*.so*  
%dir %{_datadir}/mof/%{name}  
%{_datadir}/mof/%{name}/*  

%changelog
