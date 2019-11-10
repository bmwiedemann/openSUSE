#
# spec file for package canna
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


Name:           canna
Version:        3.7p3
Release:        0
Summary:        Kana and Kanji Conversion System
# http://canna.sourceforge.jp/
License:        BSD-3-Clause
Group:          System/I18n/Japanese
URL:            http://www.nec.co.jp/japanese/product/computer/soft/canna/
# select mirror from
# http://sourceforge.jp/projects/canna/downloads/9565/Canna37p3.tar.bz2/
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
BuildRequires:  automake
BuildRequires:  gcc
BuildRequires:  imake
BuildRequires:  ncurses-devel
BuildRequires:  pwdutils
BuildRequires:  termcap
Requires(pre):  %{_sbindir}/groupadd
Requires(pre):  %{_sbindir}/useradd
Requires(pre):  /bin/rm
Recommends:     cannadic
%if 0%{?suse_version} < 1230
Requires(pre):  %insserv_prereq
%else
BuildRequires:  pkgconfig(systemd)
%{?systemd_requires}
%endif
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
Summary:        Canna Shared Libraries
Group:          System/Libraries
Provides:       canna:%{_prefix}/lib/libcanna.so.1.1
#Summary(ja): Canna ユーザインタフェースレベルのライブラリ
# %description -n canna-libs -l ja
# Canna ユーザインタフェースレベルのライブラリ

%description -n canna-libs
Canna Shared Libraries

%package -n canna-devel
Summary:        Canna Development Headers and Libraries
Group:          Development/Libraries/C and C++
Requires:       %{name} = %{version}
Requires:       %{name}-libs = %{version}
Provides:       cannadev = %{version}-%{release}
Obsoletes:      cannadev < %{version}-%{release}
#Summary(ja): Canna ユーザインタフェースレベルのライブラリ
# %description -n canna-devel -l ja
# Canna ユーザインタフェースレベルのライブラリ

%description -n canna-devel
Canna development headers and libraries.

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
%patch20  -b .noredefine
perl -pi -e 's#%{_prefix}/lib/termcap#%{_libdir}/termcap#' canuum/Imakefile
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
make -j1 CDEBUGFLAGS="%{optflags} -fPIC -fno-strict-aliasing" CXXDEBUGFLAGS="%{optflags} -fPIC -fno-strict-aliasing" canna
pushd canuum
    cp %{_datadir}/automake*/config.{guess,sub} .
    export CDEBUGFLAGS="%{optflags} -fno-strict-aliasing"
    export CXXDEBUGFLAGS="%{optflags} -fno-strict-aliasing"
    xmkmf -a
    make %{?_smp_mflags} CDEBUGFLAGS="%{optflags} -fno-strict-aliasing" CXXDEBUGFLAGS="%{optflags} -fno-strict-aliasing"
popd

%install
# create home directory for user 'wnn':
mkdir -p %{buildroot}%{_localstatedir}/lib/wnn
# add user 'wnn' (also used for Canna, not only for wnn)
%{_sbindir}/useradd -r -o -g bin -u 66 -s /bin/false -c "Wnn System Account" -d %{_localstatedir}/lib/wnn wnn 2> /dev/null || :
make install DESTDIR=%{?buildroot} RPM_BUILD=TRUE
make install.man MANSUFFIX=1 LIBMANSUFFIX=3 DESTDIR=%{?buildroot}
# Make links for utility programs
# (excluded from Make process via RPM_BUILD=TRUE)
#.....................................................................
(cd %{?buildroot}%{_prefix}/bin; \
for i in cpdic lsdic mkdic mvdic rmdic syncdic addwords delwords
do
	ln -sf catdic $i
done; \
ln -sf ../bin/catdic ../sbin/cannakill)
#.....................................................................
pushd canuum
    make install DESTDIR=%{?buildroot}
    make install.man MANSUFFIX=1 LIBMANSUFFIX=3 DESTDIR=%{?buildroot}
    chmod 755 %{buildroot}%{_bindir}/canuum
