#
# spec file for package gengetopt
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


Name:           gengetopt
Version:        2.23
Release:        0
Summary:        Commandline parser generator
License:        GPL-3.0-or-later
Group:          Development/Languages/C and C++
URL:            https://www.gnu.org/software/gengetopt/
Source0:        https://ftp.gnu.org/gnu/gengetopt/%{name}-%{version}.tar.xz
Source1:        https://ftp.gnu.org/gnu/gengetopt/%{name}-%{version}.tar.xz.sig
Source2:        https://savannah.gnu.org/project/memberlist-gpgkeys.php?group=%{name}&download=1#/%{name}.keyring
BuildRequires:  bison
BuildRequires:  flex
BuildRequires:  gcc-c++
BuildRequires:  help2man
BuildRequires:  makeinfo

%description
Gengetopt is a tool to generate C code to parse getopt styled command line
arguments.
It's similar or even more powerful than the well known libpopt but does not
add any run or compile time dependencies to your projects. Moreover
reading/writing the options from/to config files is also supported.

%prep
%autosetup

%build
%configure
%make_build

%install
%make_install

# our system's getopt.h has getopt_long() on board, no need to install sources
rm -rf %{buildroot}%{_datadir}/%{name}
# info's dir file is not auto ignored on some systems
rm -rf %{buildroot}%{_infodir}/dir
# documentation is handled by doc macr
rm -rf %{buildroot}%{_datadir}/doc/%{name}

%check
%make_build check

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
%{_infodir}/index.info%{?ext_info}
%{_mandir}/man1/%{name}.1%{?ext_man}

%changelog
