#
# spec file for package libidn
#
# Copyright (c) 2022 SUSE LLC
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


%define lname	libidn12
Name:           libidn
Version:        1.41
Release:        0
Summary:        Support for Internationalized Domain Names (IDN)
License:        (GPL-2.0-or-later OR LGPL-3.0-or-later) AND GPL-3.0-or-later AND Apache-2.0
Group:          Development/Libraries/C and C++
URL:            https://www.gnu.org/software/libidn/
Source0:        https://ftp.gnu.org/gnu/%{name}/%{name}-%{version}.tar.gz
Source1:        https://ftp.gnu.org/gnu/%{name}/%{name}-%{version}.tar.gz.sig
Source2:        https://josefsson.org/key-20190320.txt#/%{name}.keyring
Source3:        baselibs.conf
BuildRequires:  pkgconfig

%description
GNU Libidn is an implementation of the Stringprep, Punycode, and IDNA
specifications defined by the IETF Internationalized Domain Names (IDN)
working group. It is used to prepare internationalized strings (such as
domain name labels, usernames, and passwords) in order to increase the
likelihood that string input and string comparison work in ways that
make sense for typical users around the world. The library contains a
generic Stringprep implementation that does Unicode 3.2 NFKC
normalization, mapping and prohibition of characters, and bidirectional
character handling. Profiles for iSCSI, Kerberos 5, Nameprep, SASL, and
XMPP are included. Punycode and ASCII Compatible Encoding (ACE) via
IDNA is supported.

%package tools
Summary:        Command line utility to convert Int. Domain Names
License:        (GPL-2.0-or-later OR LGPL-3.0-or-later) AND GPL-3.0-or-later
Group:          Productivity/Networking/DNS/Utilities

%description tools
GNU Libidn is an implementation of the Stringprep, Punycode, and IDNA
specifications defined by the IETF Internationalized Domain Names
(IDN) working group. It is used to prepare internationalized strings
(such as domain name labels, usernames, and passwords) in order to
increase the likelihood that string input and string comparison work
in ways that make sense for typical users around the world. The
library contains a generic Stringprep implementation that does
Unicode 3.2 NFKC normalization, mapping and prohibition of
characters, and bidirectional character handling. Profiles for iSCSI,
Kerberos 5, Nameprep, SASL, and XMPP are included. Punycode and ASCII
Compatible Encoding (ACE) via IDNA is supported.

%package -n %{lname}
Summary:        Support for Internationalized Domain Names (IDN)
License:        (GPL-2.0-or-later OR LGPL-3.0-or-later) AND GPL-3.0-or-later
Group:          System/Libraries
Provides:       libidn = %{version}
Obsoletes:      libidn < %{version}

%description -n %{lname}
GNU Libidn is an implementation of the Stringprep, Punycode, and IDNA
specifications defined by the IETF Internationalized Domain Names
(IDN) working group. It is used to prepare internationalized strings
(such as domain name labels, usernames, and passwords) in order to
increase the likelihood that string input and string comparison work
in ways that make sense for typical users around the world. The
library contains a generic Stringprep implementation that does
Unicode 3.2 NFKC normalization, mapping and prohibition of
characters, and bidirectional character handling. Profiles for iSCSI,
Kerberos 5, Nameprep, SASL, and XMPP are included. Punycode and ASCII
Compatible Encoding (ACE) via IDNA is supported.

%package devel
Summary:        Development files for libidn
License:        LGPL-2.1-or-later
Group:          Development/Libraries/C and C++
Requires:       %{lname} = %{version}
Requires:       glibc-devel

%description devel
GNU Libidn is an implementation of the Stringprep, Punycode, and IDNA
specifications defined by the IETF Internationalized Domain Names (IDN)
working group. It is used to prepare internationalized strings (such as
domain name labels, usernames, and passwords) in order to increase the
likelihood that string input and string comparison work in ways that
make sense for typical users around the world. The library contains a
generic Stringprep implementation that does Unicode 3.2 NFKC
normalization, mapping and prohibition of characters, and bidirectional
character handling. Profiles for iSCSI, Kerberos 5, Nameprep, SASL, and
XMPP are included. Punycode and ASCII Compatible Encoding (ACE) via
IDNA is supported.

%prep
%setup -q

%build
%configure \
    --disable-silent-rules \
    --disable-static \
    --disable-gtk-doc
%make_build

%install
%make_install
find %{buildroot} -type f -name "*.la" -delete -print

%find_lang %{name}

%check
%if ! 0%{?qemu_user_space_build}
%make_build check
%endif

%post -n %{lname} -p /sbin/ldconfig
%postun -n %{lname} -p /sbin/ldconfig

%files tools -f %{name}.lang
%license COPYING*
%dir %{_datadir}/emacs
%dir %{_datadir}/emacs/site-lisp
%doc AUTHORS ChangeLog FAQ NEWS README THANKS
%{_infodir}/libidn*
%{_bindir}/idn
%{_mandir}/man1/idn.1%{?ext_man}
%{_datadir}/emacs/site-lisp/idna.el
%{_datadir}/emacs/site-lisp/punycode.el

%files -n %{lname}
%license COPYING*
%{_libdir}/libidn.so.12*

%files devel
%license COPYING*
%{_libdir}/libidn.so
%{_includedir}/*.h
%{_libdir}/pkgconfig/libidn.pc
%{_mandir}/man3/*

%changelog
