#
# spec file for package dvdisaster
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


# See also http://en.opensuse.org/openSUSE:Specfile_guidelines
Name:           dvdisaster
Version:        0.79.6
Release:        0
Summary:        Additional error protection for CD/DVD media
License:        GPL-3.0-or-later
Group:          Productivity/Multimedia/Other

# The official website no longer exists only this mirror
URL:            http://htmlpreview.github.io/?https://github.com/lrq3000/dvdisaster/blob/stable/dvdisaster/documentation/en/index.html

Source0:        http://deb.debian.org/debian/pool/main/d/dvdisaster/%{name}_%{version}.orig.tar.bz2#/%{name}-%{version}.tar.bz2
Source1:        http://deb.debian.org/debian/pool/main/d/%{name}/%{name}_%{version}.orig.tar.bz2.asc#/%{name}-%{version}.tar.bz2.asc
# PATCH-FIX-UPSTREAM davejplater@gmail.com Fix scripts/bash-based-configure to work in Tumbleweed.
Patch0:         dvdisaster-findmake.patch
# Patches from Debian
Patch1:         02-encryption.patch
Patch2:         03-dvdrom.patch
Patch3:         05-help-dialog.patch
#Patch4:         08-fix-gnu-make-detection.patch
Patch5:         10-use-non-size-specific-icon-and-add-keywords-to-desktop-file.patch
Patch6:         11-no-cruft.patch
Patch7:         12-fix-spelling-of-up-to.patch
Patch8:         13-fix-missing-language-field-in-po-files.patch
Patch9:         14-make-builds-reproducible.patch
Patch10:        15-show-new-pkg-tracker.patch
Patch11:        16-remove-auto-build-of-doco-from-install-rule.patch
Patch12:        17-fix-all-but-deprecated-api-warnings.patch
Patch13:        18-update-copyright-in-about-dialog.patch
Patch14:        19-show-text-files-with-abs-path.patch
Patch15:        20-display-changelog-credits-and-todo.patch
Patch16:        22-fix-hurd-i386-ftbfs.patch
Patch17:        23-add-bdrom-support.patch
Patch18:        24-show-gpl3-license.patch
Patch19:        25-fix-man-pages.patch
Patch20:        26-fix-display-of-manual.pdf.patch
Patch21:        27-allow-opening-in-browser-again.patch
Patch22:        28-pdftex-reproducibility.patch
Patch23:        29-fix-more-typos.patch
Patch24:        30-hurd-kfreebsd-ftbfs.patch
Patch25:        31-improve-hurd-and-kfreebsd-support.patch
Patch26:        32-display-compilation-commands.patch
Patch27:        33-honour-LDFLAGS.patch
Patch28:        34-gcc8-format-security.patch
Patch29:        35-archived-homepage.patch
Patch30:        36-fix-parallelism.patch
Patch31:        37-suggest-dvdisaster-doc.patch
#Patch32:        dvdisaster-0.79.5-dvdrom.patch
#PATCH-FIX-OPENSUSE  davejplater@gmail.com dvdisaster-no-tex.patch - tries to build pdfs that already exist
Patch33:        dvdisaster-no-tex.patch
Patch34:        dvdisaster-g_strdup_printf.patch
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
BuildArch:      noarch

%description docs
Documentation package for using dvdisaster in PDF format.

%prep
%setup -q
%autopatch -p1
gmake -v | grep "GNU Make" && echo $# || echo $#

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
%make_install
rm -f %{buildroot}%{_bindir}/dvdisaster-uninstall.sh
%find_lang dvdisaster

%files -f dvdisaster.lang
%{_bindir}/%{name}
%doc README CHANGELOG CREDITS.de CREDITS.en README.MODIFYING TODO
%license COPYING
%{_mandir}/de/man1/%{name}.1%{ext_man}
%{_mandir}/man1/%{name}.1%{ext_man}

%files docs
%doc documentation/user-manual/manual.pdf

%changelog
