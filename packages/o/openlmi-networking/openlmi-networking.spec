#
# spec file for package openlmi-networking
#
# Copyright (c) 2015 SUSE LINUX Products GmbH, Nuernberg, Germany.
# Copyright (c) 2013 Redhat, Inc
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


%global logfile %{_localstatedir}/log/openlmi-install.log

Name:           openlmi-networking
Version:        0.3.1
Release:        1%{?dist}
Summary:        CIM providers for network management
License:        LGPL-2.1+
Group:          System/Management

Url:            http://fedorahosted.org/openlmi/
Source0:        https://fedorahosted.org/released/openlmi-networking/%{name}-%{version}.tar.gz

# PATCH-FIX-OPENSUSE SUSE does not have libexec, kkaempf@suse.de
Patch2:         no-libexec-in-suse.patch

# PATCH-FIX-UPSTREAM cim-schema 2.40.0 adds new interfaces
Patch4:         AddIPProtocolEndpoint_RemoveIPProtocolEndpoint.patch 

# PATCH-FIX-OPENSUSE
Patch5:         0001-Adapt-to-new-NetworkManager-include-directory-layout.patch

# Upstream name has been changed from cura-networking to openlmi-networking
Provides:       cura-networking%{?_isa} = %{version}-%{release}
Obsoletes:      cura-networking < 0.0.5-1

BuildRequires:  check-devel
BuildRequires:  cim-schema
BuildRequires:  cmake
BuildRequires:  glib2-devel
BuildRequires:  konkretcmpi-devel
BuildRequires:  openlmi-providers-devel >= 0.5.0
BuildRequires:  sblim-cmpi-devel
%if 0%{?suse_version}
BuildRequires:  NetworkManager-devel
BuildRequires:  gcc-c++
%else
BuildRequires:  NetworkManager-glib-devel
%endif
BuildRequires:  libuuid-devel

# For openlmi-register-pegasus script
%if 0%{?suse_version}
Requires:       python
%else
Requires:       openlmi-pegasus-compat
Requires:       python2
%endif
# sblim-sfcb or tog-pegasus
Requires:       cim-server
# Require openlmi-providers because of registration scripts
Requires:       openlmi-providers >= 0.0.19
# For Linux_ComputerSystem class
Requires:       sblim-cmpi-base

%description
%{name} is set of CMPI providers for network management using
Common Information Model (CIM).

%prep
%setup -q
%if 0%{?suse_version}
%patch2 -p1
%endif
%patch4 -p1
%patch5 -p1

%build
%cmake
make %{?_smp_mflags}

%install
%if 0%{?suse_version}
make install/fast DESTDIR=$RPM_BUILD_ROOT -C build
mv $RPM_BUILD_ROOT%{_libexecdir}/pegasus/cmpiLMI_Networking-cimprovagt $RPM_BUILD_ROOT%{_datadir}/%{name}/cmpiLMI_Networking-cimprovagt
rm -rf $RPM_BUILD_ROOT%{_libexecdir}/pegasus
%else
make install/fast DESTDIR=$RPM_BUILD_ROOT 
%endif

%files
%defattr(-,root,root) 
%doc README COPYING
%{_libdir}/cmpi/libcmpiLMI_Networking.so
%dir %{_datadir}/%{name}
%{_datadir}/%{name}/60_LMI_Networking.mof
%{_datadir}/%{name}/70_LMI_NetworkingIndicationFilters.mof
%{_datadir}/%{name}/90_LMI_Networking_Profile.mof
%{_datadir}/%{name}/60_LMI_Networking.reg
%if 0%{?suse_version}
%{_datadir}/%{name}/cmpiLMI_Networking-cimprovagt
%else
%attr(755, root, root) %{_libexecdir}/pegasus/cmpiLMI_Networking-cimprovagt
%endif

%pre
# If upgrading, deregister old version
if [ "$1" -gt 1 ]; then
    # delete indication filters
    %{_bindir}/openlmi-mof-register --just-mofs -n root/interop unregister \
        %{_datadir}/%{name}/70_LMI_NetworkingIndicationFilters.mof || :;
    %{_bindir}/openlmi-mof-register --just-mofs -n root/interop unregister \
        %{_datadir}/%{name}/90_LMI_Networking_Profile.mof || :;
    %{_bindir}/openlmi-mof-register -v %{version} unregister \
        %{_datadir}/%{name}/60_LMI_Networking.mof \
        %{_datadir}/%{name}/60_LMI_Networking.reg || :;
fi >> %logfile 2>&1

%post
/sbin/ldconfig
%if 0%{?suse_version}
if [ -d %{_libexecdir}/pegasus ]; then
  mv %{_datadir}/%{name}/cmpiLMI_Networking-cimprovagt %{_libexecdir}/pegasus
fi
%endif
# Register Schema and Provider
if [ "$1" -ge 1 ]; then
    %{_bindir}/openlmi-mof-register -v %{version} register \
        %{_datadir}/%{name}/60_LMI_Networking.mof \
        %{_datadir}/%{name}/60_LMI_Networking.reg || :;
    # install indication filters
    %{_bindir}/openlmi-mof-register --just-mofs -n root/interop register \
        %{_datadir}/%{name}/70_LMI_NetworkingIndicationFilters.mof || :;
    %{_bindir}/openlmi-mof-register --just-mofs -n root/interop register \
        %{_datadir}/%{name}/90_LMI_Networking_Profile.mof || :;
fi >> %logfile 2>&1

%preun
# Deregister only if not upgrading
if [ "$1" -eq 0 ]; then
%if 0%{?suse_version}
    if [ -f %{_libexecdir}/pegasus/cmpiLMI_Networking-cimprovagt ]; then
      rm %{_libexecdir}/pegasus/cmpiLMI_Networking-cimprovagt
    fi
%endif
    # delete indication filters
    %{_bindir}/openlmi-mof-register --just-mofs -n root/interop unregister \
        %{_datadir}/%{name}/70_LMI_NetworkingIndicationFilters.mof || :;
    %{_bindir}/openlmi-mof-register --just-mofs -n root/interop unregister \
        %{_datadir}/%{name}/90_LMI_Networking_Profile.mof || :;
    %{_bindir}/openlmi-mof-register -v %{version} unregister \
        %{_datadir}/%{name}/60_LMI_Networking.mof \
        %{_datadir}/%{name}/60_LMI_Networking.reg || :;
fi >> %logfile 2>&1

%postun -p /sbin/ldconfig

%changelog
