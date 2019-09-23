#
# spec file for package gnuserv
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


Name:           gnuserv
Version:        3.12.6
Release:        0
Summary:        Server and Clients for Emacs
License:        GPL-2.0-or-later
Group:          Productivity/Text/Editors
Source:         http://meltin.net/hacks/emacs/gnuserv-%{version}.tar.gz
Source1:        %{name}-README.SUSE
Patch0:         gnuserv-3.12.6.diff
BuildRequires:  autoconf
BuildRequires:  emacs-nox
Provides:       fgnuserv
Obsoletes:      fgnuserv

%description
This package is not required for XEmacs, because the tools included
here are a part of the XEmacs package.

With these tools, an already running Emacs can be accessed externally,
for example, in order to edit a file or run a code in Emacs Lisp. This
way, there is no need to start a new Emacs each time another
application loads an editor.

Find hints at %{_docdir}/gnuserv/README.SUSE.

%prep
%setup -q
cp -p %{SOURCE1} README.SUSE
%patch0 -p1

%build
autoreconf -fiv
%configure
make %{?_smp_mflags} all gnuserv.elc

%install
install -d -m755 \
  %{buildroot}%{_mandir}/man1 \
  %{buildroot}%{_datadir}/emacs/site-lisp
make install  \
  exec_prefix=%{buildroot}%{_prefix} \
  prefix=%{buildroot}%{_prefix} \
  man1dir=%{buildroot}%{_mandir}/man1
make install-elisp \
  elispdir=%{buildroot}%{_datadir}/emacs/site-lisp \
  prefix=%{buildroot}%{_prefix}
pushd %{buildroot}%{_mandir}/man1
for f in *.1 ; do
  case $f in
    gnuserv.1)
      # To avoid conflict with xemacs:
      mv $f emacs-$f
      ;;
    *)
      rm -f $f
      ln -s emacs-gnuserv.1.gz emacs-$f.gz
      ;;
  esac
done
popd
mv README.orig README.%{name}

%files
%license COPYING
%doc README README.%{name} README.SUSE
%{_bindir}/*
%{_mandir}/man1/*
%{_datadir}/emacs/site-lisp/*

%changelog
