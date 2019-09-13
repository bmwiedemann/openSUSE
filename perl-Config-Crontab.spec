#
# spec file for package perl-Config-Crontab
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


Name:           perl-Config-Crontab
Version:        1.45
Release:        0
%define cpan_name Config-Crontab
Summary:        Read/Write Vixie compatible crontab(5) files
License:        GPL-1.0+ or Artistic-1.0
Group:          Development/Libraries/Perl
Url:            http://search.cpan.org/dist/Config-Crontab/
Source0:        https://cpan.metacpan.org/authors/id/S/SC/SCOTTW/%{cpan_name}-%{version}.tar.gz
Source1:        cpanspec.yml
BuildArch:      noarch
BuildRoot:      %{_tmppath}/%{name}-%{version}-build
BuildRequires:  perl
BuildRequires:  perl-macros
%{perl_requires}

%description
*Config::Crontab* provides an object-oriented interface to Vixie-style
crontab(5) files for Perl.

A *Config::Crontab* object allows you to manipulate an ordered set of
*Event*, *Env*, or *Comment* objects (also included with this package).
Descriptions of these packages may be found below.

In short, *Config::Crontab* reads and writes crontab(5) files (and does a
little pretty-printing too) using objects. The general idea is that you
create a *Config::Crontab* object and associate it with a file (if
unassociated, it will work over a pipe to 'crontab -l'). From there, you
can add lines to your crontab object, change existing line attributes, and
write everything back to file.

Now, to successfully navigate the module's ins and outs, we'll need a
little terminology lesson.

%prep
%setup -q -n %{cpan_name}-%{version}
find . -type f ! -name \*.pl -print0 | xargs -0 chmod 644

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
%doc Changes example README

%changelog
