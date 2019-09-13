#
# spec file for package perl-MIME-tools
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


Name:           perl-MIME-tools
Version:        5.509
Release:        0
%define cpan_name MIME-tools
Summary:        Tools to manipulate MIME messages
License:        Artistic-1.0 or GPL-1.0+
Group:          Development/Libraries/Perl
Url:            http://search.cpan.org/dist/MIME-tools/
Source0:        https://cpan.metacpan.org/authors/id/D/DS/DSKOLL/%{cpan_name}-%{version}.tar.gz
Source1:        cpanspec.yml
BuildArch:      noarch
BuildRoot:      %{_tmppath}/%{name}-%{version}-build
BuildRequires:  perl
BuildRequires:  perl-macros
BuildRequires:  perl(File::Temp) >= 0.18
BuildRequires:  perl(Mail::Field) >= 1.05
BuildRequires:  perl(Mail::Header) >= 1.01
BuildRequires:  perl(Mail::Internet) >= 1.0203
BuildRequires:  perl(Test::Deep)
Requires:       perl(File::Temp) >= 0.18
Requires:       perl(Mail::Field) >= 1.05
Requires:       perl(Mail::Header) >= 1.01
Requires:       perl(Mail::Internet) >= 1.0203
Recommends:     perl(Convert::BinHex)
%{perl_requires}

%description
Tools to manipulate MIME messages

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
%doc ChangeLog examples README
%license COPYING

%changelog
