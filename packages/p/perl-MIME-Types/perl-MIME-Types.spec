#
# spec file for package perl-MIME-Types
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

# Please submit bugfixes or comments via http://bugs.opensuse.org/
#


Name:           perl-MIME-Types
Version:        2.17
Release:        0
%define cpan_name MIME-Types
Summary:        Definition of MIME types
License:        Artistic-1.0 or GPL-1.0+
Group:          Development/Libraries/Perl
Url:            http://search.cpan.org/dist/MIME-Types/
Source0:        https://cpan.metacpan.org/authors/id/M/MA/MARKOV/%{cpan_name}-%{version}.tar.gz
Source1:        cpanspec.yml
BuildArch:      noarch
BuildRoot:      %{_tmppath}/%{name}-%{version}-build
BuildRequires:  perl
BuildRequires:  perl-macros
%{perl_requires}

%description
MIME types are used in many applications (for instance as part of e-mail
and HTTP traffic) to indicate the type of content which is transmitted. or
expected. See RFC2045 at _https://www.ietf.org/rfc/rfc2045.txt_

Sometimes detailed knowledge about a mime-type is need, however this module
only knows about the file-name extensions which relate to some filetype. It
can also be used to produce the right format: types which are not
registered at IANA need to use 'x-' prefixes.

This object administers a huge list of known mime-types, combined from
various sources. For instance, it contains *all IANA* types and the
knowledge of Apache. Probably the most complete table on the net!

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
%doc ChangeLog README README.md

%changelog
