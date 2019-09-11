#
# spec file for package eblook
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


Name:           eblook
Version:        1.6.1
Release:        0
Summary:        Command Line Tool for Searching Electronic Dictionaries
License:        GPL-2.0+
Group:          Productivity/Office/Dictionary
Url:            http://openlab.ring.gr.jp/lookup/eblook/
# original source: http://openlab.ring.gr.jp/edict/eblook/dist/eblook-1.5.1.tar.gz
Source0:        http://openlab.ring.gr.jp/edict/eblook/dist/eblook-%{version}.tar.bz2
Patch0:         eblook-strcpy.patch
Patch1:         eblook-size_t.patch
Patch2:         eblook-ssize_t.patch
BuildRequires:  eb
BuildRequires:  ebdev
BuildRequires:  libtool
BuildRequires:  zlib-devel
Requires:       eb
# FIXME: use proper Requires(pre/post/preun/...)
PreReq:         %{install_info_prereq}
BuildRoot:      %{_tmppath}/%{name}-%{version}-build
# Summary(ja): eblook は、EB ライブラリを用いた対話型の電子辞書検索コマンドです。
# %description -l ja
# eblook は、EB ライブラリを用いた対話型の電子辞書検索コマンドです。簡単な
# 設定とコマンドにより CD-ROM 書籍が利用出来ます。
#
# 著者:
# -----
#     Keisuke Nishida <knishida@ring.gr.jp> wrote eblook.c and eblook.texi.
#     Keisuke MORI <ksk@ntts.com> compiled eblook on the Cygwin environment.

%description
eblook is a command line tool that uses the EB library. It provides
easy access to many electronic dictionaries published on CD-ROM.

It is recommended that you install the Emacs interface lookup.el, too.
Although it is possible to use eblook from the command line, using it
with Emacs or XEmacs and lookup.el is much easier and offers many extra
features.

You can get lookup.el from http://lookup.sourceforge.net/.

lookup.el is already included as a package in recent versions of
XEmacs.

%prep
%setup -q
%patch0 -p1
%patch1 -p2
%patch2 -p1

%build
# update config.{guess,sub}
%{?suse_update_config}
libtoolize --force
autoreconf --force --install
%configure --with-eb-conf=%{_sysconfdir}/eb.conf
make %{?_smp_mflags}

%install
make transform="" DESTDIR=%{buildroot} install

%post
%install_info --info-dir=%{_infodir} %{_infodir}/eblook.info.gz

%postun
%install_info_delete --info-dir=%{_infodir} %{_infodir}/eblook.info.gz

%files
%defattr(-, root, root)
%doc AUTHORS COPYING INSTALL NEWS README VERSION ChangeLog
%{_bindir}/*
%{_infodir}/eblook*

%changelog
