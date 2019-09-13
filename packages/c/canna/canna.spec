#
# spec file for package canna
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


Name:           canna
BuildRequires:  automake
BuildRequires:  gcc
BuildRequires:  imake
BuildRequires:  ncurses-devel
BuildRequires:  pwdutils
BuildRequires:  termcap
Requires(pre):  /usr/sbin/useradd
Requires(pre):  /usr/sbin/groupadd
Requires(pre):  /bin/rm
%if %suse_version < 1230
Requires(pre):  %insserv_prereq
%else
BuildRequires:  pkgconfig(systemd)
%{?systemd_requires}
%endif
#BuildPrereq:  termcap
Recommends:     cannadic
Version:        3.7p3
Release:        0
# http://canna.sourceforge.jp/
Url:            http://www.nec.co.jp/japanese/product/computer/soft/canna/
BuildRoot:      %{_tmppath}/%{name}-%{version}-build
Summary:        Kana and Kanji Conversion System
# select mirror from
# http://sourceforge.jp/projects/canna/downloads/9565/Canna37p3.tar.bz2/
License:        BSD-3-Clause
Group:          System/I18n/Japanese
Source:         Canna37p3.tar.bz2
Source1:        candoc.tar.bz2
Source2:        rccanna
Source3:        hosts.canna
Source4:        jisx6002.kpdef
Source5:        canna.service
Source6:        canna-tmpfiles.conf
Source99:       baselibs.conf
Patch0:         unoff1.patch
Patch5:         security.patch
Patch7:         Canna.conf.patch
Patch9:         canuum.suse.patch
# multibyte patch needed for Nicolatter,
# see http://www2.airnet.ne.jp/pak04955/dl-linux.htm
# Patch can also be found in the nicolatter package
Patch11:        Canna36p3-q1.diff
Patch12:        default-dictionaries.patch
Patch14:        security-okir.patch
Patch15:        add-kpdef.patch
Patch17:        sort.patch
Patch18:        control-reaches-end-of-void-function.patch
Patch19:        noconfwrapper.patch
Patch20:        canna-noredefine_fgets.patch
Patch21:        canna-include.patch
Patch22:        fix-uninit.patch
Patch23:        canna-strip.patch
Patch24:        bug-262623-internet-usage-broken-by-security-patch.patch
Patch25:        Canna37p3-destbufferoverflow.patch
Patch26:        canna-fiximplicit.patch
# Summary(ja):  Canna - かな漢字変換システム
# %description -n canna -l ja
# UNIX 上で共通に使える日本語入力システムとして Wnn が存在しました。
# 『かんな』は UNIX 上の日本語入力として Wnn 以外にもう一つの選択肢を
# 与えることができればと思いフリーソフトウェアとして誰でも利用できるよ
# うにしました。
# 
# 
# 『かんな』は Wnn と同様、アプリケーションプログラムとかな漢字変換辞
# 書をアクセスするかな漢字変換サーバが別のプロセスとして分離されたクラ
# イアント・サーバ型の動作をします。このことを含め『かんな』の特長とし
# て以下があります。
# 
# 
# (1) クライアント・サーバ方式のかな漢字変換
# (2) 逐次自動変換のサポート
# (3) 統一的なユーザインタフェースの提供
# (4) 広範囲なカスタマイズのサポート
# (5) lisp 言語ベースのカスタマイズ記述
# (6) 単語登録時の最適な品詞づけ
# (7) 統一的なユーザインタフェースを簡単に提供するためのライブラリ
# (8) 辞書をメンテナンスするためのコマンド群
# (9) カスタマイズを簡単に行うためのカスタマイズツールの提供
# (10) Nemacs(Mule)、kinput2、uum のサポート

%description
Canna converts Kana to Kanji based on a client/server model. An
application program communicates with a Kana to Kanji conversion server
to achieve Japanese input. Canna can be used in Emacs, X Window System
environments, and on TTYs. Canna provides more than ten tools to
maintain Kana to Kanji conversion dictionaries.


