#
# spec file for package dvdisaster
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


# See also http://en.opensuse.org/openSUSE:Specfile_guidelines
Name:           dvdisaster
Version:        0.79.10
Release:        0
Summary:        Additional error protection for CD/DVD media
License:        GPL-3.0-or-later
Group:          Productivity/Multimedia/Other
URL:            https://dvdisaster.jcea.es/
Source0:        https://dvdisaster.jcea.es/downloads/%{name}-%{version}.tar.bz2
Source1:        https://dvdisaster.jcea.es/downloads/%{name}-%{version}.tar.bz2.gpg
# PATCH-FIX-OPENSUSE correct desktop catagories.
Patch0:         dvdisaster-desktop-cat.patch
Patch1:         dvdisaster-addstdio.patch
BuildRequires:  desktop-file-utils
BuildRequires:  fdupes
BuildRequires:  gettext
BuildRequires:  pkgconfig
BuildRequires:  update-desktop-files
BuildRequires:  pkgconfig(gtk+-2.0)
BuildRequires:  pkgconfig(libpng16)
Requires:       dvdisaster-docs = %{version}

%description
%{name} provides a margin of safety against data loss on CD and DVD media
caused by scratches or aging. It creates error correction data,
which is used to recover unreadable sectors if the disc becomes damaged
at a later time.

%description -l cs
%{name} poskytuje dodatečnou ochranu proti ztrátě dat na médiích CD a DVD
způsobených poškrábáním nebo stárnutím. Vytváří data oprav chyb, která
jsou použita pro obnovu nečitelných sektorů, pokud se disk později
poškodí.

%description -l de
%{name} erzeugt einen Sicherheitspuffer gegen Datenverluste, die auf
CD- und DVD-Datenträgern durch Alterung oder Kratzer entstehen. Es erzeugt
Fehlerkorrekturdaten, um bei nachfolgenden Datenträger-Problemen unlesbare
Sektoren zu rekonstruieren.

%description -l it
%{name} offre un margine di sicurezza contro la perdita di dati dei supporti
CD e DVD causata dall'invecchiamento e dai graffi. Crea dei dati di correzione
degli errori che saranno poi utilizzati per recuperare i settori illeggibili
se il supporto dovesse danneggiarsi col tempo.

%package docs
Summary:        PDF Documentation for dvdisaster
Group:          Documentation/Other
BuildArch:      noarch

%description docs
Documentation package for using dvdisaster in PDF format.

%prep
%setup -q
%autopatch -p1
gmake -v | grep "GNU Make"

%build
#gcc10 is picky about global headers without extern, -fcommon fixes this for now.
export CFLAGS="%{optflags} -fcommon"
%configure --with-nls=yes \
           --docdir=%{_docdir} \
           --docsubdir=%{name} \
           --localedir=%{_datadir}/locale \
           --buildroot=%{buildroot}
make --trace

# Parallel make breaks translations sometimes.
#%%{?_smp_mflags}
%install
rm -f dvdisaster.lang
%make_install
mkdir -p %{buildroot}%{_datadir}/applications
cp -v contrib/%{name}.desktop %{buildroot}%{_datadir}/applications/
%suse_update_desktop_file %{name}
%find_lang %{name}
pushd %{buildroot}%{_docdir}/%{name}
rm -f `ls |grep -v manual.pdf
popd`
rm -f %{buildroot}%{_bindir}/dvdisaster-uninstall.sh
%fdupes -s %{buildroot}/%{_prefix}

%files -f dvdisaster.lang
%{_bindir}/%{name}
# NOTE: adding COPYING to the doc directory as well as license
#is not a mistake it's for the license display in the help menu
%doc README CHANGELOG CREDITS.de CREDITS.en TODO
%license COPYING
%{_mandir}/de/man1/%{name}.1%{ext_man}
%{_mandir}/man1/%{name}.1%{ext_man}
%{_datadir}/applications/%{name}.desktop

%files docs
%{_docdir}/%{name}/manual.pdf

%changelog
