#
# spec file for package console-setup
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


Name:           console-setup
Version:        1.215
Release:        0
Summary:        Tools for configuring the console using X Window System key maps
License:        GPL-2.0-or-later AND MIT AND SUSE-Public-Domain
Group:          System/Console
URL:            https://salsa.debian.org/installer-team/console-setup
Source:         https://deb.debian.org/debian/pool/main/c/%{name}/%{name}_%{version}.tar.xz
# PATCH-FIX-OPENSUSE console-setup-1.76-fsf-address.patch -- Fix the FSF address.
Patch0:         console-setup-1.76-fsf-address.patch
# PATCH-FIX-OPENSUSE console-setup-paths.patch -- Change installing paths to SUSE-style.
Patch1:         console-setup-paths.patch
BuildRequires:  perl
BuildRequires:  perl(encoding)
Suggests:       xkeyboard-config
BuildArch:      noarch

%description
This package provides the console with the same keyboard
configuration scheme that X Window System has.
Besides the keyboard, the package also configures the font on the
console.  It includes a rich collection of fonts and supports
several languages that would be otherwise unsupported on the
console (such as Armenian, Georgian, Lao and Thai).

%package -n bdf2psf
Summary:        Generate console fonts from BDF source fonts

%description -n bdf2psf
This package provides a command-line converter that can be used in
scripts to build console fonts from BDF sources automatically.
The converter comes with a collection of font encodings that cover
many of the world's languages. The output font can use a different
character encoding from the input. When the source font does not
define a glyph for a particular symbol in the encoding table, that
glyph position in the console font is not wasted but used for
another symbol.

%prep
%autosetup -n %{name} -p1

cp -a debian/changelog ChangeLog
cp -a debian/copyright COPYING

%build
%make_build build-linux

%install
make prefix=%{buildroot}%{_prefix} install-linux
# we don't want another set of keyboard descriptions, we want to use descriptions from
# xkeyboard-config (require it?), so removing it
# or maybe have these from tarball it in optional subpackage?
rm -r %{buildroot}%{_sysconfdir}/console-setup/

install -Dpm 0755 Fonts/bdf2psf %{buildroot}%{_bindir}/bdf2psf
install -Dpm 0644 man/bdf2psf.1 %{buildroot}%{_mandir}/man1/bdf2psf.1

mkdir -p %{buildroot}%{_datadir}/bdf2psf/
cp -a Fonts/fontsets/ Fonts/*.equivalents Fonts/*.set \
  %{buildroot}%{_datadir}/bdf2psf/

%files
%license COPYING copyright.fonts copyright.xkb Fonts/copyright
%doc ChangeLog README
%config(noreplace) %{_sysconfdir}/default/console-setup
%config(noreplace) %{_sysconfdir}/default/keyboard
%{_bindir}/ckbcomp
%{_bindir}/setupcon
%dir %{_datadir}/kbd
%{_datadir}/kbd/consolefonts/
%{_datadir}/kbd/consoletrans/
%{_mandir}/man1/setupcon.1%{?ext_man}
%{_mandir}/man1/ckbcomp.1%{?ext_man}
%{_mandir}/man5/keyboard.5%{?ext_man}
%{_mandir}/man5/console-setup.5%{?ext_man}

%files -n bdf2psf
%{_bindir}/bdf2psf
%{_datadir}/bdf2psf/
%{_mandir}/man1/bdf2psf.1%{?ext_man}

%changelog
