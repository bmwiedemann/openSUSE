#
# spec file for package manpages-l10n
#
# Copyright (c) 2024 SUSE LLC
# Copyright (c) 2020-2024 Antoine Belvire <antoine.belvire@opensuse.org>
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


Name:           manpages-l10n
Version:        4.23.1
Release:        0
Summary:        Translation of man pages
License:        GPL-3.0-or-later
URL:            https://manpages-l10n-team.pages.debian.net/manpages-l10n
Source0:        https://salsa.debian.org/manpages-l10n-team/manpages-l10n/-/archive/%{version}/%{name}-%{version}.tar.bz2
Source1:        macros.%{name}
# PATCH-FIX-UPSTREAM manpages-l10n-4.20.0-fix-links.patch -- Fix incorrect links in man2 (boo#1202798)
Patch0:         manpages-l10n-4.20.0-fix-links.patch
BuildRequires:  po4a
BuildArch:      noarch
%{load:%{SOURCE1}}

%description
This package provides translations of man pages in multiple languages.

%man_lang_package cs Czech
%man_lang_package da Danish
%man_lang_package de German
%man_lang_package el Greek
%man_lang_package es Spanish
%man_lang_package fi Finnish
%man_lang_package fr French
%man_lang_package hu Hungarian
%man_lang_package id Indonesian
%man_lang_package it Italian
%man_lang_package mk Macedonian
%man_lang_package nb %{quote:Norwegian Bokmål}
%man_lang_package nl Dutch
%man_lang_package pl Polish
%man_lang_package pt_BR %{quote:Brazilian Portuguese}
%man_lang_package ko Korean
%man_lang_package ro Romanian
%man_lang_package ru Russian
%man_lang_package sr Serbian
%man_lang_package sv Swedish
%man_lang_package uk Ukrainian
%man_lang_package vi Vietnamese

%prep
%autosetup -p1

%build
%configure --enable-distribution=%{distribution_id}
%make_build

%install
%make_install
# net-tools translations conflict on all supported RPM-based distributions
# https://salsa.debian.org/manpages-l10n-team/manpages-l10n/-/issues/8
rm -vf %{buildroot}%{_mandir}/de/man5/ethers.5*

%changelog
