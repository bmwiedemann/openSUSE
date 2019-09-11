#
# spec file for package perl-Gtk2-Unique
#
# Copyright (c) 2019 SUSE LINUX GmbH, Nuernberg, Germany.
# Copyright (c) 2011 Sascha Manns <saigkill@opensuse.org>
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


%define		cpan_name Gtk2-Unique
Name:           perl-Gtk2-Unique
Version:        0.05
Release:        0
Summary:        Perl bindings for the C library "libunique"
License:        LGPL-2.1-or-later
Group:          Development/Libraries/Perl
Url:            http://search.cpan.org/dist/Gtk2-Unique/
Source:         http://mirrors.ibiblio.org/CPAN/modules/by-module/Gtk2/%{cpan_name}-%{version}.tar.gz
# PATCH-FIX-UPSTREAM Gtk2-Unique-rt120115-Fix-crash.patch rt#120115 dimstar@opensuse.org -- Fix crash on starting second instance
Patch0:         Gtk2-Unique-rt120115-Fix-crash.patch
# PATCH-FIX-UPSTREAM Gtk2-Unique-Fix-crash.patch see boo#1099774 -- upstream commit: 8ac892efdf480efbca75dc1729fc9aa45708618e
Patch1:         Gtk2-Unique-Fix-crash.patch
# libnotify-devel seems to be missing this.  see BZ#216946
BuildRequires:  gtk2-devel
# non-perl
BuildRequires:  libnotify-devel
BuildRequires:  perl
BuildRequires:  perl(ExtUtils::Depends) >= 0.20
# core
BuildRequires:  perl(ExtUtils::MakeMaker)
BuildRequires:  perl(ExtUtils::PkgConfig) >= 1.03
# cpan
BuildRequires:  perl(Glib) >= 1.180
BuildRequires:  perl(Glib::MakeHelper)
BuildRequires:  perl(Gtk2) >= 1.00
BuildRequires:  perl(Test::More)
BuildRequires:  perl(Test::Pod)
BuildRequires:  perl(Test::Pod::Coverage)
#BuildRequires:	libunique-devel
BuildRequires:  pkgconfig(unique-1.0)
Requires:       perl(ExtUtils::Depends) >= 0.20
Requires:       perl(ExtUtils::PkgConfig) >= 1.03
Requires:       perl(Glib) >= 1.180
Requires:       perl(Gtk2) >= 1.00
BuildRoot:      %{_tmppath}/%{name}-%{version}-build
%if 0%{?suse_version} < 1120
BuildRequires:  perl-macros
%endif
%if 0%{?suse_version} && 0%{?suse_version} < 1140
Requires:       perl = %{perl_version}
%else
%{perl_requires}
%endif

%description
Perl bindings for the C library "libunique" that provides a mechanism for
writing single instance applications. If you launch a single instance
application twice, the second instance will either just quit or will send a
message to the running instance.

%prep
%setup -q -n %{cpan_name}-%{version}
%patch0 -p1
%patch1 -p1

%build
perl Makefile.PL INSTALLDIRS="vendor" OPTIMIZE="%{optflags}"
make %{?_smp_mflags}

%check
make %{?_smp_mflags} test

%install
%perl_make_install
%perl_process_packlist
%perl_gen_filelist

# make sure filelist grabs *all* shared libaries.
sed -i.orig -e 's/\.so[\.0-9]*$/\.so*/' %{name}.files

%files -f %{name}.files
%defattr(644,root,root,755)
%doc Changes README examples/ t/
%dir %{perl_vendorarch}/Gtk2/Unique
%dir %{perl_vendorarch}/Gtk2/Unique/Install

%changelog
