#
# spec file for package anthy
#
# Copyright (c) 2020 SUSE LLC
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


%bcond_with     xemacs

Name:           anthy
Version:        9100h
Release:        0
Summary:        Kana-Kanji Conversion Engine
# Summary(ja): 仮名漢字変換エンジン
# Anthy(旧称Ancy)
#
# PC-Unix用の仮名漢字変換エンジンとしては Canna、 FreeWnn等が有名ですが、
# いずれも1990年前後の国産Unixワークステーションのために開発され、 フリー
# なものの開発はほぼ停止している状態です。 Hekeプロジェクトでは新たな変
# 換エンジンを辞書を除いてフルスクラッチで 開発を行っています。
#
# 著者：
# ------
#     田畑 悠介 <yusuke@kmc.kyoto-u.ac.jp>
License:        GPL-2.0-or-later AND LGPL-2.1-or-later
Group:          System/I18n/Japanese
URL:            https://osdn.jp/projects/anthy/
Source0:        anthy-%{version}.tar.bz2
Source1:        suse-start-anthy.el
Source2:        baselibs.conf
Patch2:         anthy-last-command-char-xemacs.patch
Patch3:         bugzilla-224463-comparison-with-string-literal.patch
# PATCH-FIX-OPENSUSE anthy-use-last-command-event.diff bnc#849211 tiwai@suse.de
Patch4:         anthy-use-last-command-event.diff
Patch5:         bugzilla-1175274-emacs-27.1.patch
BuildRequires:  emacs-x11
BuildRequires:  fdupes
BuildRequires:  libtool
%if %{with xemacs}
BuildRequires:  xemacs
%endif

%description
Anthy is a package for an input method editor backend for Unix-like
systems for the Japanese language. It can convert Hiragana to Kanji
as per the language rules. As a preconversion stage, Latin characters
(Romaji) can be used to input Hiragana. Anthy is commonly used with
an input method framework such as ibus, fcitx or SCIM.

%package -n libanthy0
Summary:        Kana–Kanji conversion engine
License:        GPL-2.0-or-later AND LGPL-2.1-or-later
Group:          System/Libraries

%description -n libanthy0
A Kana–Kanji conversion engine.

%package devel
Summary:        Header files for the Anthy Kana–Kanji conversion engine
License:        GPL-2.0-or-later
Group:          Development/Libraries/C and C++
Requires:       libanthy0 = %{version}
# Summary(ja): Anthy のヘッダファイル及びライブラリです。
# %description devel -l ja
# Anthy のヘッダファイル及びライブラリです。

%description devel
This package contains all necessary include files and libraries needed
to develop applications that require libanthy.

%prep
%setup -q
%patch2 -p 1
%patch3 -p 1
%patch4 -p 1
%patch5 -p 0

%build
autoreconf --force --install
CFLAGS="%{optflags} -fno-strict-aliasing" \
CXXFLAGS="%{optflags} -fno-strict-aliasing" \
%configure --disable-static --with-pic
make %{?_smp_mflags}

%check
cd test
./anthy --all

%install
%make_install
install -m 644 $RPM_SOURCE_DIR/suse-start-anthy.el %{buildroot}%{_datadir}/emacs/site-lisp/
%if %{with xemacs}
# compile the XEmacs versions of the emacs-lisp files and install them:
pushd src-util
    rm -f *.elc
    # make EMACS=xemacs
    EMACS=xemacs ../elisp-comp *.el
    mkdir -p %{buildroot}%{_datadir}/xemacs/site-packages/lisp/anthy
    install -m 644 *.el *.elc %{buildroot}%{_datadir}/xemacs/site-packages/lisp/anthy
popd
%endif
%fdupes %{buildroot}%{_datadir}
find %{buildroot} -type f -name "*.la" -delete -print
# remove unneeded Makefiles for documents
rm -f doc/Makefile.*

%post   -n libanthy0 -p /sbin/ldconfig
%postun -n libanthy0 -p /sbin/ldconfig

%files
%doc AUTHORS ChangeLog DIARY NEWS README doc
%license COPYING
%config %{_sysconfdir}/anthy-conf
%dir %{_datadir}/anthy/
%{_datadir}/anthy/*
%{_bindir}/*
%{_datadir}/emacs/site-lisp/*
%if %{with xemacs}
%{_datadir}/xemacs/*
%endif

%files -n libanthy0
%{_libdir}/*.so.*

%files devel
%dir %{_includedir}/anthy/
%{_includedir}/anthy/*
%{_libdir}/*.so
%{_libdir}/pkgconfig/anthy.pc

%changelog
