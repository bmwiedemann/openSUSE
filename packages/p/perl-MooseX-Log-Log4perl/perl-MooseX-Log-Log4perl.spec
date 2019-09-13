#
# spec file for package perl-MooseX-Log-Log4perl
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


Name:           perl-MooseX-Log-Log4perl
Version:        0.47
Release:        0
%define cpan_name MooseX-Log-Log4perl
Summary:        Logging Role for Moose based on Log::Log4perl
License:        Artistic-1.0 or GPL-1.0+
Group:          Development/Libraries/Perl
Url:            http://search.cpan.org/dist/MooseX-Log-Log4perl/
Source0:        https://cpan.metacpan.org/authors/id/L/LA/LAMMEL/%{cpan_name}-%{version}.tar.gz
Source1:        cpanspec.yml
BuildArch:      noarch
BuildRoot:      %{_tmppath}/%{name}-%{version}-build
BuildRequires:  perl
BuildRequires:  perl-macros
BuildRequires:  perl(IO::Scalar)
BuildRequires:  perl(Log::Log4perl) >= 1.13
BuildRequires:  perl(Moo) >= 1.000007
Requires:       perl(Log::Log4perl) >= 1.13
Requires:       perl(Moo) >= 1.000007
Recommends:     perl(Moose) >= 0.65
%{perl_requires}

%description
A logging role building a very lightweight wrapper to Log::Log4perl for use
with your Moose or Moo classes. The initialization of the Log4perl instance
must be performed prior to logging the first log message. Otherwise the
default initialization will happen, probably not doing the things you
expect.

For compatibility the 'logger' attribute can be accessed to use a common
interface for application logging.

Using the logger within a class is as simple as consuming a role:

    package MyClass;
    use Moose;
    with 'MooseX::Log::Log4perl';

    sub dummy {
        my $self = shift;
        $self->log->info("Dummy log entry");
    }

The logger needs to be setup before using the logger, which could happen in
the main application:

    package main;
    use Log::Log4perl qw(:easy);
    use MyClass;

    BEGIN { Log::Log4perl->easy_init() };

    my $myclass = MyClass->new();
    $myclass->log->info("In my class"); # Access the log of the object
    $myclass->dummy;                    # Will log "Dummy log entry"

%prep
%setup -q -n %{cpan_name}-%{version}
# MANUAL BEGIN
sed -i -e 's/use inc::Module::Install/use lib q[.];\nuse inc::Module::Install/' Makefile.PL
# MANUAL END

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
