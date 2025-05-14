#
# spec file for package perl-Test-Object
#
# Copyright (c) 2025 SUSE LLC
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


%define cpan_name Test-Object
Name:           perl-Test-Object
Version:        0.80.0
Release:        0
# 0.08 -> normalize -> 0.80.0
%define cpan_version 0.08
License:        Artistic-1.0 OR GPL-1.0-or-later
Summary:        Thoroughly testing objects via registered handlers
URL:            https://metacpan.org/release/%{cpan_name}
Source0:        https://cpan.metacpan.org/authors/id/E/ET/ETHER/%{cpan_name}-%{cpan_version}.tar.gz
Source1:        cpanspec.yml
BuildArch:      noarch
BuildRequires:  perl
BuildRequires:  perl-macros
Provides:       perl(Test::Object) = %{version}
Provides:       perl(Test::Object::Test) = %{version}
%undefine       __perllib_provides
%{perl_requires}

%description
In situations where you have deep trees of classes, there is a common
situation in which you test a module 4 or 5 subclasses down, which should
follow the correct behaviour of not just the subclass, but of all the
parent classes.

This should be done to ensure that the implementation of a subclass has not
somehow "broken" the object's behaviour in a more general sense.

'Test::Object' is a testing package designed to allow you to easily test
what you believe is a valid object against the expected behaviour of *all*
of the classes in its inheritance tree in one single call.

To do this, you "register" tests (in the form of CODE or function
references) with 'Test::Object', with each test associated with a
particular class.

When you call 'object_ok' in your test script, 'Test::Object' will check
the object against all registered tests. For each class that your object
responds to '$object->isa($class)' for, the appropriate testing function
will be called.

Doing it this way allows adapter objects and other things that respond to
'isa' differently that the default to still be tested against the classes
that it is advertising itself as correctly.

This also means that more than one test might be "counted" for each call to
'object_ok'. You should account for this correctly in your expected test
count.

%prep
%autosetup  -n %{cpan_name}-%{cpan_version} -p1

# MANUAL BEGIN
sed -i -e 's/use inc::Module::Install/use lib q[.];\nuse inc::Module::Install/' Makefile.PL
# MANUAL END

%build
perl Makefile.PL INSTALLDIRS=vendor
%make_build

%check
make test

%install
%perl_make_install
%perl_process_packlist
%perl_gen_filelist

%files -f %{name}.files
%doc Changes CONTRIBUTING README
%license LICENSE

%changelog
