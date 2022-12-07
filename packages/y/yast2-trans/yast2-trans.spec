#
# spec file for package yast2-trans
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


Name:           yast2-trans
Version:        84.87.20221203.a7355e12ff
Release:        0
Summary:        YaST2 - Translation Container Package
License:        GPL-2.0-or-later
Group:          System/YaST
Source0:        %{name}-%{version}.tar.xz
Source1:        COPYING
Source2:        po-stats
BuildRoot:      %{_tmppath}/%{name}-%{version}-build
BuildArch:      noarch
URL:            https://github.com/yast/yast2-translations/
Obsoletes:      yast2-trans-en
Obsoletes:      yast2-trans-en_US
#@SOURCES@
%define build_languages af am ar ast be bg bn bs ca cs cy da de el en_GB eo es es_AR et eu fa fi fr gl gu he hi hr hu id it ja jv ka kab km kn ko ku lo lt lv mk mr ms my nb nds ne nl nn pa pl ps pt pt_BR ro ru si sk sl sq sr sr@latin sv sw ta tg th tk tr uk vi wa xh zh_CN zh_TW zu

%description
This is a container package.  Its only purpose is to build the
yast2-trans-LL, yast2-trans-LLL, and yast2-trans-LL_CC packages as
subpackages.

%package af
Summary:        YaST2 - Afrikaans Translations
Group:          System/YaST
Provides:       locale(yast2:af)
URL:            http://l10n.opensuse.org/

%description af
YaST2 - Translations for Afrikaans.

%package am
Summary:        YaST2 - Amharic Translations
Group:          System/YaST
Provides:       locale(yast2:am)
URL:            http://l10n.opensuse.org/

%description am
YaST2 - Translations for Amharic.

%package ar
Summary:        YaST2 - Arabic Translations
Group:          System/YaST
Provides:       locale(yast2:ar)
URL:            http://l10n.opensuse.org/

%description ar
YaST2 - Translations for Arabic.

%package ast
Summary:        YaST2 - Asturian Translations
Group:          System/YaST
Provides:       locale(yast2:ast)
URL:            http://l10n.opensuse.org/

%description ast
YaST2 - Translations for Asturian.

%package be
Summary:        YaST2 - Byelorussian Translations
Group:          System/YaST
Provides:       locale(yast2:be)
URL:            http://l10n.opensuse.org/

%description be
YaST2 - Translations for Byelorussian (Belarusian).

%package bg
Summary:        YaST2 - Bulgarian Translations
Group:          System/YaST
Provides:       locale(yast2:bg)
URL:            http://l10n.opensuse.org/

%description bg
YaST2 - Translations for Bulgarian.

%package bn
Summary:        YaST2 - Bengali Translations
Group:          System/YaST
Provides:       locale(yast2:bn)
URL:            http://l10n.opensuse.org/

%description bn
YaST2 - Translations for Bengali.

%package bs
Summary:        YaST2 - Bosnian Translations
Group:          System/YaST
Provides:       locale(yast2:bs)
URL:            http://l10n.opensuse.org/

%description bs
YaST2 - Translations for Bosnian.

%package ca
Summary:        YaST2 - Catalan Translations
Group:          System/YaST
Provides:       locale(yast2:ca)
URL:            http://l10n.opensuse.org/

%description ca
YaST2 - Catalan translations.

%package cs
Summary:        YaST2 - Czech Translations
Group:          System/YaST
Provides:       locale(yast2:cs)
URL:            http://l10n.opensuse.org/

%description cs
YaST2 - Czech translations.

%package cy
Summary:        YaST2 - Welsh Translations
Group:          System/YaST
Provides:       locale(yast2:cy)
URL:            http://l10n.opensuse.org/

%description cy
YaST2 - Welsh translations.

%package da
Summary:        YaST2 - Danish Translations
Group:          System/YaST
Provides:       locale(yast2:da)
URL:            http://l10n.opensuse.org/

%description da
YaST2 - Translations for Danish.

%package de
Summary:        YaST2 - German Translations
Group:          System/YaST
Provides:       locale(yast2:de)
URL:            http://l10n.opensuse.org/

