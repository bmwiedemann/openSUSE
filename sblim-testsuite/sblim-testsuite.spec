#
# spec file for package sblim-testsuite
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


Name:           sblim-testsuite
BuildRequires:  automake
BuildRequires:  sblim-wbemcli
Version:        1.3.0
Release:        0
BuildRoot:      %{_tmppath}/%{name}-%{version}-build
Requires:       sblim-wbemcli
BuildArch:      noarch
Url:            http://sblim.wiki.sourceforge.net/
Source0:        http://prdownloads.sourceforge.net/sblim/%{name}-%{version}.tar.bz2
Patch0:         %{name}-1.3.0-fix-bashisms.patch
Summary:        SBLIM Testsuite
License:        EPL-1.0
Group:          Development/Tools/Other

%description
Standards Based Linux Instrumentation Base Providers Test Suite



Authors:
--------
    SBLIM Project

%prep
%setup
%patch0 -p1

%build
%configure
make

%install
[ "$RPM_BUILD_ROOT" != "/" ] && rm -rf $RPM_BUILD_ROOT
%if 0%{?suse_version}
%makeinstall docdir=%{_docdir}/%{name}
%else
make DESTDIR=$RPM_BUILD_ROOT install
%endif

%files
%defattr(-,root,root) 
%if 0%{?fedora_version} || 0%{?centos_version} || 0%{?rhel_version} || 0%{?fedora} || 0%{?rhel}
%doc %{_datadir}/doc/%{name}-%{version}
%else
%doc %{_docdir}/%{name}
%endif
%{_datadir}/%{name}
%{_localstatedir}/lib/%{name}

%changelog
