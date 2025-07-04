#
# spec file for package automake
#
# Copyright (c) 2025 SUSE LLC
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


# remove bogus Automake perl dependencies and provides
%global __requires_exclude %{?__requires_exclude:%__requires_exclude|}^perl\\(Automake::
%global __provides_exclude %{?__provides_exclude:%__provides_exclude|}^perl\\(Automake::
%define flavor @BUILD_FLAVOR@%{nil}
%if "%{flavor}" == "testsuite"
%define nsuffix -testsuite
%else
%define nsuffix %{nil}
%endif
Name:           automake%{nsuffix}
Version:        1.18.1
Release:        0
Summary:        A Program for Automatically Generating GNU-Style Makefile.in Files
# docs ~> GFDL, sources ~> GPLv2+, mkinstalldirs ~> PD and install-sh ~> MIT
License:        GFDL-1.3-or-later AND GPL-2.0-or-later AND SUSE-Public-Domain AND MIT
Group:          Development/Tools/Building
URL:            https://www.gnu.org/software/automake
Source0:        https://ftp.gnu.org/gnu/automake/automake-%{version}.tar.xz
Source1:        https://ftp.gnu.org/gnu/automake/automake-%{version}.tar.xz.sig
# taken from https://savannah.gnu.org/project/release-gpgkeys.php?group=automake&download=1
Source2:        automake.keyring
Source3:        automake-rpmlintrc
Patch100:       automake-suse-vendor.patch
BuildRequires:  autoconf >= 2.69
BuildRequires:  bison
BuildRequires:  gcc-c++
BuildRequires:  gcc-fortran
BuildRequires:  xz
BuildRequires:  perl(Thread::Queue)
BuildRequires:  perl(threads)
Requires:       autoconf >= 2.69
Requires:       perl
Requires(post): info
Requires(preun): info
BuildArch:      noarch
%if "%{flavor}" == "testsuite"
BuildRequires:  cscope
BuildRequires:  dejagnu
BuildRequires:  etags
BuildRequires:  expect
BuildRequires:  flex
BuildRequires:  gettext-tools
BuildRequires:  libtool
BuildRequires:  makedepend
BuildRequires:  makeinfo
BuildRequires:  pkgconfig
BuildRequires:  python3
BuildRequires:  sharutils
BuildRequires:  zip
Requires:       expect
Requires:       flex
Requires:       libtool
%if 0%{?suse_version} >= 1500
BuildRequires:  vala
BuildRequires:  pkgconfig(gobject-2.0)
%endif
%endif

%description
Automake is a tool for automatically generating "Makefile.in" files
from "Makefile.am" files.  "Makefile.am" is a series of "make" macro
definitions (with rules occasionally thrown in).  The generated
"Makefile.in" files are compatible with the GNU Makefile standards.

%prep
%setup -q -n automake-%{version}
%autopatch -p1

%build
%configure --docdir=%{_docdir}/%{name}
%make_build

%if "%{flavor}" == "testsuite"
%check
# Some architectures can't keep up the pace.
%ifnarch %{arm}
%make_build check
%endif

%install
%else

%install
%make_install
mkdir %{buildroot}%{_sysconfdir}
echo %{_prefix}/local/share/aclocal >%{buildroot}%{_sysconfdir}/aclocal_dirlist
ln -s %{_sysconfdir}/aclocal_dirlist %{buildroot}%{_datadir}/aclocal/dirlist
install -m644 AUTHORS ChangeLog NEWS README THANKS %{buildroot}%{_docdir}/%{name}
# info's dir file is not auto ignored on some systems
rm -rf %{buildroot}%{_infodir}/dir
%endif

%post
%install_info --info-dir=%{_infodir} %{_infodir}/automake.info%{ext_info}

%preun
%install_info_delete --info-dir=%{_infodir} %{_infodir}/automake.info%{ext_info}

%if "%{flavor}" == ""
%files
%license COPYING
%doc %{_docdir}/%{name}
%{_bindir}/*
%{_infodir}/*%{ext_info}
%{_mandir}/man1/*
%{_datadir}/aclocal*
%{_datadir}/automake-*
%config %{_sysconfdir}/aclocal_dirlist
%endif

%changelog
