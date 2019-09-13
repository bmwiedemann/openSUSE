#
# spec file for package xmanja
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


Name:           xmanja
Version:        0.7
Release:        0
Summary:        Japanese online manuals for X11
License:        MIT
Group:          Documentation/Man
Summary(ja):  XFree86 のオンラインマニュアル、 日本語版
Url:            http://xjman.dsl.gr.jp/
Source0:        http://xjman.dsl.gr.jp/dist/xjman-0.7.tar.bz2
Source1:        license.txt
BuildRoot:      %{_tmppath}/%{name}-%{version}-build
BuildArch:      noarch
Provides:       locale(xorg-x11:ja)
# %description -l ja
# XFree86 のオンラインマニュアル、 日本語版

%description
Japanese online manuals for X11



Authors:
--------
    X Japanese Documentation Project <xjman-ml@dsl.gr.jp>

%prep
%setup -qn xjman

%build
cp %{SOURCE1} license.txt

%install
for i in man? ; do
  mkdir -p $RPM_BUILD_ROOT/usr/share/man/ja/$i
  install -m 644 $i/* $RPM_BUILD_ROOT/usr/share/man/ja/$i
done
# install Japanese WindowMaker man-pages in /usr/share/man
# because that's where the English ones are
mkdir -p $RPM_BUILD_ROOT/usr/share/man/ja/man1/
install -m 644 non-xfree86/WindowMaker/*.1x $RPM_BUILD_ROOT/usr/share/man/ja/man1/
# conflicts with man-pages-ja package:
rm $RPM_BUILD_ROOT/usr/share/man/ja/man4/mouse.4*

%files
%defattr(-,root,root)
%doc README license.txt ChangeLog
%dir /usr/share/man/ja/
%doc /usr/share/man/ja/*

%changelog
