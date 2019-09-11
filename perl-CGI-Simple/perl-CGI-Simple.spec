#
# spec file for package perl-CGI-Simple
#
# Copyright (c) 2018 SUSE LINUX GmbH, Nuernberg, Germany.
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


Name:           perl-CGI-Simple
Version:        1.21
Release:        0
%define cpan_name CGI-Simple
Summary:        Object-oriented CGI interface compliant to CGI.pm
License:        Artistic-1.0 OR GPL-1.0-or-later
Group:          Development/Libraries/Perl
Url:            https://metacpan.org/release/%{cpan_name}
Source0:        https://cpan.metacpan.org/authors/id/M/MA/MANWAR/%{cpan_name}-%{version}.tar.gz
Source1:        cpanspec.yml
BuildArch:      noarch
BuildRoot:      %{_tmppath}/%{name}-%{version}-build
BuildRequires:  perl
BuildRequires:  perl-macros
BuildRequires:  perl(IO::Scalar)
BuildRequires:  perl(Module::Build)
BuildRequires:  perl(Test::Exception)
BuildRequires:  perl(Test::NoWarnings)
Requires:       perl(IO::Scalar)
Requires:       perl(Test::Exception)
Requires:       perl(Test::NoWarnings)
%{perl_requires}
# MANUAL BEGIN
# after 1.115 came 1.12 - provide the zero padded version number to fix version checks
Provides:       perl(CGI::Simple) = %{version}0
Provides:       perl(CGI::Simple::Cookie) = %{version}0
# MANUAL END

%description
CGI::Simple provides a relatively lightweight drop in replacement for
CGI.pm. It shares an identical OO interface to CGI.pm for parameter
parsing, file upload, cookie handling and header generation. This module is
entirely object oriented, however a complete functional interface is
available by using the CGI::Simple::Standard module.

Essentially everything in CGI.pm that relates to the CGI (not HTML) side of
things is available. There are even a few new methods and additions to old
ones! If you are interested in what has gone on under the hood see the
Compatibility with CGI.pm section at the end.

In practical testing this module loads and runs about twice as fast as
CGI.pm depending on the precise task.

%prep
%setup -q -n %{cpan_name}-%{version}

%build
perl Build.PL installdirs=vendor
./Build build flags=%{?_smp_mflags}

%check
./Build test

%install
./Build install destdir=%{buildroot} create_packlist=0
%perl_gen_filelist

%files -f %{name}.files
%defattr(-,root,root,755)
%doc Changes README

%changelog
