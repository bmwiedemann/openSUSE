#
# spec file for package perl-Log-Message
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


Name:           perl-Log-Message
Version:        0.08
Release:        0
%define cpan_name Log-Message
Summary:        A generic message storing mechanism
License:        Artistic-1.0 or GPL-1.0+
Group:          Development/Libraries/Perl
Url:            http://search.cpan.org/dist/Log-Message/
Source:         http://www.cpan.org/authors/id/B/BI/BINGOS/%{cpan_name}-%{version}.tar.gz
BuildArch:      noarch
BuildRoot:      %{_tmppath}/%{name}-%{version}-build
BuildRequires:  perl
BuildRequires:  perl-macros
BuildRequires:  perl(Locale::Maketext::Simple)
BuildRequires:  perl(Module::Load)
BuildRequires:  perl(Params::Check)
Requires:       perl(Locale::Maketext::Simple)
Requires:       perl(Module::Load)
Requires:       perl(Params::Check)
%{perl_requires}

%description
Log::Message is a generic message storage mechanism. It allows you to store
messages on a stack -- either shared or private -- and assign meta-data to
it. Some meta-data will automatically be added for you, like a timestamp
and a stack trace, but some can be filled in by the user, like a tag by
which to identify it or group it, and a level at which to handle the
message (for example, log it, or die with it)

Log::Message also provides a powerful way of searching through items by
regexes on messages, tags and level.

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
%doc CHANGES README

%changelog
