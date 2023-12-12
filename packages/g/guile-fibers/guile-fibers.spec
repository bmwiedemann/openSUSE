#
# spec file for package guile-fibers
#
# Copyright (c) 2023 Jonathan Brielmaier <jbrielmaier@opensuse.org>
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


Name:           guile-fibers
Version:        1.3.1
Release:        0
Summary:        Concurrent ML-like concurrency for Guile
License:        LGPL-3.0-or-later
Group:          System/Libraries
URL:            https://github.com/wingo/fibers
Source0:        https://github.com/wingo/fibers/releases/download/v%{version}/fibers-%{version}.tar.gz
BuildRequires:  autoconf
BuildRequires:  automake
BuildRequires:  guile-devel >= 2.1.7
Requires:       guile >= 2.1.7

%description
Fibers is a library written in Guile which provides Concurrent ML-like concurrency.

%prep
%setup -q -n fibers-%{version}

%build
%configure
# do sequential build for reproducible .go files = https://issues.guix.gnu.org/issue/20272 - boo#1102408
make

%install
%make_install

%files
%{_datadir}/guile/*
%{_infodir}/fibers.info.gz
%{_libdir}/guile/*

%changelog
