#
# spec file for package rzsz
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


%define realver 0.12.21rc
Name:           rzsz
Version:        0.12.21~rc
Release:        0
Summary:        X-, Y-, and Z-Modem Data Transfer Protocols
License:        GPL-2.0-or-later
Group:          Hardware/Modem
URL:            http://www.ohse.de/uwe/software/lrzsz.html
Source:         http://www.ohse.de/uwe/testing/lrzsz-%{realver}.tar.gz
Patch1:         lrzsz-po.patch
Patch2:         lrzsz-0.12.20-use-after-free.patch
Patch4:         lrzsz-autotools.patch
Patch5:         lrzsz-implicit-decl.patch
Patch6:         lrzsz-0.12.20-automake-1.12.patch
Patch7:         lrzsz-0.12.20-automake-1.13.patch
Patch8:         lrzsz-0.12.20-null-pointer.patch
# PATCH-FIX-UPSTREAM fix getopt optstring boo#1076576
Patch9:         lrzsz-0.12.20-fix-lsz-getopt.patch
Patch10:        lrzsz-0.12.21rc-drop-po-intl.patch
BuildRequires:  autoconf
BuildRequires:  automake
BuildRequires:  gettext-runtime
Provides:       lrzsz

%description
rzsz allows you to use "sz filename" to send a file to your local
system.

%prep
%autosetup -n lrzsz-%{realver} -p1

# Missing file
>> config.rpath
# Too old
rm -f missing
# Broken header
rm -f acconfig.h

%build
autoreconf -fvi
%configure
make %{?_smp_mflags}
# generate translation
msgfmt -o po/de.mo po/de.po

%install
%make_install

# install translation
mkdir -p "%{buildroot}/%{_datarootdir}/locale/de/LC_MESSAGES"
cp po/de.mo "%{buildroot}/%{_datarootdir}/locale/de/LC_MESSAGES/lrzsz.mo"
%find_lang lrzsz

# Fix various symlinks
for x in {r,s}{b,x,z} ; do
    pushd "%{buildroot}/%{_bindir}"
    ln -s l$x $x
    popd
    pushd "%{buildroot}/%{_mandir}/man1"
    ln -s l${x:0:1}z.1 ${x}.1
    popd
done

%check
%ifarch ppc64 s390x
make vcheck -j1 || echo "Warning: ignore ZMODEMtcp* tests failure for %{_arch}";
%else
make vcheck -j1
%endif

%files -f lrzsz.lang
%{_mandir}/man1/*
%license COPYING
%doc README.* ABOUT-NLS AUTHORS COMPATABILITY ChangeLog NEWS THANKS TODO
%{_bindir}/rb
%{_bindir}/rx
%{_bindir}/rz
%{_bindir}/sb
%{_bindir}/sx
%{_bindir}/sz
%{_bindir}/lrb
%{_bindir}/lrx
%{_bindir}/lrz
%{_bindir}/lsb
%{_bindir}/lsx
%{_bindir}/lsz

%changelog