%description de
YaST2 - German translations.

%package el
Summary:        YaST2 - Greek Translations
Group:          System/YaST
Provides:       locale(yast2:el)
URL:            http://l10n.opensuse.org/

%description el
YaST2 - Translations for Greek.

%package eo
Summary:        YaST2 - Esperanto Translations
Group:          System/YaST
Provides:       locale(yast2:eo)
URL:            http://l10n.opensuse.org/

%description eo
YaST2 - Esperanto Translations.

%package es
Summary:        YaST2 - Spanish Translations
Group:          System/YaST
Provides:       locale(yast2:es)
URL:            http://l10n.opensuse.org/

%description es
YaST2 - Spanish Translations.

%package es_AR
Summary:        YaST2 - Spanish (Argentina) Translations
Group:          System/YaST
Provides:       locale(yast2:es_AR)
URL:            http://l10n.opensuse.org/

%description es_AR
YaST2 - Spanish (Argentina) Translations.

%package et
Summary:        YaST2 - Estonian Translations
Group:          System/YaST
Provides:       locale(yast2:et)
URL:            http://l10n.opensuse.org/

%description et
YaST2 - Translations for Estonian.

%package eu
Summary:        YaST2 - Esperanto Translations
Group:          System/YaST
Provides:       locale(yast2:eu)
URL:            http://l10n.opensuse.org/

%description eu
YaST2 - Translations for Esperanto.

%package fa
Summary:        YaST2 - Persian Translations
Group:          System/YaST
Provides:       locale(yast2:fa)
URL:            http://l10n.opensuse.org/

%description fa
YaST2 - Persian Translations.

%package fi
Summary:        YaST2 - Finnish Translations
Group:          System/YaST
Provides:       locale(yast2:fi)
URL:            http://l10n.opensuse.org/

%description fi
YaST2 - Finnish translations.

%package fr
Summary:        YaST2 - French Translations
Group:          System/YaST
Provides:       locale(yast2:fr)
URL:            http://l10n.opensuse.org/

%description fr
YaST2 - Translations for French.

%package gl
Summary:        YaST2 - Galician Translations
Group:          System/YaST
Provides:       locale(yast2:gl)
URL:            http://l10n.opensuse.org/

%description gl
YaST2 - Galician translations.

%package gu
Summary:        YaST2 - Gujarati Translations
Group:          System/YaST
Provides:       locale(yast2:gu)
URL:            http://l10n.opensuse.org/

%description gu
YaST2 - Translations for Gujarati.

%package he
Summary:        YaST2 - Hebrew Translations
Group:          System/YaST
Provides:       locale(yast2:he)
URL:            http://l10n.opensuse.org/

%description he
YaST2 - Translations for Hebrew.

%package hi
Summary:        YaST2 - Hindi Translations
Group:          System/YaST
Provides:       locale(yast2:hi)
URL:            http://l10n.opensuse.org/

%description hi
YaST2 - Translations for Hindi.

%package hr
Summary:        YaST2 - Croatian Translations
Group:          System/YaST
Provides:       locale(yast2:hr)
URL:            http://l10n.opensuse.org/

%description hr
YaST2 - Croatian Translations.

%package hu
Summary:        YaST2 - Hungarian Translations
Group:          System/YaST
Provides:       locale(yast2:hu)
URL:            http://l10n.opensuse.org/

%description hu
YaST2 - Hungarian translations.

%package id
Summary:        YaST2 - Indonesian Translations
Group:          System/YaST
Provides:       locale(yast2:id)
URL:            http://l10n.opensuse.org/

%description id
YaST2 - Indonesian Translations.

%package it
Summary:        YaST2 - Italian Translations
Group:          System/YaST
Provides:       locale(yast2:it)
URL:            http://l10n.opensuse.org/

%description it
YaST2 - translations for Italian.

%package ja
Summary:        YaST2 - Japanese Translations
Group:          System/YaST
Provides:       locale(yast2:ja)
URL:            http://l10n.opensuse.org/

%description ja
YaST2 - Japanese translations.

