#
# spec file for package tamago
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


Name:           tamago
#Upstream name is tamago-tsunagi
%define tsunagiName %{name}-tsunagi
# 2015-02-03 Mitsutoshi NAKANO <bkbin005@rinku.zaq.ne.jp>
# I think tamago does not need X.
# tamago-tsunagi needs Emacs >= 23
#BuildRequires:  emacs-x11
BuildRequires:  emacs-nox >= 23
Requires:       emacs >= 23
Version:        5.0.7.1
Release:        0
Url:            http://sourceforge.jp/projects/tamago-tsunagi/
# Other useful, tamago related URLs:
#     http://emacs-20.ki.nu/tamago/
#     http://cgi18.plala.or.jp/~nyy/canna/
#     http://www.gcd.org/sengoku/boiling-egg/
#     ftp://ftp.ki.nu/pub/emcws/README.html  (obsoleted by tamago)

Source0:        http://osdn.dl.sourceforge.jp/tamago-tsunagi/62701/%{tsunagiName}-%{version}.tar.gz

# egg-canna.el was deleted 2013-08-27 by bkbin005@rinku.zaq.ne.jp
#Source1:        http://cgi18.plala.or.jp/nyy/canna/egg-canna.el.bz2

Source2:        boiling-egg.el.bz2
Source3:        http://iij.dl.sourceforge.jp/tamago-tsunagi/62684/ISFST99.pdf.bz2
Source4:        http://iij.dl.sourceforge.jp/tamago-tsunagi/62685/LC99.pdf.bz2
Source5:        suse-start.el
Patch0:         eggrc.patch
#BuildRoot:      %%{_tmppath}/%%{name}-%%{version}-build
BuildArch:      noarch
Summary:        Multilingual input method for Emacs
License:        GPL-2.0+
Group:          System/I18n/Japanese

%description
Tamago offers a multilingual input environment for GNU Emacs (>= 23.x).
It is completely written in Emacs Lisp and can use the backends FreeWnn
(jserver, cserver, tserver), Wnn6, SJ3 Ver.2, and Canna.

%prep
%setup -q -n %{tsunagiName}-%{version}
%patch0 -p1

cp -p $RPM_SOURCE_DIR/suse-start.el .
#cp -p $RPM_SOURCE_DIR/egg-canna.el.bz2 . # deleted 2013-08-27 .
cp -p $RPM_SOURCE_DIR/boiling-egg.el.bz2 .
cp -p $RPM_SOURCE_DIR/*.pdf.bz2 .
bunzip2 *.bz2
find -type d -name "CVS" | xargs rm -rfv

%build
%define emacs_sitelisp_dir %{_datadir}/emacs/site-lisp
%define emacs_package_dir %{emacs_sitelisp_dir}/egg
./configure --prefix=/usr
make
for i in boiling-egg # egg-canna was deleted 2013-08-27
do
   emacs -batch -q -no-site-file -no-init-file -f batch-byte-compile $i.el
done

%install
if [ -n "%{?buildroot}" ] ; then
   [ %{buildroot} != "/" ] && rm -rf %{buildroot}
fi
mkdir -p $RPM_BUILD_ROOT%{emacs_sitelisp_dir}
make install prefix=$RPM_BUILD_ROOT/usr
for i in boiling-egg # egg-canna was deleted 2013-08-27 .
do
    install -m644 $i.{el,elc} $RPM_BUILD_ROOT%{emacs_sitelisp_dir}
done
{
  echo ";; %{emacs_sitelisp_dir}/suse-start-%{name}.el"
  echo ""
  echo "(add-to-list 'load-path \"%{emacs_package_dir}\")"
  echo ""
  cat suse-start.el
  echo ""
  echo ";; %{emacs_sitelisp_dir}/suse-start-%{name}.el ends here"
} > %{buildroot}%{emacs_sitelisp_dir}/suse-start-%{name}.el

%clean
rm -fr $RPM_BUILD_ROOT

%files
%defattr(-,root,root)
%doc AUTHORS COPYING ChangeLog* PROBLEMS README* TODO NEWS *.pdf doc/*
%{emacs_package_dir}
%{emacs_package_dir}/egg/.nosearch
%{emacs_package_dir}/its/.nosearch
%{emacs_sitelisp_dir}/suse-start-%{name}.el
%{emacs_sitelisp_dir}/boiling-egg.el
%{emacs_sitelisp_dir}/boiling-egg.elc

%changelog
