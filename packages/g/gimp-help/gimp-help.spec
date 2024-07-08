#
# spec file for package gimp-help
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


Name:           gimp-help
Version:        2.10.0
Release:        0
Summary:        Help System Data for GIMP
License:        GFDL-1.2
Group:          Productivity/Graphics/Bitmap Editors
Url:            https://docs.gimp.org/
Source0:        https://download.gimp.org/pub/gimp/help/gimp-help-%{version}.tar.bz2
# PATCH-FIX-UPSTREAM -- https://gitlab.gnome.org/GNOME/gimp-help/-/issues/201
Patch0:         gimp-help-2.10.0-python3.patch
BuildRequires:  docbook-xsl-stylesheets
BuildRequires:  fdupes
BuildRequires:  libxslt
BuildRequires:  memory-constraints
BuildRequires:  pngcrush
BuildRequires:  python3-libxml2-python
Requires:       gimp
Enhances:       gimp
Provides:       gimp-help-2 = %{version}
Obsoletes:      gimp-help-2 < %{version}
BuildArch:      noarch

%description
GIMP-Help is a help system designed for use with the internal GIMP help
browser, external Web browser and HTML renderers, and human eyeballs.

%package ca
Summary:        Catalanian Help System Data for GIMP
Group:          System/Localization
Requires:       %{name} = %{version}
Provides:       locale(%{name}:ca)

%description ca
GIMP-Help is a help system designed for use with the internal GIMP help
browser, external Web browser and HTML renderers, and human eyeballs.

This package provides Catalanian data for gimp-help.

%package da
Summary:        Danish Help System Data for GIMP
Group:          System/Localization
Requires:       %{name} = %{version}
Provides:       locale(%{name}:da)

%description da
GIMP-Help is a help system designed for use with the internal GIMP help
browser, external Web browser and HTML renderers, and human eyeballs.

This package provides Danish data for gimp-help.

%package de
Summary:        German Help System Data for GIMP
Group:          System/Localization
Requires:       %{name} = %{version}
Provides:       locale(%{name}:de)

%description de
GIMP-Help is a help system designed for use with the internal GIMP help
browser, external Web browser and HTML renderers, and human eyeballs.

This package provides German data for gimp-help.

%package el
Summary:        Greek Help System Data for GIMP
Group:          System/Localization
Requires:       %{name} = %{version}
Provides:       locale(%{name}:el)

%description el
GIMP-Help is a help system designed for use with the internal GIMP help
browser, external Web browser and HTML renderers, and human eyeballs.

This package provides Greek data for gimp-help.

%package en_GB
Summary:        British English Help System Data for GIMP
Group:          System/Localization
Requires:       %{name} = %{version}
Provides:       locale(%{name}:en_GB)

%description en_GB
GIMP-Help is a help system designed for use with the internal GIMP help
browser, external Web browser and HTML renderers, and human eyeballs.

This package provides British English data for gimp-help.

%package es
Summary:        Spanish Help System Data for GIMP
Group:          System/Localization
Requires:       %{name} = %{version}
Provides:       locale(%{name}:es)

%description es
GIMP-Help is a help system designed for use with the internal GIMP help
browser, external Web browser and HTML renderers, and human eyeballs.

This package provides Spanish data for gimp-help.

%package fi
Summary:        Finnish Help System Data for GIMP
Group:          System/Localization
Requires:       %{name} = %{version}
Provides:       locale(%{name}:fi)

%description fi
GIMP-Help is a help system designed for use with the internal GIMP help
browser, external Web browser and HTML renderers, and human eyeballs.

This package provides Finnish data for gimp-help.

%package fr
Summary:        French Help System Data for GIMP
Group:          System/Localization
Requires:       %{name} = %{version}
Provides:       locale(%{name}:fr)

%description fr
GIMP-Help is a help system designed for use with the internal GIMP help
browser, external Web browser and HTML renderers, and human eyeballs.

This package provides French data for gimp-help.

