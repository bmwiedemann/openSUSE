#
# spec file for package mono-upnp
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


Name:           mono-upnp
Version:        0.1.2
Release:        0
Summary:        Client/server libraries for the Universal Plug 'n Play specifications
License:        MIT
Group:          Development/Languages/Mono
Url:            https://github.com/mono/mono-upnp
Source:         http://cloud.github.com/downloads/mono/mono-upnp/%{name}-%{version}.tar.gz
# PATCH-FIX-OPENSUSE mono-upnp-pkgconfig-mono-nunit.patch nmo.marques@gmail.com -- use mono-nunit for pkgconfig() calls
Patch0:         mono-upnp-pkgconfig-mono-nunit.patch
# PATCH-FIX-OPENSUSE -- disable unit tests as the nunit path is busted for Mono 3
Patch1:         mono-upnp-disable-unit-tests.Makefile.am.patch
Patch2:         mono-upnp-disable-unit-tests-configure.ac.patch
BuildArch:      noarch
BuildRoot:      %{_tmppath}/%{name}-%{version}-build
# -- Required for the patch
BuildRequires:  autoconf
BuildRequires:  automake
# -- normal dependencies
BuildRequires:  pkgconfig
BuildRequires:  pkgconfig(glade-sharp-2.0)
BuildRequires:  pkgconfig(glib-sharp-2.0)
BuildRequires:  pkgconfig(gtk-sharp-2.0)
BuildRequires:  pkgconfig(mono)
BuildRequires:  pkgconfig(mono-addins)
BuildRequires:  pkgconfig(mono-nunit)
BuildRequires:  pkgconfig(taglib-sharp)

%description
Mono.Upnp is a set of client/server libraries for the Universal Plug
'n Play specifications (see http://www.upnp.org).

%package devel
Summary:        Client/server libraries for the Universal PnP specification - development files
Group:          Development/Languages/Mono
Requires:       %{name} = %{version}
#Requires:       %{name}-tests = %{version}

%description devel
Mono.Upnp is a set of client/server libraries for the Universal Plug
'n Play specifications (see http://www.upnp.org).

This package provides the development files.

%prep
%setup -q
%patch0 -p1
%patch1
%patch2

%build
autoreconf -fi -I.
%configure \
   --libdir=%{_prefix}/lib
make %{?_smp_mflags}

%install
%makeinstall
# -- move pkgconfig files to %%_datadir
mkdir %{buildroot}%{_datadir}/pkgconfig -p
pushd %{buildroot}%{_prefix}/lib/pkgconfig
for i in `ls | grep \.pc`; do
   %{__install} -D -m 0644 $i %{buildroot}%{_datadir}/pkgconfig/$i
   %{__rm} $i
done
popd

%files
%defattr(-,root,root)
%doc AUTHORS COPYING README.md
%{_bindir}/mono-upnp-gtk
%{_bindir}/mono-upnp-simple-media-server
%{_prefix}/lib/mono-upnp/

%files devel
%defattr(-,root,root)
%{_datadir}/pkgconfig/*.pc

%changelog
