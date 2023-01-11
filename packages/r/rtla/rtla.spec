#
# spec file for package rtla
#
# Copyright (c) 2023 SUSE LLC
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


%define version %(rpm -q --qf '%%{VERSION}' kernel-source)

Name:           rtla
Version:        %{version}
Release:        0
Summary:        Real-Time Linux Analysis tools
License:        GPL-2.0-only
URL:            https://www.kernel.org/
BuildRequires:  kernel-source
BuildRequires:  libtraceevent-devel
BuildRequires:  libtracefs-devel
BuildRequires:  procps-devel
BuildRequires:  python3-docutils

%description
The rtla is a meta-tool that includes a set of commands that
aims to analyze the real-time properties of Linux. But, instead of
testing Linux as a black box, rtla leverages kernel tracing
capabilities to provide precise information about the properties
and root causes of unexpected results.

%package rebuild
Summary:        Empty package to ensure rebuilding rtla in OBS
%requires_eq kernel-source

%description rebuild
This is an empty package that ensures rtla is rebuilt every time
kernel-default is rebuilt in OBS.

There is no reason to install this package.

%prep
(cd %{_prefix}/src/linux ; tar -cf - COPYING CREDITS README tools include scripts Kbuild Makefile arch/*/{include,lib,Makefile} lib Documentation/tools/rtla) | tar -xf -
# Workaround for missing lib dependency
sed -i 's/--libs libtracefs/--libs libtracefs libtraceevent/' tools/tracing/rtla/Makefile

%build
cd tools/tracing/rtla
make %{?_smp_mflags}

%install
cd tools/tracing/rtla
make install DESTDIR=%{buildroot} STRIP=true

# Fixup symlinks as they are pointing to DESTDIR instead prefix
rm %{buildroot}%{_bindir}/osnoise
rm %{buildroot}%{_bindir}/timerlat
ln -sf %{_bindir}/rtla %{buildroot}%{_bindir}/osnoise
ln -sf %{_bindir}/rtla %{buildroot}%{_bindir}/timerlat

%files
%license COPYING
%doc CREDITS README
%{_mandir}/man1/rtla*.1*%{?ext_man}
%{_bindir}/rtla
%{_bindir}/osnoise
%{_bindir}/timerlat

%files rebuild
%license COPYING

%changelog
