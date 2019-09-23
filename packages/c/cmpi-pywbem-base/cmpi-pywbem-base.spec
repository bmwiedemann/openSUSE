#
# spec file for package cmpi-pywbem-base
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


Name:           cmpi-pywbem-base
Version:        0.2.0
Release:        0
Summary:        Base System Providers
License:        BSD-3-Clause
Group:          System/Management
Url:            http://omc-project.org
Source0:        %{name}-%{version}.tar.gz
BuildRequires:  cmpi-bindings-pywbem
BuildRequires:  cmpi-provider-register
BuildRequires:  python-devel
BuildRequires:  python-ply
BuildRequires:  python-six
BuildRequires:  python-xml
BuildRequires:  sblim-sfcb
Requires:       cim-server
Requires:       cmpi-bindings-pywbem
Requires:       python-pywbem
Requires(pre):  cmpi-provider-register
BuildRoot:      %{_tmppath}/%{name}-%{version}-build
%if 0%{?suse_version} > 1010
BuildRequires:  fdupes
BuildArch:      noarch
%endif
%if 0%{?fedora}
#!BuildIgnore: pywebm
%endif
%if 0%{?suse_version} < 1130
BuildRequires:  python-m2crypto
%else
BuildRequires:  python-M2Crypto
%endif

%description
Base System CIM Providers

%prep
%setup -q

%build
python setup.py build

%install
# http://lists.opensuse.org/opensuse-packaging/2007-02/msg00005.html
python setup.py install --prefix=%{_prefix} --root %{buildroot} \
        --install-lib=/usr/lib/pycim -O1
mkdir -p %{buildroot}%{_datadir}/mof/%{name}
install *.{mof,reg} %{buildroot}%{_datadir}/mof/%{name}/
%if 0%{?suse_version} > 1010
%fdupes %{buildroot}/%{_prefix}
%endif
# END OF INSTALL

%files
%defattr(-,root,root,-)
%dir /usr/lib/pycim
/usr/lib/pycim/*
%{_datadir}/mof/%{name}

%pre
if [ $1 -gt 1 ]; then
  %{_sbindir}/cmpi-provider-register -r -x -d %{_datadir}/mof/%{name}
fi

%post
%{_sbindir}/cmpi-provider-register -d %{_datadir}/mof/%{name}

%preun
if [ "$1" = "0" ] ; then
  %{_sbindir}/cmpi-provider-register -r -d %{_datadir}/mof/%{name}
fi

%changelog
