#
# spec file for package xiterm
#
# Copyright (c) 2019 SUSE LINUX GmbH, Nuernberg, Germany.
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


%define	appdefdir  %{_datadir}/X11
%define xincludes  %{_prefix}/include
%define xlibraries %{_prefix}/%{_lib}
Name:           xiterm
Version:        0.5.20040304
Release:        0
Summary:        Internationalized Terminal Emulator for X11
License:        SUSE-CPL-0.5
Group:          System/X11/Terminals
# cvs -d:pserver:anonymous@www.openi18n.org:/cvsroot login (no password to login)
# cvs -d:pserver:anonymous@www.openi18n.org:/cvsroot co iterm
# tar jcvf iterm-0.5.20040304.tar.bz2 iterm
Source0:        iterm-0.5.20040304.tar.bz2
Source1:        fonts.tar.bz2
Patch0:         xiterm-fontset.patch
Patch1:         fbiterm-enhance.dif
Patch2:         intptr.patch
Patch3:         null-pointer.patch
Patch4:         enable-scrollbar.patch
Patch5:         fbiterm-exit-code.dif
Patch6:         fbiterm-devconsole.dif
Patch7:         fbiterm-combine-optimize.patch
Patch8:         xiterm-implicit-fortify-decl.patch
Patch9:         xiterm-asneeded-and-dso.patch
Patch10:        xiterm-automake-1.13.patch
Patch11:        implict-ptsname-decl.patch
Patch12:        stropts.patch
BuildRequires:  bdftopcf
BuildRequires:  fribidi-devel
BuildRequires:  gtk2-devel
BuildRequires:  libtool
BuildRequires:  ncurses-devel
BuildRequires:  pkgconfig
BuildRequires:  update-desktop-files
BuildRequires:  pkgconfig(x11)
BuildRequires:  pkgconfig(xaw7)
BuildRequires:  pkgconfig(xfont)
BuildRequires:  pkgconfig(xmu)
BuildRequires:  pkgconfig(xt)
Provides:       locale(xorg-x11:ja;ko;zh)
%if 0%{?suse_version} > 1130
BuildRequires:  utempter-devel
%else
BuildRequires:  utempter
%endif
%if 0%{?suse_version} >= 1330
Requires(pre):  group(tty)
%endif

%description
Internationalized Terminal Emulator for X11

%package -n fbiterm
Summary:        Internationalized Terminal Emulator for Framebuffers
Group:          System/X11/Terminals
Provides:       locale(ja;ko;zh)
%if 0%{?suse_version} >= 1330
Requires(pre):  group(tty)
%endif

%description -n fbiterm
An internationalized terminal emulator for framebuffers.

%package -n gtkiterm
Summary:        Internationalized Terminal Emulator for GTK
Group:          System/X11/Terminals
Provides:       locale(gtk2:ja;ko;zh)
%if 0%{?suse_version} >= 1330
Requires(pre):  group(tty)
%endif

%description -n gtkiterm
An internationalized terminal emulator for GTK.

%package -n libiterm1
Summary:        Internationalized Terminal Emulator Library
Group:          System/Libraries
# ncurses provides an alternative /usr/share/terminfo/i/iterm, the files conflict though
Conflicts:      terminfo-iterm
# O/P added in 12.3
Provides:       libiterm = %version-%release
Obsoletes:      libiterm < %version-%release

%description -n libiterm1
This is a portable library for internationalized terminal emulator. All
you need to make terminal emulator is to implements Callback functions,
like a drawing string on specific column and row, or set
fore/background color and so on.

%package -n libiterm-devel
Summary:        Header files and development libraries for libiterm
Group:          Development/Libraries/Other
Requires:       libiterm1 = %{version}

%description -n libiterm-devel
Header files and development libraries for libiterm

%package -n libXiterm1
Summary:        Terminal emulator Xaw widget library based on libiterm
Group:          System/Libraries
# O/P added in 12.3
Provides:       libXiterm = %version-%release
Obsoletes:      libXiterm < %version-%release

%description -n libXiterm1
Terminal emulator Xaw widget library based on libiterm

%package -n libXiterm-devel
Summary:        Header files and development libraries for libXiterm
Group:          Development/Libraries/Other
Requires:       libXiterm1 = %{version}

%description -n libXiterm-devel
Header files and development libraries for libXiterm

%prep
%setup -q -n iterm -a 1
%patch0 -p 1 -b .fontset
%patch1 -p 0
%patch2 -p 0 -b .intptr
%patch3 -p 1 -b .null-pointer
%patch4 -p 1 -b .enable-scrollbar
%patch5 -p 0 -b .exit-code
%patch6 -p 0
%patch7
%patch8
%patch9 -p1
%patch10 -p1
%patch11 -p1
%patch12 -p1
find . -name CVS -type d | xargs rm -rf
find . -name .cvsignore -type f | xargs rm -f
find . -type f | xargs chmod u+w
for i in INSTALL* README*
do
   mv $i $i.framework
done

%build
export CFLAGS="%{optflags}"
pushd lib
    autoreconf --force --install
%configure --with-pic --disable-static --x-includes=%{xincludes} \
		--x-libraries=%{xlibraries} \
		--with-utempter \
		--enable-fribidi
