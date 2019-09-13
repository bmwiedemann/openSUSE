#
# spec file for package patterns-desktop
#
# Copyright (c) 2019 SUSE LINUX GmbH, Nuernberg, Germany.
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


%bcond_with betatest

Name:           patterns-desktop
Version:        20170319
Release:        0
Summary:        Patterns for Installation (desktop patterns)
License:        MIT
Group:          Metapackages
Url:            https://github.com/openSUSE/patterns
Source0:        %{name}-rpmlintrc
BuildRoot:      %{_tmppath}/%{name}-%{version}-build
BuildRequires:  patterns-rpm-macros

%description
This is an internal package that is used to create the patterns as part
of the installation source setup.  Installation of this package does
not make sense.

This particular package contains all the desktop related patterns that are not 
specific too one particular desktop environment

################################################################################

%package books
%pattern_documentation
Summary:        Documentation
Group:          Metapackages
Provides:       patterns-openSUSE-books = %{version}
Provides:       pattern() = books
Provides:       pattern-icon() = pattern-documentation
Provides:       pattern-order() = 5200
Provides:       pattern-visible()
Obsoletes:      patterns-openSUSE-books < %{version}

Recommends:     opensuse-manuals_en
Recommends:     opensuse-startup_en-pdf
Suggests:       ImageMagick-doc
Suggests:       amavisd-new-docs
Suggests:       apache2-doc
Suggests:       apparmor-docs
Suggests:       bash-doc
Suggests:       bind-doc
Suggests:       digikam-doc
Suggests:       dhcp-doc
Suggests:       docbook-tdg
Suggests:       gcc-info
Suggests:       gcc46-info
Suggests:       gnome-devel-docs
Suggests:       gnome-user-docs
Suggests:       kernel-docs
Suggests:       kiwi-doc
Suggests:       man-pages
Suggests:       man-pages-fr
Suggests:       man-pages-it
Suggests:       man-pages-ja
Suggests:       man-pages-ko
Suggests:       man-pages-posix
Suggests:       man-pages-ru
Suggests:       nfs-doc
Suggests:       ntp-doc
Suggests:       perl-doc
Suggests:       php-doc
Suggests:       postfix-doc
Suggests:       postgresql-docs
Suggests:       python-doc
Suggests:       python3-doc
Suggests:       python-doc-pdf
Suggests:       python3-doc-pdf
Suggests:       samba-doc
Suggests:       selinux-doc
Suggests:       subversion-doc
Suggests:       texlive-doc
Suggests:       texlive-latex-doc
Suggests:       xorg-docs
Suggests:       yast2-devel-doc
Suggests:       opensuse-manuals_de
Suggests:       opensuse-manuals_hu
Suggests:       opensuse-manuals_ru
Suggests:       opensuse-startup_de-pdf
Suggests:       opensuse-startup_ru-pdf

%description books
Help and Documentation, various books.

%files books
%dir /usr/share/doc/packages/patterns
/usr/share/doc/packages/patterns/books.txt

################################################################################

%package imaging
%pattern_desktopfunctions
Summary:        Graphics
Group:          Metapackages
Provides:       pattern() = imaging
Provides:       pattern-icon() = pattern-x11
Provides:       pattern-order() = 1860
Provides:       pattern-visible()
Requires:       pattern() = x11
Provides:       patterns-openSUSE-imaging = %{version}
Obsoletes:      patterns-openSUSE-imaging < %{version}
# from data/IMAGE
Recommends:     gimp
Recommends:     gimp-help
Suggests:       exiftool
Suggests:       ufraw
Suggests:       gimp-ufraw
Suggests:       pfstools
Suggests:       pfstmo
Suggests:       pfscalibration
Suggests:       calibre

%description imaging
Handling of digital photos and graphics.

%files imaging
%dir /usr/share/doc/packages/patterns
/usr/share/doc/packages/patterns/imaging.txt

################################################################################

%package laptop
%pattern_basetechnologies
Summary:        Laptop
Group:          Metapackages
Provides:       patterns-openSUSE-laptop = %{version}
Provides:       pattern() = laptop
Provides:       pattern-icon() = pattern-laptop
Provides:       pattern-order() = 1200
Provides:       pattern-visible()
Requires:       pattern() = base
Obsoletes:      patterns-openSUSE-laptop < %{version}

