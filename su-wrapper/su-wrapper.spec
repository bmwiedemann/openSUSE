#
# spec file for package su-wrapper
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


Name:           su-wrapper
Version:        1.2.0
Release:        0
Summary:        The su-wrapper Runs Programs as Another User and Group
License:        GPL-2.0-or-later
Group:          System/Base
PreReq:         permissions
Url:            https://github.com/metux/su-wrapper/commits/master
Source0:        su-wrapper-1.2.0.tar.bz2
Patch:          su-wrapper-1.2.0.dif
# PATCH-FIX-OPENSUSE su-wrapper-1.2.0-term.dif -- bnc#795063 - su-wrapper segfault if TERM variabile is not in environment
Patch1:         su-wrapper-1.2.0-term.dif
BuildRoot:      %{_tmppath}/%{name}-%{version}-build

%description
su-wrapper is a little utility that allows special users to execute
processes under another uid and gid.

It uses a table (/etc/su-wrapper.conf) to decide whatto do in certain
situation. Therefore it walks through the table and tries to match the
current situation (the later entries have precedence).

For more information, read /usr/share/doc/packages/su-wrapper/README.



Authors:
--------
    Enrico Weigelt <weigelt@nibiru.thur.de>
    Werner Fink <werner@suse.de>

%prep
%setup
%patch -p0
%patch1 -p0

%build
  pushd src
  make
  popd

%install
  pushd src
  mkdir -p %{buildroot}%{_sbindir}
  make install DESTDIR=%{buildroot}
  popd
  mkdir -p %{buildroot}%{_sysconfdir}
  install -m 0640 su-wrapper.conf.dist %{buildroot}%{_sysconfdir}/su-wrapper.conf

  file %{buildroot}%{_sbindir}/su-wrapper

%if %{defined verify_permissions}
%verifyscript
%verify_permissions -e %{_sbindir}/su-wrapper
%endif

%if %{defined set_permissions}
%post
%set_permissions %{_sbindir}/su-wrapper
%endif

%files
%defattr(-, root, root)
%doc doc/COPYING doc/README doc/TODO doc/VERSION
%config %{_sysconfdir}/su-wrapper.conf
%attr(00755,root,root) %verify(not mode) %{_sbindir}/su-wrapper

%changelog
