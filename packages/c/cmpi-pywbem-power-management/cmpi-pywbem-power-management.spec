#
# spec file for package cmpi-pywbem-power-management
#
# Copyright (c) 2016 SUSE LINUX GmbH, Nuernberg, Germany.
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


Name:           cmpi-pywbem-power-management
BuildRequires:  cmpi-bindings-pywbem
BuildRequires:  cmpi-provider-register
BuildRequires:  cmpi-pywbem-base
%if 0%{?suse_version} < 1130
BuildRequires:  python-m2crypto
%else
BuildRequires:  python-M2Crypto
%endif
BuildRequires:  python-devel
BuildRequires:  python-ply
BuildRequires:  python-six
BuildRequires:  python-xml
BuildRequires:  sblim-sfcb
PreReq:         /usr/sbin/cmpi-provider-register
Version:        0.2.0
Release:        0
Summary:        Power Management Providers
License:        BSD-3-Clause
Group:          System/Management
Url:            http://omc-project.org
BuildArch:      noarch
Source0:        %{name}-%{version}.tar.gz
Requires:       cmpi-bindings-pywbem
Requires:       cmpi-pywbem-base
Requires:       python-pywbem
%if 0%{?fedora}
BuildRequires:  -pywbem
%endif
BuildRoot:      %{_tmppath}/%{name}-%{version}-build

%description
Power Management Providers based on DSP1027.



Authors:
--------
    Bart Whiteley

%prep
%setup  

%build
python setup.py build 

%install
# http://lists.opensuse.org/opensuse-packaging/2007-02/msg00005.html
%{__rm} -rf $RPM_BUILD_ROOT
%{__mkdir} $RPM_BUILD_ROOT
python setup.py install --prefix=%{_prefix} --root $RPM_BUILD_ROOT \
        --install-lib=/usr/lib/pycim -O1
%{__mkdir} -p $RPM_BUILD_ROOT/usr/share/mof/%{name}
install *.{mof,reg} $RPM_BUILD_ROOT/usr/share/mof/%{name}/
# END OF INSTALL

%clean
%{__rm} -rf $RPM_BUILD_ROOT

%files
%defattr(-,root,root,-)
/usr/lib/pycim/*
/usr/share/mof/%{name}

%pre
if [ $1 -gt 1 ]; then
  /usr/sbin/cmpi-provider-register -r -x -d /usr/share/mof/%{name}
fi
#if [ $1 -gt 1 ]; then
#  if [ -x /usr/bin/peg-loadmof.sh ]; then
#    peg-loadmof.sh -r -n root/PG_InterOp /usr/share/mof/%{name}/*.peg.reg
#    peg-loadmof.sh -r -n root/cimv2 /usr/share/mof/%{name}/*.mof
#  fi
#  if [ -x /usr/bin/sfcbrepos -a -d /var/lib/sfcb/stage ]; then
#    pushd /usr/share/mof/%{name}/
#    for i in *.mof; do
#      %{__rm} -f /var/lib/sfcb/stage/mofs/root/cimv2/$i
#    done
#    for i in *.sfcb.reg; do
#      %{__rm} /var/lib/sfcb/stage/regs/$i
#    done
#    popd
#    /usr/bin/sfcbrepos -f
#  fi
#fi

%post
/usr/sbin/cmpi-provider-register -d /usr/share/mof/%{name}
#if [ -x /usr/bin/peg-loadmof.sh ]; then
#  peg-loadmof.sh -n root/cimv2 /usr/share/mof/%{name}/*.mof
#  peg-loadmof.sh -n root/PG_InterOp /usr/share/mof/%{name}/*.peg.reg
#fi
#if [ -x /usr/bin/sfcbrepos -a -d /var/lib/sfcb/stage ]; then
#  mkdir -p /var/lib/sfcb/stage/mofs/root/cimv2/
#  ln -sf /usr/share/mof/%{name}/*.mof /var/lib/sfcb/stage/mofs/root/cimv2/
#  ln -sf /usr/share/mof/%{name}/*.sfcb.reg /var/lib/sfcb/stage/regs/
#  /usr/bin/sfcbrepos -f
#  /etc/init.d/sfcb condrestart
#fi 

%preun
if [ "$1" = "0" ] ; then 
  /usr/sbin/cmpi-provider-register -r -d /usr/share/mof/%{name}
fi
#if [ "$1" = "0" ] ; then 
#  if [ -x /usr/bin/peg-loadmof.sh ] ; then 
#	# last uninstall, not upgrade
#    peg-loadmof.sh -r -n root/PG_InterOp /usr/share/mof/%{name}/*.peg.reg
#    peg-loadmof.sh -r -n root/cimv2 /usr/share/mof/%{name}/*.mof
#  fi
#  if [ -x /usr/bin/sfcbrepos -a -d /var/lib/sfcb/stage ]; then
#    pushd /usr/share/mof/%{name}/
#    for i in *.mof; do
#      %{__rm} -f /var/lib/sfcb/stage/mofs/root/cimv2/$i
#    done
#    for i in *.sfcb.reg; do
#      %{__rm} /var/lib/sfcb/stage/regs/$i
#    done
#    popd
#    /usr/bin/sfcbrepos -f
#    /etc/init.d/sfcb condrestart
#  fi
#fi

%changelog
