#
# spec file for package nkf
#
# Copyright (c) 2015 SUSE LINUX Products GmbH, Nuernberg, Germany.
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


Name:           nkf
License:        BSD-3-Clause
Group:          System/I18n/Japanese
Requires:       perl = %{perl_version}
Provides:       locale(ja)
Version:        2.1.3
Release:        0
Url:            http://sourceforge.jp/projects/nkf/
#             http://www01.tcp-ip.or.jp/~furukawa/nkf_utf8/
Source0:        %{name}-%{version}.tar.gz
BuildRoot:      %{_tmppath}/%{name}-%{version}-build
Summary:        Network Kanji Code Conversion Filter
# Summary(ja):  ネットワーク用漢字コード変換フィルタ 
# %description -l ja
# nkfはネットワークでメールやニュースの読み書きをするために作られた、漢
# 字コードの変換フィルタである。
# 
# このnkfの特徴としては、入力漢字コード系の統計的な自動認識機能がある。
# このため、利用者は、入力漢字コード系が何であるかを知らなくても、出力漢字
# コード系のみ指定すれば良いことになる。ただ、この判定機構は、理論的には完
# 全ではないが、通常のニュースやメールのメッセージについては確実に動作する
# 安全なものにはなっている。
# 
# 現在、nkfが認識できる入力の漢字コード系は、いわゆる「JISコード」(ISO-
# 2022-JPに基づくもの)、MS漢字コード(シフトJIS)、日本語EUC(AT&Tコード)のい
# ずれかである。出力する漢字コード系も、この3種類である。
# 
# Authors:
# --------
#     Itaru ICHIKAWA <ichikawa@flab.fujitsu.co.jp>
#     Akihiko Kuroe <a_kuroe@hoffman.cc.sophia.ac.jp>
#     Shinji KONO  <kono@ie.u-ryukyu.ac.jp>

%description
Nkf is a yet another Kanji code converter among networks, hosts, and
terminals. It converts input Kanji code to designated Kanji code, such
as 7-bit JIS, MS-kanji (shifted-JIS) or EUC.

One of the most unique facility of nkf is the guess of the input kanji
code.  It currently recognizes 7-bit JIS, MS-kanji (shifted-JIS), and 
EUC. So users do not need the input Kanji code specification.

By  default,  X0201  kana is converted into X0208 kana. For X0201 kana,
SO/SI, SSO and ESC-(-I methods are  supported. For automatic code
detection, nkf assumes no X0201 kana in MS-Kanji. To accept X0201 in
MS-Kanji, use -X, -x, or -S.

%package -n perl-NKF
License:        BSD-3-Clause
Group:          Development/Libraries/Perl
Requires:       perl >= 5.6.0
Summary:        Perl extension for nkf (Network Kanji Filter)
BuildRequires:  perl
# Summary(ja):  Perl拡張モジュール版NKF
# %description -n perl-NKF -l ja
# これは、Perl から nkf を使う拡張モジュールです。
# 
# 使い方は、
#
# 	use NKF;
# 	$output = nkf($flag,$input);
# 
# のように使います。flag は、nkf と同じです。
# 
# Authors:
# --------
# 
#   Shinji Kono  <kono@ie.u-ryukyu.ac.jp>

%description -n perl-NKF 
This is a Perl Extension version of nkf (Network Kanji Filter ) 1.9.

Usage:

use NKF; $output = nkf($flag,$input);

$flag has the same meaning as with nkf.

%prep
%setup -q
iconv -f ISO-2022-JP -t EUC-JP nkf.1j > nkf.1j.EUC-JP
mv nkf.1j.EUC-JP nkf.1j

%build
export CFLAGS="$RPM_OPT_FLAGS"
make CFLAGS="$RPM_OPT_FLAGS"
make test
make perl

%install
install -d %{buildroot}/usr/bin
install -d %{buildroot}%{_mandir}/ja/man1/
install -d %{buildroot}%{_mandir}/man1
install -m 755 nkf %{buildroot}/usr/bin/nkf
install -m 644 nkf.1 %{buildroot}%{_mandir}/man1
install -m 644 nkf.1j \
                         %{buildroot}%{_mandir}/ja/man1/nkf.1
make -C NKF.mod DESTDIR=$RPM_BUILD_ROOT install_vendor
%perl_process_packlist

%files
%defattr(-,root,root)
%doc nkf.doc
%{_bindir}/nkf
%{_mandir}/man1/nkf.1.gz
%{_mandir}/ja/man1/nkf.1.gz

%files -n perl-NKF
%defattr(-,root,root)
%{_mandir}/man3/NKF.3pm.gz
%{perl_vendorarch}/NKF.pm
%{perl_vendorarch}/auto/NKF/

%changelog
