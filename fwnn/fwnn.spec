#
# spec file for package fwnn
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

# Please submit bugfixes or comments via http://bugs.opensuse.org/
#


%define base_version 1.1.1
%define alpha_version a023.1
Name:           fwnn
Version:        1.1.1a023.1
Release:        0
Summary:        FreeWnn Japanese Input System--Server Only
License:        GPL-2.0-or-later
Group:          System/I18n/Japanese
Url:            http://freewnn.sourceforge.jp/
# Upstream hasn't released tarball yet.
# I entered the following commands.
# cvs -d :pserver:anonymous@cvs.osdn.net:/cvsroot/freewnn export -r freewnn-1-1-1-a023-1 -d FreeWnn-1.1.1-a023.1 FreeWnn
# tar --xz -cf FreeWnn-1.1.1-a023.1.tar.xz FreeWnn-1.1.1-a023.1
Source:         FreeWnn-%{base_version}-%{alpha_version}.tar.xz
Source1:        FreeWnn-%{base_version}-%{alpha_version}.tar.xz.asc
Source2:        %{name}.keyring
Source5:        fwnn.service
Source6:        fcwnn.service
Source7:        fkwnn.service
Source8:        ftwnn.service
Source99:       fwnn-rpmlintrc
Patch0:         FreeWnn-fsstnd.patch
Patch1:         FreeWnn-ja.patch
# PATCH-FIX-UPSTREAM don't install as wnn user and don't setuid/setgid
Patch2:         FreeWnn-noroot.patch
Patch7:         FreeWnn-s390x.patch
Patch8:         FreeWnn-warnings.patch
BuildRequires:  fdupes
BuildRequires:  ncurses-devel
BuildRequires:  tcpd-devel
Requires:       fwnncom = %{version}
# %%{_sbindir}/useradd
Requires(pre):	shadow
Conflicts:      wnn6
BuildRoot:      %{_tmppath}/%{name}-%{version}-build

%description
FreeWnn is a Kana-Kanji translation system intended as a system
powerful enough to translate entire sentences at once.

Wnn works in a client/server manner. The server portion of Wnn, or
jserver, is used as a Kana-Kanji translation engine for clients like
"xwnmo" and "kinput2" (input systems for the X Window System) or for
clients like "Egg", which are part of Mule (MUlti-Lingual Emacs) and
XEmacs.

This package contains only the Japanese server.

%package -n libjd0
Summary:        FreeWnn Japanese Input System library
Group:          System/Libraries

%description -n libjd0
This subpackage contains a core library of the Wnn input system.

%package -n libwnn0
Summary:        FreeWnn Input System library
Group:          System/Libraries

%description -n libwnn0
This subpackage contains a core library of the Wnn input system.

%package -n fwnn-devel
Summary:        Development Library and Header Files for FreeWnn
Group:          Development/Libraries/C and C++
Requires:       fcwnn-devel = %{version}
Requires:       fwnn = %{version}
Requires:       libjd0 = %{version}
Requires:       libwnn0 = %{version}
Provides:       fwnndev = %{version}
Obsoletes:      fwnndev < %{version}

%description -n fwnn-devel
This package contains the header files and libraries for building
client programs which use FreeWnn for Japanese input.

%package -n fwnncom
Summary:        Common Files for FreeWnn
Group:          System/I18n/Japanese
Requires(pre):         shadow

%description -n fwnncom
This package includes files you need to run FreeWnn, Free cWnn, Free
tWnn, or Free kWnn.  Install this package if you will be using any part
of the Wnn System.

%package -n fcwnn
Summary:        Free cWnn Chinese Input System (Mainland China)
Group:          System/I18n/Chinese
Requires:       fcwnncom = %{version}
Requires:       fkwnn = %{version}
Requires:       fwnn = %{version}
Requires(pre):	shadow
Requires(post):	fcwnncom

%description -n fcwnn
Free cWnn Chinese Input System (mainland China).