%package jv
Summary:        YaST2 - Javanese Translations
Group:          System/YaST
Provides:       locale(yast2:jv)
URL:            http://l10n.opensuse.org/

%description jv
YaST2 - Translations for Javanese.

%package ka
Summary:        YaST2 - Georgian Translations
Group:          System/YaST
Provides:       locale(yast2:ka)
URL:            http://l10n.opensuse.org/

%description ka
YaST2 - Translations for Georgian.

%package kab
Summary:        YaST2 - Kabyle Translations
Group:          System/YaST
Provides:       locale(yast2:kab)
URL:            http://l10n.opensuse.org/

%description kab
YaST2 - Translations for Kabyle.

%package km
Summary:        YaST2 - Khmer Translations
Group:          System/YaST
Provides:       locale(yast2:km)
URL:            http://l10n.opensuse.org/

%description km
YaST2 - Translations for Khmer.

%package kn
Summary:        YaST2 - Kannada Translations
Group:          System/YaST
Provides:       locale(yast2:ka)
URL:            http://l10n.opensuse.org/

%description kn
YaST2 - Translations for Kannada.

%package ko
Summary:        YaST2 - Korean Translations
Group:          System/YaST
Provides:       locale(yast2:ko)
URL:            http://l10n.opensuse.org/

%description ko
YaST2 - Translations for Korean.

%package ku
Summary:        YaST2 - Kurdish Translations
Group:          System/YaST
Provides:       locale(yast2:ku)
URL:            http://l10n.opensuse.org/

%description ku
YaST2 - Kurdish Translations.

%package lo
Summary:        YaST2 - Lao Translations
Group:          System/YaST
Provides:       locale(yast2:lo)
URL:            http://l10n.opensuse.org/

%description lo
YaST2 - Translations for Lao.

%package lt
Summary:        YaST2 - Lithuanian Translations
Group:          System/YaST
Provides:       locale(yast2:lt)
URL:            http://l10n.opensuse.org/

%description lt
YaST2 - Translations for Lithuanian.

%package lv
Summary:        YaST2 - Latvian Translations
Group:          System/YaST
Provides:       locale(yast2:lv)
URL:            http://l10n.opensuse.org/

%description lv
YaST2 - Translations for Latvian.

%package mk
Summary:        YaST2 - Macedonian Translations
Group:          System/YaST
Provides:       locale(yast2:mk)
URL:            http://l10n.opensuse.org/

%description mk
YaST2 - Translations for Macedonian.

%package mr
Summary:        YaST2 - Marathi Translations
Group:          System/YaST
Provides:       locale(yast2:mr)
URL:            http://l10n.opensuse.org/

%description mr
YaST2 - Translations for Marathi.

%package ms
Summary:        YaST2 - Malay Translations
Group:          System/YaST
Provides:       locale(yast2:ms)
URL:            http://l10n.opensuse.org/

%description ms
YaST2 - Translations for Malay.

%package my
Summary:        YaST2 - Burmese Translations
Group:          System/YaST
Provides:       locale(yast2:my)
URL:            http://l10n.opensuse.org/

%description my
YaST2 - Translations for Burmese.

%package nb
Summary:        YaST2 - Norwegian Bokmål Translations
Group:          System/YaST
Provides:       locale(yast2:nb)
URL:            http://l10n.opensuse.org/

%description nb
YaST2 - Translations for Norwegian Bokmål.

%package nds
Summary:        YaST2 - Low Saxonian Translations
Group:          System/YaST
Provides:       locale(yast2:nds)
URL:            http://l10n.opensuse.org/

%description nds
YaST2 - Translations for Low Saxonian.

%package ne
Summary:        YaST2 - Nepali Translations
Group:          System/YaST
Provides:       locale(yast2:ne)
URL:            http://l10n.opensuse.org/

%description ne
YaST2 - Translations for Nepali.

%package nl
Summary:        YaST2 - Dutch Translations
Group:          System/YaST
Provides:       locale(yast2:nl)
URL:            http://l10n.opensuse.org/

%description nl
YaST2 - Translations for Dutch.

