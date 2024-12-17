#
# spec file for package postfish
#
# Copyright (c) 2024 SUSE LLC
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


Name:           postfish
Version:        svn17492
Release:        0
Summary:        A digital audio post-processing tool
License:        GPL-2.0-or-later
Group:          Productivity/Multimedia/Sound/Editors and Convertors
URL:            https://trac.xiph.org/browser/trunk/postfish/
Source:         %{name}-%{version}.tar.bz2
Patch0:         happy-gcc43.diff
Patch1:         bnc_536201_fclose.patch
Patch2:         postfish-gtk2.19.7.patch
Patch3:         reproducible.patch
Patch4:         postfix-fix-proto.patch
BuildRoot:      %{_tmppath}/%{name}-%{version}-build
BuildRequires:  fftw3-devel
BuildRequires:  gtk2-devel
Requires:       fftw3
Requires:       gtk2
PreReq:         %install_info_prereq

%description
The Postfish is a digital audio post-processing, restoration, filtering
and mixdown tool. It works as a linear audio filter, much like a rack
of analog effects. The first stage of the filter pipeline provides a
bank of configurable per-channel processing filters for up to 32 input
channels. The second stage provides mixdown of the processed input
audio into a group of up to eight output channels. The third stage
applies processing filters to the output group post-mixdown.

%prep
%autosetup -p1

%build
%define archopt %{nil}
%ifarch ppc ppc64
%define archopt -maltivec
%endif
make CC="gcc %{archopt} $RPM_OPT_FLAGS"  ETCDIR=%{_datadir}/%{name}

%install
install -d -m 0755 $RPM_BUILD_ROOT/%{_bindir}
install -d -m 0755 $RPM_BUILD_ROOT/%{_mandir}/man1
install -d -m 0755 $RPM_BUILD_ROOT/%{_datadir}/%{name}
install -m 0755 postfish   $RPM_BUILD_ROOT/%{_bindir}
install -m 0644 postfish.1 $RPM_BUILD_ROOT/%{_mandir}/man1
install -m 0644 postfish-*rc $RPM_BUILD_ROOT/%{_datadir}/%{name}

%files
%defattr(-,root,root)
%doc README COPYING
%{_mandir}/man1/postfish.1.gz
%{_bindir}/*
%{_datadir}/postfish

%changelog
