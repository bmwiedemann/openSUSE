#
# spec file for package indent
#
# Copyright (c) 2020 SUSE LLC
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


Name:           indent
Version:        2.2.12
Release:        0
Summary:        Indentation of Source Code in various styles
License:        GPL-3.0-or-later
Group:          Development/Languages/C and C++
URL:            https://www.gnu.org/software/indent
Source0:        ftp://ftp.gnu.org/gnu/%{name}/%{name}-%{version}.tar.xz
Source1:        ftp://ftp.gnu.org/gnu/%{name}/%{name}-%{version}.tar.xz.sig
Source2:        https://savannah.gnu.org/project/memberlist-gpgkeys.php?group=%{name}&download=1#/%{name}.keyring
BuildRequires:  makeinfo
BuildRequires:  texi2html

%description
Indent can be used to make code easier to read. It can also convert
from one style of writing C code to another. indent understands a
substantial amount of C syntax, but it also tries to cope with
incomplete and malformed syntax.

%lang_package

%prep
%autosetup

%build
%configure
%make_build

%install
%make_install
# indent.html is installed with doc below
rm -f %{buildroot}%{_prefix}/doc/indent/indent.html %{buildroot}%{_bindir}/texinfo2man %{buildroot}/%{_infodir}/dir
%find_lang %{name}

%check
%make_build check

%post
%install_info --info-dir=%{_infodir} %{_infodir}/%{name}.info.gz

%preun
%install_info_delete --info-dir=%{_infodir} %{_infodir}/%{name}.info.gz

%files
%{_bindir}/*
%license COPYING
%doc NEWS ChangeLog doc/indent.html
%{_infodir}/%{name}.info%{?ext_info}
%{_mandir}/man1/indent.1%{?ext_man}

%files lang -f %{name}.lang

%changelog