%package hr
Summary:        Croatian Help System Data for GIMP
Group:          System/Localization
Requires:       %{name} = %{version}
Provides:       locale(%{name}:hr)

%description hr
GIMP-Help is a help system designed for use with the internal GIMP help
browser, external Web browser and HTML renderers, and human eyeballs.

This package provides Croatian data for gimp-help.

%package it
Summary:        Italian Help System Data for GIMP
Group:          System/Localization
Requires:       %{name} = %{version}
Provides:       locale(%{name}:it)

%description it
GIMP-Help is a help system designed for use with the internal GIMP help
browser, external Web browser and HTML renderers, and human eyeballs.

This package provides Italian data for gimp-help.

%package ja
Summary:        Japanese Help System Data for GIMP
Group:          System/I18n/Korean
Requires:       %{name} = %{version}
Provides:       locale(%{name}:ja)

%description ja
GIMP-Help is a help system designed for use with the internal GIMP help
browser, external Web browser and HTML renderers, and human eyeballs.

This package provides Japanese data for gimp-help.

%package ko
Summary:        Korean Help System Data for GIMP
Group:          System/I18n/Korean
Requires:       %{name} = %{version}
Provides:       locale(%{name}:ko)

%description ko
GIMP-Help is a help system designed for use with the internal GIMP help
browser, external Web browser and HTML renderers, and human eyeballs.

This package provides Korean data for gimp-help.

%package lt
Summary:        Lithuanian Help System Data for GIMP
Group:          System/I18n/Korean
Requires:       %{name} = %{version}
Provides:       locale(%{name}:lt)

%description lt
GIMP-Help is a help system designed for use with the internal GIMP help
browser, external Web browser and HTML renderers, and human eyeballs.

This package provides Lithuanian data for gimp-help.

%package nl
Summary:        Dutch Help System Data for GIMP
Group:          System/Localization
Requires:       %{name} = %{version}
Provides:       locale(%{name}:nl)

%description nl
GIMP-Help is a help system designed for use with the internal GIMP help
browser, external Web browser and HTML renderers, and human eyeballs.

This package provides Dutch data for gimp-help.

%package nn
Summary:        Norwegian Nynorsk Help System Data for GIMP
Group:          System/Localization
Requires:       %{name} = %{version}
Provides:       locale(%{name}:nn)

%description nn
GIMP-Help is a help system designed for use with the internal GIMP help
browser, external Web browser and HTML renderers, and human eyeballs.

This package provides Norwegian Nynorsk data for gimp-help.

%package pl
Summary:        Polish Help System Data for GIMP
Group:          System/Localization
Requires:       %{name} = %{version}
Provides:       locale(%{name}:pl)

%description pl
GIMP-Help is a help system designed for use with the internal GIMP help
browser, external Web browser and HTML renderers, and human eyeballs.

This package provides Polish data for gimp-help.

%package pt_BR
Summary:        Brazilian Portuguese Help System Data for GIMP
Group:          System/Localization
Requires:       %{name} = %{version}
Provides:       locale(%{name}:pt_BR)

%description pt_BR
GIMP-Help is a help system designed for use with the internal GIMP help
browser, external Web browser and HTML renderers, and human eyeballs.

This package provides Brazilian Portuguese data for gimp-help.

%package ro
Summary:        Romanian Help System Data for GIMP
Group:          System/Localization
Requires:       %{name} = %{version}
Provides:       locale(%{name}:ro)

%description ro
GIMP-Help is a help system designed for use with the internal GIMP help
browser, external Web browser and HTML renderers, and human eyeballs.

This package provides Romanian data for gimp-help.

%package ru
Summary:        Russian Help System Data for GIMP
Group:          System/Localization
Requires:       %{name} = %{version}
Provides:       locale(%{name}:ru)

%description ru
GIMP-Help is a help system designed for use with the internal GIMP help
browser, external Web browser and HTML renderers, and human eyeballs.

This package provides Russian data for gimp-help.

