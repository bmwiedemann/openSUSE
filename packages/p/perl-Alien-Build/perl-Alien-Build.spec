#
# spec file for package perl-Alien-Build
#
# Copyright (c) 2022 SUSE LLC
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


%define cpan_name Alien-Build
Name:           perl-Alien-Build
Version:        2.76
Release:        0
License:        Artistic-1.0 OR GPL-1.0-or-later
Summary:        Build external dependencies for use in CPAN
URL:            https://metacpan.org/release/%{cpan_name}
Source0:        https://cpan.metacpan.org/authors/id/P/PL/PLICEASE/%{cpan_name}-%{version}.tar.gz
Source1:        cpanspec.yml
BuildRequires:  perl
BuildRequires:  perl-macros
BuildRequires:  perl(Capture::Tiny) >= 0.17
BuildRequires:  perl(Digest::SHA)
BuildRequires:  perl(ExtUtils::CBuilder)
BuildRequires:  perl(ExtUtils::MakeMaker) >= 6.64
BuildRequires:  perl(ExtUtils::ParseXS) >= 3.30
BuildRequires:  perl(FFI::CheckLib) >= 0.11
BuildRequires:  perl(File::Which) >= 1.10
BuildRequires:  perl(File::chdir)
BuildRequires:  perl(JSON::PP)
BuildRequires:  perl(List::Util) >= 1.33
BuildRequires:  perl(Path::Tiny) >= 0.077
BuildRequires:  perl(Test2::API) >= 1.302096
BuildRequires:  perl(Test2::V0) >= 0.000121
BuildRequires:  perl(Text::ParseWords) >= 3.26
BuildRequires:  perl(parent)
Requires:       perl(Capture::Tiny) >= 0.17
Requires:       perl(Digest::SHA)
Requires:       perl(ExtUtils::CBuilder)
Requires:       perl(ExtUtils::MakeMaker) >= 6.64
Requires:       perl(ExtUtils::ParseXS) >= 3.30
Requires:       perl(FFI::CheckLib) >= 0.11
Requires:       perl(File::Which) >= 1.10
Requires:       perl(File::chdir)
Requires:       perl(JSON::PP)
Requires:       perl(List::Util) >= 1.33
Requires:       perl(Path::Tiny) >= 0.077
Requires:       perl(Test2::API) >= 1.302096
Requires:       perl(Text::ParseWords) >= 3.26
Requires:       perl(parent)
%{perl_requires}
# MANUAL BEGIN
BuildRequires:  pkg-config
# MANUAL END

%description
This module provides tools for building external (non-CPAN) dependencies
for CPAN. It is mainly designed to be used at install time of a CPAN
client, and work closely with Alien::Base which is used at runtime.

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
%doc author.yml Changes Changes.Alien-Base Changes.Alien-Base-Wrapper Changes.Alien-Build-Decode-Mojo Changes.Test-Alien example README SUPPORT
%license LICENSE

%changelog
