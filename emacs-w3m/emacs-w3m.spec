#
# spec file for package emacs-w3m
#
# Copyright (c) 2018 SUSE LINUX GmbH, Nuernberg, Germany.
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


Name:           emacs-w3m
Summary:        An interface program to use w3m with Emacs
License:        GPL-2.0-or-later
Group:          Productivity/Networking/Web/Browsers
# Summary(ja): w3m を Emacs 上で動かすためのプログラムです
Version:        1.4.631
Release:        0
Url:            http://emacs-w3m.namazu.org/
# cvs -d :pserver:anonymous@cvs.namazu.org:/storage/cvsroot login
# (CVS password empty)
# cvs -d :pserver:anonymous@cvs.namazu.org:/storage/cvsroot co emacs-w3m
Source0:        emacs-w3m-%{version}.tar.bz2
Source1:        suse-start.el
Patch1:         w3m-el-1.3-map.patch
BuildRoot:      %{_tmppath}/%{name}-%{version}-build
BuildArch:      noarch
BuildRequires:  autoconf
BuildRequires:  emacs-nox
BuildRequires:  flim
BuildRequires:  makeinfo
Requires:       apel
Requires:       emacs
Requires:       flim
Requires:       w3m
Provides:       w3m-el = %{version}
Obsoletes:      w3m-el < %{version}
# %description -l ja
# Emacs 上で動作するブラウザと言えば，普通 W3 のことですが，動作が非常に
# 遅いので，なかなか常用しようという気になれません．
# 
# それに対して，w3m というテキストベースで動作するブラウザがあり，非常に
# 軽快に動作するので重宝しているのですが，端末に移動しなければいけないの
# が面倒です．
# 
# そこで，w3m を HTML の rendering engine として使用し，表示とインタフェー
# スのみをEmacs で動かすようにすればいいんじゃないだろうか，ということを
# 考えました．

%description
Emacs-w3m is an interface program to use w3m with Emacs.

W3 is the most well known WEB browser which works on (X)Emacs, but it
is very slow. Emacs-w3m is an alternative. It uses w3m, which is a pager
with WWW capability, developed by Akinori ITO. It is a pager, but it
can be used as a text-mode WWW browser.

%prep
%setup -q
%patch1

%build
%define emacs_sitelisp_dir %{_datadir}/emacs/site-lisp
%define emacs_package_dir %{emacs_sitelisp_dir}/w3m
autoreconf --force --install
%configure \
            --with-lispdir=%{emacs_package_dir} \
            --with-icondir=%{emacs_package_dir} \
            --with-emacs=emacs 
make 

%install
mkdir -p %{buildroot}/%{emacs_package_dir}
%make_install install-icons
{
  echo ";; %{emacs_sitelisp_dir}/suse-start-%{name}.el"
  echo ""
  echo "(add-to-list 'load-path \"%{emacs_package_dir}\")"
  echo ""
  cat %{_sourcedir}/suse-start.el
  echo ""
  echo ";; %{emacs_sitelisp_dir}/suse-start-%{name}.el ends here"
} > %{buildroot}%{emacs_sitelisp_dir}/suse-start-%{name}.el
rm -f %{buildroot}/%{_infodir}/dir
rm -f %{buildroot}/%{emacs_package_dir}/ChangeLog*

%post
for i in emacs-w3m emacs-w3m-ja
do
    %install_info --info-dir=%{_infodir} %{_infodir}/${i}.info.gz
done

%preun
for i in emacs-w3m emacs-w3m-ja
do
    %install_info_delete --info-dir=%{_infodir} %{_infodir}/${i}.info.gz
done

%files
%defattr(-,root,root)
%license COPYING
%doc ChangeLog* README*
%{emacs_package_dir}
%config %{emacs_sitelisp_dir}/suse-start-%{name}.el
%{_infodir}/*

%changelog
