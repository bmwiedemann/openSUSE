#
# spec file for package gpp
#
# Copyright (c) 2017 SUSE LINUX GmbH, Nuernberg, Germany.
# Copyright (c) 2017 Tristan Miller <psychonaut@nothingisreal.com>
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


Name:           gpp
Version:        2.25
Release:        0
Summary:        Generic Preprocessor
License:        LGPL-3.0+
Group:          Development/Tools/Other
Url:            https://logological.org/gpp/
Source0:        https://files.nothingisreal.com/software/gpp/gpp-%{version}.tar.bz2
Source1:        https://files.nothingisreal.com/software/gpp/gpp-%{version}.tar.bz2.sig
Source2:        %{name}.keyring

%description
GPP is a general-purpose preprocessor with customizable syntax, suitable
for a wide range of preprocessing tasks. Its independence from any one
programming language makes it much more versatile than the C preprocessor
(cpp), while its syntax is lighter and more flexible than that of GNU m4.
There are built-in macros for use with C/C++, LaTeX, HTML, XHTML, and
Prolog files.

%prep
%setup -q

%build
%configure \
  --docdir=%{_docdir}/%{name}
make %{?_smp_mflags}

%install
%make_install

%files
%doc AUTHORS COPYING COPYING.LESSER README THANKS
%{_bindir}/gpp
%{_docdir}/%{name}
%{_mandir}/man1/gpp.1%{ext_man}

%changelog
