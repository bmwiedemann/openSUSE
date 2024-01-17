#
# spec file for package fastjar
#
# Copyright (c) 2021 SUSE LLC
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


%{!?make_build:%global make_build make %{?_smp_mflags}}
Name:           fastjar
Version:        0.98
Release:        0
Summary:        Java package archiver
License:        GPL-2.0-or-later
Group:          Development/Languages/Java
URL:            https://savannah.nongnu.org/projects/fastjar/
Source0:        http://download.savannah.gnu.org/releases/%{name}/%{name}-%{version}.tar.gz
Patch2:         fix-update-mode.diff
# PATCH-FIX-UPSTREAM bsc#1188517 CVE-2010-2322 directory traversal vulnerabilities
Patch3:         fastjar-CVE-2010-2322.patch
BuildRequires:  zlib-devel
%if 0%{?suse_version}
Requires(post): %{install_info_prereq}
Requires(preun):%{install_info_prereq}
%endif

%description
Fastjar is an implementation of Sun's jar utility that comes with the
JDK, written entirely in C, and runs in a fraction of the time while
being 100% feature compatible.

%prep
%setup -q
%autopatch -p1

%build
%configure
%make_build

%install
%make_install

%post
%install_info --info-dir=%{_infodir} %{_infodir}/%{name}.info%{ext_info}

%preun
%install_info_delete --info-dir=%{_infodir} %{_infodir}/%{name}.info%{ext_info}

%files
%doc AUTHORS README NEWS ChangeLog
%{_mandir}/man1/fastjar.1%{?ext_man}
%{_mandir}/man1/grepjar.1%{?ext_man}
%{_infodir}/fastjar.info%{?ext_info}
%{_bindir}/fastjar
%{_bindir}/grepjar
%if ! 0%{?suse_version}
%exclude %{_infodir}/dir
%endif

%changelog
