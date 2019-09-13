#
# spec file for package po-utils
#
# Copyright (c) 2015 SUSE LINUX GmbH, Nuernberg, Germany.
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


Name:           po-utils
Version:        0.5
Release:        0
Summary:        Free PO Utilities
License:        GPL-2.0+
Group:          Development/Tools/Other
Url:            http://po-utils.progiciels-bpi.ca/
Source:         http://www.iro.umontreal.ca/contrib/po-utils/po-utils-%{version}.tar.gz
Patch0:         po-utils-%{version}.diff
Patch1:         warn.patch
Patch2:         lflags.patch
BuildRequires:  autoconf
BuildRequires:  automake
BuildRequires:  bison
BuildRequires:  emacs-nox
BuildRequires:  flex
BuildRoot:      %{_tmppath}/%{name}-%{version}-build

%description
A collection of tools for handling PO files.

%prep
%setup -q
%patch0
%patch1
%patch2

%build
autoreconf -fi
%configure
export EMACS_UNIBYTE=1
make %{?_smp_mflags}

%install
make install DESTDIR="$RPM_BUILD_ROOT"
rm -f %{buildroot}%{_datadir}/emacs/site-lisp/po-mode.el*

%files
%defattr(-, root, root)
%doc AUTHORS COPYING NEWS README THANKS
%{_bindir}/xpot
# /usr/share/emacs/site-lisp/po-mode.el
# /usr/share/emacs/site-lisp/po-mode.elc

%changelog
