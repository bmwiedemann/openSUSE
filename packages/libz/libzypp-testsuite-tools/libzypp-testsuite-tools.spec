#
# spec file for package libzypp-testsuite-tools
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


Name:           libzypp-testsuite-tools
BuildRequires:  fdupes
BuildRequires:  gcc-c++ >= 4.6
BuildRequires:  libexpat-devel
BuildRequires:  libtool
BuildRequires:  libzypp-devel >= 15.10.0
BuildRoot:      %{_tmppath}/%{name}-%{version}-build
Summary:        Package, Patch, Pattern, and Product Management - testsuite-tools
License:        GPL-2.0
Group:          System/Packages
Version:        5.0.3
Release:        0
Source:         zypp-testsuite-tools-5.0.3.tar.bz2

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
%setup -q -n zypp-testsuite-tools-5.0.3

%build
mv configure.ac x
grep -v devel/ x > configure.ac
autoreconf --force --install --symlink --verbose
%{?suse_update_config:%{suse_update_config -f}}
CXXFLAGS="$RPM_OPT_FLAGS" \
%configure --disable-static
make %{?jobs:-j %jobs}

%install
make install DESTDIR=$RPM_BUILD_ROOT
# legacy symlinks
ln -s deptestomatic $RPM_BUILD_ROOT/%{_prefix}/lib/zypp/testsuite/bin/deptestomatic.multi
ln -s deptestomatic $RPM_BUILD_ROOT/%{_prefix}/lib/zypp/testsuite/bin/deptestomatic.noui
%fdupes -s $RPM_BUILD_ROOT

%clean

%files
%defattr(0755,root,root)
%dir %{_prefix}/lib/zypp
%dir %{_prefix}/lib/zypp/testsuite/
%dir %{_prefix}/lib/zypp/testsuite/bin
%{_prefix}/lib/zypp/testsuite/bin/

%changelog
