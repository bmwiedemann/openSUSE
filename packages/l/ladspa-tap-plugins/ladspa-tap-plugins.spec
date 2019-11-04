#
# spec file for package ladspa-tap-plugins
#
# Copyright (c) 2019 SUSE LINUX GmbH, Nuernberg, Germany.
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


Name:           ladspa-tap-plugins
Version:        1.0.1
Release:        0
Summary:        LADSPA TAP plugins
License:        GPL-2.0-or-later
URL:            http://tap-plugins.sourceforge.net/
Source:         https://github.com/tomszilagyi/tap-plugins/archive/v%{version}.tar.gz#/tap-plugins-%{version}.tar.gz
Patch1:         tap-type-punning-fix.dif
BuildRequires:  ladspa-devel
Supplements:    ladspa

%description
This package provides a collection of LADSPA (Linux Audio Developer's
Simple Plug-in API) TAP plugins, short for Tom's Audio Processing,
which contains a collection of various audio plugins.

%prep
%setup -q -n tap-plugins-%{version}
%patch1

%build
make %{?_smp_mflags} CFLAGS="%{optflags} -fPIC -ggdb -c"

%install
make INSTALL_PLUGINS_DIR=%{buildroot}%{_libdir}/ladspa \
  INSTALL_LRDF_DIR=%{buildroot}%{_datadir}/ladspa/rdf \
  install

%files
%{_libdir}/ladspa
%{_datadir}/ladspa
%license COPYING
%doc CREDITS README

%changelog
