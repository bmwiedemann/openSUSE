#
# spec file for package perl-Prima
#
# Copyright (c) 2024 SUSE LLC
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


%define cpan_name Prima
Name:           perl-Prima
Version:        1.75000
Release:        0
%define cpan_version 1.75
#Upstream: SUSE-Public-Domain
License:        AGPL-3.0-only AND BSD-2-Clause
Summary:        Perl graphic toolkit
URL:            https://metacpan.org/release/%{cpan_name}
Source0:        https://cpan.metacpan.org/authors/id/K/KA/KARASIK/%{cpan_name}-%{cpan_version}.tar.gz
Source1:        cpanspec.yml
BuildRequires:  perl
BuildRequires:  perl-macros
Provides:       perl(Prima) = %{version}
%undefine       __perllib_provides
%{perl_requires}
# MANUAL BEGIN
BuildRequires:  giflib-devel
BuildRequires:  libpng-devel
BuildRequires:  libtiff-devel
BuildRequires:  xkeyboard-config
BuildRequires:  xorg-x11
BuildRequires:  xorg-x11-Xvfb
BuildRequires:  pkgconfig(x11)
BuildRequires:  pkgconfig(xcomposite)
BuildRequires:  pkgconfig(xcursor)
BuildRequires:  pkgconfig(xext)
BuildRequires:  pkgconfig(xft)
BuildRequires:  pkgconfig(xpm)
BuildRequires:  pkgconfig(xproto)
BuildRequires:  pkgconfig(xrandr)
BuildRequires:  pkgconfig(xrender)
%define         X_display         ":98"
Requires:       xorg-x11
# MANUAL END

%description
Prima is a classic 2D GUI toolkit that works under Windows and X11
environments. The toolkit features a rich widget library, extensive 2D
graphic support, PDF generation, modern Unicode text input and output, and
supports a wide set of image formats. Additionally, the RAD-style Visual
Builder and POD viewer are included. The toolkit can interoperate with
other popular event loop libraries.

%prep
%autosetup  -n %{cpan_name}-%{cpan_version}

find . -type f ! -path "*/t/*" ! -name "*.pl" ! -path "*/bin/*" ! -path "*/script/*" ! -path "*/scripts/*" ! -name "configure" -print0 | xargs -0 chmod 644

%build
perl Makefile.PL INSTALLDIRS=vendor OPTIMIZE="%{optflags}"
%make_build

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
%doc AGPLv3 Changes examples README.md
%license Copying LICENSE

%changelog
