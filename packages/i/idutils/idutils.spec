#
# spec file for package idutils
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


Name:           idutils
Version:        4.6
Release:        0
Summary:        Language-Independent Identifier Database Tool
License:        GPL-2.0-or-later
Group:          Productivity/Text/Utilities
Url:            http://www.gnu.org/software/idutils/
Source0:        ftp://ftp.gnu.org/pub/gnu/idutils/idutils-%{version}.tar.xz
Source1:        ftp://ftp.gnu.org/pub/gnu/idutils/idutils-%{version}.tar.xz.sig
Source2:        %{name}.keyring
Patch0:         gnulib.patch
BuildRequires:  emacs-nox
BuildRequires:  xz
Requires(preun): %{install_info_prereq}
Requires(post): %{install_info_prereq}
Recommends:     %{name}-lang
Provides:       id-utils
Obsoletes:      id-utils
BuildRoot:      %{_tmppath}/%{name}-%{version}-build

%description
Mkid is a simple, fast, high-capacity, and language-independent
identifier database tool.  Actually, the term identifier is too
limiting--mkid stores tokens, be they program identifiers of any form,
literal numbers, or ordinary words.  Database queries can be issued
from the command line or from within Emacs, serving as an augmented
tags facility.

%lang_package

%prep
%setup -q
%patch0 -p1

%build
%configure
# fix gets compile error https://lists.gnu.org/archive/html/grub-devel/2012-07/msg00051.html
sed -i -e '/gets is a security/d' lib/stdio.in.h
make %{?_smp_mflags}

%install
make DESTDIR=%{buildroot} install %{?_smp_mflags}
install -d %{buildroot}%{_localstatedir}/lib/idutils
mv %{buildroot}%{_datadir}/id-lang.map %{buildroot}%{_localstatedir}/lib/idutils
ln -s ../..%{_localstatedir}/lib/idutils/id-lang.map %{buildroot}%{_datadir}/id-lang.map
# Conflict with libuser
rm -f %{buildroot}%{_mandir}/man1/lid.1
%find_lang %{name}

%post
if test -f %{_infodir}/id-utils.info.gz; then
  mv %{_infodir}/id-utils.info.gz %{_infodir}/id-utils.info.gz.rpmdelete
  %install_info_delete --info-dir=%{_infodir} %{_infodir}/id-utils.info.gz
  mv %{_infodir}/id-utils.info.gz.rpmdelete %{_infodir}/id-utils.info.gz
fi
%install_info --info-dir=%{_infodir} %{_infodir}/idutils.info.gz

%preun
%install_info_delete --info-dir=%{_infodir} %{_infodir}/idutils.info.gz

%files
%defattr(-,root,root)
%doc ABOUT-NLS AUTHORS NEWS README THANKS TODO
%license COPYING
%config %{_localstatedir}/lib/idutils/id-lang.map
%dir %{_localstatedir}/lib/idutils
%{_datadir}/id-lang.map
%{_datadir}/emacs/site-lisp/idutils.el
%{_datadir}/emacs/site-lisp/idutils.elc
%{_bindir}/*
%{_mandir}/man1/*
%{_infodir}/idutils.info*

%files lang -f %{name}.lang
%defattr(-,root,root)

%changelog
