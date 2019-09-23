#
# spec file for package ladspa-tap-plugins
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


Name:           ladspa-tap-plugins
Version:        0.7.1
Release:        0
Summary:        LADSPA TAP plugins
License:        GPL-2.0+
Group:          Productivity/Multimedia/Sound/Utilities
Url:            http://tap-plugins.sourceforge.net/
Source:         tap-plugins-%{version}.tar.bz2
Patch1:         tap-type-punning-fix.dif
BuildRequires:  gcc
BuildRequires:  ladspa-devel
Supplements:    ladspa
BuildRoot:      %{_tmppath}/%{name}-%{version}-build

%description
This package provides a collection of LADSPA (Linux Audio Developer's
Simple Plug-in API) TAP plugins, short for Tom's Audio Processing,
which contains a collection of various audio plugins.

%prep
%setup -q -n tap-plugins-%{version}
%patch1

%build
# This package failed when testing with -Wl,-as-needed being default.
# So we disable it here, if you want to retest, just delete this comment and the line below.
export SUSE_ASNEEDED=0
make %{?_smp_mflags} CFLAGS="%{optflags} -fPIC -ggdb -c"

%install
make INSTALL_PLUGINS_DIR=%{buildroot}%{_libdir}/ladspa \
  INSTALL_LRDF_DIR=%{buildroot}%{_datadir}/ladspa/rdf \
  install

%files
%defattr(-,root,root)
%{_libdir}/ladspa
%{_datadir}/ladspa
%doc COPYING CREDITS README

%changelog