%package sl
Summary:        Slovenian Help System Data for GIMP
Group:          System/Localization
Requires:       %{name} = %{version}
Provides:       locale(%{name}:sl)

%description sl
GIMP-Help is a help system designed for use with the internal GIMP help
browser, external Web browser and HTML renderers, and human eyeballs.

This package provides Slovenian data for gimp-help.

%package sv
Summary:        Swedish Help System Data for GIMP
Group:          System/Localization
Requires:       %{name} = %{version}
Provides:       locale(%{name}:sv)

%description sv
GIMP-Help is a help system designed for use with the internal GIMP help
browser, external Web browser and HTML renderers, and human eyeballs.

This package provides Swedish data for gimp-help.

%package zh
Summary:        Chinese Help System Data for GIMP
Group:          System/Localization
Requires:       %{name} = %{version}
Provides:       locale(%{name}:zh)

%description zh
GIMP-Help is a help system designed for use with the internal GIMP help
browser, external Web browser and HTML renderers, and human eyeballs.

This package provides Chinese data for gimp-help.

%prep
%autosetup -p1

find . -iname \*.py -exec sed -i -e '1 s@env python.\?@python3@' '{}' \;

%build
%limit_build -m 3400
# We install the help to the same prefix as gimp itself, so no
# need to query gimp for the prefix at build time
%configure \
    --without-gimp
unset MALLOC_CHECK_
unset MALLOC_PERTURB_

%if 0%{?sle_version} <= 150100
export LANG=en_US.utf-8
%endif
%make_build

# unify the permissions of images, to make fdupes working again (bnc#784670)
find images/ -type f -exec chmod 0644 {} +

%install
%make_install
for locale in %{buildroot}%{_datadir}/gimp/2.0/help/*; do
  %fdupes $locale
done

%clean
rm -rf %{buildroot}

%files
%doc AUTHORS NEWS
%license COPYING
%dir %{_datadir}/gimp
%dir %{_datadir}/gimp/2.0
%dir %{_datadir}/gimp/2.0/help
%{_datadir}/gimp/2.0/help/en/

%files ca
%lang(ca) %{_datadir}/gimp/2.0/help/ca/

%files da
%lang(da) %{_datadir}/gimp/2.0/help/da/

%files de
%lang(de) %{_datadir}/gimp/2.0/help/de/

%files el
%lang(el) %{_datadir}/gimp/2.0/help/el/

%files en_GB
%lang(en_GB) %{_datadir}/gimp/2.0/help/en_GB/

%files es
%lang(es) %{_datadir}/gimp/2.0/help/es/

%files fi
%lang(fi) %{_datadir}/gimp/2.0/help/fi/

%files fr
%lang(fr) %{_datadir}/gimp/2.0/help/fr/

%files hr
#lang(hr) %%{_datadir}/gimp/2.0/help/hr/

%files it
%lang(it) %{_datadir}/gimp/2.0/help/it/

%files ja
%lang(ja) %{_datadir}/gimp/2.0/help/ja/

%files ko
%lang(ko) %{_datadir}/gimp/2.0/help/ko/

%files lt
#lang(lt) %%{_datadir}/gimp/2.0/help/lt/

%files nl
%lang(nl) %{_datadir}/gimp/2.0/help/nl/

%files nn
%lang(nn) %{_datadir}/gimp/2.0/help/nn/

%files pl
#lang(pl) %%{_datadir}/gimp/2.0/help/pl/

%files pt_BR
%lang(pt_BR) %{_datadir}/gimp/2.0/help/pt_BR/

%files ro
%lang(ro) %{_datadir}/gimp/2.0/help/ro/

%files ru
%lang(ru) %{_datadir}/gimp/2.0/help/ru/

%files sl
#%lang(sl) %%{_datadir}/gimp/2.0/help/sl/

%files sv
#%lang(sv) %%{_datadir}/gimp/2.0/help/sv/

%files zh
%lang(zh) %{_datadir}/gimp/2.0/help/zh_CN/

%changelog
