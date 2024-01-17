#
# spec file for package libzypp-testsuite-tools
#
# Copyright (c) 2022 SUSE LLC
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


Name:           libzypp-testsuite-tools
Version:        5.0.5
Release:        0
License:        GPL-2.0-only
BuildRoot:      %{_tmppath}/%{name}-%{version}-build
Summary:        Package, Patch, Pattern, and Product Management - testsuite-tools
Group:          System/Packages
Source:         %{name}-%{version}.tar.bz2
BuildRequires:  cmake >= 3.1
BuildRequires:  gcc-c++ >= 7
BuildRequires:  libzypp-devel >= 17.25.3

%description
Package, Patch, Pattern, and Product Management - testsuite-tools

Authors:
--------
    Michael Andres <ma@suse.de>
    Jiri Srain <jsrain@suse.cz>
    Stefan Schubert <schubi@suse.de>
    Duncan Mac-Vicar <dmacvicar@suse.de>
    Klaus Kaempf <kkaempf@suse.de>
    Marius Tomaschewski <mt@suse.de>
    Stanislav Visnovsky <visnov@suse.cz>
    Ladislav Slezak <lslezak@suse.cz>

%prep
%setup -q

%build
mkdir -p build
cd build
CMAKE_FLAGS=
cmake $CMAKE_FLAGS \
      -DCMAKE_INSTALL_PREFIX=%{_prefix} \
      -DSYSCONFDIR=%{_sysconfdir} \
      -DMANDIR=%{_mandir} \
      -DCMAKE_VERBOSE_MAKEFILE=TRUE \
      -DCMAKE_C_FLAGS_RELEASE:STRING="$RPM_OPT_FLAGS" \
      -DCMAKE_CXX_FLAGS_RELEASE:STRING="$RPM_OPT_FLAGS" \
      -DCMAKE_BUILD_TYPE=Release \
      ..

%install
cd build
make install DESTDIR=$RPM_BUILD_ROOT
# legacy symlinks
ln -s deptestomatic $RPM_BUILD_ROOT/%{_prefix}/lib/zypp/testsuite/bin/deptestomatic.multi
ln -s deptestomatic $RPM_BUILD_ROOT/%{_prefix}/lib/zypp/testsuite/bin/deptestomatic.noui

%clean
rm -rf "$RPM_BUILD_ROOT"

%files
%defattr(0755,root,root)
%dir %{_prefix}/lib/zypp
%dir %{_prefix}/lib/zypp/testsuite/
%dir %{_prefix}/lib/zypp/testsuite/bin
%{_prefix}/lib/zypp/testsuite/bin/

%changelog
