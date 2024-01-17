#
# spec file for package gnome-keyring-sharp
#
# Copyright (c) 2017 SUSE LINUX GmbH, Nuernberg, Germany.
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


Name:           gnome-keyring-sharp
Summary:        Managed Implementation of libgnome-keyring
License:        MIT
Group:          Development/Libraries/Other
Version:        1.0.2
Release:        0
BuildRoot:      %{_tmppath}/%{name}-%{version}-build
BuildRequires:  glib-sharp2
BuildRequires:  gnome-keyring-devel >= 2.30
BuildRequires:  libtool
BuildRequires:  mono-devel
Requires:       gnome-keyring >= 2.30
Source:         %{name}-%{version}.tar.bz2
Source99:       %{name}-rpmlintrc
Patch0:         pkgconfigdir.patch
Patch1:         add-delay-sign-attribute.patch
Patch2:         sign-delay-signed-assembly.patch

%description
When the gnome-keyring-daemon is running, you can use this to
retrieve/store confidential information such as passwords, notes or
network services user information.



%package devel
Requires:       %{name} = %{version} pkg-config
Summary:        Managed implementation of libgnome-keyring
Group:          Development/Libraries/Other

%description devel
When the gnome-keyring-daemon is running, you can use this to retrieve
and store confidential information such as passwords, notes or network
services user information.



%prep
%setup
%patch0
%patch1 -p1
%patch2 -p1

%build
autoreconf -f -i
%configure --disable-static
make %{?jobs:-j%jobs}

%install
make install DESTDIR="$RPM_BUILD_ROOT"
find %{buildroot} -type f -name "*.la" -exec %{__rm} -fv {} +
# mono 5.0 may create this stuff, we do not package it for now
rm -rf %{buildroot}%{_prefix}/%{_lib}/monodoc

%files
%defattr(-,root,root)
%{_libdir}/libgnome-keyring-sharp-glue.so
%dir %{_prefix}/lib/mono/gnome-keyring-sharp-1.0
%{_prefix}/lib/mono/gnome-keyring-sharp-1.0/Gnome.Keyring.dll
%{_prefix}/lib/mono/gac/Gnome.Keyring

%files devel
%defattr(-,root,root)
%{_datadir}/pkgconfig/gnome-keyring-sharp-1.0.pc

%changelog
