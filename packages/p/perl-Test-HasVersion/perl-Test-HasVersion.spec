#
# spec file for package perl-Test-HasVersion
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


Name:           perl-Test-HasVersion
Version:        0.014
Release:        0
%define cpan_name Test-HasVersion
Summary:        Check Perl modules have version numbers
License:        Artistic-1.0 or GPL-1.0+
Group:          Development/Libraries/Perl
Url:            http://search.cpan.org/dist/Test-HasVersion/
Source0:        http://www.cpan.org/authors/id/F/FE/FERREIRA/%{cpan_name}-%{version}.tar.gz
Source1:        cpanspec.yml
BuildArch:      noarch
BuildRoot:      %{_tmppath}/%{name}-%{version}-build
BuildRequires:  perl
BuildRequires:  perl-macros
BuildRequires:  perl(Test::Builder::Tester) >= 1.04
Requires:       perl(Test::Builder::Tester) >= 1.04
%{perl_requires}

%description
Do you wanna check that every one of your Perl modules in a distribution
has a version number? You wanna make sure you don't forget the brand new
modules you just added? Well, that's the module you have been looking for.
Use it!

Do you wanna check someone else's distribution to make sure the author have
not committed the sin of leaving Perl modules without a version that can be
used to tell if you have this or that feature? 'Test::HasVersion' is also
for you, nasty little fellow.

There's a script _test_version_ which is installed with this distribution.
You may invoke it from within the root directory of a distribution you just
unpacked, and it will check every _.pm_ file in the directory and under
_lib/_ (if any).

  $ test_version

You may also provide directories and files as arguments.

  $ test_version *.pm lib/ inc/
  $ test_version .

(Be warned that many Perl modules in a _t/_ directory do not receive
versions because they are not used outside the distribution.)

Ok. That's not a very useful module by now. But it will be. Wait for the
upcoming releases.

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
%doc Changes LICENSE README

%changelog
