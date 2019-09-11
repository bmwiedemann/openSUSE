#
# spec file for package perl-URI-Find
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


Name:           perl-URI-Find
Version:        20160806
Release:        0
%define cpan_name URI-Find
Summary:        Find URIs in arbitrary text
License:        Artistic-1.0 or GPL-1.0+
Group:          Development/Libraries/Perl
Url:            http://search.cpan.org/dist/URI-Find/
Source0:        http://www.cpan.org/authors/id/M/MS/MSCHWERN/%{cpan_name}-%{version}.tar.gz
Source1:        cpanspec.yml
BuildArch:      noarch
BuildRoot:      %{_tmppath}/%{name}-%{version}-build
BuildRequires:  perl
BuildRequires:  perl-macros
BuildRequires:  perl(Module::Build) >= 0.300000
BuildRequires:  perl(Test::More) >= 0.88
BuildRequires:  perl(URI) >= 1.60
Requires:       perl(URI) >= 1.60
%{perl_requires}

%description
This module does one thing: Finds URIs and URLs in plain text. It finds
them quickly and it finds them *all* (or what URI.pm considers a URI to
be.) It only finds URIs which include a scheme (http:// or the like), for
something a bit less strict have a look at URI::Find::Schemeless.

For a command-line interface, urifind is provided.

%prep
%setup -q -n %{cpan_name}-%{version}

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
%doc appveyor.yml Changes LICENSE README TODO

%changelog
