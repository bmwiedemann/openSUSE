#
# spec file for package elib
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


Name:           elib
BuildRequires:  emacs-x11
%if 0%{suse_version} > 1220
BuildRequires:  makeinfo
%endif
Requires:       emacs
PreReq:         %install_info_prereq
Version:        1.0
Release:        0
Summary:        A Lisp Library for GNU Emacs
License:        GPL-2.0+
Group:          Productivity/Editors/Emacs
Source:         elib-1.0.tar.bz2
Patch:          elib-1.0.dif
BuildRoot:      %{_tmppath}/%{name}-%{version}-build
BuildArch:      noarch

%description
This package contains the complete GNU Emacs Lisp Library, Elib Version
1.0.  Elib was developed as a library for Emacs-Lisp programs for the
same reasons that libg++ was developed for C++ programs.

Elib contains macros for:

- container data structures (queues, stacks, AVL trees, and more)

- string handling routines missing in standard Emacs

- routines to handle cookies in a buffer

%prep
%setup -q
%patch

%build
%define prefix /usr
%define datadir %{prefix}/share
%define locallisppath %{datadir}/emacs/site-lisp
%define ELIBDIR %{locallisppath}/elib
export LC_CTYPE=ISO-8859-1
export EMACS_UNIBYTE=1
make prefix=%{prefix} \
     datadir=%{datadir} \
     locallisppath=%{locallisppath} \
     ELIBDIR=%{ELIBDIR} \
     infodir=%{_infodir} \
     MAKEINFO="makeinfo --force"

%install
export LC_CTYPE=ISO-8859-1
export EMACS_UNIBYTE=1
mkdir -p $RPM_BUILD_ROOT%{ELIBDIR}
mkdir -p $RPM_BUILD_ROOT%{_infodir}
make install \
     prefix=$RPM_BUILD_ROOT%{prefix} \
     datadir=$RPM_BUILD_ROOT%{datadir} \
     locallisppath=$RPM_BUILD_ROOT%{locallisppath} \
     ELIBDIR=$RPM_BUILD_ROOT%{ELIBDIR} \
     infodir=$RPM_BUILD_ROOT%{_infodir} \
     MAKEINFO="makeinfo --force"
{
  echo ";; %{locallisppath}/suse-start-%{name}.el"
  echo ""
  echo "(add-to-list 'load-path \"%{ELIBDIR}\")"
  echo ""
  echo ";; %{locallisppath}/suse-start-%{name}.el ends here"
} > %{buildroot}%{locallisppath}/suse-start-%{name}.el

%post
%install_info --info-dir=%{_infodir} %{_infodir}/%{name}.info.gz

%postun
%install_info_delete --info-dir=%{_infodir} %{_infodir}/%{name}.info.gz

%files
%defattr(-,root,root)
%doc ChangeLog INSTALL NEWS RELEASING TODO COPYING README
%doc %{_infodir}/elib*
%{ELIBDIR}
%config %{locallisppath}/suse-start-%{name}.el

%changelog
