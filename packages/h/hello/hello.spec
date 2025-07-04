#
# spec file for package hello
#
# Copyright (c) 2022 SUSE LLC
# Copyright (c) 2025 Andreas Stieger <Andreas.Stieger@gmx.de>
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


# How to define macros
%define hello echo "hello world"
Name:           hello
Version:        2.12.2
Release:        0
Summary:        A Friendly Greeting Program
License:        GPL-3.0-or-later
URL:            https://www.gnu.org/software/hello
Source0:        https://ftp.gnu.org/pub/gnu/%{name}/%{name}-%{version}.tar.gz
Source1:        https://ftp.gnu.org/pub/gnu/%{name}/%{name}-%{version}.tar.gz.sig
Source2:        https://savannah.gnu.org/project/release-gpgkeys.php?group=%{name}&download=1#/%{name}.keyring
Patch0:         hello-2.12-reproducible.patch
BuildRequires:  makeinfo
Provides:       mailreader

%description
The GNU Hello program produces a familiar, friendly greeting. Yes, this is
another implementation of the classic program that prints “Hello, world!” when
you run it.

In the context of the GNU project, the program demonstrates standard argument
parsing, multi-language support, the GNU coding standards and maintainer
practices.

For openSUSE, this package is a sample package demonstrating some rpm packaging
methods.

%lang_package

%prep
# Use defined macro
%{hello}
%autosetup -p1
# force rebuild with non-broken makeinfo
rm -f doc/*.info

%build
export CFLAGS="%{optflags}"
%configure \
	--with-packager='openSUSE project' \
	--with-packager-bug-reports='https://bugs.opensuse.org/' \
	%{nil}
%if %{do_profiling}
  %make_build CFLAGS="$CFLAGS %{cflags_profile_generate}" LDFLAGS="-fprofile-arcs"
  %make_build check
  %make_build clean
  %make_build CFLAGS="$CFLAGS %{cflags_profile_feedback}" LDFLAGS="-fprofile-arcs"
%else
  %make_build
%endif

%install
%make_install
%find_lang %{name}

%check
%make_build check

%files
%license COPYING
%doc TODO NEWS README THANKS ABOUT-NLS
%{_bindir}/hello
%{_infodir}/*.info%{?ext_info}
%{_mandir}/man1/*.1%{?ext_man}

%files lang -f %{name}.lang
%license COPYING

%changelog