%package -n canna-libs
Summary:        Canna Libraries
Group:          System/I18n/Japanese
Provides:       canna:/usr/lib/libcanna.so.1.1
#Summary(ja): Canna ユーザインタフェースレベルのライブラリ
# %description -n canna-libs -l ja
# Canna ユーザインタフェースレベルのライブラリ

%description -n canna-libs
Canna Libraries


%package -n canna-devel
Summary:        Libraries of Canna
Group:          Development/Libraries/C and C++
Requires:       %{name} = %{version}
Requires:       %{name}-libs = %{version}
Provides:       cannadev
Obsoletes:      cannadev
#Summary(ja): Canna ユーザインタフェースレベルのライブラリ
# %description -n canna-devel -l ja
# Canna ユーザインタフェースレベルのライブラリ

%description -n canna-devel
Canna libraries.


%prep
%setup -q -n Canna37p3 -a 1
%patch0 -p1 -b .unoff1
%patch5 -p1 -b .security
%patch7 -p1 -b .Canna.conf
%patch9 -p1 -b .canuum.suse
%patch11 -p1 -b .Canna36p3-q1.diff
%patch12 -p1 -b .default-dictionaries
%patch14 -p1 -b .security-okir
%patch15 -p1 -b .add-kpdef
%patch17 -p1 -b .sortcall
%patch18 -p1 -b .control-reaches-end-of-void-function
%patch19 -p1 -b .noconfwrapper
%patch20 -p0 -b .noredefine
perl -pi -e 's#/usr/lib/termcap#%{_libdir}/termcap#' canuum/Imakefile
perl -pi -e 's#lib64#%{_lib}#' Canna.conf
cp ${RPM_SOURCE_DIR}/jisx6002.kpdef dic/phono/
%patch21 -p1
%patch22
%patch23
%patch24 -p1
%patch25
%patch26 -p1

%build
xmkmf 
# parallel make does not work in some stages
make -j1 Makefile
make -j1 CDEBUGFLAGS="$RPM_OPT_FLAGS -fPIC -fno-strict-aliasing" CXXDEBUGFLAGS="$RPM_OPT_FLAGS -fPIC -fno-strict-aliasing" canna
pushd canuum
    cp /usr/share/automake*/config.{guess,sub} .
    export CDEBUGFLAGS="$RPM_OPT_FLAGS -fno-strict-aliasing"
    export CXXDEBUGFLAGS="$RPM_OPT_FLAGS -fno-strict-aliasing"
    xmkmf -a
    make %{?_smp_mflags} CDEBUGFLAGS="$RPM_OPT_FLAGS -fno-strict-aliasing" CXXDEBUGFLAGS="$RPM_OPT_FLAGS -fno-strict-aliasing"
popd

%install
# create home directory for user 'wnn':
mkdir -p $RPM_BUILD_ROOT/var/lib/wnn
# add user 'wnn' (also used for Canna, not only for wnn)
/usr/sbin/useradd -r -o -g bin -u 66 -s /bin/false -c "Wnn System Account" -d /var/lib/wnn wnn 2> /dev/null || :
make install DESTDIR=%{?buildroot} RPM_BUILD=TRUE
make install.man MANSUFFIX=1 LIBMANSUFFIX=3 DESTDIR=%{?buildroot}
# Make links for utility programs 
# (excluded from Make process via RPM_BUILD=TRUE)
#.....................................................................
(cd %{?buildroot}/usr/bin; \
for i in cpdic lsdic mkdic mvdic rmdic syncdic addwords delwords
do
	ln -sf catdic $i
done; \
ln -sf ../bin/catdic ../sbin/cannakill)
#.....................................................................
pushd canuum
    make install DESTDIR=%{?buildroot}
    make install.man MANSUFFIX=1 LIBMANSUFFIX=3 DESTDIR=%{?buildroot}
    chmod 755 $RPM_BUILD_ROOT/usr/bin/canuum
