#
# spec file for package libpulp-load-default
#
# Copyright (c) 2023 SUSE LINUX GmbH, Nuernberg, Germany.
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

Name:           libpulp-load-default
Version:        0.1
Release:        0
Summary:        Enable ULP on all processes
License:        MIT
# FIXME: use correct group, see "https://en.opensuse.org/openSUSE:Package_group_guidelines"
BuildRequires:  coreutils

Requires:       libpulp0
Requires:       coreutils

BuildArch:      noarch

%global debug_package %{nil}

%define ld_so_conf  /etc/ld.so.preload
%define addline     /usr/lib64/libpulp.so.0

%define skip_if_buildenv \
  if test -e /.buildenv; then \
    exit 0; \
  fi;

%prep

%description
This package adds libpulp.so into /etc/ld.so.preload to add livepatching capabilities into all processes in the system.

%build

%install

%post

%{skip_if_buildenv}

# Create file if doesn't exist.
if [ ! -f "%{ld_so_conf}" ]; then
  touch "%{ld_so_conf}"
fi

# Add instance of libpulp if not already present.
grep -qxF '%{addline}' %{ld_so_conf} || echo '%{addline}' >> %{ld_so_conf}

%postun

%{skip_if_buildenv}

# Delete all instances of libpulp in the ld_so_conf.
sed -i '\#%{addline}#d' %{ld_so_conf}

# Remove file if it is now empty.
if [ ! -s "%{ld_so_conf}" ]; then
  rm -f "%{ld_so_conf}"
fi

%files

%changelog
