#
# spec file for package dvdisaster
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


# See also http://en.opensuse.org/openSUSE:Specfile_guidelines
Name:           dvdisaster
Version:        0.79.6
Release:        0
Summary:        Additional error protection for CD/DVD media
License:        GPL-3.0
Group:          Productivity/Multimedia/Other
Url:            http://dvdisaster.net/en/index.html
Source0:        http://dvdisaster.net/downloads/%{name}-%{version}.tar.bz2
Source1:        http://dvdisaster.net/downloads/%{name}-%{version}.tar.bz2.gpg
# PATCH-FIX-UPSTREAM davejplater@gmail.com Fix scripts/bash-based-configure to work in Tumbleweed.
Patch0:         dvdisaster-findmake.patch
BuildRequires:  desktop-file-utils
BuildRequires:  gettext
BuildRequires:  pkgconfig
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
Summary:        Additional error protection for CD/DVD media
Group:          Documentation/Other
BuildArch:      noarch

%description docs
Documentation package for using dvdisaster in PDF format.

%prep
%setup -q
%patch0
gmake -v | grep "GNU Make" && echo $# || echo $#

%build
%configure --with-nls=yes \
           --docdir=%{_docdir} \
           --docsubdir=%{name} \
           --localedir=%{_datadir}/locale \
           --buildroot=%{buildroot}
make V=1
# Parallel make breaks translations sometimes.
#%%{?_smp_mflags}
%install
%make_install
rm -f %{buildroot}%{_bindir}/dvdisaster-uninstall.sh
%find_lang dvdisaster

%files -f dvdisaster.lang
%{_bindir}/%{name}
%doc README CHANGELOG COPYING CREDITS.de CREDITS.en README.MODIFYING TODO
%{_mandir}/de/man1/%{name}.1%{ext_man}
%{_mandir}/man1/%{name}.1%{ext_man}
%exclude %{_docdir}/%{name}/manual.pdf

%files docs
%doc %{_docdir}/%{name}/manual.pdf

%changelog
