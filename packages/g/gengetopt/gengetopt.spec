#
# spec file for package gengetopt
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


Name:           gengetopt
Version:        2.22.6
Release:        0
Summary:        Commandline parser generator
License:        GPL-3.0-or-later
Group:          Development/Languages/C and C++
URL:            https://www.gnu.org/software/gengetopt/
Source0:        https://ftp.gnu.org/gnu/gengetopt/%{name}-%{version}.tar.gz
Source1:        https://ftp.gnu.org/gnu/gengetopt/%{name}-%{version}.tar.gz.sig
Source2:        %{name}.keyring
# PATCH-FIX-UPSTREAM sbrabec@suse.cz savannah54996 -- Fix glibc license. https://savannah.gnu.org/bugs/?54996
Patch1:         gengetopt-glibc-license.patch
# PATCH-FIX-UPSTREAM bmwiedemann boo#1047218 https://savannah.gnu.org/bugs/index.php?55311
Patch2:         reproducible.patch
BuildRequires:  bison
BuildRequires:  flex
BuildRequires:  gcc-c++
BuildRequires:  help2man
BuildRequires:  makeinfo
Requires(post): %{install_info_prereq}
Requires(preun): %{install_info_prereq}

%description
Gengetopt is a tool to generate C code to parse getopt styled command line
arguments.
It's similar or even more powerful than the well known libpopt but does not
add any run or compile time dependencies to your projects. Moreover
reading/writing the options from/to config files is also supported.

%prep
%setup -q
%patch1 -p1
%patch2 -p1

%build
%configure
make --jobs 1

%install
%make_install

# our system's getopt.h has getopt_long() on board, no need to install sources
rm -rf %{buildroot}%{_datadir}/%{name}
# info's dir file is not auto ignored on some systems
rm -rf %{buildroot}%{_infodir}/dir
# documentation is handled by doc macr
rm -rf %{buildroot}%{_datadir}/doc/%{name}

%check
make check --jobs 1

%post
%install_info --info-dir=%{_infodir} %{_infodir}/%{name}.info%{ext_info}

%preun
%install_info_delete --info-dir=%{_infodir} %{_infodir}/%{name}.info%{ext_info}

%files
%license COPYING LICENSE
%doc ChangeLog NEWS README THANKS
%doc doc/*.h doc/*.c doc/*.ggo doc/README.example
%{_bindir}/%{name}
%{_infodir}/%{name}.info%{?ext_info}
%{_mandir}/man1/%{name}.1%{?ext_man}

%changelog
