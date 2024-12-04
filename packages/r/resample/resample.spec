#
# spec file for package resample
#
# Copyright (c) 2024 SUSE LLC
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


Name:           resample
Version:        1.8.1
Release:        0
Summary:        Sampling-rate conversion program
License:        LGPL-2.1-or-later
Group:          Productivity/Multimedia/Video/Editors and Convertors
URL:            http://www-ccrma.stanford.edu/~jos/resample
#Url2:          https://ccrma.stanford.edu/~jos/resample/Free_Resampling_Software.html
Source:         http://ccrma.stanford.edu/~jos/gz/%name-%version.tar.gz
Patch0:         resample-filename-length-fix.diff
Patch1:         resample-compile-gcc14.patch
BuildRequires:  gcc
BuildRequires:  make
BuildRoot:      %{_tmppath}/%{name}-%{version}-build

%description
The resample program is a high-quality resampling program. For example,
it can be used to convert the sampling rate from 48 kHz (used by DAT
machines) to 44.1 kHz (the standard sampling rate for Compact Discs).

%prep
%autosetup -p1

%build
%configure
%make_build

%check
%make_build check

%install
%make_install
chmod 0644 [A-Z]*

%files
%defattr(-,root,root)
%doc README INSTALL AUTHORS ChangeLog NEWS
%license COPYING
%_bindir/*
%_mandir/man?/*

%changelog
