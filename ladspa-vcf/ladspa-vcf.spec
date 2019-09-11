#
# spec file for package ladspa-vcf
#
# Copyright (c) 2014 SUSE LINUX Products GmbH, Nuernberg, Germany.
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


Name:           ladspa-vcf
Version:        0.0.5
Release:        0
Summary:        LADSPA VCF plugin
License:        GPL-2.0
Group:          Productivity/Multimedia/Sound/Utilities
Source:         vcf-%{version}.tar.bz2
Source1:        README_VCF
Source2:        COPYING
Patch1:         vcf-Makefile.dif
BuildRequires:  gcc
BuildRequires:  ladspa-devel
Supplements:    ladspa
BuildRoot:      %{_tmppath}/%{name}-%{version}-build

%description
This package provides LADSPA (Linux Audio Developer's Simple Plug-in API)
plugins for audio EQ biquad filters.

%prep
%setup -q -n vcf-%{version}
%patch1
cp %{SOURCE1} README
cp %{SOURCE2} .

%build
# This package failed when testing with -Wl,-as-needed being default.
# So we disable it here, if you want to retest, just delete this comment and the line below.
export SUSE_ASNEEDED=0
make %{?_smp_mflags} CFLAGS="%{optflags} -fPIC -ggdb"

%install
mkdir -p %{buildroot}%{_libdir}/ladspa
install -c *.so %{buildroot}%{_libdir}/ladspa

%files
%defattr(-,root,root)
%{_libdir}/ladspa
%doc COPYING README

%changelog
