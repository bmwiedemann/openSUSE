#
# spec file for package mono-zeroconf
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


Name:           mono-zeroconf
Summary:        A cross platform Zero Configuration Networking library for Mono
License:        MIT
Group:          Development/Languages/Mono
Url:            http://mono-project.com/Mono.Zeroconf
Version:        0.9.0
Release:        0
Source0:        %{name}-%{version}.tar.bz2
Patch0:         mono-search-path.patch
BuildArch:      noarch
BuildRoot:      %{_tmppath}/%{name}-%{version}-build
BuildRequires:  mono-devel
Requires:       mono-zeroconf-provider
%define assembly_version 4.0.0.90
## --- Build Configuration --- ##
%define build_avahi 1
%define build_mdnsr 1
%define build_docs 1
# openSUSE Configuration
%if 0%{?suse_version}
%if %{suse_version} >= 1030
%define build_avahi 1
%define build_mdnsr 0
%endif
%if %{suse_version} >= 1020 && %{suse_version} < 1030
%define build_avahi 1
%define build_mdnsr 1
%endif
%if %{suse_version} < 1020
%define build_avahi 0
%define build_mdnsr 1
%endif
%endif
# Fedora Configuration
%if 0%{?fedora_version}
%define env_options export MONO_SHARED_DIR=/tmp
%define build_docs 0
%define build_mdnsr 0
%define build_avahi 1
%endif
# Mandriva Configuration
%if 0%{?mandriva_version}
%define build_docs 0
%define build_avahi 1
%define build_mdnsr 0
%endif
%if 0%{?build_docs}
BuildRequires:  monodoc-core
%endif
## --- Base Package Information --- ##

%description
Mono.Zeroconf is a cross platform Zero Configuration Networking library
for Mono and .NET. It provides a unified API for performing the most
common zeroconf operations on a variety of platforms and subsystems:
all the operating systems supported by Mono and both the Avahi and
Bonjour/mDNSResponder transports.



Authors:
--------
    Aaron Bockover <abockover@novell.com>

