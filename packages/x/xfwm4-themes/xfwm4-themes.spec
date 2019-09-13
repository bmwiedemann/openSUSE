#
# spec file for package xfwm4-themes
#
# Copyright (c) 2012 SUSE LINUX Products GmbH, Nuernberg, Germany.
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


Name:           xfwm4-themes
Version:        4.10.0
Release:        0
Summary:        Additional Themes for xfwm4
License:        GPL-2.0+
Group:          System/GUI/XFCE
Url:            http://www.xfce.org/
Source:         http://archive.xfce.org/src/art/xfwm4-themes/4.10/%{name}-%{version}.tar.bz2
BuildRequires:  fdupes
Requires:       xfwm4 >= %{version}
BuildRoot:      %{_tmppath}/%{name}-%{version}-build
BuildArch:      noarch

%description
A set of additional themes for the xfwm4 window manager.

%prep
%setup -q

%build
%configure
make %{?_smp_mflags}

%install
%make_install

%fdupes %{buildroot}%{_datadir}/themes

%clean
rm -rf %{buildroot}

%files
%defattr(-,root,root)
%doc AUTHORS COPYING ChangeLog NEWS README TODO
%{_datadir}/themes/Adept/
%{_datadir}/themes/Agua/
%{_datadir}/themes/Agualemon/
%{_datadir}/themes/Alternate/
%{_datadir}/themes/Atlanta/
%{_datadir}/themes/Atlanta2/
%{_datadir}/themes/B5/
%{_datadir}/themes/B6/
%{_datadir}/themes/Basix/
%{_datadir}/themes/BBS/
%{_datadir}/themes/Beastie/
%{_datadir}/themes/Biz/
%{_datadir}/themes/Blackwall/
%{_datadir}/themes/Buzz/
%{_datadir}/themes/Coldsteel/
%{_datadir}/themes/Coolclean/
%{_datadir}/themes/Crux/
%{_datadir}/themes/Cruxish/
%{_datadir}/themes/Curve/
%{_datadir}/themes/Default-4.0/
%{_datadir}/themes/Default-4.2/
%{_datadir}/themes/Default-4.4/
%{_datadir}/themes/Default-4.6/
%{_datadir}/themes/Default-4.8/
%{_datadir}/themes/Defcon-IV/
%{_datadir}/themes/Eazel-blue/
%{_datadir}/themes/Elberg/
%{_datadir}/themes/Exocet/
%{_datadir}/themes/Fbx/
%{_datadir}/themes/G2/
%{_datadir}/themes/Galaxy/
%{_datadir}/themes/Gaudy/
%{_datadir}/themes/Gelly/
%{_datadir}/themes/Gnububble/
%{_datadir}/themes/Gorilla/
%{_datadir}/themes/Gtk/
%{_datadir}/themes/Iceg/
%{_datadir}/themes/Kde/
%{_datadir}/themes/Kde1/
%{_datadir}/themes/Keramik/
%{_datadir}/themes/Kindaker/
%{_datadir}/themes/Kleanux/
%{_datadir}/themes/Koynacity/
%{_datadir}/themes/Linea/
%{_datadir}/themes/LineArt/
%{_datadir}/themes/Meenee/
%{_datadir}/themes/Metabox/
%{_datadir}/themes/Microcurve/
%{_datadir}/themes/Microdeck/
%{_datadir}/themes/Microdeck2/
%{_datadir}/themes/Microdeck3/
%{_datadir}/themes/Microgui/
%{_datadir}/themes/Mofit/
%{_datadir}/themes/Next/
%{_datadir}/themes/Ops/
%{_datadir}/themes/Opta/
%{_datadir}/themes/Oroborus/
%{_datadir}/themes/Perl/
%{_datadir}/themes/Pills/
%{_datadir}/themes/Piranha/
%{_datadir}/themes/Platinum/
%{_datadir}/themes/Prune/
%{_datadir}/themes/Quiet-purple/
%{_datadir}/themes/Quinx/
%{_datadir}/themes/R9X/
%{_datadir}/themes/Redmond/
%{_datadir}/themes/RedmondXP/
%{_datadir}/themes/Retro/
%{_datadir}/themes/Sassandra/
%{_datadir}/themes/Silverado/
%{_datadir}/themes/Slick/
%{_datadir}/themes/Slimline/
%{_datadir}/themes/Smallscreen/
%{_datadir}/themes/Smoothwall/
%{_datadir}/themes/Stoneage/
%{_datadir}/themes/Symphony/
%{_datadir}/themes/Synthetic/
%{_datadir}/themes/Tabs/
%{_datadir}/themes/Tgc/
%{_datadir}/themes/Tgc-large/
%{_datadir}/themes/Therapy/
%{_datadir}/themes/Today/
%{_datadir}/themes/Totem/
%{_datadir}/themes/Trench/
%{_datadir}/themes/Triviality/
%{_datadir}/themes/Tubular/
%{_datadir}/themes/TUX/
%{_datadir}/themes/Tyrex/
%{_datadir}/themes/Variation/
%{_datadir}/themes/Wallis/
%{_datadir}/themes/Waza/
%{_datadir}/themes/Wildbush/
%{_datadir}/themes/Xfce/

%changelog