%package nn
Summary:        YaST2 - Norwegian Nynorsk
Group:          System/YaST
Provides:       locale(yast2:nn)
URL:            http://l10n.opensuse.org/

%description nn
YaST2 - Translations for Norwegian Nynorsk.

%package pa
Summary:        YaST2 - Punjabi Translations
Group:          System/YaST
Provides:       locale(yast2:pa)
URL:            http://l10n.opensuse.org/

%description pa
Translations for Punjabi.

%package pl
Summary:        YaST2 - Polish Translations
Group:          System/YaST
Provides:       locale(yast2:pl)
URL:            http://l10n.opensuse.org/

%description pl
YaST2 - Translations for Polish.

%package ps
Summary:        YaST2 - Pashto Translations
Group:          System/YaST
Provides:       locale(yast2:ps)
URL:            http://l10n.opensuse.org/

%description ps
YaST2 - Translations for Pashto.

%package pt
Summary:        YaST2 - Portuguese Translations
Group:          System/YaST
Provides:       locale(yast2:pt)
URL:            http://l10n.opensuse.org/

%description pt
YaST2 - Translations for Portuguese.

%package ro
Summary:        YaST2 - Romanian Translations
Group:          System/YaST
Provides:       locale(yast2:ro)
URL:            http://l10n.opensuse.org/

%description ro
YaST2 - Translations for Romanian.

%package ru
Summary:        YaST2 - Russian Translations
Group:          System/YaST
Provides:       locale(yast2:ru)
URL:            http://l10n.opensuse.org/

%description ru
YaST2 - Translations for Russian.

%package si
Summary:        YaST2 - Sinhala Translations
Group:          System/YaST
Provides:       locale(yast2:si)
URL:            http://l10n.opensuse.org/

%description si
YaST2 - Translations for Sinhala.

%package sk
Summary:        YaST2 - Slovak Translations
Group:          System/YaST
Provides:       locale(yast2:sk)
URL:            http://l10n.opensuse.org/

%description sk
YaST2 - Slovak Translations.

%package sl
Summary:        YaST2 - Slovene Translations
Group:          System/YaST
Provides:       locale(yast2:sl)
URL:            http://l10n.opensuse.org/

%description sl
YaST2 - Translations for Slovene.

%package sq
Summary:        YaST2 - Albanian Translations
Group:          System/YaST
Provides:       locale(yast2:sq)
URL:            http://l10n.opensuse.org/

%description sq
YaST2 - Translations for Albanian.

%package sr
Summary:        YaST2 - Serbian Translations
Group:          System/YaST
Provides:       locale(yast2:sr)
URL:            http://l10n.opensuse.org/

%description sr
YaST2 - Translations for Serbian.

%package sr-latin
Summary:        YaST2 - Serbian (Latin) Translations
Group:          System/YaST
Provides:       locale(yast2:sr@latin)
Obsoletes:      yast2-trans-sr-latin
URL:            http://l10n.opensuse.org/

%description sr-latin
YaST2 - Translations for Serbian (Latin).

%package sv
Summary:        YaST2 - Swedish Translations
Group:          System/YaST
Provides:       locale(yast2:sv)
URL:            http://l10n.opensuse.org/

%description sv
YaST2 - Translations for Swedish.

%package sw
Summary:        YaST2 - Swahili Translations
Group:          System/YaST
Provides:       locale(yast2:sw)
URL:            http://l10n.opensuse.org/

%description sw
YaST2 - Translations for Swahili.

%package ta
Summary:        YaST2 - Tamil Translations
Group:          System/YaST
Provides:       locale(yast2:ta)
URL:            http://l10n.opensuse.org/

%description ta
YaST2 - Tamil translations.

%package tg
Summary:        YaST2 - Tajik Translations
Group:          System/YaST
Provides:       locale(yast2:tg)
URL:            http://l10n.opensuse.org/

%description tg
YaST2 - Tajik translations.

%package th
Summary:        YaST2 - Thai Translations
Group:          System/YaST
Provides:       locale(yast2:th)
URL:            http://l10n.opensuse.org/

%description th
YaST2 - Thai translations.

