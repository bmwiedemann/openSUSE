#
# spec file for package perl-Module-Runtime
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


Name:           perl-Module-Runtime
Version:        0.016
Release:        0
%define cpan_name Module-Runtime
Summary:        Runtime Module Handling
License:        Artistic-1.0 or GPL-1.0+
Group:          Development/Libraries/Perl
Url:            http://search.cpan.org/dist/Module-Runtime/
Source0:        https://cpan.metacpan.org/authors/id/Z/ZE/ZEFRAM/%{cpan_name}-%{version}.tar.gz
Source1:        cpanspec.yml
BuildArch:      noarch
BuildRoot:      %{_tmppath}/%{name}-%{version}-build
BuildRequires:  perl
BuildRequires:  perl-macros
BuildRequires:  perl(Module::Build)
%{perl_requires}

%description
The functions exported by this module deal with runtime handling of Perl
modules, which are normally handled at compile time. This module avoids
using any other modules, so that it can be used in low-level
infrastructure.

The parts of this module that work with module names apply the same syntax
that is used for barewords in Perl source. In principle this syntax can
vary between versions of Perl, and this module applies the syntax of the
Perl on which it is running. In practice the usable syntax hasn't changed
yet. There's some intent for Unicode module names to be supported in the
future, but this hasn't yet amounted to any consistent facility.

The functions of this module whose purpose is to load modules include
workarounds for three old Perl core bugs regarding 'require'. These
workarounds are applied on any Perl version where the bugs exist, except
for a case where one of the bugs cannot be adequately worked around in pure
Perl.

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
