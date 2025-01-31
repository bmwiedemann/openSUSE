#
# spec file for package perl-Feature-Compat-Class
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


%define cpan_name Feature-Compat-Class
Name:           perl-Feature-Compat-Class
Version:        0.70.0
Release:        0
# 0.07 -> normalize -> 0.70.0
%define cpan_version 0.07
License:        Artistic-1.0 OR GPL-1.0-or-later
Summary:        Make class syntax available
URL:            https://metacpan.org/release/%{cpan_name}
Source0:        https://cpan.metacpan.org/authors/id/P/PE/PEVANS/%{cpan_name}-%{cpan_version}.tar.gz
Source1:        cpanspec.yml
BuildArch:      noarch
BuildRequires:  perl
BuildRequires:  perl-macros
BuildRequires:  perl(Module::Build) >= 0.4004
BuildRequires:  perl(Object::Pad) >= 0.806
BuildRequires:  perl(Test::More) >= 0.88
Requires:       perl(Object::Pad) >= 0.806
Provides:       perl(Feature::Compat::Class) = %{version}
%undefine       __perllib_provides
%{perl_requires}

%description
This module provides the new 'class' keyword and related others ('method',
'field' and 'ADJUST') in a forward-compatible way.

Perl added such syntax at version 5.38.0, which is enabled by

   use feature 'class';

This syntax was further expanded in 5.40, adding the '__CLASS__' keyword
and ':reader' attribute on fields.

On that version of perl or later, this module simply enables the core
feature equivalent of using it directly. On such perls, this module will
install with no non-core dependencies, and requires no C compiler.

On older versions of perl before such syntax is availble in core, it is
currently provided instead using the Object::Pad module, imported with a
special set of options to configure it to only recognise the same syntax as
the core perl feature, thus ensuring any code using it will still continue
to function on that newer perl.

This module is a work-in-progress, because the underlying 'feature 'class''
is too. Many of the limitations and inabilities listed below are a result
of the early-access nature of this branch, and are expected to be lifted as
work progresses towards a more featureful and complete implementation.

%prep
%autosetup  -n %{cpan_name}-%{cpan_version} -p1

%build
perl Build.PL --installdirs=vendor
./Build build --flags=%{?_smp_mflags}

%check
./Build test

%install
./Build install --destdir=%{buildroot} --create_packlist=0
%perl_gen_filelist

%files -f %{name}.files
%doc Changes README
%license LICENSE

%changelog
