#
# spec file for package perl-Data-Clone
#
# Copyright (c) 2023 SUSE LLC
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


%define cpan_name Data-Clone
Name:           perl-Data-Clone
Version:        0.6.0
Release:        0
%define cpan_version 0.006
License:        Artistic-1.0 OR GPL-1.0-or-later
Summary:        Polymorphic data cloning
URL:            https://metacpan.org/release/%{cpan_name}
Source0:        https://cpan.metacpan.org/authors/id/I/IS/ISHIGAKI/%{cpan_name}-%{cpan_version}.tar.gz
Source1:        perl-Data-Clone-rpmlintrc
Source2:        cpanspec.yml
BuildRequires:  perl
BuildRequires:  perl-macros
BuildRequires:  perl(Devel::PPPort) >= 3.19
BuildRequires:  perl(ExtUtils::MakeMaker) >= 6.59
BuildRequires:  perl(ExtUtils::ParseXS) >= 3.18
BuildRequires:  perl(Module::Build) >= 0.4005
BuildRequires:  perl(Module::Build::XSUtil) >= 0.03
BuildRequires:  perl(Test::More) >= 0.88
BuildRequires:  perl(Test::Requires) >= 0.03
BuildRequires:  perl(parent)
Requires:       perl(parent)
Provides:       perl(Data::Clone) = %{version}
%define         __perllib_provides /bin/true
%{perl_requires}

%description
'Data::Clone' does data cloning, i.e. copies things recursively. This is
smart so that it works with not only non-blessed references, but also with
blessed references (i.e. objects). When 'clone()' finds an object, it calls
a 'clone' method of the object if the object has a 'clone', otherwise it
makes a surface copy of the object. That is, this module does polymorphic
data cloning.

Although there are several modules on CPAN which can clone data, this
module has a different cloning policy from almost all of them. See Cloning
policy and Comparison to other cloning modules for details.

%prep
%autosetup  -n %{cpan_name}-%{cpan_version}

%build
perl Build.PL --installdirs=vendor optimize="%{optflags}"
./Build build --flags=%{?_smp_mflags}

%check
./Build test

%install
./Build install --destdir=%{buildroot} --create_packlist=0
%perl_gen_filelist

%files -f %{name}.files
%doc Changes example README.md
%license LICENSE

%changelog
