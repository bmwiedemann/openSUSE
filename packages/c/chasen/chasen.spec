#
# spec file for package chasen
#
# Copyright (c) 2025 SUSE LLC
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


Name:           chasen
Version:        2.4.5
Release:        0
Summary:        Japanese Morphological Analysis System
License:        BSD-3-Clause
Group:          System/I18n/Japanese
URL:            https://osdn.net/projects/chasen-legacy
Source0:        %{URL}/downloads/56305/chasen-%{version}.tar.xz
Patch1:         chasen-decls.diff
# PATCH-FIX-UPSTREAM
Patch2:         chasen-initialize-memory.patch
#PATCH-FIX-UPSTREAM fix arbitrary arguments
Patch3:         chasen-2.4.5-gcc15.patch
BuildRequires:  darts
BuildRequires:  gcc-c++
BuildRequires:  libtool
Requires:       ipadic
# Summary(ja): 形態素解析システム 茶筌
# %description -l ja
# 計算機による日本語の解析において，欧米の言語の解析と比べてまず問題になるの
# に次の2点があります．一つは形態素解析の問題です．ワードプロセッサの普及など
# によって日本語の入力には大きな問題がなくなりましたが，計算機による日本語解
# 析では，まず入力文内の個々の形態素を認識する必要があります．これには実用に
# 耐えられるだけの大きな辞書も必要であり，これを如何に整備するかという問題も
# 同時に存在します．もう一つの問題として，日本語には広く認められ同意を得られ
# た文法，ないし，文法用語がないという現実です．学校文法の単語分類および文法
# 用語は一般には広く知られていますが，研究者の間ではあまり評判がよくありませ
# んし，計算機向きではありません．
#
# 日本語の解析に真っ先に必要な形態素解析システムは，多くの研究グループによっ
# て既に開発され技術的な問題が洗い出されているにも係わらず，共通のツールとし
# て世の中に流布しているものはありません．計算機可読な日本語辞書についても同
# 様です．
#
# 本システムは，計算機による日本語の解析の研究を目指す多くの研究者に共通に使
# える形態素解析ツールを提供するために開発されました．その際，上の二つ目の問
# 使用者によって文法の定義，単語間の接続関係の定義などを容易に変更
# できるように配慮しました．
#
# 大学で小人数で開発したシステムであり，色々な点で不完全な部分があると思いま
# す．可能な限り順次改良を重ねる予定です．皆様の寛容な利用をお願いいたします．
#
#
# 本茶筌システムの原形は，京都大学長尾研究室および奈良先端科学技術大学院大学
# 松本研究室において開発された日本語形態素解析システムJUMAN(version2.0)です．
# JUMANは，京都大学および奈良先端科学技術大学院大学のスタッフおよび多くの学生
# の協力を得て作成したものです．また，辞書に関しては，Wnnかな漢字変換システム
# の辞書，および，ICOTから公開された日本語辞書を利用し，独自に修正を加えまし
# た．JUMAN 2.0をともに開発した京都大学の黒橋禎夫さん，現在キャノン勤務の妙木
# 裕さんには特に感謝いたします．
#
# JUMAN開発のきっかけを作って下さった京都大学長尾真先生に感謝します．JUMAN開
# 発に関して様々な形で協力していただいた奈良先端大宇津呂武仁氏に感謝します．
# 奈良先端大の知念賢一氏には，茶筌システムの開発に関して多くの助言をいただき
# ました．
# 奈良先端大在学時の今一修氏，今村友明氏には茶筌1.0の開発の際に種々の助
# 力をいただきました．両氏および茶筌の開発に協力いただいた松本研究室のメ
# ンバーに深く感謝します．
# 奈良先端大の鹿野清宏教授を代表とする「日本語ディクテーショ
# ン基本ソフトウェアの開発」グループの方々には，IPA品詞体系辞書の大幅な
# 整備を行っていただきました．特に，御尽力いただいた電子技術総合研究所の
# 伊藤氏，ASTEMの山田篤氏に感謝いたします．
# また，一人一人の名を挙げることはできませんが，JUMANシステムおよび
# 茶筌システムに対して多くのコメントと質問をいただいた利用者の方々に感謝します．
#
#
# 本システムに関するお問い合わせは以下にお願いします．

%description
ChaSen is a Japanese morphological analysis system.

%package devel
Summary:        Libraries and header files for ChaSen developers
Group:          Development/Libraries/C and C++
Requires:       %{name} = %{version}
# Summary(ja): 茶筌のライブラリとヘッダファイルです.
# %description -l ja devel
#
# 茶筌のライブラリとヘッダファイルです.

%description devel
Libraries and header files for ChaSen developers.

%package -n perl-Text-ChaSen
Summary:        ChaSen Perl Module
Group:          Development/Libraries/Perl
Requires:       %{name} = %{version}
Requires:       perl = %{perl_version}
Provides:       chasen-perl
Obsoletes:      chasen-perl
# Summary(ja): このモジュールは、「茶筌」をperlから扱うためのものです.
# %description -l ja perl-Text-ChaSen
#
# このモジュールは、奈良先端科学技術大学が作成した形態素解析ソフトウェア
# 「茶筌」をperlから扱うためのものです.

%description -n perl-Text-ChaSen
ChaSen Perl Module

%prep
%setup -q
%patch -P 1
%patch -P 2 -p1
%patch -P 3 -p1

%build
autoreconf --force --install
export CFLAGS="%{optflags}"
# fix build
export CXXFLAGS="%{optflags} -fpermissive"
%configure --disable-static --with-darts="%{_includedir}"
%make_build
pushd perl
    perl Makefile.PL
    %make_build INC="-I../src -I%{_includedir} -I/usr/include" \
         LDDLFLAGS="-shared -Wl,-rpath -Wl,%{_prefix}/lib -L../lib/.libs -lchasen"
         CCFLAGS="$CCFLAGS -Dna=PL_na -Dsv_undef=PL_sv_undef"
popd

%install
%make_install
make -C perl DESTDIR=%{buildroot} install_vendor
%perl_process_packlist
find %{buildroot} -type f -name "*.la" -delete -print

%post -p /sbin/ldconfig
%postun -p /sbin/ldconfig

%files
%license COPYING
%doc AUTHORS ChangeLog NEWS README*
%doc doc/*.tex doc/*.pdf
%{_bindir}/chasen
%{_libdir}/*.so.*
%{_libexecdir}/chasen
%if 0%{?suse_version} < 1140
%ghost %{_localstatedir}/adm/perl-modules/chasen
%endif

%files devel
%{_bindir}/chasen-config
%{_includedir}/*
%{_libdir}/*.so

%files -n perl-Text-ChaSen
%doc perl/README
%{_mandir}/man3/Text::ChaSen.3pm.gz
%{perl_vendorarch}/Text/
%{perl_vendorarch}/auto/Text/

%changelog