%package -n fcwnncom
Summary:        Free cWnn/tWnn Chinese Input System Common Files (Mainland and Taiwan)
Group:          System/I18n/Chinese
Requires:       fwnncom = %{version}
Requires(pre):	shadow

%description -n fcwnncom
This package includes the common files for the Free cWnn and Free tWnn
Chinese Input Systems. Free cWnn is for mainland Chinese and free tWnn
is for Taiwan-Chinese.

%package -n libcwnn0
Summary:        FreeWnn Chinese Input System library
Group:          System/Libraries

%description -n libcwnn0
This subpackage contains a core library of the Wnn input system.

%package -n fcwnn-devel
Summary:        Development Libraries and Header Files for Free cWnn
Group:          Development/Libraries/C and C++
Requires:       fcwnn = %{version}
Requires:       libcwnn0 = %{version}
Obsoletes:      fcwnndev < %{version}-%{release}
Provides:       fcwnndev = %{version}-%{release}

%description -n fcwnn-devel
This package contains the header files and libraries for building
client programs that use the Chinese Input System, Free cWnn.

%package -n ftwnn
Summary:        Free tWnn Chinese Input System (Taiwan)
Group:          System/I18n/Chinese
Requires:       fcwnn = %{version}
Requires:       fcwnncom = %{version}
Requires(pre):	shadow
Requires(post):	fcwnncom

%description -n ftwnn
Free tWnn Chinese input system (Taiwan).

%package -n fkwnn
Summary:        Free kWnn Korean Input System
Group:          System/I18n/Korean
Requires:       fwnncom = %{version}
Requires(pre):	shadow

%description -n fkwnn
Free kWnn Korean input system.

%package -n libkwnn0
Summary:        FreeWnn Korean Input System library
Group:          System/Libraries

%description -n libkwnn0
This subpackage contains a core library of the Wnn input system.

%package -n fkwnn-devel
Summary:        Development Libraries and Header Files for Free kWnn
Group:          Development/Libraries/C and C++
Requires:       fcwnn-devel = %{version}
Requires:       fkwnn = %{version}
Obsoletes:      fwknndev < %{version}-%{release}
Provides:       fwknndev = %{version}-%{release}

%description -n fkwnn-devel
This package contains the header files and libraries for building
client programs that use the Korean Input System, Free kWnn.

######################################################################
# package xwnmo
# I don't know how to build xwnmo. Will try that later ...
# %%package -n xwnmo
# Requires: wnn
# Summary: xwnmo - Input Manager for the X11 Window System
# Summary(ja): xwnmo - Ｘウィンドウ・インプットマネージャー
# Group: Applications/X11
#
# %%description -n xwnmo
#
# Xwnmo is a input manager for the Input Method of the X Window System.
# It is based on the X11 Input Method Specifications.  It provides a
# multi-language input environment for multiple clients in the X11
# Window System. Clients can connect to it by using the XIM library. The
# conversion engine xwnmo uses the internationalized Wnn. It selects
# the conversion server in accordance with language of clients.
#
%prep
%setup -q -n FreeWnn-%{base_version}-%{alpha_version}
%patch0 -p1
%patch1 -p1
%patch2 -p1
%patch7 -p2 -b .s390x
%patch8
#%%setup -b 1 -n Xsi           # add include-files for Xwnmo
# SuSE setlocale patch, try to set LC_CTYPE if LC_ALL fails (Xwnmo) and
#......................................................................
# %%patch2 -p1
# Trying to make Xwnmo work...
#..................................................................
# %%patch3 -p1

%build
%configure --prefix=%{_prefix} \
            --libdir=%{_libdir} \
            --mandir=%{_mandir} \
            --infodir=%{_infodir} \
            %{_target_cpu}-suse-linux-gnu \
            --disable-sub-bindir \
            --enable-client \
	    --disable-client-setuid \
	    --disable-client-setgid \
            --with-libwrap
