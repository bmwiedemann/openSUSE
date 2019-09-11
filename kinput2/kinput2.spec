#
# spec file for package kinput2
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


Name:           kinput2
Version:        v3.1
Release:        0
Summary:        Kanji Input Server for the X Window System
License:        HPND
Group:          System/I18n/Japanese
Url:            ftp://ftp.sra.co.jp/pub/x11/kinput2
Source:         ftp://ftp.sra.co.jp/pub/x11/kinput2/%{name}-v3.1.tar.bz2
Source10:       etc-x11-xim.d-kinput2-canna
Source11:       etc-x11-xim.d-kinput2-wnn
Patch0:         kinput2.app-defaults.patch
Patch1:         Kinput2.conf.patch
Patch2:         kinput2.man-page.patch
Patch3:         %{name}-v3.1-beta3.dif
Patch4:         %{name}-v3.1-beta3-java.dif
Patch5:         kinput2-v3.1-rootwindow-1.patch
Patch6:         reset_state.patch
Patch7:         kinput2-nonvoid.patch
Patch8:         64bit.patch
Patch9:         bugzilla-47203-keep-auxiliary-windows-on-top.patch
Patch10:        bugzilla-63978-hoge.patch
Patch11:        bugzilla-62553-spotlocation.patch
Patch12:        %{name}-%{version}-prototypes.patch
Patch13:        canna_c-warn.diff
Patch14:        bugzilla-137396-cannot-work-after-specific-function-calls.patch
Patch15:        bugzilla-368441-local-variable-used-before-set.patch
# PATCH-FIX-UPSTREAM getline() is a standard function in stdio.h
# rename to getLine
Patch16:        kinput2-v3.1-getline.patch
BuildRequires:  canna-devel
BuildRequires:  fwnn-devel
BuildRequires:  imake
BuildRequires:  pkgconfig(x11)
BuildRequires:  pkgconfig(xaw7)
BuildRequires:  pkgconfig(xmu)
BuildRequires:  pkgconfig(xt)
# Own /etc/X11/xim.d
BuildRequires:  x11-tools
BuildRoot:      %{_tmppath}/%{name}-%{version}-build

%description
Kinput2 is an input server for X Window System applications that
require Japanese text input.

%prep
%setup -n %{name}-v3.1
%patch0 -p1
%patch1 -p1
%patch2 -p1
%patch3 -p1
# doesn't help for this version of kinput2, Java problem still exists.
#%patch4 -p1
%patch5 -p1
%patch6 -p1
%patch7
%patch8 -p1
%patch9 -p1
%patch10 -p1
%patch11 -p1
%patch12 -p1
%patch13
%patch14 -p1
%patch15 -p1
%patch16 -p1
head -n 21 cmd/kinput2.c > Copyright

%build
xmkmf
make %{?_smp_mflags} Makefiles
make %{?_smp_mflags} depend
make %{?_smp_mflags} CCOPTIONS="%{optflags}"

%install
make DESTDIR=%{buildroot} install %{?_smp_mflags}
make install.man MANSUFFIX=1 LIBMANSUFFIX=3 DESTDIR=%{buildroot}
mkdir -p %{buildroot}%{_sysconfdir}/X11/xim.d/ja
install -m 644 %{SOURCE10} \
               %{buildroot}%{_sysconfdir}/X11/xim.d/kinput2-canna
install -m 644 %{SOURCE11} \
               %{buildroot}%{_sysconfdir}/X11/xim.d/kinput2-wnn
pushd  %{buildroot}%{_sysconfdir}/X11/xim.d/
    ln -s kinput2-canna kinput2
    pushd ja
        ln -s ../kinput2-canna 70-kinput2-canna
	ln -s ../kinput2-wnn   71-kinput2-wnn
    popd
popd

%files
%defattr(-, root, root)
%doc Copyright NEWS doc
%doc client/README
%config %{_sysconfdir}/X11/xim.d/*
%{_bindir}/*
%{_datadir}/X11/app-defaults
%doc %{_mandir}/*/*
%dir %{_libexecdir}/X11/ccdef/
%{_libexecdir}/X11/ccdef/*

%changelog
