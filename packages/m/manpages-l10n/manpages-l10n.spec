#
# spec file for package manpages-l10n
#
# Copyright (c) 2021 SUSE LLC
# Copyright (c) 2021 Antoine Belvire <antoine.belvire@opensuse.org>
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


%define parent_tag 4.9.3
%define tag_offset +406
%define revision 90d1e9dc2c70df3f60a987d8366030728f4b6352

Name:           manpages-l10n
Version:        %{parent_tag}%{?tag_offset}
Release:        0
Summary:        Translation of man pages
License:        GPL-3.0-only
URL:            https://manpages-l10n-team.pages.debian.net/manpages-l10n
Source0:        https://salsa.debian.org/manpages-l10n-team/manpages-l10n/-/archive/%{revision}/%{name}-v%{version}.tar.bz2
Source1:        macros.%{name}
BuildRequires:  po4a
BuildArch:      noarch
%{load:%{SOURCE1}}

%description
This package provides translations of man pages in multiple languages.

%man_lang_package cs Czech
%man_lang_package da Danish
%man_lang_package de German
%man_lang_package es Spanish
%man_lang_package it Italian
%man_lang_package mk Macedonian
%man_lang_package nl Dutch
%man_lang_package pl Polish
%man_lang_package pt_BR %{quote:Brazilian Portuguese}
%man_lang_package ro Romanian

# French translations used to be splitted into a main and an extra package on openSUSE.
# Let's obsolete the extra package until openSUSE Leap 15.2 EOL (Dec. 2021).
%man_lang_package fr French -o %{quote:man-pages-fr-extra <= 20151231}

%prep
%setup -q -n %{name}-%{revision}

%build
%configure --enable-distribution=%{distribution_id}
%make_build

%install
%make_install

%changelog
