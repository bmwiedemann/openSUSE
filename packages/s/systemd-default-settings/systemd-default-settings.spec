#
# spec file for package systemd-default-settings
#
# Copyright (c) 2026 SUSE LLC and contributors
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


%define extra_version %{nil}
Name:           systemd-default-settings
Version:        1.0
Release:        0
Summary:        Generic SUSE Customization of systemd defaults
License:        GPL-2.0-or-later
URL:            https://github.com/openSUSE/systemd-default-settings
Source0:        %{name}-%{version}%{extra_version}.tar.gz
BuildRequires:  systemd-rpm-macros
Requires:       %{name}-branding = %{version}-%{release}
BuildArch:      noarch

%description
This package overrides some of the upstream default settings which are
better suited for openSUSE or SLE distributions.

This package should not be installed alone but is supposed to be
pulled in by the branding package instead.

%package branding-SLE
Summary:        SLE Specific Customization of systemd defaults
Requires:       %{name} = %{version}-%{release}
Supplements:    (%{name} and branding-SLE)
Conflicts:      %{name}-branding
Provides:       %{name}-branding = %{version}-%{release}

%description branding-SLE
This package overrides some of the upstream default settings to make
them better suited for SLE distributions.

%package branding-openSUSE
Summary:        openSUSE Specific Customization of systemd defaults
Requires:       %{name} = %{version}-%{release}
Supplements:    (%{name} and branding-openSUSE)
Conflicts:      %{name}-branding
Provides:       %{name}-branding = %{version}-%{release}

%description branding-openSUSE
This package overrides some of the upstream default settings to make
them better suited for openSUSE distributions.

%package branding-upstream
Summary:        Restore upstream systemd defaults
Supplements:    (%{name} and branding-upstream)
Conflicts:      %{name}
Conflicts:      %{name}-branding
Provides:       %{name}-branding = %{version}-%{release}

%description branding-upstream
Installing this package restores some of the upstream default settings
by uninstalling all drop-ins shipped by %{name} and its branding sub
package.

%package branding-SLE-Micro
Summary:        SLE-Micro Specific Customization of systemd defaults
Requires:       %{name} = %{version}-%{release}
Supplements:    (%{name} and branding-SLE-Micro)
Conflicts:      %{name}-branding
Provides:       %{name}-branding = %{version}-%{release}

%description branding-SLE-Micro
This package overrides some of the upstream default settings to make
them better suited for SLE-Micro distributions.

%prep
%setup -q -n %{name}-%{version}%{extra_version}

%build

%install
%make_install

make -s list-base >SUSE.list
for b in SLE openSUSE SLE-Micro; do
	make -s list-branding BRANDING=$b >$b.list
done

%post
# Reloading PID1 is probably not enough as some changes will require
# service restarts or even a reboot. But it might be useful in a few
# cases so...
[ -x %{_bindir}/systemctl ] &&
	%{_bindir}/systemctl daemon-reload || :

%files -f SUSE.list

%files branding-SLE -f SLE.list

%files branding-openSUSE -f openSUSE.list

%files branding-SLE-Micro -f SLE-Micro.list

%files branding-upstream

%changelog
