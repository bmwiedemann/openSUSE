#
# spec file for package hello
#
# Copyright (c) 2017 SUSE LINUX GmbH, Nuernberg, Germany.
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


Name:           hello
# How to define macros
%define hello echo "hello world"
Provides:       mailreader
Summary:        A Friendly Greeting Program
License:        GPL-3.0+
Group:          Development/Tools/Other
Version:        2.10
Release:        0
Url:            http://www.gnu.org/software/hello
Source0:        ftp://ftp.gnu.org/pub/gnu/hello/hello-%{version}.tar.gz
Source1:        ftp://ftp.gnu.org/pub/gnu/hello/hello-%{version}.tar.gz.sig
# https://savannah.gnu.org/project/memberlist-gpgkeys.php?group=hello&download=1
Source2:        %{name}.keyring
Patch0:         hello-1.3.dif
BuildRoot:      %{_tmppath}/%{name}-%{version}-build
BuildRequires:  makeinfo
PreReq:         %install_info_prereq
Recommends:     %{name}-lang

%description
The GNU hello program produces a familiar, friendly greeting.  It
allows nonprogrammers to use a classic computer science tool that would
otherwise be unavailable to them.  Because it is protected by the GNU
General Public License, users are free to share and change it.

GNU hello supports many native languages.

%lang_package

%prep
# Use defined macro
%{hello}
%setup -q
%patch0
# force rebuild with non-broken makeinfo
rm -f doc/*.info

%build
export CFLAGS="%{optflags}"
%configure
%if %do_profiling
  make CFLAGS="$CFLAGS %cflags_profile_generate" LDFLAGS="-fprofile-arcs"
  make check
  make clean
  make CFLAGS="$CFLAGS %cflags_profile_feedback" LDFLAGS="-fprofile-arcs"
%else
  make
%endif

%check
make check

%install
%make_install
%find_lang %{name}

%post
%install_info --info-dir=%{_infodir} %{_infodir}/%{name}.info.gz

%postun
%install_info_delete --info-dir=%{_infodir} %{_infodir}/%{name}.info.gz

%files
%defattr(-, root, root)
%doc COPYING TODO NEWS README THANKS ABOUT-NLS
%{_bindir}/*
%{_infodir}/*.gz
%{_mandir}/*/*

%files lang -f %{name}.lang

%changelog