%package tk
Summary:        YaST2 -  Turkmen Translations
Group:          System/YaST
Provides:       locale(yast2:tk)
URL:            http://l10n.opensuse.org/

%description tk
YaST2 - Translations for Turkmen.

%package tr
Summary:        YaST2 - Turkish Translations
Group:          System/YaST
Provides:       locale(yast2:tr)
URL:            http://l10n.opensuse.org/

%description tr
YaST2 - Translations for Turkish.

%package uk
Summary:        YaST2 - Ukrainian Translations
Group:          System/YaST
Provides:       locale(yast2:uk)
URL:            http://l10n.opensuse.org/

%description uk
YaST2 - Translations for Ukrainian.

%package vi
Summary:        YaST2 - Vietnamese Translations
Group:          System/YaST
Provides:       locale(yast2:vi)
URL:            http://l10n.opensuse.org/

%description vi
YaST2 - Translations for Vietnamese.

%package wa
Summary:        YaST2 - Walloon Translations
Group:          System/YaST
Provides:       locale(yast2:wa)
URL:            http://l10n.opensuse.org/

%description wa
YaST2 - Translations for Walloon.

%package xh
Summary:        YaST2 - Xhosa Translations
Group:          System/YaST
Provides:       locale(yast2:xh)
URL:            http://l10n.opensuse.org/

%description xh
YaST2 - Translations for Xhosa.

%package zu
Summary:        YaST2 - Zulu Translations
Group:          System/YaST
Provides:       locale(yast2:zu)
URL:            http://l10n.opensuse.org/

%description zu
YaST2 - Translations for Zulu.

%package en_GB
Summary:        YaST2 - British English Translations
Group:          System/YaST
Provides:       locale(yast2:en_GB)
URL:            http://l10n.opensuse.org/

%description en_GB
YaST2 - Translations for British English.

%package pt_BR
Summary:        YaST2 - Brazilian Portuguese Translations
Group:          System/YaST
Provides:       locale(yast2:pt_BR)
URL:            http://l10n.opensuse.org/

%description pt_BR
YaST2 - Translations for Brazilian Portuguese.

%package zh_CN
Summary:        YaST2 - Simplified Chinese Translations
Group:          System/YaST
Provides:       locale(yast2:zh_CN)
URL:            http://l10n.opensuse.org/

%description zh_CN
YaST2 - Simplified Chinese translations.

%package zh_TW
Summary:        YaST2 - Traditional Chinese Translations
Group:          System/YaST
Provides:       locale(yast2:zh_TW)
URL:            http://l10n.opensuse.org/

%description zh_TW
YaST2 - Translations for Traditional Chinese.

%prep
%setup -q

%build
:

%install
pushd po
for l in %build_languages; do
  target_dir=%{buildroot}/usr/share/YaST2/locale/$l/LC_MESSAGES
  mkdir -p $target_dir
  pack_dir=%{buildroot}/usr/share/doc/packages/yast2-trans-$l
  mkdir -p $pack_dir
  cp %{S:1} $pack_dir/COPYING
  # touch %%{buildroot}/usr/share/doc/packages/yast2-trans-$l/status.txt
  for po in */$l.po; do
    domain="${po%%/*}"
    if ! msgfmt --statistics -o $target_dir/$domain.mo $po > out 2>&1; then
      cat out >> failed
    fi
  done | tee $l.txt
  bash %{S:2} < $l.txt | head -n 6 \
    > %{buildroot}/usr/share/doc/packages/yast2-trans-$l/status.txt
done
if [ -s "failed" ]; then
	echo "## PO FILES WITH FAILED CHECKS ###"
        cat failed
	exit 1
fi
popd

%clean
rm -rf %{buildroot}

%files
%defattr(-,root,root)
%dir %{_datadir}/YaST2
%dir %{_datadir}/YaST2/locale

%files af
%defattr(-,root,root)
%doc %{_docdir}/yast2-trans-af
%lang(af) %{_datadir}/YaST2/locale/af

%files am
%defattr(-,root,root)
%doc %{_docdir}/yast2-trans-am
%lang(am) %{_datadir}/YaST2/locale/am

