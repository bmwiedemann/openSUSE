#
# spec file for package perl-Gravatar-URL
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


Name:           perl-Gravatar-URL
Version:        1.07
Release:        0
%define cpan_name Gravatar-URL
Summary:        Make URLs for Gravatars from an email address
License:        Artistic-1.0 or GPL-1.0+
Group:          Development/Libraries/Perl
Url:            http://search.cpan.org/dist/Gravatar-URL/
Source0:        http://www.cpan.org/authors/id/M/MS/MSCHWERN/%{cpan_name}-%{version}.tar.gz
Source1:        cpanspec.yml
BuildArch:      noarch
BuildRoot:      %{_tmppath}/%{name}-%{version}-build
BuildRequires:  perl
BuildRequires:  perl-macros
BuildRequires:  perl(Digest::SHA)
BuildRequires:  perl(Module::Build) >= 0.420000
BuildRequires:  perl(Net::DNS) >= 1.01
BuildRequires:  perl(Test::MockRandom) >= 1.01
BuildRequires:  perl(Test::Warn) >= 0.11
BuildRequires:  perl(URI::Escape)
BuildRequires:  perl(parent)
Requires:       perl(Digest::SHA)
Requires:       perl(Net::DNS) >= 1.01
Requires:       perl(URI::Escape)
Requires:       perl(parent)
%{perl_requires}

%description
A Gravatar is a Globally Recognized Avatar for a given email address. This
allows you to have a global picture associated with your email address. You
can look up the Gravatar for any email address by constructing a URL to get
the image from gravatar.com. This module does that.

Examples of use include the author faces on http://search.cpan.org.

See http://gravatar.com for more info.

%prep
%setup -q -n %{cpan_name}-%{version}
find . -type f ! -name \*.pl -print0 | xargs -0 chmod 644

%build
%{__perl} Build.PL installdirs=vendor
./Build build flags=%{?_smp_mflags}

%check
./Build test

%install
./Build install destdir=%{buildroot} create_packlist=0
%perl_gen_filelist

%files -f %{name}.files
%defattr(-,root,root,755)
%doc Changes LICENSE README

%changelog
