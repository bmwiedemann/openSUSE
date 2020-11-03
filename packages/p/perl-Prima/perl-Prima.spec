#
# spec file for package perl-Prima
#
# Copyright (c) 2020 SUSE LLC
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


Name:           perl-Prima
Version:        1.60
Release:        0
#Upstream: SUSE-Public-Domain
%define cpan_name Prima
Summary:        Perl graphic toolkit
License:        BSD-2-Clause AND AGPL-3.0-only
Group:          Development/Libraries/Perl
URL:            https://metacpan.org/release/%{cpan_name}
Source0:        https://cpan.metacpan.org/authors/id/K/KA/KARASIK/%{cpan_name}-%{version}.tar.gz
Source1:        cpanspec.yml
BuildRoot:      %{_tmppath}/%{name}-%{version}-build
BuildRequires:  perl
BuildRequires:  perl-macros
%{perl_requires}
# MANUAL BEGIN
BuildRequires:  giflib-devel
BuildRequires:  libpng-devel
BuildRequires:  libtiff-devel
BuildRequires:  xkeyboard-config
BuildRequires:  xorg-x11
BuildRequires:  xorg-x11-Xvfb
BuildRequires:  xorg-x11-devel
%define         X_display         ":98"
Requires:       xorg-x11
# MANUAL END

%description
The toolkit is combined from two basic set of classes - core and external.
The core classes are coded in C and form a base line for every Prima object
written in perl. The usage of C is possible together with the toolkit;
however, its full power is revealed in the perl domain. The external
classes present easily expandable set of widgets, written completely in
perl and communicating with the system using Prima library calls.

%prep
%setup -q -n %{cpan_name}-%{version}

%build
perl Makefile.PL INSTALLDIRS=vendor OPTIMIZE="%{optflags}"
make %{?_smp_mflags}

%check
make test

%install
%perl_make_install
%perl_process_packlist
# MANUAL BEGIN
## oops, Prima/Config.pm must not contain BUILD_ROOT
find $RPM_BUILD_ROOT -name 'Config.pm' -print0 | xargs -0 perl -i -pe "s{\\Q$RPM_BUILD_ROOT}"'{}g'
###
### should these go to a perl-Prima-devel ?
find $RPM_BUILD_ROOT/%{perl_vendorarch} -name \*.h | xargs -t rm
# MANUAL END
%perl_gen_filelist

%files -f %{name}.files
%defattr(-,root,root,755)
%doc AGPLv3 Changes examples README.md
%license Copying LICENSE

%changelog