%files
%defattr(-, root, root)
%doc AUTHORS COPYING ChangeLog NEWS README
%dir %_prefix/lib/mono-zeroconf
%dir %_prefix/lib/mono/mono-zeroconf
%dir %_prefix/lib/mono/gac/Mono.Zeroconf
%dir %_prefix/lib/mono/gac/Mono.Zeroconf/%{assembly_version}__e60c4f4a95e1099e
%dir %_prefix/lib/mono/gac/policy.1.0.Mono.Zeroconf
%dir %_prefix/lib/mono/gac/policy.1.0.Mono.Zeroconf/0.0.0.0__e60c4f4a95e1099e
%dir %_prefix/lib/mono/gac/policy.2.0.Mono.Zeroconf
%dir %_prefix/lib/mono/gac/policy.2.0.Mono.Zeroconf/0.0.0.0__e60c4f4a95e1099e
%dir %_prefix/lib/mono/gac/policy.3.0.Mono.Zeroconf
%dir %_prefix/lib/mono/gac/policy.3.0.Mono.Zeroconf/0.0.0.0__e60c4f4a95e1099e
%dir %_prefix/lib/mono/gac/policy.4.0.Mono.Zeroconf
%dir %_prefix/lib/mono/gac/policy.4.0.Mono.Zeroconf/0.0.0.0__e60c4f4a95e1099e
%_bindir/mzclient
%_prefix/lib/mono/gac/Mono.Zeroconf/*/*.dll*
%_prefix/lib/mono/gac/policy.1.0.Mono.Zeroconf/*/*
%_prefix/lib/mono/gac/policy.2.0.Mono.Zeroconf/*/*
%_prefix/lib/mono/gac/policy.3.0.Mono.Zeroconf/*/*
%_prefix/lib/mono/gac/policy.4.0.Mono.Zeroconf/*/*
%_prefix/lib/mono/mono-zeroconf/Mono.Zeroconf.dll*
%_prefix/lib/mono-zeroconf/MZClient.exe*
## --- mDNSResponder Provider --- ##
%if %{build_mdnsr} == 1

%package provider-mDNSResponder
Summary:        A cross platform Zero Configuration Networking library for Mono
Group:          Development/Languages/Mono
BuildRequires:  mDNSResponder-devel
Requires:       mDNSResponder
Provides:       mono-zeroconf-provider

%description provider-mDNSResponder
Mono.Zeroconf is a cross platform Zero Configuration Networking library
for Mono and .NET. It provides a unified API for performing the most
common zeroconf operations on a variety of platforms and subsystems:
all the operating systems supported by Mono and both the Avahi and
Bonjour/mDNSResponder transports.



Authors:
--------
    Aaron Bockover <abockover@novell.com>

%files provider-mDNSResponder
%defattr(-, root, root)
%dir %_prefix/lib/mono-zeroconf
%_prefix/lib/mono-zeroconf/Mono.Zeroconf.Providers.Bonjour.dll*
%endif
## --- Avahi Provider --- ##
%if %{build_avahi} == 1

%package provider-avahi
Summary:        A cross platform Zero Configuration Networking library for Mono
Group:          Development/Languages/Mono
Requires:       avahi
Provides:       mono-zeroconf-provider

%description provider-avahi
Mono.Zeroconf is a cross platform Zero Configuration Networking library
for Mono and .NET. It provides a unified API for performing the most
common zeroconf operations on a variety of platforms and subsystems:
all the operating systems supported by Mono and both the Avahi and
Bonjour/mDNSResponder transports.



Authors:
--------
    Aaron Bockover <abockover@novell.com>

%files provider-avahi
%defattr(-, root, root)
%dir %_prefix/lib/mono-zeroconf
%_prefix/lib/mono-zeroconf/Mono.Zeroconf.Providers.AvahiDBus.dll*
%endif
## --- Monodoc Developer API Documentation --- ##
%if %{build_docs} == 1

%package doc
Summary:        A cross platform Zero Configuration Networking library for Mono
Group:          Development/Languages/Mono

%description doc
Mono.Zeroconf is a cross platform Zero Configuration Networking library
for Mono and .NET. It provides a unified API for performing the most
common zeroconf operations on a variety of platforms and subsystems:
all the operating systems supported by Mono and both the Avahi and
Bonjour/mDNSResponder transports.



Authors:
--------
    Aaron Bockover <abockover@novell.com>

%files doc
%defattr(-, root, root)
%dir %_prefix/lib/monodoc/sources/
%_prefix/lib/monodoc/sources/mono-zeroconf-docs*
%endif
## --- Devel Package (pkg-config file) --- ##

%package devel
Summary:        A cross platform Zero Configuration Networking library for Mono
Group:          Development/Languages/Mono
Requires:       %{name} = %{version}

%description devel
Mono.Zeroconf is a cross platform Zero Configuration Networking library
for Mono and .NET. It provides a unified API for performing the most
common zeroconf operations on a variety of platforms and subsystems:
all the operating systems supported by Mono and both the Avahi and
Bonjour/mDNSResponder transports.



Authors:
--------
    Aaron Bockover <abockover@novell.com>

%files devel
%defattr(-, root, root)
%_prefix/share/pkgconfig/mono-zeroconf.pc
## --- Build/Install --- #

%prep
%setup -q
%define mcsver %({ mcs --version | awk '{print $5}' | cut -f1 -d"." ; mcs --version | awk '{print $5}' | cut -f2 -d"." ; } | xargs printf "%03d")
%if 0%{?mcsver} >= 4004
%patch0 -p1
%endif

%build
%{?env_options}
./configure --prefix=/usr \
%if %{build_docs} == 0
	--disable-docs \
%else
	--enable-docs \
%endif
%if %{build_avahi} == 0
	--disable-avahi \
%else
	--enable-avahi \
%endif
%if %{build_mdnsr} == 0
	--disable-mdnsresponder
%else
	--enable-mdnsresponder
%endif
make

%install
%{?env_options}
make install DESTDIR=$RPM_BUILD_ROOT
mkdir -p $RPM_BUILD_ROOT/usr/share/pkgconfig
mv $RPM_BUILD_ROOT/usr/lib/pkgconfig/* $RPM_BUILD_ROOT/usr/share/pkgconfig

%clean
rm -rf $RPM_BUILD_ROOT

%changelog
