#
# spec file for package autoconf-testsuite
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


Name:           autoconf-testsuite
Version:        2.69
Release:        0
Summary:        A GNU Tool for Automatically Configuring Source Code
License:        GPL-3.0-or-later
Url:            http://www.gnu.org/software/autoconf
Source0:        http://ftp.gnu.org/gnu/autoconf/autoconf-%{version}.tar.gz
Source1:        http://ftp.gnu.org/gnu/autoconf/autoconf-%{version}.tar.gz.sig
Source2:        %{name}.keyring
Patch0:         autoreconf-ltdl.diff
# PATCH-FIX-UPSTREAM autoconf-perl-5.17-fixes.patch dimstar@opensuse.org -- autoscan: port to perl 5.17 (with perl 5.22, it is now fatal).
Patch1:         autoconf-perl-5.17-fixes.patch
# PATCH-FIX-UPSTREAM AC_HEADER_MAJOR: port to glibc 2.25
Patch2:         ac-header-major.patch
# PATCH-FIX-UPSTREAM Port tests to Bash 5
Patch3:         port-tests-to-bash-5.patch
BuildRequires:  help2man
BuildRequires:  m4 >= 1.4.6
Requires:       info
Requires:       m4 >= 1.4.6
Requires:       perl-base >= 5.6
Requires(post): %{install_info_prereq}
Requires(preun): %{install_info_prereq}
BuildRoot:      %{_tmppath}/%{name}-%{version}-build
BuildArch:      noarch

%description
GNU Autoconf is a tool for configuring source code and makefiles. Using
autoconf, programmers can create portable and configurable packages,
because the person building the package is allowed to specify various
configuration options.

You should install autoconf if you are developing software and would
like to create shell scripts to configure your source code packages.

Note that the autoconf package is not required for the end user who may
be configuring software with an autoconf-generated script; autoconf is
only required for the generation of the scripts, not their use.

%prep
%setup -q -n autoconf-%{version}
%patch0
%patch1 -p1
%patch2 -p1
%patch3 -p1

%build
%configure
make %{?_smp_mflags}

%if "%{name}" == "autoconf-testsuite"
%check
trap 'test $? -ne 0 && cat tests/testsuite.log' EXIT
make %{?_smp_mflags} check

%install
%else
%install
%{?make_install} %{!?make_install:make install DESTDIR=%{buildroot}}
rm -f %{buildroot}%{_datadir}/emacs/site-lisp/*.el*
# info's dir file is not auto ignored on some systems
rm -rf %{buildroot}%{_infodir}/dir
%endif

%post
%install_info --info-dir=%{_infodir} %{_infodir}/autoconf.info.gz

%preun
%install_info_delete --info-dir=%{_infodir} %{_infodir}/autoconf.info.gz

%if "%{name}" == "autoconf"
%files
%defattr(-,root,root)
%doc AUTHORS NEWS README TODO
%license COPYING
%{_bindir}/*
%{_datadir}/autoconf
%doc %{_infodir}/*.gz
%doc %{_mandir}/man1/*.gz
%endif

%changelog
