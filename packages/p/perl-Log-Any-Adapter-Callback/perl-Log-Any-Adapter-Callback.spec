#
# spec file for package perl-Log-Any-Adapter-Callback
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


%define cpan_name Log-Any-Adapter-Callback
Name:           perl-Log-Any-Adapter-Callback
Version:        0.102.0
Release:        0
%define cpan_version 0.102
License:        Artistic-1.0 OR GPL-1.0-or-later
Summary:        (DEPRECATED)(ADOPTME) Send Log::Any logs to a subroutine
URL:            https://metacpan.org/release/%{cpan_name}
Source0:        https://cpan.metacpan.org/authors/id/P/PE/PERLANCAR/%{cpan_name}-%{cpan_version}.tar.gz
BuildArch:      noarch
BuildRequires:  perl
BuildRequires:  perl-macros
BuildRequires:  perl(Log::Any::Adapter) >= 0.11
BuildRequires:  perl(Test::More) >= 0.98
Requires:       perl(Log::Any::Adapter) >= 0.11
Provides:       perl(Log::Any::Adapter::Callback) = %{version}
%define         __perllib_provides /bin/true
%{perl_requires}

%description
DEPRECATION NOTICE: Log::Any distribution since 1.708 comes with
Log::Any::Adapter::Capture which does the same thing. I'm deprecating this
adapter now.

This adapter lets you specify callback subroutine to be called by
Log::Any's logging methods (like $log->debug(), $log->error(), etc) and
detection methods (like $log->is_warning(), $log->is_fatal(), etc.).

This adapter is used for customized logging, and is mostly a convenient
construct to save a few lines of code. You could achieve the same effect by
creating a full Log::Any adapter class.

Your logging callback subroutine will be called with these arguments:

 ($method, $self, $format, @params)

where $method is the name of method (like "debug") and ($self, $format,
@params) are given by Log::Any.

%prep
%autosetup  -n %{cpan_name}-%{cpan_version}

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
%doc Changes README
%license LICENSE

%changelog