# not -j safe, see Wnn/pubdicplus/Makefile.in
make
#pushd Wnn/uum
#make CCOPTIONS="$RPM_OPT_FLAGS"
#popd

%install
make DESTDIR=%{buildroot} install %{?_smp_mflags}
make install.man DESTDIR=%{buildroot}
#pushd Wnn/uum
#make install DESTDIR=$RPM_BUILD_ROOT INSTPGMFLAGS=
#popd

#----------------------------------------------------------------------
# move Japanese man pages to their correct destination:
# (the above 'make install.man' command installs Japanese AND English
#  manpages, but unfortunately all of them into the same directory.
#  The Japanese manpages should be in a subdirectory 'ja'
#  (or maybe ja_JP.eucJP), therefore I move them here:
for i in 1 3 4 5 ; do
    mkdir -p %{buildroot}/%{_mandir}/ja/man$i
done
for i in atod.1 atof.1 dtoa.1 jserver.1 oldatonewa.1 uum.1 wddel.1 wdreg.1 \
	  wnnkill.1 wnnstat.1 wnntouch.1
do
	  mv %{buildroot}/%{_mandir}/man1/$i %{buildroot}/%{_mandir}/ja/man1/
done
mv %{buildroot}/%{_mandir}/man3/* %{buildroot}/%{_mandir}/ja/man3/
for i in 2a_ctrl.4 2b_romkana.4 cvt_key_tbl.4 fzk.data.4 fzk.u.4 \
	  hinsi_data.4 jserverrc.4 mode.4 serverdefs.4 ujis_dic.4 \
	  uumkey.4 uumrc.4 wnnenvrc.4
do
	  mv %{buildroot}/%{_mandir}/man4/$i %{buildroot}/%{_mandir}/ja/man4/
done
for i in pubdic.5 usr_dic.5
do
	  mv %{buildroot}/%{_mandir}/man5/$i %{buildroot}/%{_mandir}/ja/man5/
done
install -d %{buildroot}%{_unitdir}
install -m 644 %{SOURCE5} %{buildroot}%{_unitdir}
install -m 644 %{SOURCE6} %{buildroot}%{_unitdir}
install -m 644 %{SOURCE7} %{buildroot}%{_unitdir}
install -m 644 %{SOURCE8} %{buildroot}%{_unitdir}
install -d %{buildroot}%{_sbindir}
ln -s -f service %{buildroot}%{_sbindir}/rcfwnn
ln -s -f service %{buildroot}%{_sbindir}/rcfcwnn
ln -s -f service %{buildroot}%{_sbindir}/rcftwnn
ln -s -f service %{buildroot}%{_sbindir}/rcfkwnn
ln -s -f %{_localstatedir}/lib/wnn/ja/dic %{buildroot}%{_sysconfdir}/FreeWnn/ja/dic
ln -s -f %{_localstatedir}/lib/wnn/zh_CN/dic %{buildroot}%{_sysconfdir}/FreeWnn/zh_CN/dic
ln -s -f %{_localstatedir}/lib/wnn/zh_TW/dic %{buildroot}%{_sysconfdir}/FreeWnn/zh_TW/dic
ln -s -f %{_localstatedir}/lib/wnn/ko_KR/dic %{buildroot}%{_sysconfdir}/FreeWnn/ko_KR/dic
#----------------------------------------------------------------------
find %{buildroot} -type f -name "*.la" -delete -print
find %{buildroot} -type f -name "*.a" -delete -print

%fdupes -s %{buildroot}

%pre -n fwnn
%service_add_pre fwnn.service
getent passwd wnn >/dev/null || \
	%{_sbindir}/useradd -r -o -g root -u 66 -s /bin/false \
	-c "Wnn System Account" -d %{_localstatedir}/lib/wnn wnn

%post -n fwnn
%service_add_post fwnn.service
# touch all public dictionary files:
chroot . usr/bin/wnntouch var/lib/wnn/ja/dic/gerodic/g-jinmei.dic
chroot . usr/bin/wnntouch var/lib/wnn/ja/dic/pubdic/*.*

%preun -n fwnn
%service_del_preun fwnn.service
%stop_on_removal fwnn

%postun -n fwnn
%service_del_postun fwnn.service
%restart_on_update fwnn

%post   -n libjd0 -p /sbin/ldconfig
%postun -n libjd0 -p /sbin/ldconfig
%post   -n libwnn0 -p /sbin/ldconfig
%postun -n libwnn0 -p /sbin/ldconfig

%pre -n fwnncom
getent passwd wnn >/dev/null || \
	%{_sbindir}/useradd -r -o -g root -u 66 -s /bin/false \
	-c "Wnn System Account" -d %{_localstatedir}/lib/wnn wnn

%pre -n fcwnncom
getent passwd wnn >/dev/null || \
	%{_sbindir}/useradd -r -o -g root -u 66 -s /bin/false \
	-c "Wnn System Account" -d %{_localstatedir}/lib/wnn wnn

%pre -n fcwnn
%service_add_pre fcwnn.service
getent passwd wnn >/dev/null || \
	%{_sbindir}/useradd -r -o -g root -u 66 -s /bin/false \
	-c "Wnn System Account" -d %{_localstatedir}/lib/wnn wnn

%preun -n fcwnn
%service_del_preun fcwnn.service
%stop_on_removal fcwnn

%post -n fcwnn
%service_add_post fcwnn.service
# touch all public dictionary files:
chroot . usr/bin/cwnntouch var/lib/wnn/zh_CN/dic/sys/*.*
# Create symbolic run level links:

%postun -n fcwnn
%service_del_postun fcwnn.service
%restart_on_update fcwnn

%post   -n libcwnn0 -p /sbin/ldconfig
%postun -n libcwnn0 -p /sbin/ldconfig

%pre -n ftwnn
%service_add_pre ftwnn.service
getent passwd wnn >/dev/null || \
	%{_sbindir}/useradd -r -o -g root -u 66 -s /bin/false \
	-c "Wnn System Account" -d %{_localstatedir}/lib/wnn wnn

%preun -n ftwnn
%service_del_preun ftwnn.service
%stop_on_removal ftwnn

%post -n ftwnn
%service_add_post ftwnn.service
# touch all public dictionary files:
chroot . usr/bin/cwnntouch var/lib/wnn/zh_TW/dic/sys/*.*
# Create symbolic run level links:

%postun -n ftwnn
%service_del_postun ftwnn.service
%restart_on_update ftwnn

%pre -n fkwnn
%service_add_pre fkwnn.service
getent passwd wnn >/dev/null || \
	%{_sbindir}/useradd -r -o -g root -u 66 -s /bin/false \
	-c "Wnn System Account" -d %{_localstatedir}/lib/wnn wnn

%preun -n fkwnn
%service_del_preun fkwnn.service
%stop_on_removal fkwnn

%post -n fkwnn
%service_add_post fkwnn.service
# touch all public dictionary files:
chroot . usr/bin/kwnntouch var/lib/wnn/ko_KR/dic/sys/*.*
# Create symbolic run level links:

%postun -n fkwnn
%service_del_postun fkwnn.service
%restart_on_update fkwnn

%post   -n libkwnn0 -p /sbin/ldconfig
%postun -n libkwnn0 -p /sbin/ldconfig

%files
%defattr(-,root,root)
%{_sbindir}/rcfwnn
%{_unitdir}/fwnn.service
%{_bindir}/atod
%{_bindir}/dtoa
%{_bindir}/oldatonewa
%{_bindir}/wdreg
%{_bindir}/wnnstat
%{_bindir}/atof
%{_bindir}/jserver
%{_bindir}/wddel
%{_bindir}/wnnkill
%{_bindir}/uum
%{_bindir}/wnntouch
%dir %attr(-,wnn,root) %{_localstatedir}/lib/wnn/
%dir %attr(-,wnn,root) %{_localstatedir}/lib/wnn/ja/
%attr(-,wnn,root) %{_localstatedir}/lib/wnn/ja/dic
%dir %{_sysconfdir}/FreeWnn/ja/
%{_sysconfdir}/FreeWnn/ja/dic
%config %{_sysconfdir}/FreeWnn/ja/hinsi.data
%config %{_sysconfdir}/FreeWnn/ja/jserverrc
%config %{_sysconfdir}/FreeWnn/ja/libwnn.msg
%config %{_sysconfdir}/FreeWnn/ja/rk
%config %{_sysconfdir}/FreeWnn/ja/rk.vi
%config %{_sysconfdir}/FreeWnn/ja/uum.msg
%config %{_sysconfdir}/FreeWnn/ja/uumkey
%config %{_sysconfdir}/FreeWnn/ja/uumkey.omr
%config %{_sysconfdir}/FreeWnn/ja/uumkey_e
%config %{_sysconfdir}/FreeWnn/ja/uumrc
%config %{_sysconfdir}/FreeWnn/ja/uumrc.omr
%config %{_sysconfdir}/FreeWnn/ja/uumrc.rev
%config %{_sysconfdir}/FreeWnn/ja/uumrc_e
%config %{_sysconfdir}/FreeWnn/ja/uumrc_vi
%config %{_sysconfdir}/FreeWnn/ja/wnnenvrc
%config %{_sysconfdir}/FreeWnn/ja/wnnenvrc.omr
%config %{_sysconfdir}/FreeWnn/ja/wnnenvrc.rem
%config %{_sysconfdir}/FreeWnn/ja/wnnenvrc.rev
%config %{_sysconfdir}/FreeWnn/ja/wnnenvrc_R
%config %{_sysconfdir}/FreeWnn/ja/wnnenvrc_R.omr
%config %{_sysconfdir}/FreeWnn/ja/wnnenvrc_R.rem
%config %{_sysconfdir}/FreeWnn/ja/wnnstat.msg
%dir %{_sysconfdir}/FreeWnn/lt_LN/
%dir %{_sysconfdir}/FreeWnn/lt_LN/rk
%config %{_sysconfdir}/FreeWnn/lt_LN/rk/*
%config %{_sysconfdir}/FreeWnn/lt_LN/uum.msg
%config %{_sysconfdir}/FreeWnn/lt_LN/uumkey
%config %{_sysconfdir}/FreeWnn/lt_LN/uumkey_e
%config %{_sysconfdir}/FreeWnn/lt_LN/uumrc

%files -n libjd0
%defattr(-,root,root)
%{_libdir}/libjd.so.0*

%files -n libwnn0
%defattr(-,root,root)
%{_libdir}/libwnn.so.0*

%files -n fwnn-devel
%defattr(-,root,root)
%{_includedir}/wnn/
%{_libdir}/libjd.so
%{_libdir}/libwnn.so

%files -n fwnncom
%defattr(-,root,root)
%doc CONTRIBUTORS COPYRIGHT COPYRIGHT-j ChangeLog ChangeLog.old
%doc olddoc/ Wnn/manual/ Wnn/manual.en/
%doc cWnn/manual cWnn/manual.en
%{_mandir}/man?/*
%dir %{_mandir}/ja/
%dir %{_mandir}/ja/*/
%{_mandir}/ja/man?/*
%dir %attr(-,wnn,root) %{_localstatedir}/lib/wnn
%dir %{_sysconfdir}/FreeWnn/
%config %{_sysconfdir}/FreeWnn/cvt_key_empty
%config %{_sysconfdir}/FreeWnn/cvt_key_tbl
%config %{_sysconfdir}/FreeWnn/cvt_key_tbl.ST
%config %{_sysconfdir}/FreeWnn/cvt_key_tbl.gm
%config %{_sysconfdir}/FreeWnn/cvt_key_tbl.kt
%config %{_sysconfdir}/FreeWnn/cvt_key_tbl.mv
%config %{_sysconfdir}/FreeWnn/cvt_key_tbl.vt
%config %{_sysconfdir}/FreeWnn/serverdefs

%files -n fcwnn
%defattr(-,root,root)
%{_sbindir}/rcfcwnn
%{_unitdir}/fcwnn.service
%{_bindir}/cserver
%config %{_sysconfdir}/FreeWnn/zh_CN/cixing.data
%config %{_sysconfdir}/FreeWnn/zh_CN/cserverrc
%{_sysconfdir}/FreeWnn/zh_CN/dic
%dir %attr(-,wnn,root) %{_localstatedir}/lib/wnn/
%dir %attr(-,wnn,root) %{_localstatedir}/lib/wnn/zh_CN/
%{_localstatedir}/lib/wnn/zh_CN/dic
%config %{_sysconfdir}/FreeWnn/zh_CN/libwnn.msg
%dir %{_sysconfdir}/FreeWnn/
%dir %{_sysconfdir}/FreeWnn/zh_CN/
%dir %{_sysconfdir}/FreeWnn/zh_CN/rk
%dir %{_sysconfdir}/FreeWnn/zh_CN/rk_p
%dir %{_sysconfdir}/FreeWnn/zh_CN/rk_z
%config %{_sysconfdir}/FreeWnn/zh_CN/rk/*
%config %{_sysconfdir}/FreeWnn/zh_CN/rk_p/*
%config %{_sysconfdir}/FreeWnn/zh_CN/rk_z/*
%config %{_sysconfdir}/FreeWnn/zh_CN/uum.msg
%config %{_sysconfdir}/FreeWnn/zh_CN/uumkey
%config %{_sysconfdir}/FreeWnn/zh_CN/uumkey_e
%config %{_sysconfdir}/FreeWnn/zh_CN/uumkey_p
%config %{_sysconfdir}/FreeWnn/zh_CN/uumrc
%config %{_sysconfdir}/FreeWnn/zh_CN/uumrc_p
%config %{_sysconfdir}/FreeWnn/zh_CN/uumrc_z
%config %{_sysconfdir}/FreeWnn/zh_CN/wnnenvrc
%config %{_sysconfdir}/FreeWnn/zh_CN/wnnenvrc_Qi
%config %{_sysconfdir}/FreeWnn/zh_CN/wnnenvrc_QiR
%config %{_sysconfdir}/FreeWnn/zh_CN/wnnenvrc_R
%config %{_sysconfdir}/FreeWnn/zh_CN/wnnenvrc_Wu
%config %{_sysconfdir}/FreeWnn/zh_CN/wnnenvrc_WuR
%config %{_sysconfdir}/FreeWnn/zh_CN/wnnstat.msg

%files -n libcwnn0
%defattr(-,root,root)
%{_libdir}/libcwnn.so.0*

%files -n fcwnncom
%defattr(-,root,root)
%{_bindir}/catod
%{_bindir}/catof
%{_bindir}/cdtoa
%{_bindir}/cwddel
%{_bindir}/cwdreg
%{_bindir}/cwnnkill
%{_bindir}/cwnnstat
%{_bindir}/cwnntouch
%{_bindir}/cuum

%files -n fcwnn-devel
%defattr(-,root,root)
%{_includedir}/cwnn/
%{_libdir}/libcwnn.so

%files -n ftwnn
%defattr(-,root,root)
%{_sbindir}/rcftwnn
%{_unitdir}/ftwnn.service
%{_bindir}/tserver
%config %{_sysconfdir}/FreeWnn/zh_TW/cixing.data
%{_sysconfdir}/FreeWnn/zh_TW/dic
%dir %attr(-,wnn,root) %{_localstatedir}/lib/wnn/
%dir %attr(-,wnn,root) %{_localstatedir}/lib/wnn/zh_TW/
%{_localstatedir}/lib/wnn/zh_TW/dic
%config %{_sysconfdir}/FreeWnn/zh_TW/libwnn.msg
%dir %{_sysconfdir}/FreeWnn/
%dir %{_sysconfdir}/FreeWnn/zh_TW/
%dir %{_sysconfdir}/FreeWnn/zh_TW/rk
%dir %{_sysconfdir}/FreeWnn/zh_TW/rk_p
%dir %{_sysconfdir}/FreeWnn/zh_TW/rk_z
%config %{_sysconfdir}/FreeWnn/zh_TW/rk/*
%config %{_sysconfdir}/FreeWnn/zh_TW/rk_p/*
%config %{_sysconfdir}/FreeWnn/zh_TW/rk_z/*
%config %{_sysconfdir}/FreeWnn/zh_TW/tserverrc
%config %{_sysconfdir}/FreeWnn/zh_TW/uum.msg
%config %{_sysconfdir}/FreeWnn/zh_TW/uumkey
%config %{_sysconfdir}/FreeWnn/zh_TW/uumkey_e
%config %{_sysconfdir}/FreeWnn/zh_TW/uumkey_p
%config %{_sysconfdir}/FreeWnn/zh_TW/uumrc
%config %{_sysconfdir}/FreeWnn/zh_TW/uumrc_p
%config %{_sysconfdir}/FreeWnn/zh_TW/uumrc_z
%config %{_sysconfdir}/FreeWnn/zh_TW/wnnenvrc
%config %{_sysconfdir}/FreeWnn/zh_TW/wnnenvrc_R
%config %{_sysconfdir}/FreeWnn/zh_TW/wnnstat.msg

%files -n fkwnn
%defattr(-,root,root)
%{_sbindir}/rcfkwnn
%{_unitdir}/fkwnn.service
%{_bindir}/kserver
%{_bindir}/katod
%{_bindir}/katof
%{_bindir}/kdtoa
%{_bindir}/kwddel
%{_bindir}/kwdreg
%{_bindir}/kwnnkill
%{_bindir}/kwnnstat
%{_bindir}/kwnntouch
%{_bindir}/kuum
%dir %{_sysconfdir}/FreeWnn/
%dir %{_sysconfdir}/FreeWnn/ko_KR/
%{_sysconfdir}/FreeWnn/ko_KR/dic
%dir %attr(-,wnn,root) %{_localstatedir}/lib/wnn/
%dir %attr(-,wnn,root) %{_localstatedir}/lib/wnn/ko_KR/
%{_localstatedir}/lib/wnn/ko_KR/dic
%config %{_sysconfdir}/FreeWnn/ko_KR/hinsi.data
%config %{_sysconfdir}/FreeWnn/ko_KR/kserverrc
%config %{_sysconfdir}/FreeWnn/ko_KR/libwnn.msg
%dir %{_sysconfdir}/FreeWnn/ko_KR/rk
%config %{_sysconfdir}/FreeWnn/ko_KR/rk/*
%config %{_sysconfdir}/FreeWnn/ko_KR/uum.msg
%config %{_sysconfdir}/FreeWnn/ko_KR/uumkey
%config %{_sysconfdir}/FreeWnn/ko_KR/uumrc
%config %{_sysconfdir}/FreeWnn/ko_KR/wnnenvrc
%config %{_sysconfdir}/FreeWnn/ko_KR/wnnenvrc_R
%config %{_sysconfdir}/FreeWnn/ko_KR/wnnstat.msg

%files -n libkwnn0
%defattr(-,root,root)
%{_libdir}/libkwnn.so.0*

%files -n fkwnn-devel
%defattr(-,root,root)
%{_includedir}/kwnn/
%{_libdir}/libkwnn.so
# I don't know how to build xwnmo. Will try that later ...
# %%files -n xwnmo
# %%doc Xwnmo/manual Xwnmo/manual.en Xwnmo/README Xwnmo/README.j
# %%doc Xwnmo/X11R6/README Xwnmo/X11R6/include/README
# %%doc Xwnmo/xjutil/README Xwnmo/xjutil/README.j Xwnmo/xwnmo/README
# %%doc Xwnmo/xwnmo/README.j Xwnmo/xwnmo/SEP_README Xwnmo/xwnmo/SEP_README.j
# /usr/X11R6/lib/X11/app-defaults/Xwnmo
# /usr/X11R6/bin/xwnmo
# /usr/X11R6/bin/killxwnmo
# /usr/X11R6/bin/xjutil
# /usr/X11R6/man/ja_JP.ujis/man1/xwnmo.1.gz
# /usr/X11R6/man/ja_JP.ujis/man1/ximrc.1.gz
# /usr/X11R6/man/ja_JP.ujis/man1/ximconf.1.gz
# /usr/X11R6/man/ja_JP.ujis/man1/cvt_fun_tbl.1.gz
# /usr/X11R6/man/ja_JP.ujis/man1/cvt_meta_tbl.1.gz
# /usr/X11R6/man/ja_JP.ujis/man1/killxwnmo.1.gz
# /usr/X11R6/man/ja_JP.ujis/man1/cvt_xim_tbl.1.gz
# /usr/X11R6/man/ja_JP.ujis/man1/xjutil.1.gz
# /usr/X11R6/man/man1/xwnmo.1.gz
# /usr/X11R6/man/man1/ximrc.1.gz
# /usr/X11R6/man/man1/ximconf.1.gz
# /usr/X11R6/man/man1/cvt_fun_tbl.1.gz
# /usr/X11R6/man/man1/cvt_meta_tbl.1.gz
# /usr/X11R6/man/man1/killxwnmo.1.gz
# /usr/X11R6/man/man1/cvt_xim_tbl.1.gz
# /usr/X11R6/man/man1/xjutil.1.gz
# /var/lib/wnn/ja_JP/uumrc.xim
# /var/lib/wnn/ja_JP/uumrc_vi.xim
# /var/lib/wnn/ja_JP/uumrc_e.xim
# /var/lib/wnn/ja_JP/uumkey.xim
# /var/lib/wnn/ja_JP/uumkey_v.xim
# /var/lib/wnn/ja_JP/uumkey_e.xim
# /var/lib/wnn/ja_JP/xim.msg
# /var/lib/wnn/ja_JP/xjutil.msg
# /var/lib/wnn/lt_LN/uumrc.xim
# /var/lib/wnn/lt_LN/uumkey.xim
# /var/lib/wnn/lt_LN/xim.msg
# /var/lib/wnn/zh_CN/uumrc.xim
# /var/lib/wnn/zh_CN/uumrc_p.xim
# /var/lib/wnn/zh_CN/uumrc_z.xim
# /var/lib/wnn/zh_CN/uumkey.xim
# /var/lib/wnn/zh_CN/uumkey_p.xim
# /var/lib/wnn/zh_CN/xim.msg
# /var/lib/wnn/zh_CN/xjutil.msg
# /var/lib/wnn/zh_TW/uumrc.xim
# /var/lib/wnn/zh_TW/uumrc_p.xim
# /var/lib/wnn/zh_TW/uumrc_z.xim
# /var/lib/wnn/zh_TW/uumkey.xim
# /var/lib/wnn/zh_TW/uumkey_p.xim
# /var/lib/wnn/zh_TW/xim.msg
# /var/lib/wnn/zh_TW/xjutil.msg
# /var/lib/wnn/ko_KR/uumrc.xim
# /var/lib/wnn/ko_KR/uumkey.xim
# /var/lib/wnn/ko_KR/xim.msg
# /var/lib/wnn/ko_KR/xjutil.msg
# %%config /var/lib/wnn/ximconf
# %%config /var/lib/wnn/ximrc
# %%config /var/lib/wnn/ximrc_vi
# %%config /var/lib/wnn/cvt_xim_tbl

%changelog
