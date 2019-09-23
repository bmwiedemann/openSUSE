#
# spec file for package librep
#
# Copyright (c) 2018 SUSE LINUX GmbH, Nuernberg, Germany.
# Copyright (c) 2007 John Harper <john@dcs.warwick.ac.uk>
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


Name:           librep
Version:        0.92.7
Release:        0
Summary:        Implementation of rep, a lisp dialect
License:        GPL-2.0-or-later
Group:          Development/Languages/Scheme
Url:            http://sawfish.wikia.com/wiki/Librep
Source:         http://download.tuxfamily.org/librep/%{name}_%{version}.tar.xz
BuildRequires:  chrpath
BuildRequires:  emacs-nox
BuildRequires:  fdupes
BuildRequires:  gdbm-devel
BuildRequires:  gmp-devel
BuildRequires:  libffi-devel
BuildRequires:  ncurses-devel
BuildRequires:  pkg-config
BuildRequires:  readline-devel
%if 0%{?suse_version} <= 1210
BuildRequires:  xz
%endif
%if 0%{suse_version} > 1220
BuildRequires:  makeinfo
%endif

Requires(pre):  %install_info_prereq
BuildRoot:      %{_tmppath}/%{name}-%{version}-build
# PATCH-FEATURE-OPENSUSE 0001-install-byte-compiled-emacs-lisp.patch toganm@opensuse.org
Patch1:         0001-install-byte-compiled-emacs-lisp.patch
# PATCH-FIX_UPSTREAM 0001-string-to-number.patch toganm@opensuse.org use newer emacs functions
Patch2:         0001-string-to-number.patch
# PATCH-FEATURE-OPENSUSE toganm@opensuse.org remove builddate to prevent unnecessary builds
Patch3:         librep-remove-build_date.patch

%description
Librep is a shared library implementing a Lisp dialect that is
lightweight, reasonably fast, and highly extensible. It contains an
interpreter, byte-code compiler and virtual machine. Applications may
use the interpreter as an extension language, or it may be used for
standalone scripts.

Rep was originally inspired by Emacs Lisp. However one of the main
deficiencies of elisp -- the reliance on dynamic scope -- has been
removed. Also, rep only has a single namespace for symbols.

%package -n librep16
Summary:        Implementation of rep, a lisp dialect - Libraries
Group:          Development/Languages/Scheme

%description -n librep16
Librep is a shared library implementing a Lisp dialect that is
lightweight, reasonably fast, and highly extensible. It contains an
interpreter, byte-code compiler and virtual machine. Applications may
use the interpreter as an extension language, or it may be used for
standalone scripts.

Rep was originally inspired by Emacs Lisp. However one of the main
deficiencies of elisp -- the reliance on dynamic scope -- has been
removed. Also, rep only has a single namespace for symbols.

%package devel
Summary:        Implementation of rep, a lisp dialect - Development Files
Group:          Development/Languages/Scheme
Requires:       %{name} = %{version}
Requires:       librep16 = %{version}

%description devel
Librep is a shared library implementing a Lisp dialect that is
lightweight, reasonably fast, and highly extensible. It contains an
interpreter, byte-code compiler and virtual machine. Applications may
use the interpreter as an extension language, or it may be used for
standalone scripts.

Rep was originally inspired by Emacs Lisp. However one of the main
deficiencies of elisp -- the reliance on dynamic scope -- has been
removed. Also, rep only has a single namespace for symbols.

%prep
%setup -q -n %{name}_%{version}
%patch1 -p1
%patch2 -p1
%patch3 -p1

%build
export CFLAGS="%{optflags} -D_GNU_SOURCE -fno-strict-aliasing -fgnu89-inline"
export CXXFLAGS="$CFLAGS"
export CPPFLAGS="$CFLAGS"

%configure --disable-static --with-readline --enable-shared
make %{?_smp_mflags}

%install
%make_install
chrpath --delete %{buildroot}%{_bindir}/rep
# note: we need to keep some .la files, see http://mail.gnome.org/archives/sawfish-list/2008-October/msg00001.html
# Nevertheless I am removing them if anything fails then comment below
find %{buildroot}%{_libdir} -name \*.la -exec rm '{}' \;

%fdupes %{buildroot}%{_libdir}/rep
%fdupes %{buildroot}%{_datadir}/rep
%fdupes %{buildroot}%{_libexecdir}/rep/%{version}

%clean
rm -rf %{buildroot}

%post
%install_info --info-dir=%{_infodir} %{_infodir}/%{name}.info.gz

%post -n librep16 -p /sbin/ldconfig

%postun
%install_info_delete --info-dir=%{_infodir} %{_infodir}/%{name}.info.gz

%postun -n librep16 -p /sbin/ldconfig

%files
%defattr(-,root,root)
%license COPYING
%doc ChangeLog MAINTAINERS README TODO
%{_bindir}/rep
%{_bindir}/rep-remote
%doc %{_mandir}/man?/rep.*
%doc %{_mandir}/man?/rep-remote.*
%{_datadir}/rep
%{_libdir}/rep/
%{_infodir}/%{name}.info.gz
%{_datadir}/emacs/site-lisp/rep-*.elc

%files -n librep16
%defattr(-,root,root)
%{_libdir}/librep.so.*

%files devel
%defattr(-,root,root)
%{_bindir}/rep-xgettext
%{_bindir}/repdoc
%doc %{_mandir}/man?/rep-xgettext.*
%doc %{_mandir}/man?/repdoc.*
%{_libdir}/librep.so
%{_includedir}/rep/
%{_libdir}/pkgconfig/librep.pc

%changelog