Recommends:     pcmciautils
Recommends:     wpa_supplicant
# bnc#480879
Recommends:     crda
Recommends:     wireless-regdb
Recommends:     iw
# https://www.reddit.com/r/openSUSE/comments/3rzzrx/notebook_powersaving_in_leap_421/
Recommends:     tlp
Suggests:       irda
Suggests:       smbios-utils-python
Suggests:       powertop
# fate#303035
Suggests:       laptop-mode-tools

%description laptop
Tools designed specifically for laptop computers.

%files laptop
%dir /usr/share/doc/packages/patterns
/usr/share/doc/packages/patterns/laptop.txt

################################################################################

%package multimedia
%pattern_desktopfunctions
Summary:        Multimedia
Group:          Metapackages
Provides:       patterns-openSUSE-multimedia = %{version}
Provides:       pattern() = multimedia
Provides:       pattern-icon() = pattern-multimedia
Provides:       pattern-order() = 1580
Provides:       pattern-visible()
Obsoletes:      patterns-openSUSE-multimedia < %{version}

Recommends:     yast2-sound
Recommends:     dvd+rw-tools
Recommends:     vorbis-tools
Recommends:     ImageMagick
Recommends:     mjpegtools
Suggests:       blender
Suggests:       ripit
# maintained by coolo - must be good
Suggests:       abcde
Suggests:       audacity
Suggests:       timidity
Suggests:       vdr
Suggests:       xawtv
Suggests:       flac

%description multimedia
Multimedia players, sound editing tools, video and image manipulation applications.

%files multimedia
%dir /usr/share/doc/packages/patterns
/usr/share/doc/packages/patterns/multimedia.txt

################################################################################

%package technical_writing
%pattern_desktopfunctions
Summary:        Technical Writing
Group:          Metapackages
Provides:       patterns-openSUSE-technical_writing = %{version}
Provides:       pattern() = technical_writing
Provides:       pattern-icon() = pattern-technical-writing
Provides:       pattern-order() = 2000
Provides:       pattern-visible()
Obsoletes:      patterns-openSUSE-technical_writing < %{version}

Recommends:     xmlto
Recommends:     docbook-dsssl-stylesheets
Recommends:     docbook-xsl-stylesheets
Recommends:     psutils
Recommends:     emacs
Recommends:     emacs-x11
Recommends:     xmlgraphics-fop
Recommends:     svg-schema
Recommends:     xslide
# General XML Packages
Recommends:     xmlgraphics-batik
Recommends:     dia
Recommends:     inkscape
Recommends:     mxml
Recommends:     sablot
Recommends:     saxon
#LATER xmlroff
Recommends:     xmlformat
Recommends:     xmlstarlet
# Packages Specific to DocBook
Recommends:     dbsplit-tools
#LATER docbook2odf
Recommends:     docbook_5
Recommends:     docbook5-xsl-stylesheets
Recommends:     docbook-xml-website
#LATER doclifter
Recommends:     susedoc
#LATER texi2db
#LATER wt2db
# Text Encoding Initiative
Recommends:     tei-xsl-stylesheets
Recommends:     tei-roma
Recommends:     texlive-scheme-tetex
Suggests:       lyx
Suggests:       texlive-cjk
Suggests:       texlive-metapost
Suggests:       texlive-omega
Suggests:       texlive-xetex
Suggests:       texlive-context
Suggests:       texlive-omega
Suggests:       texlive-xetex
Suggests:       texlive-tools
Suggests:       texlive-latex-doc
Suggests:       texlive-doc
# 441536
Suggests:       djvulibre

%description technical_writing
Authoring tools and editors for creating technical documentation.

%files technical_writing
%dir /usr/share/doc/packages/patterns
/usr/share/doc/packages/patterns/technical_writing.txt

################################################################################

%prep

%build

%install
mkdir -p "%{buildroot}/usr/share/doc/packages/patterns"
for i in books imaging laptop multimedia \
    technical_writing; do
	echo "This file marks the pattern $i to be installed." \
		>"%{buildroot}/usr/share/doc/packages/patterns/$i.txt"
done

%changelog
