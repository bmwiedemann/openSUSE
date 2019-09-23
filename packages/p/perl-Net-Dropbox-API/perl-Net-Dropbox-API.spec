#
# spec file for package perl-Net-Dropbox-API
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


Name:           perl-Net-Dropbox-API
Version:        1.9
Release:        0
%define cpan_name Net-Dropbox-API
Summary:        A dropbox API interface
License:        Artistic-1.0 or GPL-1.0+
Group:          Development/Libraries/Perl
Url:            http://search.cpan.org/dist/Net-Dropbox-API/
Source:         http://www.cpan.org/authors/id/N/NO/NORBU/%{cpan_name}-%{version}.tar.gz
BuildArch:      noarch
BuildRoot:      %{_tmppath}/%{name}-%{version}-build
BuildRequires:  perl
BuildRequires:  perl-macros
BuildRequires:  perl(Data::Random)
BuildRequires:  perl(HTTP::Request::Common)
BuildRequires:  perl(JSON)
BuildRequires:  perl(LWP::UserAgent)
BuildRequires:  perl(Mouse)
BuildRequires:  perl(Net::OAuth)
BuildRequires:  perl(URI)
BuildRequires:  perl(common::sense)
Requires:       perl(Data::Random)
Requires:       perl(HTTP::Request::Common)
Requires:       perl(JSON)
Requires:       perl(LWP::UserAgent)
Requires:       perl(Mouse)
Requires:       perl(Net::OAuth)
Requires:       perl(URI)
Requires:       perl(common::sense)
%{perl_requires}

%description
A dropbox API interface

%prep
%setup -q -n %{cpan_name}-%{version}
find . -type f -print0 | xargs -0 chmod 644

%build
PERL5LIB=. %{__perl} Makefile.PL INSTALLDIRS=vendor
%{__make} %{?_smp_mflags}

%check
%{__make} test

%install
%perl_make_install
%perl_process_packlist
%perl_gen_filelist

%files -f %{name}.files
%defattr(-,root,root,755)
%doc Changes examples ignore.txt README

%changelog
