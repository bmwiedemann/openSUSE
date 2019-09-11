#
# spec file for package perl-Mock-Quick
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


Name:           perl-Mock-Quick
Version:        1.111
Release:        0
%define cpan_name Mock-Quick
Summary:        Quickly mock objects and classes, even temporarily replace them,
License:        Artistic-1.0 or GPL-1.0+
Group:          Development/Libraries/Perl
Url:            http://search.cpan.org/dist/Mock-Quick/
Source0:        http://www.cpan.org/authors/id/E/EX/EXODIST/%{cpan_name}-%{version}.tar.gz
Source1:        cpanspec.yml
BuildArch:      noarch
BuildRoot:      %{_tmppath}/%{name}-%{version}-build
BuildRequires:  perl
BuildRequires:  perl-macros
BuildRequires:  perl(Exporter::Declare) >= 0.103
BuildRequires:  perl(Fennec::Lite) >= 0.004
BuildRequires:  perl(Module::Build) >= 0.420000
BuildRequires:  perl(Test::Exception) >= 0.290000
BuildRequires:  perl(Test::Simple) >= 0.88
Requires:       perl(Exporter::Declare) >= 0.103
%{perl_requires}

%description
Mock-Quick is here to solve the current problems with Mocking libraries.

There are a couple Mocking libraries available on CPAN. The primary
problems with these libraries include verbose syntax, and most importantly
side-effects. Some Mocking libraries expect you to mock a specific class,
and will unload it then redefine it. This is particularly a problem if you
only want to override a class on a lexical level.

Mock-Quick provides a declarative mocking interface that results in a very
concise, but clear syntax. There are separate facilities for mocking object
instances, and classes. You can quickly create an instance of an object
with custom attributes and methods. You can also quickly create an
anonymous class, optionally inheriting from another, with whatever methods
you desire.

Mock-Quick also provides a tool that provides an OO interface to overriding
methods in existing classes. This tool also allows for the restoration of
the original class methods. Best of all this is a localized tool, when your
control object falls out of scope the original class is restored.

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
%doc Changes README

%changelog
