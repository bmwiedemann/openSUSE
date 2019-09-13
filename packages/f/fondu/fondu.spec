#
# spec file for package fondu
#
# Copyright (c) 2011 SUSE LINUX Products GmbH, Nuernberg, Germany.
# Copyright (c) Peter Linnell, 2010 SUSE LINUX Products GmbH, Nuernberg, Germany.
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

Name:           fondu
Version:        1.0.060102
Release:        0
Summary:        Converts between mac and unix fonts
License:        BSD-3-Clause
Group:          System/X11/Fonts
Url:            http://fondu.sourceforge.net/

Source0:        http://fondu.sourceforge.net/fondu_src-060102.tgz
# PATCH-FIX-UPSTREAM fondu-flags.diff status=notsentyet
Patch1:         fondu-flags.diff
# PATCH-FIX-UPSTREAM fondu-shadow.diff status=notsentyet
Patch2:         fondu-shadow.diff
BuildRoot:      %{_tmppath}/%{name}-%{version}-build

%description
fondu allows you to convert a mac font into a unix one. ufond converts
a unix font into a mac one.

Author: George Williams <gww at silcom.com>

%prep
%setup -T -b 0 -n fondu-060102
%patch -P 1 -P 2 -p1

%build
%configure
make %{?_smp_mflags}

%install
mkdir -p %{buildroot}%{_bindir}
%makeinstall

%files
%defattr(-,root,root)
%{_bindir}/fondu
%{_bindir}/ufond
%{_bindir}/showfond
%{_bindir}/dfont2res
%{_bindir}/frombin
%{_bindir}/tobin
%{_bindir}/lumper
%{_bindir}/setfondname

%doc LICENSE README

%changelog