%files ast
%defattr(-,root,root)
%doc %{_docdir}/yast2-trans-ast
%lang(ast) %{_datadir}/YaST2/locale/ast

%files ar
%defattr(-,root,root)
%doc %{_docdir}/yast2-trans-ar
%lang(ar) %{_datadir}/YaST2/locale/ar

%files be
%defattr(-,root,root)
%doc %{_docdir}/yast2-trans-be
%lang(be) %{_datadir}/YaST2/locale/be

%files bg
%defattr(-,root,root)
%doc %{_docdir}/yast2-trans-bg
%lang(bg) %{_datadir}/YaST2/locale/bg

%files bn
%defattr(-,root,root)
%doc %{_docdir}/yast2-trans-bn
%lang(bn) %{_datadir}/YaST2/locale/bn

%files bs
%defattr(-,root,root)
%doc %{_docdir}/yast2-trans-bs
%lang(bs) %{_datadir}/YaST2/locale/bs

%files ca
%defattr(-,root,root)
%doc %{_docdir}/yast2-trans-ca
%lang(ca) %{_datadir}/YaST2/locale/ca

%files cs
%defattr(-,root,root)
%doc %{_docdir}/yast2-trans-cs
%lang(cs) %{_datadir}/YaST2/locale/cs

%files cy
%defattr(-,root,root)
%doc %{_docdir}/yast2-trans-cy
%lang(cy) %{_datadir}/YaST2/locale/cy

%files da
%defattr(-,root,root)
%doc %{_docdir}/yast2-trans-da
%lang(da) %{_datadir}/YaST2/locale/da

%files de
%defattr(-,root,root)
%doc %{_docdir}/yast2-trans-de
%lang(de) %{_datadir}/YaST2/locale/de

%files el
%defattr(-,root,root)
%doc %{_docdir}/yast2-trans-el
%lang(el) %{_datadir}/YaST2/locale/el

%files eo
%defattr(-,root,root)
%doc %{_docdir}/yast2-trans-eo
%lang(el) %{_datadir}/YaST2/locale/eo

%files es
%defattr(-,root,root)
%doc %{_docdir}/yast2-trans-es
%lang(es) %{_datadir}/YaST2/locale/es

%files es_AR
%defattr(-,root,root)
%doc %{_docdir}/yast2-trans-es_AR
%lang(es_AR) %{_datadir}/YaST2/locale/es_AR

%files et
%defattr(-,root,root)
%doc %{_docdir}/yast2-trans-et
%lang(et) %{_datadir}/YaST2/locale/et

%files eu
%defattr(-,root,root)
%doc %{_docdir}/yast2-trans-eu
%lang(eu) %{_datadir}/YaST2/locale/eu

%files fa
%defattr(-,root,root)
%doc %{_docdir}/yast2-trans-fa
%lang(fa) %{_datadir}/YaST2/locale/fa

%files fi
%defattr(-,root,root)
%doc %{_docdir}/yast2-trans-fi
%lang(fi) %{_datadir}/YaST2/locale/fi

%files fr
%defattr(-,root,root)
%doc %{_docdir}/yast2-trans-fr
%lang(fr) %{_datadir}/YaST2/locale/fr

%files gl
%defattr(-,root,root)
%doc %{_docdir}/yast2-trans-gl
%lang(gl) %{_datadir}/YaST2/locale/gl

%files gu
%defattr(-,root,root)
%doc %{_docdir}/yast2-trans-gu
%lang(gu) %{_datadir}/YaST2/locale/gu

%files he
%defattr(-,root,root)
%doc %{_docdir}/yast2-trans-he
%lang(he) %{_datadir}/YaST2/locale/he

%files hi
%defattr(-,root,root)
%doc %{_docdir}/yast2-trans-hi
%lang(hi) %{_datadir}/YaST2/locale/hi

%files hr
%defattr(-,root,root)
%doc %{_docdir}/yast2-trans-hr
%lang(hr) %{_datadir}/YaST2/locale/hr

%files hu
%defattr(-,root,root)
%doc %{_docdir}/yast2-trans-hu
%lang(hu) %{_datadir}/YaST2/locale/hu

