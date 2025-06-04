#
# spec file for package perl-CSS-Sass
#
# Copyright (c) 2021 SUSE LLC
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


%define cpan_name CSS-Sass
Name:           perl-CSS-Sass
Version:        3.6.4
Release:        0
Summary:        Compile .scss files using libsass
License:        MIT
URL:            https://metacpan.org/release/%{cpan_name}
Source0:        https://cpan.metacpan.org/authors/id/O/OC/OCBNET/%{cpan_name}-%{version}.tar.gz
Source1:        cpanspec.yml
BuildRequires:  perl
BuildRequires:  perl-macros
BuildRequires:  perl(Encode::Locale) >= 0.01
BuildRequires:  perl(ExtUtils::CppGuess) >= 0.14
BuildRequires:  perl(ExtUtils::MakeMaker) >= 6.52
BuildRequires:  perl(File::chdir) >= 0.01
BuildRequires:  perl(Filesys::Notify::Simple) >= 0.01
BuildRequires:  perl(List::Util) >= 1.45
BuildRequires:  perl(Test::Differences) >= 0.01
BuildRequires:  perl(YAML::XS) >= 0.01
BuildRequires:  perl(version)
Requires:       perl(Encode::Locale) >= 0.01
Requires:       perl(Filesys::Notify::Simple) >= 0.01
Requires:       perl(List::Util) >= 1.45
Requires:       perl(version)
%{perl_requires}
# MANUAL BEGIN
BuildRequires:  gcc-c++
BuildRequires:  perl(ExtUtils::CppGuess)
BuildRequires:  perl(Test::Differences)
BuildRequires:  perl(YAML::XS)
# MANUAL END

%description
CSS::Sass provides a perl interface to libsass, a fairly complete Sass
compiler written in C++. It is currently around ruby sass 3.3/3.4 feature
parity and heading towards full 3.4 compatibility. It can compile .scss and
.sass files.

%prep
%autosetup  -n %{cpan_name}-%{version}
find . -type f ! -path "*/t/*" ! -name "*.pl" ! -path "*/bin/*" ! -path "*/script/*" ! -name "configure" -print0 | xargs -0 chmod 644

%build
perl Makefile.PL INSTALLDIRS=vendor OPTIMIZE="%{optflags}"
%make_build

%check
make test

%install
%perl_make_install
%perl_process_packlist
%perl_gen_filelist

%files -f %{name}.files
%doc appveyor.yml Changes CODE_OF_CONDUCT.md perlobject.map README.md util
%license LICENSE

%changelog
