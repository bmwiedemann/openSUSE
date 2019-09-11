#
# spec file for package mono-uia
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


Name:           mono-uia
Version:        2.1
Release:        0
Url:            http://www.mono-project.com/Accessibility
Source0:        %{name}-%{version}.tar.bz2
# PATCH-FIX-UPSTREAM mono-uia-%{version}-mono-2.8.patch --fix building with mono 2.8 and later
Patch0:         mono-uia-%{version}-mono-2.8.patch
# PATCH-FIX-UPSTREAM 0001-UIAutomationClient-AutomationElement.FromLocalProvid.patch
Patch1:         0001-UIAutomationClient-AutomationElement.FromLocalProvid.patch
# PATCH-FIX-UPSTREAM  avoid_obsolete_security_requests --remove obsolets security requests
Patch2:         avoid_obsolete_security_requests
# PATCH-FIX-UPSTREAM use_net40dir_for_pcfile --use net40dir instead of net20dir
Patch3:         use_net40dir_for_pcfile
# PATCH-FIX-UPSTREAM use_specific_libX11_soname --soname the specific X11 library to avoid conflicts
Patch4:         use_specific_libX11_soname
Patch5:         dmcs_net40_build.patch
# use_net40dir_for_pcfile patch for use with mono 4.4 and newer
Patch6:         use_net40dir_for_pcfile_new
BuildRoot:      %{_tmppath}/%{name}-%{version}-build
Requires:       mono-core >= 2.4
Requires:       mono-winfxcore
BuildRequires:  autoconf
BuildRequires:  automake
BuildRequires:  gtk-sharp2 >= 2.12.8
BuildRequires:  mono-core >= 2.4
BuildRequires:  mono-devel >= 2.4
BuildRequires:  mono-nunit >= 2.4
Summary:        Implementations of members and interfaces based on MS UIA API
License:        MIT
Group:          System/Libraries

%description
User Interface Automation (UIA) is a new accessibility standard

%package devel
Summary:        Devel package for mono-uia
Group:          Development/Languages
Requires:       mono-uia == %{version}-%{release}

%description devel
Implementations of the members and interfaces based on MS UIA API

%prep
%setup -q
%patch0
%patch1 -p1
%patch2 -p1
%define mcsver %({ mcs --version | awk '{print $5}' | cut -f1 -d"." ; mcs --version | awk '{print $5}' | cut -f2 -d"." ; } | xargs printf "%03d")
%if 0%{?mcsver} >= 4004
%patch6 -p1
%else
%patch3 -p1
%endif
%patch4 -p1
%patch5 -p1

%build
autoreconf -fi -I .
%configure --disable-tests --enable-winfxcore
#Break build with parrallel make
make

%install
make DESTDIR=%{buildroot} install
rm %{buildroot}%{_prefix}/lib/mono/2.0/WindowsBase.dll
rm -r %{buildroot}%{_prefix}/lib/mono/gac/WindowsBase

%clean
rm -rf %{buildroot}

%files
%defattr(-,root,root)
%doc README COPYING NEWS
%{_prefix}/lib/mono/accessibility
%{_prefix}/lib/mono/gac/UIAutomationProvider
%{_prefix}/lib/mono/accessibility/UIAutomationProvider.dll
%{_prefix}/lib/mono/gac/UIAutomationTypes
%{_prefix}/lib/mono/accessibility/UIAutomationTypes.dll
%{_prefix}/lib/mono/gac/UIAutomationBridge
%{_prefix}/lib/mono/accessibility/UIAutomationBridge.dll
%{_prefix}/lib/mono/gac/UIAutomationClient
%{_prefix}/lib/mono/accessibility/UIAutomationClient.dll
%{_prefix}/lib/mono/gac/UIAutomationSource
%{_prefix}/lib/mono/accessibility/UIAutomationSource.dll

%files devel
%defattr(-,root,root,-)
%{_libdir}/pkgconfig/*.pc

%changelog