popd
%if %suse_version < 1230
mkdir -p $RPM_BUILD_ROOT/etc/init.d
mkdir -p $RPM_BUILD_ROOT/usr/sbin
%else
mkdir -p $RPM_BUILD_ROOT/%{_unitdir}
mkdir -p $RPM_BUILD_ROOT/usr/lib/tmpfiles.d
%endif
mkdir -p $RPM_BUILD_ROOT/etc/hosts.canna
mkdir -p $RPM_BUILD_ROOT/var/lib/canna/log
%if %suse_version < 1230
install -m 755 $RPM_SOURCE_DIR/rccanna $RPM_BUILD_ROOT/etc/init.d/canna
ln -s ../../etc/init.d/canna $RPM_BUILD_ROOT/usr/sbin/rccanna
%else
install -m 644 $RPM_SOURCE_DIR/canna.service $RPM_BUILD_ROOT/%{_unitdir}/canna.service
install -m 644 $RPM_SOURCE_DIR/canna-tmpfiles.conf $RPM_BUILD_ROOT/usr/lib/tmpfiles.d/canna-tmpfiles.conf
%endif
install -m 644 $RPM_SOURCE_DIR/hosts.canna %{?buildroot}/etc/hosts.canna
# Remove all cannakill manpages because we've disabled it in
# the server.
rm -f `find $RPM_BUILD_ROOT/usr/share/man -name 'cannakill*'`
rm -f $RPM_BUILD_ROOT/usr/sbin/cannakill

%pre -n canna
/usr/sbin/useradd -r -o -g bin -u 66 -s /bin/false -c "Wnn System Account" -d /var/lib/wnn wnn 2> /dev/null || :
%if %suse_version >= 1230
%service_add_post canna.service
%endif

%post -n canna
%if %suse_version < 1230
%{fillup_and_insserv -y canna}
%else
%service_add_post canna.service
%endif

%preun -n canna
%if %suse_version < 1230
%stop_on_removal canna
%else
%service_del_preun canna.service
%endif

%postun -n canna
%if %suse_version < 1230
%restart_on_update canna
%insserv_cleanup
%else
%service_del_postun canna.service
%endif
if [ "$1" = "0" ]; then
  rm -rf /tmp/.iroha_unix
fi

%post -n canna-libs -p /sbin/ldconfig

%postun -n canna-libs -p /sbin/ldconfig

%files
%defattr(-,root,root,-)
%doc CHANGES.jp README{,.jp} WHATIS{,.jp} candoc
%dir %attr(-,wnn,root) /var/log/canna
%dir %attr(-,wnn,root) /var/lib/canna/log
%dir %attr(-,wnn,root) /var/lib/wnn
/etc/hosts.canna
%if %suse_version < 1230
/etc/init.d/canna
/usr/sbin/rccanna
%else
%{_unitdir}/canna.service
%{_libexecdir}/tmpfiles.d/canna-tmpfiles.conf
%endif
# don't package cannakill, it is disabled by okir's security patch anyway
# /usr/sbin/cannakill
# more secure permission for cannaserver
# (setuid and setgid bits was set per default).
%attr(755,root,root) /usr/sbin/cannaserver
/usr/bin/*
%config /var/lib/canna/default.canna
#%config /var/lib/canna/engine.cf
%dir /var/lib/canna/
%dir %attr(755,wnn,root) /var/lib/canna/dic/
%attr(-,wnn,root) /var/lib/canna/dic/*cbp
%dir %attr(755,wnn,root) /var/lib/canna/dic/canna/
%attr(-,wnn,root) /var/lib/canna/dic/canna/*
/var/lib/canna/sample/
%dir /usr/share/man/ja/
%dir /usr/share/man/ja/man1/
/usr/share/man/ja/man1/*
/usr/share/man/man1/*

%files -n canna-libs
%defattr(-, root, root)
%{_libdir}/lib*.so.*
%{_libdir}/lib*.so

%files -n canna-devel
%defattr(-, root, root)
%{_libdir}/lib*.*a
%dir /usr/include/canna
/usr/include/canna/*.h
%dir /usr/share/man/ja/
%dir /usr/share/man/ja/man3/
/usr/share/man/ja/man3/*
/usr/share/man/man3/*

%changelog
