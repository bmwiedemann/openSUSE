#
# spec file for package vilistextum
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


Name:           vilistextum
Version:        2.6.9
Release:        0
Summary:        Convert HTML to text with hyperlink references
License:        GPL-2.0-only
URL:            https://bhaak.net/vilistextum/index.html
Source:         http://bhaak.net/vilistextum/vilistextum-2.6.9.tar.bz2
Patch1:         vilistextum-fix-unused-variable-warnings.patch

%description
Simple program for viewing HTML in the terminal.

It displays hyperlinks as footnotes.

.mailcap:
text/html; vilistextum -ul --charset %{charset} - - ; copiousoutput;

%prep
%setup -q
%autopatch -p1

%build
CPPFLAGS=-D_POSIX_C_SOURCE=200809L
CFLAGS="-Werror -fcommon"
export CPPFLAGS CFLAGS
%configure --enable-multibyte
make %{?_smp_mflags}

%install
%make_install

%check
make %{?_smp_mflags} test

%post
%postun

%files
%license COPYING
%doc CHANGES README
%{_bindir}/vilistextum
%{_mandir}/man1/vilistextum.1%{?ext_man}

%changelog
