#
# spec file for package skkdic
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


%global         skkdic_commit  4eb91a3bbfef70bde940668ec60f3beae291e971
%global         commit_date    20240829
Name:           skkdic
Version:        %{commit_date}
Release:        0
Summary:        SKK (Simple Kana-Kanji) dictionary files.
License:        Unicode-DFS-2016
Group:          System/I18n/Japanese
URL:            https://skk-dev.github.io/dict/
Source0:        https://github.com/skk-dev/dict/archive/%{skkdic_commit}/skkdic-%{commit_date}.git%{skkdic_commit}.tar.gz
Requires(post): info
Requires(preun): info
Provides:       locale(scim-skk:ja)
BuildArch:      noarch

%description
main dictionary for SKK.

%package -n skkdic-extra
Summary:        Optional, additional dictionaries for SKK
Group:          System/I18n/Japanese
URL:            https://skk-dev.github.io/dict/
Requires(post): info
Requires(preun): info
BuildArch:      noarch

%description -n skkdic-extra
optional, additional dictionaries for SKK.

%prep
%autosetup -n dict-%{skkdic_commit}

%build

%install
install -d -m 755 "%{buildroot}%{_datadir}/skk"
for skkdic in SKK-JISYO* zipcode/SKK-JISYO*; do
    [ -f "$skkdic" ] && install -p -m 644 "$skkdic" "%{buildroot}%{_datadir}/skk/"
done

%files
%dir %{_datadir}/skk/
%{_datadir}/skk/SKK-JISYO.L
%{_datadir}/skk/SKK-JISYO.L.unannotated

%files -n skkdic-extra
%dir %{_datadir}/skk/
%{_datadir}/skk/SKK-JISYO.JIS2
%{_datadir}/skk/SKK-JISYO.JIS2004
%{_datadir}/skk/SKK-JISYO.JIS3_4
%{_datadir}/skk/SKK-JISYO.M
%{_datadir}/skk/SKK-JISYO.ML
%{_datadir}/skk/SKK-JISYO.S
%{_datadir}/skk/SKK-JISYO.assoc
%{_datadir}/skk/SKK-JISYO.china_taiwan
%{_datadir}/skk/SKK-JISYO.china_taiwan.header
%{_datadir}/skk/SKK-JISYO.edict
%{_datadir}/skk/SKK-JISYO.edict2
%{_datadir}/skk/SKK-JISYO.emoji
%{_datadir}/skk/SKK-JISYO.fullname
%{_datadir}/skk/SKK-JISYO.geo
%{_datadir}/skk/SKK-JISYO.hukugougo
%{_datadir}/skk/SKK-JISYO.itaiji
%{_datadir}/skk/SKK-JISYO.itaiji.JIS3_4
%{_datadir}/skk/SKK-JISYO.ivd
%{_datadir}/skk/SKK-JISYO.jinmei
%{_datadir}/skk/SKK-JISYO.law
%{_datadir}/skk/SKK-JISYO.lisp
%{_datadir}/skk/SKK-JISYO.mazegaki
%{_datadir}/skk/SKK-JISYO.noregist
%{_datadir}/skk/SKK-JISYO.not_wrong
%{_datadir}/skk/SKK-JISYO.notes
%{_datadir}/skk/SKK-JISYO.office.zipcode
%{_datadir}/skk/SKK-JISYO.okinawa
%{_datadir}/skk/SKK-JISYO.pinyin
%{_datadir}/skk/SKK-JISYO.propernoun
%{_datadir}/skk/SKK-JISYO.pubdic+
%{_datadir}/skk/SKK-JISYO.requested
%{_datadir}/skk/SKK-JISYO.station
%{_datadir}/skk/SKK-JISYO.wrong
%{_datadir}/skk/SKK-JISYO.wrong.annotated
%{_datadir}/skk/SKK-JISYO.zipcode

%changelog
