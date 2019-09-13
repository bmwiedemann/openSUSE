#
# spec file for package canna-yubin
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


Name:           canna-yubin
BuildRequires:  canna
Version:        0.4.0.20190228.0
Release:        0
Url:            https://osdn.net/projects/canna-yubin/
Source0:        https://jaist.dl.osdn.jp/%{name}/70759/%{name}-%{version}.tar.xz
Source1:        https://jaist.dl.osdn.jp/%{name}/70759/%{name}-%{version}.tar.xz.asc
Source2:        https://jaist.dl.osdn.jp/%{name}/70760/%{name}.keyring
BuildRoot:      %{_tmppath}/%{name}-%{version}-build
Summary:        Postal Code Extension Dictionary for Canna
License:        GPL-2.0-or-later AND SUSE-Public-Domain
Group:          System/I18n/Japanese
BuildArch:      noarch
Requires(pre):  shadow

# Summary(ja): 郵便番号データのCanna用の辞書
# _description -l ja
# 郵便番号データのCanna用の辞書
# 
# 著者：
# ------
#     Japanese Ministry of Posts and Telecommunications
#     Yoshito Komatsu

%description
A Japanese postal code number extension dictionary for Canna .

%prep
%setup -q

%build
%configure
# make binary dictionaries:
make

%install
%define canna_system_dic_dir %{_var}/lib/canna/dic/canna
%make_install

%pre
getent passwd wnn >/dev/null || \
	%{_sbindir}/useradd -r -o -g root -u 66 -s /bin/false \
	-c "Wnn System Account" -d %{_localstatedir}/lib/wnn wnn

%files
%defattr(-, root, root)
%doc README* AUTHORS NEWS COPYING COPYING.GPL2
%attr(-, wnn, root) %{canna_system_dic_dir}/*

%changelog
