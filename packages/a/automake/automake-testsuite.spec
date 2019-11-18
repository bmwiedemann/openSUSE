#
# spec file for package automake-testsuite
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


# PLEASE run pre_checkin.sh in this directory before submitting
# this package. Otherwise the .spec and .changes for automake-testsuite
# aren't updated.

Name:           automake-testsuite
Version:        1.16.1
Release:        0
Summary:        A Program for Automatically Generating GNU-Style Makefile.in Files
# docs ~> GFDL, sources ~> GPLv2+, mkinstalldirs ~> PD and install-sh ~> MIT
License:        GPL-2.0-or-later AND GFDL-1.3-or-later AND SUSE-Public-Domain AND MIT
Group:          Development/Tools/Building
Url:            https://www.gnu.org/software/automake
Source0:        https://ftp.gnu.org/gnu/automake/automake-%{version}.tar.xz
Source1:        https://ftp.gnu.org/gnu/automake/automake-%{version}.tar.xz.sig
Source2:        https://savannah.gnu.org/project/memberlist-gpgkeys.php?group=automake&download=1#/automake.keyring
Source3:        automake-rpmlintrc
#Source4:        http://git.savannah.gnu.org/cgit/config.git/plain/config.sub
#Source5:        http://git.savannah.gnu.org/cgit/config.git/plain/config.guess
Patch2:         automake-require_file.patch
Patch3:         automake-1.13.4-fix-primary-prefix-invalid-couples-test.patch
Patch5:         0001-correct-parameter-parsing-in-test-driver-script.patch
Patch100:       automake-SuSE.patch
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
%if "%{name}" == "automake-testsuite"
BuildRequires:  cscope
BuildRequires:  dejagnu
BuildRequires:  expect
BuildRequires:  flex
BuildRequires:  gettext-tools
BuildRequires:  libtool
BuildRequires:  makedepend
BuildRequires:  makeinfo
BuildRequires:  pkg-config
BuildRequires:  python
BuildRequires:  sharutils
%if 0%{suse_version} >= 1500
BuildRequires:  vala
BuildRequires:  pkgconfig(gobject-2.0)
%endif
BuildRequires:  zip
Requires:       expect
Requires:       flex
Requires:       libtool
%endif

# remove bogus Automake perl dependencies and provides
%global __requires_exclude %{?__requires_exclude:%__requires_exclude|}^perl\\(Automake::
%global __provides_exclude %{?__provides_exclude:%__provides_exclude|}^perl\\(Automake::

%description
Automake is a tool for automatically generating "Makefile.in" files
from "Makefile.am" files.  "Makefile.am" is a series of "make" macro
definitions (with rules occasionally thrown in).  The generated
"Makefile.in" files are compatible with the GNU Makefile standards.

%prep
%setup -q -n automake-%{version}
%patch2 -p1
%patch3 -p1
%patch5 -p1
%patch100

%build
sh bootstrap
%configure --docdir=%{_docdir}/%{name}
make #%%{?_smp_mflags}

%if "%{name}" == "automake-testsuite"
%check
# Some architectures can't keep up the pace.
%ifnarch alpha %{arm}
make %{?_smp_mflags} check VERBOSE=1
%endif

%install
%else
%install
%make_install
mkdir %{buildroot}/etc
echo %{_prefix}/local/share/aclocal >%{buildroot}%{_sysconfdir}/aclocal_dirlist
ln -s %{_sysconfdir}/aclocal_dirlist %{buildroot}%{_datadir}/aclocal/dirlist
install -m644 AUTHORS COPYING ChangeLog NEWS README THANKS %{buildroot}%{_docdir}/%{name}
# info's dir file is not auto ignored on some systems
rm -rf %{buildroot}%{_infodir}/dir
#name == automake
%endif

%post
%install_info --info-dir=%{_infodir} %{_infodir}/automake.info%{ext_info}

%preun
%install_info_delete --info-dir=%{_infodir} %{_infodir}/automake.info%{ext_info}

%if "%{name}" == "automake"
%files
%defattr(-,root,root)
%doc %{_docdir}/%{name}
%{_bindir}/*
%{_infodir}/*%{ext_info}
%{_mandir}/man1/*
%{_datadir}/aclocal*
%{_datadir}/automake-*
%config %{_sysconfdir}/aclocal_dirlist
%endif

%changelog
