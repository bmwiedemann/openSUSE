#
# spec file for package barrel
#
# Copyright (c) 2021 SUSE LLC, Nuernberg, Germany.
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

Name:           barrel
Version:        0.0.5
Release:        0
BuildRoot:      %{_tmppath}/%{name}-%{version}-build
Source:         barrel-%{version}.tar.xz

%if 0%{?fedora_version}
BuildRequires:  boost-devel
BuildRequires:  json-c-devel
BuildRequires:  docbook-style-xsl
%else
BuildRequires:  libboost_headers-devel
BuildRequires:  libboost_test-devel
BuildRequires:  libjson-c-devel
BuildRequires:  docbook-xsl-stylesheets
%endif
BuildRequires:  libstorage-ng-devel >= 4.4.44
BuildRequires:  libtool
BuildRequires:  libxslt
BuildRequires:  readline-devel

Requires:       libstorage-ng1 >= 4.4.50

Summary:        Tool for storage management
Url:            http://github.com/aschnell/barrel
License:        GPL-2.0-only
Group:          System/Packages

%description
barrel is a command line tool for storage management.

%prep
%setup

%build
export CFLAGS="%{optflags} -DNDEBUG"
export CXXFLAGS="%{optflags} -DNDEBUG"

autoreconf -fvi
%configure \
    --docdir="%{_docdir}/%{name}"
make %{?_smp_mflags}

%check
make %{?_smp_mflags} check VERBOSE=1

%install
%make_install

%files
%defattr(-,root,root)
%{_sbindir}/barrel
%dir %{_sysconfdir}/barrel
%doc %dir %{_docdir}/%{name}
%doc %{_docdir}/%{name}/AUTHORS
%doc %{_mandir}/*/barrel.8*
%license %{_docdir}/%{name}/LICENSE

%changelog
