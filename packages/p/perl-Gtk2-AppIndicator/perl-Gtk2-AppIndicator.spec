#
# spec file for package perl-Gtk2-AppIndicator
#
# Copyright (c) 2014 SUSE LINUX Products GmbH, Nuernberg, Germany.
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


%define cpan_name Gtk2-AppIndicator
Name:           perl-Gtk2-AppIndicator
Version:        0.15
Release:        0
Summary:        Perl interface to the libappindicator
License:        Artistic-1.0-Perl
Group:          Development/Languages/Perl
Url:            https://launchpad.net/libgtk2-appindicator-perl
Source:         https://launchpad.net/libgtk2-appindicator-perl/trunk/hades/+download/%{cpan_name}-%{version}.tar.gz
BuildRequires:  perl
BuildRequires:  perl(ExtUtils::Constant)
BuildRequires:  perl(Gtk2)
BuildRequires:  perl-macros
BuildRequires:  pkg-config
BuildRequires:  pkgconfig(appindicator-0.1)
BuildRequires:  pkgconfig(gtk+-2.0)
Requires:       perl(Gtk2)
%{perl_requires}

%description
This package provides perl bindings for libappindicator.
libappindicator is a library which provides a tray icon in desktop
environments via StatusNotifierItem implementation.

%prep
%setup -q -n %{cpan_name}-%{version}

%build
perl Makefile.PL INSTALLDIRS=vendor OPTIMIZE='%{optflags}'
make %{?_smp_mflags}

%install
%perl_make_install
%perl_process_packlist
%perl_gen_filelist

%files -f %{name}.files
%defattr(-,root,root)
%doc Changes COPYRIGHT LICENSE README

%changelog
