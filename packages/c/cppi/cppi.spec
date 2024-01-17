#
# spec file for package cppi
#
# Copyright (c) 2016 SUSE LINUX GmbH, Nuernberg, Germany.
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


Name:           cppi
Version:        1.18
Release:        0
Summary:        C preprocessor directive indenter
License:        GPL-3.0+
Group:          Development/Languages/C and C++
Url:            https://savannah.gnu.org/projects/cppi
Source0:        https://ftp.gnu.org/gnu/cppi/cppi-%{version}.tar.xz
Source1:        https://ftp.gnu.org/gnu/cppi/cppi-%{version}.tar.xz.sig
Source2:        %{name}.keyring
BuildRequires:  flex
Recommends:     %{name}-lang

%description
cppi indents the C preprocessor directives to reflect their nesting and ensures
that there is exactly one space character between each #if, #elif, #define
directive and the following token.

%lang_package

%prep
%setup -q

%build
%configure --disable-silent-rules
%make_build

%install
%make_install
%find_lang %{name}

%check
make %{?_smp_mflags} check

%files
%defattr(-,root,root,-)
%doc AUTHORS ChangeLog COPYING NEWS THANKS TODO
%{_bindir}/cppi
%{_mandir}/man1/cppi.1%{ext_man}

%files lang -f %{name}.lang
%defattr(-,root,root)

%changelog
