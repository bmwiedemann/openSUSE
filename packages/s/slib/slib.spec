#
# spec file for package slib
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


Name:           slib
Version:        3b7
Release:        0
Summary:        Portable Scheme Library
License:        SUSE-SLIB
Group:          Development/Languages/Scheme
URL:            https://swissnet.ai.mit.edu/~jaffer/SLIB.html
Source:         https://groups.csail.mit.edu/mac/ftpdir/scm/slib-%{version}.tar.gz
# this is not upstreamable (bnc#754532):
Patch0:         remove-resene-colors.diff
Requires(post): %{install_info_prereq}
Requires(post): coreutils
Requires(post): guile1
BuildArch:      noarch

%description
SLIB is a portable Scheme library providing compatibility and utility
functions for all standard Scheme implementations.

%prep
%setup -q
%patch0 -p1

%build

%install
install -m 755 -d %{buildroot}%{_datadir}/slib/
install -m 755 -d %{buildroot}/%{_infodir}/
install -m 644 *.scm *.init %{buildroot}%{_datadir}/slib/
install -m 644 slib.info* %{buildroot}%{_infodir}/

%triggerin -- guile1
# install guile library
# We need new guile for registration, see "Incompatible change in guile 1.8.2".
# During update must be slib-3a5 installed first (See Conflits: slib < 3a5 in guile.spec)
# because of %triggerin in slib, 3a1 for example, though.
if [ -d %{_datadir}/guile/site ] ; then
  # we have guile >= 1.8.2
  if [ ! -e %{_datadir}/guile/site/slib ] ; then
    # link slib library into guile
    ln -sf ../../slib %{_datadir}/guile/site/slib
  fi
  %{_bindir}/guile1 -c "(use-modules (ice-9 slib)) (require 'new-catalog)"
fi
exit 0

%triggerpostun -- guile1
# Delete slib library files, only if guile1 was uninstalled.
if ! test -e %{_bindir}/guile1 ; then
    rm -f %{_datadir}/guile/site/slib
    rm -f %{_datadir}/guile/site/slibcat
    rmdir --ignore-fail-on-non-empty %{_datadir}/guile/site
    rmdir --ignore-fail-on-non-empty %{_datadir}/guile
fi
exit 0

%post
%install_info --info-dir=%{_infodir} %{_infodir}/%{name}.info%{ext_info}
# install guile library
# We need new guile for registration, see "Incompatible change in guile 1.8.2".
# During update must be slib-3a5 installed first (See Conflits: slib < 3a5 in guile.spec)
# because of %triggerin in slib, 3a1 for example, though.
if [ -d %{_datadir}/guile/site -o -e %{_bindir}/guile1 ] ; then
  if [ ! -d %{_datadir}/guile/site ] ; then
    # This is in orderd to fixup eventually removed guile/site folders
    # which could have happened due to bnc#780827.
    mkdir %{_datadir}/guile/site
  fi
  if [ ! -e %{_datadir}/guile/site/slib ] ; then
    # link slib library into guile
    ln -sf ../../slib %{_datadir}/guile/site/slib
  fi
  %{_bindir}/guile1 -c "(use-modules (ice-9 slib)) (require 'new-catalog)"
fi

%postun
%install_info_delete --info-dir=%{_infodir} %{_infodir}/%{name}.info%{ext_info}
# Delete guile library, only if slib or guile was uninstalled.
if ! test -d %{_datadir}/slib -a -d %{_datadir}/guile/site ; then
    rm -f %{_datadir}/guile/site/slib
    rm -f %{_datadir}/guile/site/slibcat
fi

%files
%license COPYING
%doc ANNOUNCE ChangeLog FAQ README
%{_infodir}/*
%{_datadir}/slib

%changelog