make %{?_smp_mflags}
popd
pushd unix/Xaw/lib
    autoreconf --force --install
%configure --with-pic --disable-static --x-includes=%{xincludes} \
		--x-libraries=%{xlibraries}
    make %{?_smp_mflags} 'INCLUDES=-I../../../lib/include -I../lib'
popd
pushd unix/Xaw/src
autoreconf --force --install
%configure --with-pic --disable-static --x-includes=%{xincludes} \
		--x-libraries=%{xlibraries}
    make %{?_smp_mflags} 'INCLUDES=-I../../../lib/include -I../lib' 'LDFLAGS=-L../../../lib/src/.libs -L../lib/.libs'
popd
pushd unix/fbiterm
    autoreconf --force --install
    export LIBS="-lfreetype -lm"
%configure --with-pic --disable-static \
		--x-includes=%{xincludes} \
		--x-libraries=%{xlibraries}
    make %{?_smp_mflags} 'INCLUDES=-I../../../lib/include' \
         'LDFLAGS=-L../../../lib/src/.libs'
popd
pushd unix/gtk
    make %{?_smp_mflags} CFLAGS="$CFLAGS -I../../../lib/include -L../../../lib/src/.libs"
popd

%install
pushd lib
   make DESTDIR=%{buildroot} install
popd
pushd unix/Xaw/lib
   make DESTDIR=%{buildroot} install
popd
pushd unix/Xaw/src
   make DESTDIR=%{buildroot} install
popd
pushd unix/fbiterm
   make DESTDIR=%{buildroot} install
popd
pushd unix/gtk
    install -m 755 src/gtkiterm %{buildroot}%{_prefix}/bin
popd
# install terminfo entry-description
mkdir -p %{buildroot}%{_datadir}/terminfo/i
tic -o %{buildroot}%{_datadir}/terminfo/ unix/terminfo/iterm.terminfo
mkdir -p %{buildroot}%{appdefdir}/{ja,ja_JP.UTF-8,}/app-defaults
install -m 644 unix/Xaw/src/XIterm %{buildroot}%{appdefdir}/app-defaults/XIterm
install -m 644 unix/Xaw/src/XIterm.ja %{buildroot}%{appdefdir}/ja/app-defaults/XIterm
iconv -f EUC-JP -t UTF-8 < unix/Xaw/src/XIterm.ja > unix/Xaw/src/XIterm.ja.UTF-8
install -m 644 unix/Xaw/src/XIterm.ja.UTF-8 %{buildroot}%{appdefdir}/ja_JP.UTF-8/app-defaults/XIterm
# install fallback fonts for fbiterm:
mkdir -p %{buildroot}%{_datadir}/fbiterm/fonts
pushd fonts
    for i in *.bdf
    do
	bdftopcf ${i} | gzip --no-name --best --stdout --force > %{buildroot}%{_datadir}/fbiterm/fonts/${i%.bdf}.pcf.gz
    done
popd
rm -f %{buildroot}%{_libdir}/*.la
chmod 0755 %{buildroot}/%{_bindir}/*

%post -n libiterm1 -p /sbin/ldconfig

%postun -n libiterm1 -p /sbin/ldconfig

%post -n libXiterm1 -p /sbin/ldconfig

%postun -n libXiterm1 -p /sbin/ldconfig

%files
%defattr(-, root, root)
%doc unix/Xaw/README* unix/Xaw/src/{COPYING,ChangeLog,INSTALL*}
%attr(-,root,tty) %{_bindir}/xiterm
%dir %{appdefdir}/app-defaults
%{appdefdir}/app-defaults/*
%dir %{appdefdir}/ja/
%dir %{appdefdir}/ja/app-defaults/
%dir %{appdefdir}/ja_JP.UTF-8/
%dir %{appdefdir}/ja_JP.UTF-8/app-defaults/
%{appdefdir}/*/app-defaults/*

%files -n fbiterm
%defattr(-, root, root)
%doc unix/fbiterm/{AUTHORS,COPYING,ChangeLog,INSTALL,NEWS,README*}
%attr(-,root,tty) %{_bindir}/fbiterm
%dir %{_datadir}/fbiterm/
%dir %{_datadir}/fbiterm/fonts
%{_datadir}/fbiterm/fonts/*

%files -n gtkiterm
%defattr(-, root, root)
%doc unix/gtk/README*
%attr(-,root,tty) %{_bindir}/gtkiterm

%files -n libiterm1
%defattr(-, root, root)
%{_libdir}/libiterm.so.1*
%{_datadir}/terminfo/i/iterm*

%files -n libiterm-devel
%defattr(-, root, root)
%doc README* INSTALL* RELNOTES* lib/{COPYING,README*,INSTALL*,ChangeLog} lib/docs/
%doc unix/terminfo/
%{_libdir}/libiterm.so
%{_includedir}/iterm/

%files -n libXiterm1
%defattr(-, root, root)
%{_libdir}/libXiterm.so.1*

%files -n libXiterm-devel
%defattr(-, root, root)
%doc unix/Xaw/lib/ChangeLog
%{_libdir}/libXiterm.so
%{_includedir}/Iterm*.h

%changelog
