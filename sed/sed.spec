#
# spec file for package sed
#
# Copyright (c) 2018 SUSE LINUX GmbH, Nuernberg, Germany.
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
Version:        4.7
Release:        0
Summary:        A Stream-Oriented Non-Interactive Text Editor
License:        GPL-3.0-or-later
Group:          System/Base
URL:            https://www.gnu.org/software/sed/
Source0:        https://ftp.gnu.org/gnu/sed/%{name}-%{version}.tar.xz
Source1:        https://ftp.gnu.org/gnu/sed/%{name}-%{version}.tar.xz.sig
Source2:        %{name}.keyring
# PATCH-FIX-SLE sed-dont_close_twice.patch bnc@880817 tcech@suse.cz -- Fix double close.
Patch0:         sed-dont_close_twice.patch
BuildRequires:  libacl-devel
BuildRequires:  libselinux-devel
Requires(post): %{install_info_prereq}
Requires(preun): %{install_info_prereq}
Recommends:     %{name}-lang
Provides:       base:/bin/sed

%description
Sed takes text input, performs one or more operations on it, and
outputs the modified text. Sed is typically used for extracting parts
of a file using pattern matching or  for substituting multiple
occurrences of a string within a file.

%lang_package

%prep
%setup -q
%patch0 -p1

%build
%define warn_flags -Wall -Wstrict-prototypes -Wpointer-arith -Wformat-security
export CFLAGS="%{optflags} %{warn_flags} -fPIE"
export LDFLAGS="-pie"
%configure \
  --without-included-regex
%if 0%{?do_profiling}
  make %{?_smp_mflags} CFLAGS="$CFLAGS %{cflags_profile_generate}" V=1
  make CFLAGS="$CFLAGS %{cflags_profile_generate}" check
  make %{?_smp_mflags} clean
  make %{?_smp_mflags} CFLAGS="$CFLAGS %{cflags_profile_feedback}" V=1
%else
  make %{?_smp_mflags} V=1
%endif
make %{?_smp_mflags} check

%install
%make_install
#UsrMerge
mkdir -p %{buildroot}/bin
ln -s %{_bindir}/sed %{buildroot}/bin/sed
#EndUserMerge
%find_lang %{name}

%check
# run check once more with final binaries
make %{?_smp_mflags} check

%post
%install_info --info-dir=%{_infodir} %{_infodir}/%{name}.info%{ext_info}

%preun
%install_info_delete --info-dir=%{_infodir} %{_infodir}/%{name}.info%{ext_info}

%files
%license COPYING*
%doc AUTHORS BUGS NEWS README* THANKS
/bin/sed
%{_bindir}/sed
%{_mandir}/man*/*%{ext_man}
%{_infodir}/sed.info*%{ext_info}

%files lang -f %{name}.lang

%changelog
