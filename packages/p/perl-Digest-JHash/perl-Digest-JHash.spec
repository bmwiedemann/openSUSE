#
# spec file for package perl-Digest-JHash
#
# Copyright (c) 2016 SUSE LINUX GmbH, Nuernberg, Germany.
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


Name:           perl-Digest-JHash
Version:        0.10
Release:        0
%define cpan_name Digest-JHash
Summary:        Perl extension for 32 bit Jenkins Hashing Algorithm
License:        Artistic-2.0
Group:          Development/Libraries/Perl
Url:            http://search.cpan.org/dist/Digest-JHash/
Source0:        http://www.cpan.org/authors/id/S/SH/SHLOMIF/%{cpan_name}-%{version}.tar.gz
Source1:        cpanspec.yml
BuildRoot:      %{_tmppath}/%{name}-%{version}-build
BuildRequires:  perl
BuildRequires:  perl-macros
%{perl_requires}

%description
The 'Digest::JHash' module allows you to use the fast JHash hashing
algorithm developed by Bob Jenkins from within Perl programs. The algorithm
takes as input a message of arbitrary length and produces as output a
32-bit "message digest" of the input in the form of an unsigned long
integer.

Call it a low calorie version of MD5 if you like.

See http://burtleburtle.net/bob/hash/doobs.html for more information.

%prep
%setup -q -n %{cpan_name}-%{version}
find . -type f ! -name \*.pl -print0 | xargs -0 chmod 644

%build
%{__perl} Makefile.PL INSTALLDIRS=vendor OPTIMIZE="%{optflags}"
%{__make} %{?_smp_mflags}

%check
%{__make} test

%install
%perl_make_install
%perl_process_packlist
%perl_gen_filelist

%files -f %{name}.files
%defattr(-,root,root,755)
%doc Changes examples html LICENSE misc README

%changelog
