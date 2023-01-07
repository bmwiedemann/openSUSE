#
# spec file for package sed
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


Name:           sed
Version:        4.9
Release:        0
Summary:        A Stream-Oriented Non-Interactive Text Editor
License:        GPL-3.0-or-later
Group:          System/Base
URL:            https://www.gnu.org/software/sed/
Source0:        https://ftp.gnu.org/gnu/sed/%{name}-%{version}.tar.xz
Source1:        https://ftp.gnu.org/gnu/sed/%{name}-%{version}.tar.xz.sig
Source2:        %{name}.keyring
BuildRequires:  libacl-devel
BuildRequires:  libselinux-devel
Provides:       base:/bin/sed

%description
Sed takes text input, performs one or more operations on it, and
outputs the modified text. Sed is typically used for extracting parts
of a file using pattern matching or  for substituting multiple
occurrences of a string within a file.

%lang_package

%prep
%autosetup -p1

%build
%define warn_flags -Wall -Wstrict-prototypes -Wpointer-arith -Wformat-security
export CFLAGS="%{optflags} %{warn_flags} -fPIE"
export LDFLAGS="-pie"
%configure \
  --without-included-regex
%make_build

%install
%make_install
%if 0%{?suse_version} < 1550
mkdir -p %{buildroot}/bin
ln -s %{_bindir}/sed %{buildroot}/bin/sed
%endif
%find_lang %{name}

%check
%make_build check

%files
%license COPYING*
%doc AUTHORS BUGS NEWS README* THANKS
%if 0%{?suse_version} < 1550
/bin/sed
%endif
%{_bindir}/sed
%{_mandir}/man*/*%{ext_man}
%{_infodir}/sed.info*%{ext_info}

%files lang -f %{name}.lang
%license COPYING*

%changelog
