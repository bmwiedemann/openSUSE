#
# spec file for package perl-Mojolicious-Plugin-RenderFile
#
# Copyright (c) 2018 SUSE LINUX GmbH, Nuernberg, Germany.
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


Name:           perl-Mojolicious-Plugin-RenderFile
Version:        0.12
Release:        0
%define cpan_name Mojolicious-Plugin-RenderFile
Summary:        "render_file" helper for Mojolicious
License:        GPL-1.0-or-later OR Artistic-1.0
Group:          Development/Libraries/Perl
Url:            https://metacpan.org/release/%{cpan_name}
Source0:        https://cpan.metacpan.org/authors/id/K/KO/KOORCHIK/%{cpan_name}-%{version}.tar.gz
Source1:        cpanspec.yml
BuildArch:      noarch
BuildRoot:      %{_tmppath}/%{name}-%{version}-build
BuildRequires:  perl
BuildRequires:  perl-macros
BuildRequires:  perl(Mojolicious) >= 5.78
Requires:       perl(Mojolicious) >= 5.78
%{perl_requires}

%description
Mojolicious::Plugin::RenderFile is a Mojolicious plugin that adds
"render_file" helper. It does not read file in memory and just streaming it
to a client.

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
if [ -f %{buildroot}/%{perl_vendorlib}/Mojolicious/Plugin/README.pod ]; then
mv %{buildroot}/%{perl_vendorlib}/Mojolicious/Plugin/README{,-RenderFile}.pod
fi
%perl_gen_filelist

%files -f %{name}.files
%defattr(-,root,root,755)
%doc Changes

%changelog
