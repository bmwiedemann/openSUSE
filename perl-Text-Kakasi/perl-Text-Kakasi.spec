#
# spec file for package perl-Text-Kakasi
#
# Copyright (c) 2014 SUSE LINUX Products GmbH, Nuernberg, Germany.
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


Name:           perl-Text-Kakasi
BuildRequires:  kakasi-devel
Requires:       kakasi >= 2.3.4
Version:        2.04
Release:        0
Url:            http://www.daionet.gr.jp/~knok/kakasi/
Source0:        http://search.cpan.org/CPAN/authors/id/D/DA/DANKOGAI/Text-Kakasi-2.04.tar.gz
BuildRoot:      %{_tmppath}/%{name}-%{version}-build
Summary:        Perl binding for KAKASI, the kanji kana simple inverter
License:        GPL-2.0+
Group:          Development/Libraries/Perl
%{perl_requires}
BuildRequires:  perl
BuildRequires:  perl-macros
# Summary(ja): KAKASIを perlから利用するためのモジュールです。
# %description -l ja
# このモジュールは、高橋裕信さんの作成されたソフトウェアKAKASIを
# perlから用いるためのものです。
# 
# このモジュールを使うためには、最新版のKAKASI(2.3.0以降)が必要です。最
# 新版に関しては、<http://kakasi.namazu.org/>を参照してください。

%description
This module provides libkakasi interface for perl. libkakasi is a part
of KAKASI.  KAKASI is the language processing filter to convert Kanji
characters to Hiragana, Katakana or Romaji and may be helpful to read
Japanese documents.  More information about KAKASI is available at
<http://kakasi.namazu.org/>.

%prep
%setup -n Text-Kakasi-%{version} 

%build
CFLAGS="$RPM_OPT_FLAGS" perl Makefile.PL
make %{?_smp_mflags}

%install
%perl_make_install
%perl_process_packlist
%perl_gen_filelist

%files -f %{name}.files
%defattr(-,root,root)
%doc COPYING Changes ChangeLog* MANIFEST README*

%changelog
