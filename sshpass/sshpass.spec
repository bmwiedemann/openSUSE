#
# spec file for package sshpass
#
# Copyright (c) 2016 SUSE LINUX GmbH, Nuernberg, Germany.
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


Name:           sshpass
Version:        1.06
Release:        0
Summary:        Non-interactive SSH authentication utility
License:        GPL-2.0+
Group:          System/Management
Url:            http://sshpass.sourceforge.net/
Source0:        http://downloads.sourceforge.net/sshpass/sshpass-%{version}.tar.gz
# PATCH-FIX-UPSTREAM -- http://sourceforge.net/p/sshpass/patches/5/
Patch0:         sshpass-1.05-f_option_check.patch
BuildRoot:      %{_tmppath}/%{name}-%{version}-build

%description
Tool for non-interactively performing password authentication with so called
"interactive keyboard password authentication" of SSH. Most users should use
more secure public key authentication of SSH instead.

%prep
%setup -q
%patch0 -p1

%build
%configure
make %{?_smp_mflags}

%install
make %{?_smp_mflags} DESTDIR=%{buildroot} install

%files
%defattr(-,root,root)
%{_bindir}/sshpass
%{_mandir}/man1/sshpass.1%{ext_man}
%doc AUTHORS COPYING ChangeLog NEWS

%changelog
