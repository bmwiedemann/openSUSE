#
# spec file for package perl-UNIVERSAL-require
#
# Copyright (c) 2015 SUSE LINUX GmbH, Nuernberg, Germany.
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


Name:           perl-UNIVERSAL-require
Version:        0.18
Release:        0
%define cpan_name UNIVERSAL-require
Summary:        require() modules from a variable
License:        Artistic-1.0 or GPL-1.0+
Group:          Development/Libraries/Perl
Url:            http://search.cpan.org/dist/UNIVERSAL-require/
Source:         http://www.cpan.org/authors/id/N/NE/NEILB/%{cpan_name}-%{version}.tar.gz
BuildArch:      noarch
BuildRoot:      %{_tmppath}/%{name}-%{version}-build
BuildRequires:  perl
BuildRequires:  perl-macros
%{perl_requires}

%description
If you've ever had to do this...

    eval "require $module";

to get around the bareword caveats on require(), this module is for you. It
creates a universal require() class method that will work with every Perl
module and its secure. So instead of doing some arcane eval() work, you can
do this:

    $module->require;

It doesn't save you much typing, but it'll make a lot more sense to someone
who's not a ninth level Perl acolyte.

%prep
%setup -q -n %{cpan_name}-%{version}

%build
%{__perl} Makefile.PL INSTALLDIRS=vendor
%{__make} %{?_smp_mflags}

%check
%{__make} test

%install
%perl_make_install
%perl_process_packlist
%perl_gen_filelist

%files -f %{name}.files
%defattr(-,root,root,755)
%doc Changes README

%changelog
