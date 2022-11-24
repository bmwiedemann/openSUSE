#
# spec file for package nano
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


%define _version 7
Name:           nano
Version:        7.0
Release:        0
Summary:        Pico editor clone with enhancements
License:        GPL-3.0-or-later
Group:          Productivity/Text/Editors
URL:            https://nano-editor.org/
Source0:        https://nano-editor.org/dist/v%{_version}/%{name}-%{version}.tar.xz
Source1:        https://nano-editor.org/dist/v%{_version}/%{name}-%{version}.tar.xz.asc
Source2:        https://savannah.gnu.org/people/viewgpg.php?user_id=42085#/%{name}.keyring
Source3:        nanorc
# PATCH-FIX-OPENSUSE obs-channel-and-patchinfo-syntax.patch maurizio.galli@suse.com -- enable syntax for _channel and _patchinfo files used by OBS
Patch0:         obs-channel-and-patchinfo-syntax.patch
BuildRequires:  file-devel
BuildRequires:  groff-full
BuildRequires:  makeinfo
BuildRequires:  pkgconfig
BuildRequires:  pkgconfig(ncurses)
BuildRequires:  pkgconfig(zlib)

%description
GNU nano is a small and friendly text editor. It aims to emulate
the Pico text editor while also offering a few enhancements.

%lang_package

%prep
%autosetup -p1

%build
%configure \
  --disable-rpath \
  --enable-utf8
%make_build

# generate default /etc/nanorc
# - set hunspell as the default spell-checker
# - enable syntax highlighting by default
sed -e 's/^#.*set speller.*$/set speller "hunspell"/' \
    -e 's|^# \(include "%{_datadir}/nano/\*.nanorc"\)|\1|' \
    %{SOURCE3} doc/sample.nanorc > ./nanorc

%install
%make_install

# Move documents to a proper directory.
mkdir -p %{buildroot}%{_docdir}/
mv -f %{buildroot}%{_datadir}/doc/%{name}/ %{buildroot}%{_docdir}/%{name}/

# install default /etc/nanorc
mkdir -p %{buildroot}%{_sysconfdir}
install -m 0644 ./nanorc %{buildroot}%{_sysconfdir}/nanorc

# enable useful extra syntax highlighting files by default
mv %{buildroot}%{_datadir}/nano/extra/{ada,fortran,haskell,spec}.* %{buildroot}%{_datadir}/nano

%find_lang %{name} --with-man --all-name

%files
%license COPYING COPYING.DOC
%doc AUTHORS ChangeLog* IMPROVEMENTS NEWS README THANKS TODO doc/sample.nanorc
%doc %{_docdir}/nano/
%{_bindir}/nano
%{_bindir}/rnano
%config(noreplace) %{_sysconfdir}/nanorc
%{_datadir}/nano/
%{_infodir}/nano.info%{?ext_info}
%{_mandir}/man1/nano.1%{?ext_man}
%{_mandir}/man1/rnano.1%{?ext_man}
%{_mandir}/man5/nanorc.5%{?ext_man}

%files lang -f %{name}.lang
%license COPYING COPYING.DOC

%changelog
