#
# spec file for package byacc
#
# Copyright (c) 2022 SUSE LLC
# Copyright (c) 2010 Guido Berhoerster.
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


Name:           byacc
Version:        20221106
Release:        0
Summary:        LALR(1) parser generator
License:        SUSE-Public-Domain
Group:          Development/Languages/C and C++
URL:            https://invisible-island.net/byacc/byacc.html
Source0:        https://invisible-mirror.net/archives/byacc/byacc-%{version}.tgz
Source1:        https://invisible-mirror.net/archives/byacc/byacc-%{version}.tgz.asc
Source2:        %{name}.keyring

%description
Berkeley Yacc is a LALR(1) parser generator. It has been made as compatible as
possible with AT&T Yacc and it accepts any input specification that conforms to
the AT&T Yacc documentation. In contrast to bison, it is written to avoid
dependencies upon a particular compiler.

%prep
%setup -q

%build
# without --with-warnings several functions will not be marked with gcc's
# noreturn attribute and produce warnings when $RPM_OPT_FLAGS contains -Wall
%configure \
  --with-warnings \
  --enable-btyacc \
	--program-prefix=b
%make_build

%install
%make_install

%check
%make_build check

%files
%doc ACKNOWLEDGEMENTS CHANGES NEW_FEATURES NO_WARRANTY NOTES README*
%{_bindir}/byacc
%{_mandir}/man1/byacc.1%{?ext_man}

%changelog
