#
# spec file for package perl-Mail-Message
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


Name:           perl-Mail-Message
Version:        3.010
Release:        0
%define cpan_name Mail-Message
Summary:        General message object
License:        Artistic-1.0 OR GPL-1.0-or-later
Group:          Development/Libraries/Perl
URL:            https://metacpan.org/release/%{cpan_name}
Source0:        https://cpan.metacpan.org/authors/id/M/MA/MARKOV/%{cpan_name}-%{version}.tar.gz
Source1:        cpanspec.yml
BuildArch:      noarch
BuildRoot:      %{_tmppath}/%{name}-%{version}-build
BuildRequires:  perl
BuildRequires:  perl-macros
BuildRequires:  perl(Date::Format)
BuildRequires:  perl(Date::Parse)
BuildRequires:  perl(Encode) >= 2.26
BuildRequires:  perl(IO::Scalar)
BuildRequires:  perl(MIME::Types) >= 1.004
BuildRequires:  perl(Mail::Address) >= 2.17
BuildRequires:  perl(Time::Zone)
BuildRequires:  perl(URI) >= 1.23
BuildRequires:  perl(User::Identity) >= 1
Requires:       perl(Date::Format)
Requires:       perl(Date::Parse)
Requires:       perl(Encode) >= 2.26
Requires:       perl(IO::Scalar)
Requires:       perl(MIME::Types) >= 1.004
Requires:       perl(Mail::Address) >= 2.17
Requires:       perl(Time::Zone)
Requires:       perl(URI) >= 1.23
Requires:       perl(User::Identity) >= 1
%{perl_requires}

%description
A 'Mail::Message' object is a container for MIME-encoded message
information, as defined by RFC2822. Everything what is not specificaly
related to storing the messages in mailboxes (folders) is implemented in
this class. Methods which are related to folders is implemented in the
Mail::Box::Message extension.

%prep
%setup -q -n %{cpan_name}-%{version}

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
%doc ChangeLog README README.md

%changelog
