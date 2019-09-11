#
# spec file for package mono-basic
#
# Copyright (c) 2018 SUSE LINUX GmbH, Nuernberg, Germany.
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


Name:           mono-basic
Version:        4.7
Release:        0
Summary:        Mono's Visual Basic Compiler and Runtime
License:        LGPL-2.1
Group:          Development/Languages/Mono
Url:            https://github.com/mono/mono-basic
Source:         http://download.mono-project.com/sources/%{name}/%{name}-%{version}.tar.bz2
# PATCH-FIX-OPENSUSE ignore incorrect surplus "/debug:portable" command line parameter when invoking vbnc, or set debug to "full" mode if this is the only "/debug" parameter at vbnc's cmdline
Patch2:         fix-vbnc-debug-portable-cmdline.patch
BuildRequires:  mono-devel
BuildRequires:  mono-winforms
BuildRequires:  unzip
BuildRoot:      %{_tmppath}/%{name}-%{version}-build
BuildArch:      noarch

%description
The Mono Project is an open development initiative that is working to
develop an open source, Unix version of the .NET development platform.
Its objective is to enable Unix developers to build and deploy
cross-platform .NET applications. The project will implement various
technologies that have been submitted to the ECMA for standardization.

Mono's VB runtime.

%prep
%setup -q
%patch2 -p1

%build
./configure --prefix=%{_prefix}
make %{?_smp_mflags}

%install
make DESTDIR=%{buildroot} install %{?_smp_mflags}
rm -f %{buildroot}%{_libexecdir}/mono/2.0/extract-source.exe*
rm -f %{buildroot}%{_libexecdir}/mono/2.0/rt-console.exe*
rm -f %{buildroot}%{_libexecdir}/mono/2.0/rt-execute.exe*
rm -f %{buildroot}%{_libexecdir}/mono/2.0/rt.exe*

%files
%defattr(-, root, root)
%{_mandir}/man1/vbnc.1*
%{_bindir}/vbnc*
%{_libexecdir}/mono/4.5/vbnc*
%{_libexecdir}/mono/*/Microsoft.VisualBasic.dll
%{_libexecdir}/mono/*/Mono.Cecil.VB*.dll
%{_libexecdir}/mono/gac/Microsoft.VisualBasic
%{_libexecdir}/mono/gac/Mono.Cecil.VB*

%changelog
