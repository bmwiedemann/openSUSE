#
# spec file for package perl-Email-Sender
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


Name:           perl-Email-Sender
Version:        1.300035
Release:        0
%define cpan_name Email-Sender
Summary:        Library for sending email
License:        Artistic-1.0 OR GPL-1.0-or-later
Group:          Development/Libraries/Perl
URL:            https://metacpan.org/release/%{cpan_name}
Source0:        https://cpan.metacpan.org/authors/id/R/RJ/RJBS/%{cpan_name}-%{version}.tar.gz
Source1:        cpanspec.yml
BuildArch:      noarch
BuildRoot:      %{_tmppath}/%{name}-%{version}-build
BuildRequires:  perl
BuildRequires:  perl-macros
BuildRequires:  perl(Capture::Tiny) >= 0.08
BuildRequires:  perl(Email::Abstract) >= 3.006
BuildRequires:  perl(Email::Address)
BuildRequires:  perl(Email::Simple) >= 1.998
BuildRequires:  perl(File::Path) >= 2.060000
BuildRequires:  perl(List::Util) >= 1.45
BuildRequires:  perl(Module::Runtime)
BuildRequires:  perl(Moo) >= 2.000000
BuildRequires:  perl(Moo::Role)
BuildRequires:  perl(MooX::Types::MooseLike) >= 0.15
BuildRequires:  perl(MooX::Types::MooseLike::Base)
BuildRequires:  perl(Net::SMTP) >= 3.07
BuildRequires:  perl(Sub::Exporter)
BuildRequires:  perl(Sub::Exporter::Util)
BuildRequires:  perl(Test::More) >= 0.96
BuildRequires:  perl(Throwable::Error) >= 0.200003
BuildRequires:  perl(Try::Tiny)
Requires:       perl(Email::Abstract) >= 3.006
Requires:       perl(Email::Address)
Requires:       perl(Email::Simple) >= 1.998
Requires:       perl(File::Path) >= 2.060000
Requires:       perl(List::Util) >= 1.45
Requires:       perl(Module::Runtime)
Requires:       perl(Moo) >= 2.000000
Requires:       perl(Moo::Role)
Requires:       perl(MooX::Types::MooseLike) >= 0.15
Requires:       perl(MooX::Types::MooseLike::Base)
Requires:       perl(Net::SMTP) >= 3.07
Requires:       perl(Sub::Exporter)
Requires:       perl(Sub::Exporter::Util)
Requires:       perl(Throwable::Error) >= 0.200003
Requires:       perl(Try::Tiny)
%{perl_requires}

%description
Email::Sender replaces the old and sometimes problematic Email::Send
library, which did a decent job at handling very simple email sending
tasks, but was not suitable for serious use, for a variety of reasons.

Most users will be able to use Email::Sender::Simple to send mail. Users
with more specific needs should look at the available
Email::Sender::Transport classes.

Documentation may be found in Email::Sender::Manual, and new users should
start with Email::Sender::Manual::QuickStart.

%prep
%setup -q -n %{cpan_name}-%{version}
find . -type f ! -path "*/t/*" ! -name "*.pl" ! -path "*/bin/*" ! -path "*/script/*" ! -name "configure" -print0 | xargs -0 chmod 644

%build
perl Makefile.PL INSTALLDIRS=vendor
make %{?_smp_mflags}

%check
make test

%install
%perl_make_install
%perl_process_packlist
%perl_gen_filelist

%files -f %{name}.files
%defattr(-,root,root,755)
%doc Changes README util
%license LICENSE

%changelog
