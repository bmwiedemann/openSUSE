#
# spec file for package cannadic
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


Name:           cannadic
BuildRequires:  canna-devel
License:        GPL-2.0+
Group:          System/I18n/Japanese
Version:        0.95c
Release:        0
Url:            http://cannadic.oucrc.org/
Source0:        http://cannadic.oucrc.org/%{name}-%{version}.tar.gz
BuildRoot:      %{_tmppath}/%{name}-%{version}-build
Summary:        Extension Dictionary for Canna
# Summary(ja): かんな辞書(拡張版)
# %description -l ja
# 本辞書は Canna3.5b2 標準添付の辞書を補完する目的で編纂したものです。 
# GPL で配布されているかな漢字変換辞書、 および改変した辞書の再配布に制
# 限が課せられていないかな漢字変換辞書を ベースとしてかんな辞書形式に再
# 構成し、 個人的利用の中で不足した単語を逐次追加収録してあります。 現在、
# 自立語辞書および付属語辞書の総単語数は約130,000語あります。
# 著者：
# ------
#     Masao Sugimoto <nowaki@osk3.3web.ne.jp>

%description
This dictionary has been compiled as a supplement to the dictionaries
distributed with Canna3.5b2. It is based on Kana-Kanji conversion
dictionaries distributed under the GPL and Kana-Kanji conversion
distributed without restrictions. While using this dictionary, many
missing words have been successively added. Currently the main
dictionary and the suffix and prefix dictionary together contain about
130,000 words.


%prep
%setup -q

%build
%define canna_dir /var/lib/canna
%define canna_dic_dir /var/lib/canna/dic
%define canna_system_dic_dir %{canna_dic_dir}/canna
%define canna_user_dic_dir %{canna_dic_dir}/user
%define canna_root_dic_dir %{canna_user_dic_dir}/root
make maindic
make subdic

%install
mkdir -p %{buildroot}%{canna_system_dic_dir}
install -m 644 gcanna.cbd gcanna.cld $RPM_BUILD_ROOT%{canna_system_dic_dir}
# Installing the adjunct dictionary gcannaf as a binary dictionary
# crashes the cannaserver!
# Install a text dictionary of the adjunct dictionary gcannaf instead:
# (contrary to the binary version, the text version seems to work!)
#install -m 644 gcannaf.cbd gcannaf.cld $RPM_BUILD_ROOT%{canna_system_dic_dir}
install -m 644 gcannaf.ctd $RPM_BUILD_ROOT%{canna_system_dic_dir}

%pre
/usr/sbin/useradd -r -o -g bin -u 66 -s /bin/false -c "Wnn System Account" -d /var/lib/wnn wnn 2> /dev/null || :

%files -n cannadic
%defattr(-, root, root)
%doc COPYING README.ja
%dir %{canna_dir}/
%dir %attr(-, wnn, root) %{canna_dic_dir}/
%dir %attr(-, wnn, root) %{canna_system_dic_dir}/
%attr(-, wnn, root) %{canna_system_dic_dir}/*

%changelog