%files id
%defattr(-,root,root)
%doc %{_docdir}/yast2-trans-id
%lang(id) %{_datadir}/YaST2/locale/id

%files it
%defattr(-,root,root)
%doc %{_docdir}/yast2-trans-it
%lang(it) %{_datadir}/YaST2/locale/it

%files ja
%defattr(-,root,root)
%doc %{_docdir}/yast2-trans-ja
%lang(ja) %{_datadir}/YaST2/locale/ja

%files jv
%defattr(-,root,root)
%doc %{_docdir}/yast2-trans-jv
%lang(jv) %{_datadir}/YaST2/locale/jv

%files ka
%defattr(-,root,root)
%doc %{_docdir}/yast2-trans-ka
%lang(ka) %{_datadir}/YaST2/locale/ka

%files kab
%defattr(-,root,root)
%doc %{_docdir}/yast2-trans-kab
%lang(kab) %{_datadir}/YaST2/locale/kab

%files km
%defattr(-,root,root)
%doc %{_docdir}/yast2-trans-km
%lang(km) %{_datadir}/YaST2/locale/km

%files kn
%defattr(-,root,root)
%doc %{_docdir}/yast2-trans-kn
%lang(kn) %{_datadir}/YaST2/locale/kn

%files ko
%defattr(-,root,root)
%doc %{_docdir}/yast2-trans-ko
%lang(ko) %{_datadir}/YaST2/locale/ko

%files ku
%defattr(-,root,root)
%doc %{_docdir}/yast2-trans-ku
%lang(ku) %{_datadir}/YaST2/locale/ku

%files lo
%defattr(-,root,root)
%doc %{_docdir}/yast2-trans-lo
%lang(lo) %{_datadir}/YaST2/locale/lo

%files lt
%defattr(-,root,root)
%doc %{_docdir}/yast2-trans-lt
%lang(lt) %{_datadir}/YaST2/locale/lt

%files lv
%defattr(-,root,root)
%doc %{_docdir}/yast2-trans-lv
%lang(lv) %{_datadir}/YaST2/locale/lv

%files mk
%defattr(-,root,root)
%doc %{_docdir}/yast2-trans-mk
%lang(mk) %{_datadir}/YaST2/locale/mk

%files mr
%defattr(-,root,root)
%doc %{_docdir}/yast2-trans-mr
%lang(mr) %{_datadir}/YaST2/locale/mr

%files ms
%defattr(-,root,root)
%doc %{_docdir}/yast2-trans-ms
%lang(ms) %{_datadir}/YaST2/locale/ms

%files my
%defattr(-,root,root)
%doc %{_docdir}/yast2-trans-my
%lang(my) %{_datadir}/YaST2/locale/my

%files nb
%defattr(-,root,root)
%doc %{_docdir}/yast2-trans-nb
%lang(nb) %{_datadir}/YaST2/locale/nb

%files nds
%defattr(-,root,root)
%doc %{_docdir}/yast2-trans-nds
%lang(nds) %{_datadir}/YaST2/locale/nds

%files ne
%defattr(-,root,root)
%doc %{_docdir}/yast2-trans-ne
%lang(ne) %{_datadir}/YaST2/locale/ne

%files nl
%defattr(-,root,root)
%doc %{_docdir}/yast2-trans-nl
%lang(nl) %{_datadir}/YaST2/locale/nl

%files nn
%defattr(-,root,root)
%doc %{_docdir}/yast2-trans-nn
%lang(nn) %{_datadir}/YaST2/locale/nn

%files pa
%defattr(-,root,root)
%doc %{_docdir}/yast2-trans-pa
%lang(pa) %{_datadir}/YaST2/locale/pa

%files pl
%defattr(-,root,root)
%doc %{_docdir}/yast2-trans-pl
%lang(pl) %{_datadir}/YaST2/locale/pl

%files ps
%defattr(-,root,root)
%doc %{_docdir}/yast2-trans-ps
%lang(ps) %{_datadir}/YaST2/locale/ps

%files pt
%defattr(-,root,root)
%doc %{_docdir}/yast2-trans-pt
%lang(pt) %{_datadir}/YaST2/locale/pt