popd
%if 0%{?suse_version} < 1230
mkdir -p %{buildroot}%{_initddir}
mkdir -p %{buildroot}%{_sbindir}
%else
mkdir -p %{buildroot}/%{_unitdir}
mkdir -p %{buildroot}%{_prefix}/lib/tmpfiles.d
%endif
mkdir -p %{buildroot}%{_sysconfdir}/hosts.canna
mkdir -p %{buildroot}%{_localstatedir}/lib/canna/log
%if 0%{?suse_version} < 1230
install -m 755 %{_sourcedir}/rccanna %{buildroot}%{_initddir}/canna
ln -s ../..%{_initddir}/canna %{buildroot}%{_sbindir}/rccanna
%else
install -m 644 %{_sourcedir}/canna.service %{buildroot}/%{_unitdir}/canna.service
install -m 644 %{_sourcedir}/canna-tmpfiles.conf %{buildroot}%{_prefix}/lib/tmpfiles.d/canna-tmpfiles.conf
%endif
install -m 644 %{_sourcedir}/hosts.canna %{?buildroot}%{_sysconfdir}/hosts.canna
# Remove all cannakill manpages because we've disabled it in
# the server.
rm -f `find %{buildroot}%{_mandir} -name 'cannakill*'`
rm -f %{buildroot}%{_sbindir}/cannakill
find %{buildroot} -type f -name "*.a" -delete -print

%pre -n canna
%{_sbindir}/useradd -r -o -g bin -u 66 -s /bin/false -c "Wnn System Account" -d %{_localstatedir}/lib/wnn wnn 2> /dev/null || :
%if 0%{?suse_version} >= 1230
%service_add_post canna.service
%endif

%post -n canna
%if 0%{?suse_version} < 1230
%{fillup_and_insserv -y canna}
%else
%service_add_post canna.service
%tmpfiles_create %{_tmpfilesdir}/canna-tempfiles.conf
%endif

%preun -n canna
%if 0%{?suse_version} < 1230
%stop_on_removal canna
%else
%service_del_preun canna.service
%endif

%postun -n canna
%if 0%{?suse_version} < 1230
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
%doc CHANGES.jp README{,.jp} WHATIS{,.jp} candoc
%dir %attr(-,wnn,root) %{_localstatedir}/log/canna
%dir %attr(-,wnn,root) %{_localstatedir}/lib/canna/log
%dir %attr(-,wnn,root) %{_localstatedir}/lib/wnn
%{_sysconfdir}/hosts.canna
%if 0%{?suse_version} < 1230
%{_initddir}/canna
%{_sbindir}/rccanna
%else
%{_unitdir}/canna.service
%{_prefix}/lib/tmpfiles.d/canna-tmpfiles.conf
%endif
# don't package cannakill, it is disabled by okir's security patch anyway
# /usr/sbin/cannakill
# more secure permission for cannaserver
# (setuid and setgid bits was set per default).
%attr(755,root,root) %{_sbindir}/cannaserver
%{_bindir}/*
%config %{_localstatedir}/lib/canna/default.canna
#%config /var/lib/canna/engine.cf
%dir %{_localstatedir}/lib/canna/
%dir %attr(755,wnn,root) %{_localstatedir}/lib/canna/dic/
%attr(-,wnn,root) %{_localstatedir}/lib/canna/dic/*cbp
%dir %attr(755,wnn,root) %{_localstatedir}/lib/canna/dic/canna/
%attr(-,wnn,root) %{_localstatedir}/lib/canna/dic/canna/*
%{_localstatedir}/lib/canna/sample/
%dir %{_mandir}/ja/
%dir %{_mandir}/ja/man1/
%{_mandir}/ja/man1/*
%{_mandir}/man1/*

%files -n canna-libs
%{_libdir}/lib*.so.*

%files -n canna-devel
%{_libdir}/lib*.so
%dir %{_includedir}/canna
%{_includedir}/canna/*.h
%dir %{_mandir}/ja/
%dir %{_mandir}/ja/man3/
%{_mandir}/ja/man3/*
%{_mandir}/man3/*

%changelog
