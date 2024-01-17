#
# spec file for package perl-Growl-GNTP
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


Name:           perl-Growl-GNTP
Version:        0.21
Release:        0
%define cpan_name Growl-GNTP
Summary:        Perl implementation of GNTP Protocol (Client Part)
License:        Artistic-1.0 or GPL-1.0+
Group:          Development/Libraries/Perl
Url:            http://search.cpan.org/dist/Growl-GNTP/
Source0:        http://www.cpan.org/authors/id/M/MA/MATTN/%{cpan_name}-%{version}.tar.gz
Source1:        cpanspec.yml
BuildArch:      noarch
BuildRoot:      %{_tmppath}/%{name}-%{version}-build
BuildRequires:  perl
BuildRequires:  perl-macros
BuildRequires:  perl(Crypt::CBC) >= 2.29
BuildRequires:  perl(Data::UUID) >= 0.149
BuildRequires:  perl(Digest::SHA) >= 5.45
BuildRequires:  perl(Module::Build::Tiny) >= 0.035
Requires:       perl(Crypt::CBC) >= 2.29
Requires:       perl(Data::UUID) >= 0.149
Requires:       perl(Digest::SHA) >= 5.45
%{perl_requires}

%description
Growl::GNTP is Perl implementation of GNTP Protocol (Client Part)

%prep
%setup -q -n %{cpan_name}-%{version}

%build
%{__perl} Build.PL --installdirs=vendor
./Build build --flags=%{?_smp_mflags}

%check
./Build test

%install
./Build install --destdir=%{buildroot} --create_packlist=0
%perl_gen_filelist

%files -f %{name}.files
%defattr(-,root,root,755)
%doc Changes examples LICENSE README.md

%changelog