%files ro
%defattr(-,root,root)
%doc %{_docdir}/yast2-trans-ro
%lang(ro) %{_datadir}/YaST2/locale/ro

%files ru
%defattr(-,root,root)
%doc %{_docdir}/yast2-trans-ru
%lang(ru) %{_datadir}/YaST2/locale/ru

%files si
%defattr(-,root,root)
%doc %{_docdir}/yast2-trans-si
%lang(si) %{_datadir}/YaST2/locale/si

%files sk
%defattr(-,root,root)
%doc %{_docdir}/yast2-trans-sk
%lang(sk) %{_datadir}/YaST2/locale/sk

%files sl
%defattr(-,root,root)
%doc %{_docdir}/yast2-trans-sl
%lang(sl) %{_datadir}/YaST2/locale/sl

%files sq
%defattr(-,root,root)
%doc %{_docdir}/yast2-trans-sq
%lang(sq) %{_datadir}/YaST2/locale/sq

%files sr
%defattr(-,root,root)
%doc %{_docdir}/yast2-trans-sr
%lang(sr) %{_datadir}/YaST2/locale/sr

%files sr-latin
%defattr(-,root,root)
%doc %{_docdir}/yast2-trans-sr@latin
%lang(sr@latin) %{_datadir}/YaST2/locale/sr@latin

%files sv
%defattr(-,root,root)
%doc %{_docdir}/yast2-trans-sv
%lang(sv) %{_datadir}/YaST2/locale/sv

%files sw
%defattr(-,root,root)
%doc %{_docdir}/yast2-trans-sw
%lang(sw) %{_datadir}/YaST2/locale/sw

%files ta
%defattr(-,root,root)
%doc %{_docdir}/yast2-trans-ta
%lang(ta) %{_datadir}/YaST2/locale/ta

%files tg
%defattr(-,root,root)
%doc %{_docdir}/yast2-trans-tg
%lang(tg) %{_datadir}/YaST2/locale/tg

%files th
%defattr(-,root,root)
%doc %{_docdir}/yast2-trans-th
%lang(th) %{_datadir}/YaST2/locale/th

%files tk
%defattr(-,root,root)
%doc %{_docdir}/yast2-trans-tk
%lang(tk) %{_datadir}/YaST2/locale/tk

%files tr
%defattr(-,root,root)
%doc %{_docdir}/yast2-trans-tr
%lang(tr) %{_datadir}/YaST2/locale/tr

%files uk
%defattr(-,root,root)
%doc %{_docdir}/yast2-trans-uk
%lang(uk) %{_datadir}/YaST2/locale/uk

%files vi
%defattr(-,root,root)
%doc %{_docdir}/yast2-trans-vi
%lang(vi) %{_datadir}/YaST2/locale/vi

%files wa
%defattr(-,root,root)
%doc %{_docdir}/yast2-trans-wa
%lang(wa) %{_datadir}/YaST2/locale/wa

%files xh
%defattr(-,root,root)
%doc %{_docdir}/yast2-trans-xh
%lang(xh) %{_datadir}/YaST2/locale/xh

%files zu
%defattr(-,root,root)
%doc %{_docdir}/yast2-trans-zu
%lang(zu) %{_datadir}/YaST2/locale/zu

%files en_GB
%defattr(-,root,root)
%doc %{_docdir}/yast2-trans-en_GB
%lang(en_GB) %{_datadir}/YaST2/locale/en_GB

%files pt_BR
%defattr(-,root,root)
%doc %{_docdir}/yast2-trans-pt_BR
%lang(pt_BR) %{_datadir}/YaST2/locale/pt_BR

%files zh_CN
%defattr(-,root,root)
%doc %{_docdir}/yast2-trans-zh_CN
%lang(zh_CN) %{_datadir}/YaST2/locale/zh_CN

%files zh_TW
%defattr(-,root,root)
%doc %{_docdir}/yast2-trans-zh_TW
%lang(zh_TW) %{_datadir}/YaST2/locale/zh_TW

#@FILES@

%changelog
