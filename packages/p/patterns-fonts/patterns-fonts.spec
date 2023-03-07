#
# spec file for package patterns-fonts
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


%bcond_with betatest

Name:           patterns-fonts
Version:        20170319
Release:        0
Summary:        Patterns for Installation (Fonts)
License:        MIT
Group:          Metapackages
URL:            https://github.com/openSUSE/patterns
Source0:        %{name}-rpmlintrc
BuildRoot:      %{_tmppath}/%{name}-%{version}-build
BuildRequires:  patterns-rpm-macros

%description
This is an internal package that is used to create the patterns as part
of the installation source setup.  Installation of this package does
not make sense.

This particular package contains the Fonts patterns.





################################################################################
%package fonts
%pattern_graphicalenvironments
Summary:        Fonts
Group:          Metapackages
Provides:       pattern() = fonts
Provides:       pattern-icon() = pattern-x11
Provides:       pattern-order() = 1700
Provides:       pattern-visible()
Recommends:     pattern() = fonts_opt

Recommends:     dejavu-fonts
Recommends:     ghostscript-fonts-std
Recommends:     google-roboto-fonts
Recommends:     intlfonts-euro-bitmap-fonts
Recommends:     liberation-fonts
Recommends:     xorg-x11-fonts-core
# needed for instsys
Suggests:       ipa-gothic-fonts
Suggests:       ipa-mincho-fonts
Suggests:       ipa-pgothic-fonts
Suggests:       ipa-pmincho-fonts
#IPAUIGothic
Suggests:       bitstream-vera-fonts

%description fonts
Base fonts and font configuration.

%files fonts
%dir %{_defaultdocdir}/patterns
%{_defaultdocdir}/patterns/fonts.txt

################################################################################

%package fonts_opt
%pattern_graphicalenvironments
Summary:        Fonts
Group:          Metapackages
Provides:       pattern() = fonts_opt
Provides:       pattern-extends() = fonts
Provides:       pattern-icon() = pattern-x11
Provides:       pattern-order() = 1720

Recommends:     adobe-sourcecodepro-fonts
Recommends:     adobe-sourcesanspro-fonts
Recommends:     adobe-sourceserifpro-fonts
Recommends:     ghostscript-fonts-other
# noto-sans and noto-sans-cjk pulls in too much (>500MiB!)
Recommends:     efont-unicode-bitmap-fonts
Recommends:     noto-sans-fonts
Recommends:     stix-fonts
Recommends:     texlive-lm-fonts
Recommends:     xorg-x11-fonts

%description fonts_opt
Base fonts and font configuration.

%files fonts_opt
%dir %{_defaultdocdir}/patterns
%{_defaultdocdir}/patterns/fonts_opt.txt

################################################################################

%prep

%build

%install
mkdir -p %{buildroot}%{_defaultdocdir}/patterns/
for i in fonts fonts_opt; do
	echo "This file marks the pattern $i to be installed." \
		>"%{buildroot}/%{_defaultdocdir}/patterns/$i.txt"
done

%changelog
