#
# spec file for package perl-Mouse
#
# Copyright (c) 2025 SUSE LLC and contributors
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


%define cpan_name Mouse
Name:           perl-Mouse
Version:        2.6.0
Release:        0
# v2.6.0 -> normalize -> 2.6.0
%define cpan_version v2.6.0
License:        Artistic-1.0 OR GPL-1.0-or-later
Summary:        Moose minus the antlers
URL:            https://metacpan.org/release/%{cpan_name}
Source0:        https://cpan.metacpan.org/authors/id/S/SY/SYOHEX/%{cpan_name}-%{cpan_version}.tar.gz
Source1:        cpanspec.yml
Source100:      README.md
BuildRequires:  perl
BuildRequires:  perl-macros
BuildRequires:  perl(Devel::PPPort) >= 3.59
BuildRequires:  perl(ExtUtils::ParseXS) >= 3.22
BuildRequires:  perl(Module::Build) >= 0.400.500
BuildRequires:  perl(Module::Build::XSUtil) >= 0.190
BuildRequires:  perl(Test::Exception)
BuildRequires:  perl(Test::Fatal)
BuildRequires:  perl(Test::LeakTrace)
BuildRequires:  perl(Test::More) >= 0.88
BuildRequires:  perl(Test::Output)
BuildRequires:  perl(Test::Requires)
BuildRequires:  perl(Try::Tiny)
BuildRequires:  perl(version) >= 0.9913
%{perl_requires}

%description
Moose is a postmodern object system for Perl5. Moose is wonderful.

Unfortunately, Moose has a compile-time penalty. Though significant
progress has been made over the years, the compile time penalty is a
non-starter for some very specific applications. If you are writing a
command-line application or CGI script where startup time is essential, you
may not be able to use Moose (we recommend that you instead use persistent
Perl executing environments like 'FastCGI' for the latter, if possible).

Mouse is a Moose compatible object system, which aims to alleviate this
penalty by providing a subset of Moose's functionality.

We're also going as light on dependencies as possible. Mouse currently has
*no dependencies* except for building/testing modules. Mouse also works
without XS, although it has an XS backend to make it much faster.

%prep
%autosetup -n %{cpan_name}-%{cpan_version} -p1

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
